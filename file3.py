LETTERS = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯWRT124578"
ALPHABETS = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def read_file(filename: str) -> str:
    """
    This function for reading data in file

    :param filename: Name of file
    :return: No return
    """
    with open(f'{filename}.txt', "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename: str, data: str) -> None:
    """
    This function for writing data in file

    :param filename: Name of file
    :param data: data
    :return: No return
    """
    with open(f'{filename}.txt', "w", encoding='utf-8') as file:
        file.write(data)


def substitutions() -> dict:
    """
    This function for replacing letters in different cases

    :return: One dictionary has formatted (key:letter)
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
    This function for encrypting 1 text and write to file

    :param filename: Name of the file need to be written
    :return: No return
    """
    with open('task1-original_text.txt', "r", encoding='utf-8') as f:
        text = f.read().upper()

    dict1 = substitutions()
    text = text.translate(str.maketrans(dict1))
    write_file(filename, text)


def count_frequencies(text: str) -> None:
    """
    This function for counting frequencies letter in text

    :param text: Text
    :return: No return
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
    This function for decoding and write the data after that in file

    :param text: data was encoded
    :param filename: Name of file need to be written
    :return: No return
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


def main():
    encryption("task1-encode")
    text = read_file("cod7").upper()
    decode(text, 'task2-decode')


if __name__ == "__main__":
    main()
