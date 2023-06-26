import zipfile
import os
import os, sys, tarfile

# with zipfile.ZipFile(r'C:\Users\camer\Downloads\archive (10).zip', 'r') as zip_ref:
#     zip_ref.extractall("../Birds")

# def extract(tar_url, extract_path='../Birds'):
#     tar = tarfile.open(tar_url, 'r')
#     for item in tar:
#         tar.extract(item, extract_path)
#         if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
#             extract(item.name, "./" + item.name[:item.name.rfind('/')])
# try:
#     extract("../Birds/CUB_200_2011.tgz")
# except:
#     name = os.path.basename(sys.argv[0])

#with zipfile.ZipFile(r'C:\Users\camer\Downloads\archive (8).zip', 'r') as zip_ref:
#    zip_ref.extractall()
#with zipfile.ZipFile(r'C:\Users\camer\Downloads\archive (10).zip', 'r') as zip_ref:
#    zip_ref.extractall("../Birds")
# for (root,dirs,files) in os.walk('images', topdown=True): 
    # file_length=len(files)
    # if file_length>150:
    #     for i in range(151,file_length):
    #         os.remove(root + "\\\\" + files[i])
for (root,dirs,files) in os.walk('../Birds/images', topdown=True): 
    file_length=len(files)
    if file_length>49:
        for i in range(50,file_length):
            os.remove(root + "\\\\" + files[i])