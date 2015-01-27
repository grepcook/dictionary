# coding: utf-8

fin1 = open("dictionary.txt", "r")
fin2 = open("words.txt", "r")
word_set = set()

for w in fin1:
    word_set.add(w.lower())
for w in fin2:
    word_set.add(w.lower())

print (len(word_set))

lw = list(word_set)
lw.sort()
fout = open("temp.txt", "w")
fout.writelines(lw)
fout.close()
fin1.close()
fin2.close()

