refer:<br>[ParseTree操作若干-Tregex and Stanford CoreNLP](http://www.shuang0420.com/2017/03/24/ParseTree%E6%93%8D%E4%BD%9C%E8%8B%A5%E5%B9%B2-Tregex%20and%20Stanford%20CoreNLP/)<br>
more refer:<br>
[整理了Stanford NLP的部分使用方法](https://github.com/liu-nlper/Stanford-NLP-Usage)


### Tregex

Tregex 用来做句子层面的识别及操作，简单理解就是**关于 tree 的 regex**（:thumbsup:）。

Tregex语法知识：

[The Wonderful World of Tregex](https://nlp.stanford.edu/software/tregex/The_Wonderful_World_of_Tregex.ppt/)<br>[Tregex](https://nlp.stanford.edu/software/tregex.shtml)<br>[Tregex-faq](https://nlp.stanford.edu/software/tregex-faq.html)



```python
import requests

url = "http://localhost:9000/tregex"
request_params = {"pattern": "(NP[$VP]>S)|(NP[$VP]>S\\n)|(NP\\n[$VP]>S)|(NP\\n[$VP]>S\\n)"}
text = "Pusheen and Smitha walked along the beach."
r = requests.post(url, data=text, params=request_params)
print(r.json())
```

output: `{u'sentences': [{u'0': {u'namedNodes': [], u'match': u'(NP (NNP Pusheen)\n  (CC and)\n  (NNP Smitha))\n'}}]}`



```python
# Tregex - 提取同位语
from __future__ import division, unicode_literals
import nltk
from nltk.parse.stanford import StanfordParser
import requests

APPOSITION = "NP=n1 < (NP=n2 $.. (/,/ $.. NP=n3))"

def getAppositions(tree):
    url = "http://localhost:9000/tregex"
    request_params = {"pattern": APPOSITION}
    r = requests.post(url, data=text, params=request_params)
    return r.json()


text = 'Harry Potter, a young boy, is very famous in US'
print getAppositions(text)
```

output: `{u'sentences': [{u'0': {u'namedNodes': [{u'n1': u'(NP\n  (NP (NNP Harry) (NNP Potter))\n  (, ,)\n  (NP (DT a) (JJ young) (NN boy))\n  (, ,))\n'}, {u'n2': u'(NP (NNP Harry) (NNP Potter))\n'}, {u'n3': u'(NP (DT a) (JJ young) (NN boy))\n'}], u'match': u'(NP\n  (NP (NNP Harry) (NNP Potter))\n  (, ,)\n  (NP (DT a) (JJ young) (NN boy))\n  (, ,))\n'}}]}`



### coref

https://github.com/stanfordnlp/CoreNLP/issues/617



### dcoref



```python
import requests

url = 'http://localhost:9000/?properties={"annotators": "tokenize,ssplit,pos,lemma,ner,depparse,dcoref", "outputFormat": "text"}'
text='狗蛋他这个人怎么样？'
r = requests.post(url, data=text.encode('utf-8'))
print(r.content)
```

output: `java.util.concurrent.ExecutionException: java.lang.IllegalArgumentException: No head rule defined for IP using class edu.stanford.nlp.trees.SemanticHeadFinder in ...` 

solution:

https://stanfordnlp.github.io/CoreNLP/coref.html

https://nlp.stanford.edu/software/dcoref.html

https://stackoverflow.com/questions/30010340/how-do-i-use-chinese-co-reference-in-stanford-corenlp-3-5-2

https://github.com/jingyuanz/stanfordnlp_chinese_coreference



### parse

```python
import requests

url = 'http://localhost:9000/?properties={"annotators": "parse", "outputFormat": "text"}'
text='Harry Potter, a young boy, is very famous in US'
r = requests.post(url, data=text)
print(r.content)
```

output: `...`



