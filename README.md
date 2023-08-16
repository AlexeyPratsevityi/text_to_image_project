# Text_to_Image_project

Проект сервиса стоковых фотографий __Find my pic!__ для поиска картинок по пользовательскому текстовому запросу.<br>
Пользватель вводит текстовый запрос и ему возвращается несколько картинок, наиболее подходящих под описание.<br>
Сервис разработан с использованием `streamlit` и развернут на [huggingface spaces](https://huggingface.co/spaces/IvaElen/find_my_pic).<br>
Использован модуль Contrastive Language-Image Pre-Training ([CLIP](https://github.com/openai/CLIP)).<br>
Больше информации о CLIP [здесь](https://openai.com/research/clip).<br>
В качестве моделей для предсказаний выбраны  ResNet50 (RN50) и Vision Transformer(ViT-B/32).





