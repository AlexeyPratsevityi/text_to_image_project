import streamlit as st

import pandas as pd

import clip
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch
import numpy as np
import random
from get_similiarty import get_similiarity

device = "cuda" if torch.cuda.is_available() else "cpu"
#load model -resnet50


model_resnet, preprocess = clip.load("RN50", device)

#load model - ViT-B/32
model_vit, preprocess = clip.load('ViT-B/32', device)


st.title('Find my pic!')

def find_image_disc(prompt, df):
    img_descs = []
    img_descs_vit = []
    list_images_names, list_images_names_vit = get_similiarity(prompt, model_resnet, model_vit, 3)
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
