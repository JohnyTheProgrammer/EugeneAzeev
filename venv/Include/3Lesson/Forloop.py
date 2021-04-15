
#from Include.gggg.Testfile import*

#import sys
extend_lisst = [18,23,65,94,58,119,15,3,75,47]
new_some_list = [[18,23,65,0,94,58,119,15,35,75,15,47],
                 [14,23,34,4,55,89,144,10,34,18,23,65],
                 [18,23,65,0,94,58,119,15,35,75,15,47],
                 [14,23,34,4,55,89,144,10,34,18,23,65],
                 [18,23,65,0,94,58,119,15,35,75,15,47],
                 [14,23,34,4,55,89,144,10,34,18,23,65]]



def double_loop_word_work(text, keywor, number):

    searched_words = []
    word_to_compare = []
    cheking_number = 0

    for i, item in enumerate(text):
        if text[i:(i+(len(keywor)))] == keywor:
            searched_words.append(text[(i+len(keywor)) + 1 :(i+len(keywor)) + number])

    for ddd in searched_words:
        print(keywor,' ---- ', ddd)
    return searched_words
longstr = "Golang is the best project"
shortstr = ",but not always"

strlist = ' and, Python, and Java and,'

#print(strlist.count('and'))

print(strlist.replace('Java', 'C++'))