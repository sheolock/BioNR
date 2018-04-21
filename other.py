from collections import Counter
from utils import xmltoword, participle
from nltk.tokenize import word_tokenize
import os, fnmatch


def get_word():
    word_list = []
    i = 0
    for words in participle.words_of_file(
            'D:\GitHub\BioNR\Genia4ERtraining\Genia4ERtask1.iob2'):
        if i == 0:
            i = +1
        else:
            if words not in word_list:
                word_list.append(words)
            i = 0
    print(len(word_list))
    print(word_list)


def get_tag_text(filename, filepath, tag):

    title_list = []
    #################################################
    # Method 1:
    #################################################

    title_list = xmltoword.get_dom_text(filepath + '/' + filename, tag)

    #################################################

    #################################################
    # Method 2:
    #################################################

    # article_title = Counter()
    # data = xmltoword.parse_and_remove('data/pubmed/pubmed18n0001.xml',
    #                                   'PubmedArticle/MedlineCitation/Article')
    # for pothole in data:
    #     article_title[pothole.findtext('ArticleTitle')] += 1
    # for title, num in article_title.most_common():
    #     title_list.append(title)

    ##################################################

    return title_list


def all_files(root, patterns='*', single_level=False, yield_folders=False):
    patterns = patterns.split(';')
    for paths, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(paths, name)
                    break
        if single_level:
            break


if __name__ == "__main__":

    title_file = open('D:/GitHub/BioNR/data/title.txt', 'a', encoding='UTF-8')
    for root, dirs, files in os.walk('D:/GitHub/BioNR/data/pubmed'):
        for xml_file in files:
            title_list = get_tag_text(
                xml_file, root,
                'PubmedArticle/MedlineCitation/Article/ArticleTitle')
            for title in title_list:
                title_file.writelines(title + '\n')
            print(str(xml_file) + ' ' + str(len(title_list)))
    title_file.close()
    title_file = open('D:/GitHub/BioNR/data/title.txt', encoding='UTF-8')
    try:
        all_title = title_file.read()
    finally:
        title_file.close()
    title_split = word_tokenize(all_title, language='english')
    title_file = open('D:/GitHub/BioNR/data/title.txt', 'w', encoding='UTF-8')
    for title in title_split:
        title_file.write(title + '\n')
    title_file.close()

    abstract_file = open(
        'D:/GitHub/BioNR/data/abstract.txt', 'a', encoding='UTF-8')
    for root, dirs, files in os.walk('D:/GitHub/BioNR/data/pubmed'):
        for xml_file in files:
            abstract_list = get_tag_text(
                xml_file, root,
                'PubmedArticle/MedlineCitation/Article/Abstract/AbstractText')
            for abstract in abstract_list:
                abstract_file.writelines(abstract + '\n')
            print(str(xml_file) + ' ' + str(len(abstract_list)))
    abstract_file.close()
    abstract_file = open('D:/GitHub/BioNR/data/abstract.txt', encoding='UTF-8')
    try:
        all_abstract = abstract_file.read()
    finally:
        abstract_file.close()
    abstract_split = word_tokenize(all_abstract, language='english')
    abstract_file = open(
        'D:/GitHub/BioNR/data/abstract.txt', 'w', encoding='UTF-8')
    for abstract in abstract_split:
        abstract_file.write(abstract + '\n')
    abstract_file.close()
