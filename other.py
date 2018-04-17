import pretreat.participle

list=[]
i=0
for words in pretreat.participle.words_of_file('D:\GitHub\BioNR\Genia4ERtraining\Genia4ERtask1.iob2'):
    if i==0:
        i=+1
    else:
        if words not in list:
            list.append(words)
        i=0
print(len(list))
print(list)