sentence = '贝拉克·侯赛因·奥巴马的身世复杂，1961年8月4日出生在美国夏威夷州檀香山市，父亲是来自肯尼亚的留学生，母亲是堪萨斯州白人。'

import os
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer

MODELDIR="D:/software/ltp_data_v3.4.0"

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))

words = segmentor.segment(sentence)
#print "\t".join(words)
postags = postagger.postag(words)
netags = recognizer.recognize(words, postags)
arcs = parser.parse(words, postags)

word_str = "|".join(words)
word_array = word_str.split("|")

pos_str = ' '.join(postags)
pos_array = pos_str.split(" ")

ner_str = ' '.join(netags)
ner_array = ner_str.split(" ")

arc_str = ' '.join(arcs)
arc_array = arc_str.split(" ")


def build_parse_child_dict(words, postags, arcs):
    """
    为句子中的每个词语维护一个保存句法依存儿子节点的字典
    Args:
        words: 分词列表
        postags: 词性列表
        arcs: 句法依存列表
    """
    child_dict_list = []
    for index in range(len(words)):
        child_dict = dict()
        for arc_index in range(len(arcs)):
            if arcs[arc_index].head == index + 1:
                if child_dict.__contains__(arcs[arc_index].relation):
                    child_dict[arcs[arc_index].relation].append(arc_index)
                else:
                    child_dict[arcs[arc_index].relation] = []
                    child_dict[arcs[arc_index].relation].append(arc_index)
        #if child_dict.has_key('SBV'):
        #    print words[index],child_dict['SBV']
        child_dict_list.append(child_dict)
    return child_dict_list


child_dict_list = build_parse_child_dict(words, postags, arcs)

