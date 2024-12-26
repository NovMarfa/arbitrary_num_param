def single_root_words (root_word, *other_words):
    same_words = []
    root_word_u = root_word.upper()
    for word in other_words:
        word_u = word.upper()                               # не зависит от регистра
        if word_u in root_word_u or root_word_u in word_u:  # функция содержит одно из слов и наоборот
            same_words.append(word)                         # добавляет в список
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)