# Text_to_Image_project

Проект сервиса стоковых фотографий __Find my pic!__ для поиска картинок по пользовательскому текстовому запросу.<br>
Пользватель вводит текстовый запрос и ему возвращается несколько картинок, наиболее подходящих под описание.<br>
Сервис разработан с использованием `streamlit` и развернут на [huggingface spaces](https://huggingface.co/spaces/IvaElen/find_my_pic).<br>
Использован модуль Contrastive Language-Image Pre-Training ([CLIP](https://github.com/openai/CLIP)).<br>
Больше информации о CLIP [здесь](https://openai.com/research/clip).<br>
В качестве моделей для предсказаний выбраны  ResNet50 (RN50) и Vision Transformer(ViT-B/32).



FindMyPic Team: </br>
[IvaElen](https://github.com/IvaElen)<br>
[AlexeyPratsevityi](https://github.com/AlexeyPratsevityi)<br>
[GalkaMT](https://github.com/GalkaMT)<br>

## Релизы 

### Релиз 1.0 
* В данном релизе сервис принимает запрос пользователя в текстовом окне и возвращает 5 случайных картинок из папки `img` (52 фотографии) с пользовательскими описаниями картинки. 

### Релиз 2.0 
* Реализован скрипт get_similiarity.py, в котором хранится функция нахождения top_k ближайших к текстовому запросу картинок (по умолчанию -3).
* Реализован скрипт app.py, который  отвечает за функционирование сервиса.<br>

### Релиз 3.0 
* добавлена возможность генерировать описание к загруженной картинке<br>


