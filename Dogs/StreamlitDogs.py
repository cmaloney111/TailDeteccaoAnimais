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

def inferUpload(UploadedFile):
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
        'endpoint_id':  '98aab845-cf07-479c-827f-2a78509fb97b',
    }

    files = {
        'file': UploadedFile.getvalue()
        #'file_url': 'https://testbucketcameron.s3.us-east-2.amazonaws.com/n02085782_866.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJGMEQCIBYuSto3JEFXOZE03xM%2BYMrH%2FgYJEkSAofwoqIb2k9%2FzAiBP7qZU8QSRm5g7Q6n3M3WWN0jg9CpxO635bGWb9KijtyrtAgje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDI3MTg3MTMzOTA5MSIMaFRGjeiVjhYSKep8KsEC%2Bm8QC78hecEZlVJjE1j6EKtFvweKhuWiejXvFqOX%2FmYTUqBV9hwgsmpu4aMibWhbWoakfznMBgPxln8qiVqTI65dGJ85V85io0AIh76emUBu7fuWpZ8ho%2Bdo3mM6Fx529zUt7hyY6vR1MagVLoR29xc%2FeNzmdcMw7iRvg9l0AnILaj7onRMxyBMxDCELxZiwSiudeod8Iq%2BSwcy1AR8eM2vX5%2FXYSDAUQn9BM5QUX6towzI8tBgGY4Nb%2Fl7mE9bsfapl6JWptVnWEXdi%2BGBPmG3yv1Sn1HF7a6JILm2g02N%2FNBH7TbQtZmRkFGGgYwdJ11Lbf9DRH4JgnbR%2BZww4qcBqXxKPlq8DId0Do2HEJKAlcHKV5DFwW35Hcbe%2F%2Ftt22cd%2FVgnl4VaR%2BVUZ1Mek39CYHZYvS0W8%2B%2F5zphBxJ%2BeyMLTv0qQGOrQCR7WM2Dx54tUp3zNk%2BjyK71oASRN55FopvwfWn3OQxYtUGLnQzevs6m3iTBcxQ13bNQ%2FBSkAnsdRT%2BFe7vBn12AJ2QsLR6LMMLkUdFNwe25l%2BDgUkn7z6b37AJsM6PuKi805%2FosjEUNs5b7rf1AmgwrDrKZAfn3fO%2FKp%2BMRa%2FAiI4ZirlUnGK5to3HD%2F1YJNomnHF5QcgcXFS1Dj8qayc8X%2Fqqm%2FHyZQPN2txyhgJ%2BC1DLzoa%2BaO0PYnVfzmFQq%2FuIHegXGs315EGAKzMgt8Yh5CUlpp%2FS6C6%2BefO5NHvJVN7%2BYJJdH7ufVm%2BD5pGuam7%2Bfce0L3tzorPWBY%2BqOgfSq76ssXvJaIAyEMBHgCyZB9L%2FcgGd8sbENiA5iqvnzEUZdv%2Fe9YphBbosj%2FwOUgmOFN%2F8Mw%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230622T211201Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAT6TGLNJJYQSEHYE2%2F20230622%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=2c286cdbc2061d2f32686ea37d5cfd825d1b15e3acc2e756e06f622d96d36d6b',
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
        st.image(resize("Images/Tail/Captura-de-Tela-2020-08-16-às-11.57.39.png", 300))

    st.title('Bem-vindo a um detector de raças de cachorros')

    file = st.file_uploader('Carregue uma imagem')

    if file:
        inference = inferUpload(file)
        st.title("Aqui está a imagem que você selecionou")
        st.write(file.name + ":\n")
        st.image(resize(file, 500))
        st.write("predição: " + inference["predictions"]["labelName"].split("-")[1]) 

        st.title("Outros cachorros como esse:")

        files = os.listdir(os.path.join("Images/images", inference["predictions"]["labelName"]))
        try:
            filelist = []
            for f in sample(files, 8):
                filepath = os.path.join("Images/images", inference["predictions"]["labelName"], f)
                filelist.append(resize(filepath, 300))
        except FileNotFoundError:
            pass
        st.image(filelist)


if __name__ == "__main__":
    main() 
