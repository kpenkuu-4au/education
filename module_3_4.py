def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words = [x.lower() for x in other_words]
    for i in other_words:
        if root_word in i or i in root_word:
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
