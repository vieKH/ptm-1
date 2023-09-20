from bs4 import BeautifulSoup
import logging
import os
import requests
from tqdm import tqdm


HEADERS = {"User-Agent": "Mozilla/5.0 Mozilla/5.0 "
                         "(Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/106.0.0.0 Safari/537.36",
           "Accept-Language": "en-US, ru-RU",
           "Accept-Encoding": "grip, deflate",
           "Connection": "keep-alive",
           "one": "true"}


def create_file(folder) -> None:
    """
    Эта фукнция для создании папки
    Если есть ошибка, она будет появиться на вывод (logging.info)

    :param folder: Имена папки
    :return: Не возрашается
    """
    try:
        new_directory = os.path.join(folder)
        os.makedirs(new_directory)
    except OSError as err:
        logging.info(f'При создании файл {folder} есть ошибки \n {err}')


def write_images_to_file(filename, image_url) -> None:
    """
    Функция для записи фота в файле

    :param filename: Директория файла
    :param image_url: Адресс фота
    :return: Не возращается
    """

    picture = requests.get(image_url, HEADERS)
    with open(filename, "wb") as f:
        f.write(picture.content)


def download_images(folder, obj, url, counter=1000) -> None:
    """
    Эта функция для скачать фото
    Из библиотеки request получить код содержать фото
    Мз библиотеки BS4 поменять код в lxml, поиск адресс фото и скачать их

    :param folder: Имена папки
    :param obj: Объект который вы хотите найти
    :param url: Адресс страница
    :param counter: Количество фота хотите скачать ( в задаче 1000 фото)
    :return: Не возращается значения
    """
    create_file(folder)
    arr_image = []
    page = 0

    while counter > 0:
        url = f"{url}?p={page}&text={obj}"
        r = requests.get(url, HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        images = soup.findAll("img",
                              class_="serp-item__thumb justifier__thumb")

        for image in images:
            if counter == 0:
                return
            image_url = f"https:{image.get('src')}"
            arr_image.append(image_url)
            counter -= 1
        page += 1

    for a in tqdm(range(len(arr_image)),
                  desc=f'Количество фото {folder} уже скачали :'):
        filename = os.path.join(folder, f'{a:04d}.jpg')
        write_images_to_file(filename, arr_image[a])
    del arr_image


def main():
    download_images('dog', 'dog', "https://yandex.ru/images/search")
    download_images('cat', 'cat', "https://yandex.ru/images/search")


if __name__ == "__main__":
    main()
