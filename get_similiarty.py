import torchvision.datasets as datasets
import numpy as np
import clip
import torch
def get_similiarity(prompt, model_resnet, model_vit,  top_k=3):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    data_dir = 'sample/data'
    image_arr = np.loadtxt("embeddings.csv", delimiter=",")
    raw_dataset = datasets.ImageFolder(data_dir)
    # получите список всех изображений
    # create transformer-readable tokens
    inputs = clip.tokenize(prompt).to(device)
    text_emb = model_resnet.encode_text(inputs)
    text_emb = text_emb.cpu().detach().numpy()
    scores = np.dot(text_emb, image_arr.T)
    # score_vit
    # get the top k indices for most similar vecs
    idx = np.argsort(-scores[0])[:top_k]
    image_files = []
    for i in idx:
        image_files.append(raw_dataset.imgs[i][0])

    #image_arr_vit = <path>
    text_emb_vit = model_vit.encode_text(inputs)
    text_emb_vit = text_emb_vit.cpu().detach().numpy()
    scores_vit = np.dot(text_emb_vit, image_arr_vit.T)
    idx_vit = np.argsort(-scores_vit[0])[:top_k]
    image_files_vit = []
    for i in idx_vit:
        image_files_vit.append(raw_dataset.imgs[i][0])

    return image_files, image_files_vit
