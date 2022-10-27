# Напишите программу, удаляющую из текста все слова содержащие "абв".

my_text = 'Тут должен быть любой текст по желанию пользователя. Хоть алфавит, а,б,в,г,д и т.д'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)