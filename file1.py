import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def numerical(labels_path: pd.Series) -> pd.Series:
    """
    Функуия для добавления норера изображений (cat : 0, dog :1)

    :param labels_path: Series метки
    :return: Series с номером
    """
    numerical_list = []
    for label_path in labels_path:
        if label_path == "cat":
            numerical_list.append(0)
        else:
            numerical_list.append(1)
    return pd.Series(numerical_list)


def img_shape(imgs_path: pd.Series) -> tuple[pd.Series, pd.Series, pd.Series]:
    """
    Функуия для получения значении ширины высоты и глубины изображений

    :param imgs_path: Пути к каждому изображениям
    :return: Series ширины высоты и глубины
    """
    width = []
    height = []
    channels = []
    for img_path in imgs_path:
        image = cv2.imread(img_path)
        img_width, img_height, img_channels = image.shape
        width.append(img_width)
        height.append(img_height)
        channels.append(img_channels)
    return pd.Series(width), pd.Series(height), pd.Series(channels)


def label_filter(df1: pd.DataFrame, label: str) -> pd.DataFrame:
    """
    Функуия для получения значении заданной меткой

    :param df1: Заданный датафрейм
    :param label: Заданная метка
    :return: Результат после фильтрации
    """
    return df1[df1.Label == label]


def mul_filter(df2: pd.DataFrame, max_width: int,
               max_height: int, label: str) -> pd.DataFrame:
    """
    Эта функция для фильтрации данных ответа пользователя.

    :param df2: Заданный датафрейм
    :param max_width: Заданная максимальная ширина
    :param max_height: Заданная максимальная высота
    :param label: Заданная метка
    :return: Результат после фильтрации
    """
    return df2[((df2.Label == label) & (df2.Width <= max_width)
               & (df2.Height <= max_height))]


def count_pixels(df3: pd.DataFrame) -> tuple:
    """
    Функция чтобы выполнить группировку DataFrame по метке класса
    с вычислением максимального, минимального
    и среднего значения по количеству пикселей

    :param df3: Заданный датафрейм
    :return: Кортеж из 3 группировок: максимальное,
             минимальное и среднее количество пикселей изображения.
    """
    df3['pixels'] = df3['width'] * df3['height']
    return (df3.groupby('Label').max(),
            df3.groupby('Label').min(),
            df3.groupby('Label').mean())


def count_data_histogram(df4: pd.DataFrame, label: str) -> list:
    """
    Функция для вычислить значения количества пикселей
    соответствует уровню яркости изображения

    :param df4: Заданный датафрейм
    :param label: Заданная метка
    :return: Значения количества пикселей
             соответствует уровню яркости изображения
    """
    df_now = label_filter(df4, label)
    imgs_path = df_now.Absolute_Path.to_numpy()
    img_path = np.random.choice(imgs_path)
    img = cv2.imread(img_path)
    img_width, img_height, img_channel = img.shape

    his1 = (cv2.calcHist([img], [0], None, [256], [0, 256])) / \
           (img_width * img_height)
    his2 = (cv2.calcHist([img], [1], None, [256], [0, 256])) / \
           (img_width * img_height)
    his3 = (cv2.calcHist([img], [2], None, [256], [0, 256])) / \
           (img_width * img_height)

    return [his1, his2, his3]


def draw_histogram(df5: pd.DataFrame, label: str) -> None:
    """
    Функция для построить график гистограмм
    :param df5: Заданный датафрейм
    :param label: Метка нужна исследовать
    :return: Не возрашать значения
    """
    hists = count_data_histogram(df5, label)
    color = ['b', 'g', 'r']
    for i in range(3):
        plt.plot(hists[i], color=color[i])
    plt.title('Гистограмма изображения')
    plt.ylabel('Плотность пикселей')
    plt.xlabel('Яркость оттенков')
    plt.xlim([0, 256])
    plt.show()


def main():
    df = pd.read_csv('annotation.csv')
    df.drop(['Relative Path'], axis=1, inplace=True)
    df = df.rename(columns={'Absolute Path': 'Absolute_Path'})
    df['Numerical'] = numerical(df['Label'])
    df['Width'], df['Height'], df['Channels'] = img_shape(df['Absolute_Path'])
    draw_histogram(df, 'cat')


if __name__ == "__main__":
    main()