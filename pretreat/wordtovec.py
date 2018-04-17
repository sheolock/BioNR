import pretreat.participle
from gensim.models import word2vec

sentences=word2vec.Text8Corpus('D:\GitHub\BioNR\Genia4ERtraining\Genia4ERtask1.iob2')
model=word2vec.Word2Vec(sentences)

print(type(model['peri-kappa']))
print(len(model['peri-kappa']))
print(model['peri-kappa'])