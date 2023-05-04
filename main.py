import streamlit as st

import pandas as pd

import clip
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch
import numpy as np
import random
from get_similiarty import get_similiarity


#load model -resnet50
model_resnet, processor = clip.load("RN50", device=device)

#load model - ViT-B/32
#model_vit = <path_model>


st.title('Find my pic!')


# def get_similiarity(prompt, top_k=3):
#     image_arr = np.loadtxt("embeddings.csv", delimiter=",")
#     raw_dataset = datasets.ImageFolder(data_dir)
#     # получите список всех изображений
#     # create transformer-readable tokens
#     inputs = clip.tokenize(prompt).to(device)
#     text_emb = model_resnet.encode_text(inputs)
#     text_emb = text_emb.cpu().detach().numpy()
#     scores = np.dot(text_emb, image_arr.T)
#     #score_vit
#     # get the top k indices for most similar vecs
#     idx = np.argsort(-scores[0])[:top_k]
#     image_files = []
#     for i in idx:
#         image_files.append(raw_dataset.imgs[i][0])
#
#
#     #image_arr_vit = <path>
#     # text_emb_vit = model_vit.encode_text(inputs)
#     # text_emb_vit = text_emb_vit.cpu().detach().numpy()
#     # scores_vit = np.dot(text_emb_vit, image_arr_vit.T)
#     # idx_vit = np.argsort(-scores_vit[0])[:top_k]
#     # image_files_vit = []
#     # for i in idx_vit:
#     #     image_files_vit.append(raw_dataset.imgs[i][0])
#
#     return image_files#, image_files_vit


def find_image_disc(prompt, df):
    img_descs = []
    img_descs_vit = []
    list_images_names = get_similiarity(prompt, model_resnet, model_vit, 3)
    for img in list_images_names:
        img_descs.append(random.choice(df[df['image_name'] == img.split('/')[-1]]['comment'].values).replace('.', ''))
    #vit
    for img in list_images_names_vit:
        img_descs_vit.append(random.choice(df[df['image_name'] == img.split('/')[-1]]['comment'].values).replace('.', ''))

    return list_images_names, img_descs, list_images_names_vit, img_descs_vit

txt = st.text_area("Describe the picture you'd like to see")

df = pd.read_csv('results.csv', 
                 sep = '|', 
                 names = ['image_name', 'comment_number', 'comment'], 
                 header=0)


if txt is not None:
     if st.button('Find!'):

        list_images, img_desc, list_images_vit, img_descs_vit = find_image_disc(txt, df)
        col1, col2 = st.columns(2)
        for ind, pic in enumerate(zip(list_images, list_images_vit)):
            with col1:
                st.image(pic[0])
                st.write(img_desc[ind])
            with col2:
                st.image(pic[1])
                st.write(img_desc[ind])
