import os
import sqlite3
import re
class WordOperation:
    def __init__(self, folderpath):
        try:
            self.folderpath=folderpath
        except Exception as e:
            raise Exception(f"something went wrong to initialize the process: {str(e)}")

    def getAllWords(self):
        '''Returns list of words present in files'''
        try:
            folder = self.folderpath
            files = os.listdir(folder)
            list_of_words = []
            for file in files:
                with open(f'{folder}/{file}', 'r', encoding='utf-8') as f:
                    l = [line.rstrip() for line in f.readlines()]
                    list_of_words += l
            return list_of_words
        except Exception as e:
            raise Exception(f"something went wrong to get all words")

    def getWordAndCount(self, show_words=5):
        '''Returns list of tuples of each word and its count'''
        try:
            list_of_words=self.getAllWords()
            check_list = []
            word_count_list = []
            i=0
            for word in list_of_words:
                if word not in check_list:
                    i+=1
                    if i>show_words:
                        break
                    count = list_of_words.count(word)
                    word_count_list.append((word, count))
                    check_list.append(word)

            return word_count_list
        except Exception as e:
            raise Exception(f"something went wrong to get word and its count:{str(e)}")

    def getAlphabetAndCount(self):
        '''Returns list of tuples of alphabet and count of words starting with that alphabet'''
        try:
            list_of_words=self.getAllWords()
            alphabet_count_list = []
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            for alphabet in alphabets:
                count = 0
                for word in list_of_words:
                    if word.lower().startswith(alphabet):
                        count += 1
                alphabet_count_list.append((alphabet, count))
            return alphabet_count_list
        except Exception as e:
            raise Exception(f"something went wrong to get alphabatically count of words: {str(e)}")

    def filterData(self):
        '''It filters the data inside files '''
        try:
            folder = self.folderpath
            files = os.listdir(folder)
            accepted_char = 'abcdefghijklmnopqrstuvwxyz'
            accepted_regex = re.compile('[a-zA-Z]')

            folder_for_filter = './filtered_words_file'
            if not os.path.exists(folder_for_filter):
                os.mkdir(folder_for_filter)

            for file in files:
                check_list = []
                with open(f'{folder}/{file}','r', encoding='utf-8') as f_read:
                    with open(f'{folder_for_filter}/filtered_{file}', 'w') as f_write:
                        l = [line.rstrip() for line in f_read.readlines()]
                        for word in l:
                            if (accepted_regex.search(word)):
                                for char in word:
                                    if char not in accepted_char:
                                        word = word.replace(char, '')
                                if word not in check_list:
                                    f_write.write(word + '\n')
                                check_list.append(word)
            return f"Files filtered and filtered files saved into filtered_word_file"
        except Exception as e:
            raise Exception(f"something went wrong to filter data inside files")

    def insertIntoSqliteDb(self, dbName):
        '''It insert data into sqlite db'''
        try:
            folder = self.folderpath
            files = os.listdir(folder)
            db = sqlite3.connect(dbName)
            cursor=db.cursor()
            cursor.execute('create table wordTable(vocab_enron text, vocab_kos text, vocab_nips text, vocab_nytimes text, vocab_pubmed text)')

            li = []
            for file in files:
                with open(f'{folder}/{file}', 'r', encoding='utf-8') as f:
                    l = [line.rstrip() for line in f.readlines()]
                    li.append(l)

            cursor = db.cursor()
            for i in zip(li[0], li[1], li[2], li[3], li[4]):
                cursor.execute("insert into wordTable values(?,?,?,?,?)",i)
            db.commit()
            return f"Data inserted into table:wordTable of Database:{dbName} successfully"
        except Exception as e:
            raise Exception(f"something went wrong to insert data into sqlite db:{str(e)}")

    def showData(self,dbName):
        '''It shows data of sqlite'''
        try:
            db = sqlite3.connect(dbName)
            cursor = db.cursor()
            data = cursor.execute(f'select * from wordTable')
            return data
        except Exception as e:
            raise Exception(f"something went wrong to show data from sqlite:{str(e)}")