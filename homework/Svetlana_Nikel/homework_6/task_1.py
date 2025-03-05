text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
fin_words = []
for word in words:
    if word[-1] in ['.', ',']:  # ищем слова в конце которых есть точка или запятая
        new_words = word[:-1] + 'ing' + word[-1]  # добавляем 'ing' и знак препинания
    else:
        new_words = word + 'ing'  # прибавляем приставку 'ing' во все остальные слова
    fin_words.append(new_words)  # добавляем слова в новый список
print(' '.join(fin_words))
