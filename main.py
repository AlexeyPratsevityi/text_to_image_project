import streamlit as st

import pandas as pd 

import glob
import random

st.title('Find my pic!')

def load_image():
    '''
    Function for downloading pictures from folder "img"
    '''
    image_files = glob.glob("img/*.jpg")
    return image_files

def random_image(image_files, df):
    '''
    Function return list of 5 random pictures names from img-folder with 
    1 of 5 desciptions from results.csv
    '''
    rand_images = []
    img_desc = []

    while len(rand_images)<5:
        rand_pic = random.choice(image_files)
        if rand_pic not in rand_images:
            rand_images.append(rand_pic)
            img_desc.append(random.choice(df[df['image_name']==rand_pic.split('/')[-1]]['comment'].values).replace('.',''))
            
        else:
            continue

    return rand_images, img_desc

txt = st.text_area("Describe the picture you'd like to see")

df = pd.read_csv('results.csv', 
                 sep = '|', 
                 names = ['image_name', 'comment_number', 'comment'], 
                 header=0)

image_files = load_image()

if txt is not None:
    # col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    # with col7:
     if st.button('Find!'):
        rand_images, img_desc = random_image(image_files, df)
        col1, col2 = st.columns(2)
        for ind, pic in enumerate(rand_images):
            if ind%2!=0:
                col2.image(pic)
                col2.write(img_desc[ind])
            else:
                col1.image(pic)
                col1.write(img_desc[ind])
