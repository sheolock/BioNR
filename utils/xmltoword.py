from xml.etree.ElementTree import parse, iterparse


def get_dom_text(filepath, tag):
    result = []
    xml_file = open(filepath,encoding='UTF-8')
    dom = parse(xml_file)
    root = dom.getroot()
    for child_of_root in root.findall(tag):
        # result.append(Article.findtext(tag))
        # print(Article.findtext(tag))
        # for elem in child_of_root.iter(tag='tag'):
        #     print(elem.text)
        # print(child_of_root.tag)
        result.append(child_of_root.text)
    # print(len(result))
    xml_file.close()
    return result


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass