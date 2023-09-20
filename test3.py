LETTERS = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯWRT124578"
ALPHABETS = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def read_file(filename: str) -> str:
    """
    Эта функция для чтения данных в файле

    :param filename: Имя файла, который прочитать
    :return: Не возращается
    """
    with open(f'{filename}.txt', "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename: str, data: str) -> None:
    """
    Эта функция для записи данных в файл

    :param filename: Имя файла, в котором написать
    :param data: Данные
    :return: Не возращается
    """
    with open(f'{filename}.txt', "w", encoding='utf-8') as file:
        file.write(data)


def substitutions() -> dict:
    """
    Эта функция для замены букв в разных случаях

    :return: Тип данных dict имеет форму (key:letter)
    """
    dict1 = {}

    for letter in ALPHABETS:
        pos = ALPHABETS.find(letter)
        if pos < 28:
            dict1[letter] = ALPHABETS[pos + 3]
        else:
            dict1[letter] = ALPHABETS[pos - 28]

    with open("task1-key_value.txt", "w", encoding='utf-8') as f:
        f.write(str(dict1))
    return dict1


def encryption(filename: str) -> None:
    """
    Эта функция для шифрования 1 текста и записи в файл

    :param filename: Имя файла, в котором написать
    :return: Не возращается
    """
    with open('task1-original_text.txt', "r", encoding='utf-8') as f:
        text = f.read().upper()

    dict1 = substitutions()
    text = text.translate(str.maketrans(dict1))
    write_file(filename, text)


def count_frequencies(text: str) -> None:
    """
    Эта функция для подсчета букв частот в тексте

    :param text: Документ
    :return: Не возращается
    """
    text = text.upper()
    lenght = len(text)
    fre = {}

    for letter in LETTERS:
        fre[letter] = str(float(text.count(letter) / lenght))

    fre = sorted(fre.items(), key=lambda x: x[1], reverse=True)

    with open("task2_frequencies.txt", "w", encoding='utf-8') as f:
        for ele in fre:
            f.write(str(ele) + str('\n'))


def decode(text: str, filename: str) -> None:
    """
    Эта функция для декодирования и последующей записи данных в файл

    :param text: Данные были закодированы
    :param filename: Имя файла, в котором написать
    :return: Не возращается
    """
    text = text.replace(' ', 'е')
    text = text.replace('Х', ' ')
    text = text.replace('е', 'и')
    text = text.replace('1', 'л')
    text = text.replace('2', 'м')
    text = text.replace('Д', 'н')
    text = text.replace('8', 'э')
    text = text.replace('Б', 'к')
    text = text.replace('Ч', 'а')
    text = text.replace('Е', 'о')
    text = text.replace('Ъ', 'г')
    text = text.replace('T', 'р')
    text = text.replace('И', 'с')
    text = text.replace('R', 'п')
    text = text.replace('Й', 'ф')
    text = text.replace('>', 'ы')
    text = text.replace('Ы', 'е')
    text = text.replace('П', 'щ')
    text = text.replace('W', 'д')
    text = text.replace('К', 'у')
    text = text.replace('5', 'ч')
    text = text.replace('Щ', 'в')
    text = text.replace('Ф', 'я')
    text = text.replace('Я', 'з')
    text = text.replace('Ь', 'ж')
    text = text.replace('ф', 'т')
    text = text.replace('7', 'ь')
    text = text.replace('Л', 'ф')
    text = text.replace('О', 'ш')
    text = text.replace('4', 'ц')
    text = text.replace('А', 'й')
    text = text.replace('М', 'х')
    text = text.replace('У', 'ю')
    with open(f'{filename}.txt', "w", encoding='utf-8') as f:
        f.write(text)
    count_frequencies(text)
    print(text)


if __name__ == "__main__":
    encryption("task1-encode")
    text = read_file("cod7").upper()
    decode(text, 'task2-decode')
