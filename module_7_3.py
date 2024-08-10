class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as string:
                txt_to_str = str(string.read()).lower()
                need_to_del = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for delete in need_to_del:
                    txt_to_str = txt_to_str.replace(delete, '')
                word_list = txt_to_str.split()
                all_words = {string.name: word_list}
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            for search in range(len(words)):
                if word.lower() == words[search].lower():
                    return {name: words.index(words[search]) + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            find_list = []
            for find_word in range(len(words)):
                if word.lower() == words[find_word].lower():
                    find_list.append(word)
            return {name: len(find_list)}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
