# coding: utf-8

fin1 = open("dictionary.txt", "r")
fin2 = open("words.txt", "r")
word_set = set()
def add_word(w):
    word_set.add(w)
    word_set.add(w.replace(w[0], w[0].upper(), 1))
for w in fin1:
    add_word(w)

for w in fin2:
    add_word(w)

print (len(word_set))

lw = list(word_set)
lw.sort()
fout = open("temp.txt", "w")
fout.writelines(lw)
fout.close()
fin1.close()
fin2.close()

