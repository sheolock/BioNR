import participle
from gensim.models import word2vec

sentences = word2vec.Text8Corpus(
    'D:\GitHub\BioNR\Genia4ERtraining\Genia4ERtask1.iob2')
model = word2vec.Word2Vec(sentences, sg=1, size=300, workers=4)

print(type(model['peri-kappa']))
print(len(model['peri-kappa']))
print(model['peri-kappa'])

model.wv.save_word2vec_format(r'D:\GitHub\BioNR\300.txt', binary=False)