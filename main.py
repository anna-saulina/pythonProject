text = 'Введенную с клавиатуры строку вывести на экран наоборот (использовать цикл).'
length = len(text)
text_revers = ""
while length > 0:
    text_revers += text[length - 1]
    length = length - 1

print(text_revers)
