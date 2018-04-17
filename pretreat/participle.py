def words_of_file(filepath, line_to_words=str.split):
    file=open(filepath)
    for line in file:
        for word in line_to_words(line):
            yield word
    file.close()

def add_to_file(filepath, content):
    file=open(filepath,'a')
    file.write(content)
    file.close()