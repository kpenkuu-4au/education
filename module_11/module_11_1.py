import requests as rq
from PIL import Image
from matplotlib import pyplot as pt

new_image = rq.get('https://w.wallhaven.cc/full/2y/wallhaven-2yjp6x.png')
with open('download_image.png', 'wb+') as img:
    if new_image.status_code == 200:
        img.write(new_image.content)
        print('Загрузка изображения завершена')
    elif new_image.status_code == 404:
        print(f'Ссылка {new_image.url} недоступна')


def open_image():
    question = input('Открыть изображение?  -  ')
    if question.lower() == 'да':
        my_image = pt.imread('download_image.png')
        pt.imshow(my_image)
        pt.show()
    elif question.lower() == 'нет':
        pass
    else:
        print('Ответ может быть только "Да" или "Нет"')
        open_image()


def make_quad_500():
    question = input('Обрезать изображение до квадрата 500х500?  -  ')
    if question.lower() == 'да':
        picture = Image.open('download_image.png')
        crop_size = (1420, 580, picture.width, picture.height)
        crop_img = picture.crop(crop_size)
        next_question = input('Размер изменен, открыть измененное изображение?  -  ')
        if next_question.lower() == 'да':
            crop_img.show()
        elif next_question.lower() == 'нет':
            pass
        else:
            print('Ответ может быть только "Да" или "Нет"')
    elif question.lower() == 'нет':
        pass
    else:
        print('Ответ может быть только "Да" или "Нет"')
        make_quad_500()


open_image()
make_quad_500()
