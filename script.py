def frequency_function(wmap, word):
    word_guess = 0
    for i in range(5):
        flag = 0
        for j in range(i):
            if word[i] == word[j]:
                flag = 1

        if flag == 0:
            word_guess += wmap[word[i]]

    return word_guess

def is_valid(word, dict_g, dict_y, list_x):
    valid = True
    for i in range(5):
        for letter in dict_g.keys():
            for index in dict_g[letter]:
                if word[index] not in letter:
                    valid = False
        for letter in dict_y.keys():
            if letter not in word:
                valid = False
            for index in dict_y[letter]:
                if word[index] in letter:
                    valid = False
        if word[i] in list_x and word[i] not in dict_g.keys() and word[i] not in dict_y.keys():
            valid = False
    return valid

text_file = open('en_words.txt','r', encoding='utf-8')
lines = text_file.readlines()
text_file.close()
i = 0 

print("Loading words...")

for word in lines:
    lines[i] = word.split('\n')[0]
    i += 1

print("Creating frequency...")

freq_map = {}

for word in lines:
    for i in range(5):
        if word[i] in freq_map.keys():
            freq_map[word[i]] += 1
        else:
            freq_map[word[i]] = 0

word_map = {}

for word in lines:
    word_map[word] = frequency_function(freq_map, word)

sorted_word_map = sorted(word_map.items(), key=lambda item: item[1], reverse=True)

print("Best words: {}".format(sorted_word_map[:5]))

hints = [{}, {}, []]

while(1):
    print("Input: ", end='')
    inp = input()
    w, l = inp.split(" ")
    for i in range(5):
        if l[i] == 'g':
            if w[i] in hints[0].keys():
                hints[0][w[i]].append(i)
            else:
                hints[0][w[i]] = [i]
        if l[i] == 'y':
            if w[i] in hints[1].keys():
                hints[1][w[i]].append(i)
            else:
                hints[1][w[i]] = [i]
        if l[i] == 'x':
            hints[2].append(w[i])
    
    lista_palabras = {}

    for word in lines:
        if is_valid(word, hints[0], hints[1], hints[2]):
            lista_palabras[word] = frequency_function(freq_map, word)

    sorted_lista_palabras = sorted(lista_palabras.items(), key=lambda item: item[1], reverse=True)

    print("Best words with hints: {}".format(sorted_lista_palabras[:5]))