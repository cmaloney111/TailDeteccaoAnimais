import json
from PIL import Image
import os
from random import sample
import requests
import streamlit as st
from pathlib import Path
from typing import Any, Union
import io


def resize(img, size):
    image = Image.open(img)
    image.thumbnail((size, size))
    return image

def inferDir(filename: Union[Path, str], endpoint_id) -> Any:
    """
    Run inference on an image
    :param filename: path to the image file
    :return: dictionary object representing the inference results
    """
    headers = {
        'apikey':  'txfcbpqmuzht1yd2mfiz7vx46x0w4un',
        'apisecret': 'ankmh8tih6bmahuwgdeft7725zlif5wasdbkpz1bedl9x58oxy55ygs2ah7e1v',
    }

    params = {
        'endpoint_id':  endpoint_id,
    }
    img = Image.open(filename)
    output = io.BytesIO()
    img.save(output, format='JPEG')
    files = {
        'file': output.getvalue()
    }

    response = requests.post('https://predict.app.landing.ai:443/inference/v1/predict', 
                             params=params, headers=headers, files=files)
    if(response.status_code == "429"):
        st.write("Too many requests to server (HTTP Status Code 429)")
    return json.loads(response.text)

def inferUpload(UploadedFile, endpoint_id):
    """
    Run inference on an image
    :param filename: path to the image file
    :return: dictionary object representing the inference results
    """
    headers = {
        'apikey': '4q8pu5y5m53slmk0k9ejz0udeycsyet',
        'apisecret': 'r08ankvrm2fckno5xenp7kzbqeazqzhved2i3z0wa3to7ilqbxet0hsbj8r34h',
    }

    params = {
        'endpoint_id':  endpoint_id,
    }

    files = {
        'file': UploadedFile.getvalue()
    }

    response = requests.post('https://predict.app.landing.ai/inference/v1/predict', params=params, headers=headers, files=files)
    if(response.status_code == "429"):
        st.write("Too many requests to server (HTTP Status Code 429)")
    print(response.status_code)
    try:
        return json.loads(response.text)
    except json.decoder.JSONDecodeError:
        inferUpload(UploadedFile)

def main():
    st.set_page_config(layout="wide")

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    with col3:
        st.image(resize("TailImage/Captura-de-Tela-2020-08-16-às-11.57.39.png", 300))
        
    option = st.selectbox(
        'Você gostaria de detectar pássaros, gatos ou cachorros?',
        ('pássaros', 'gatos', 'cachorros'))

    with st.sidebar:
        probability = st.checkbox("Mostrar confiança da predição")  


    if option == "pássaros":
        st.title('Bem-vindo a um detector de  espécies de pássaros')
    elif option == "gatos":
        st.title('Bem-vindo a um detector de raças de gatos')
    elif option == "cachorros":
        st.title('Bem-vindo a um detector de raças de cachorros')

    file = st.file_uploader('Carregue uma imagem')

    if file:
        if option == "pássaros":
            inference = inferUpload(file, '05628429-0197-4bcd-9df6-7c6bd73771c4')  
        elif option == "gatos":
            inference = inferUpload(file, 'df7874a1-10af-4310-95fd-1e908b0e5574')  
        elif option == "cachorros":
            inference = inferUpload(file, '98aab845-cf07-479c-827f-2a78509fb97b')  
        st.title("Aqui está a imagem que você selecionou")
        st.write(file.name + ":\n")
        st.image(resize(file, 500))
        if option == "pássaros":
            st.write("predição: " + inference["predictions"]["labelName"].split(".")[1])  
        elif option == "gatos":
            st.write("predição: " + inference["predictions"]["labelName"])   
        elif option == "cachorros":
            st.write("predição: " + inference["predictions"]["labelName"].split("-")[1])  
        
        if (probability):
            st.write("confiança: " + str(inference["predictions"]["score"]))

        if option == "pássaros":
            st.title('Outros pássaros como esse:')
            files = os.listdir(os.path.join("Birds/images", inference["predictions"]["labelName"]))
            try:
                filelist = []
                for f in sample(files, 8):
                    filepath = os.path.join("Birds/images", inference["predictions"]["labelName"], f)
                    filelist.append(resize(filepath, 300))
            except FileNotFoundError:
                pass
        elif option == "gatos":
            st.title('Outros gatos como esse:')
            files = os.listdir(os.path.join("Cats/images", inference["predictions"]["labelName"]))
            try:
                filelist = []
                for f in sample(files, 8):
                    filepath = os.path.join("Cats/images", inference["predictions"]["labelName"], f)
                    filelist.append(resize(filepath, 300))
            except FileNotFoundError:
                pass
        elif option == "cachorros":
            st.title('Outros cachorros como esse:')
            files = os.listdir(os.path.join("Dogs/images", inference["predictions"]["labelName"]))
            try:
                filelist = []
                for f in sample(files, 8):
                    filepath = os.path.join("Dogs/images", inference["predictions"]["labelName"], f)
                    filelist.append(resize(filepath, 300))
            except FileNotFoundError:
                pass


        st.image(filelist)


if __name__ == "__main__":
    main() 
