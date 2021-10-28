import os


class AddDirectoryAndWord:
    """ This class need for input information about directory and about search word"""

    def __init__(self):
        self.link = input('Write directory folder books!! Example: /Users/andrewsalavei/Downloads/books :')
        self.search_word = list(input('Write search word(Через пробел.Регистр значение не имеет) :').split())
        pass


class Directory(AddDirectoryAndWord):
    """ A class for connecting to a directory and searching for txt files, as well as for a cycle with search for words"""

    def __init__(self):
        super(Directory, self).__init__()

    def dir_search(self):
        for file in os.listdir(self.link):
            if file.endswith('.txt'):
                with open(file, 'r') as f:
                    for i in f:
                        for j in self.search_word:
                            if j.lower() in i.lower():
                                print(f'слово "{j}" есть в этой книге: {file}')


d = Directory()
d.dir_search()
