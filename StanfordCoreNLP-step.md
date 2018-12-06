[CoreNLP Python接口处理中文](https://blog.csdn.net/thriving_fcl/article/details/76595253?locationNum=4&fps=1)<br>[ParseTree操作若干-Tregex and Stanford CoreNLP](http://www.shuang0420.com/2017/03/24/ParseTree%E6%93%8D%E4%BD%9C%E8%8B%A5%E5%B9%B2-Tregex%20and%20Stanford%20CoreNLP/)<br>https://stanfordnlp.github.io/CoreNLP/corenlp-server.html<br>https://stanfordnlp.github.io/CoreNLP/api.html

1. download the [official java CoreNLP release](https://stanfordnlp.github.io/CoreNLP/#download), unzip it, and define an environment variable `$CORENLP_HOME` that points to the unzipped directory.

2. Other Human Languages Support

   download an additional model file and place it in the `.../stanford-corenlp-full-....-..-..` folder. For example, you should download the `stanford-chinese-corenlp-....-..-..-models.jar` file if you want to process Chinese.

3.  go to the path of the unzipped Stanford CoreNLP and execute the below command:

   `java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt`

   notes:

   Test the file `input.txt`, the output will be in the same path.

4. run the server using the selected annotators:

   ```java
   java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,ner,depparse,dcoref" -port 9000 -timeout 30000
   ```

   ```java
   # Run a server using Chinese properties
   java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -annotators "tokenize,ssplit,pos,lemma,ner,depparse,dcoref" -port 9000 -timeout 15000
   ```

5. sending HTTP request

   parse:

   ```python
   import requests
   
   url = 'http://localhost:9000/?properties={"annotators": "parse", "outputFormat": "text"}'
   text='Harry Potter, a young boy, is very famous in US'
   r = requests.post(url, data=text)
   print(r.content)
   ```

   output: `...`

6. using Stanford CoreNLP from NLTK

```python
from __future__ import division, unicode_literals
import nltk
from nltk.parse.stanford import StanfordParser

parser = StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

def getParserTree(line):
    '''
    return parse tree of the string
    :param line: string
    :return: list of tree nodes
    '''
    return list(parser.raw_parse(line))


# get parse tree
text = 'Harry Potter, a young boy, is very famous in US'
testTree = getParserTree(text)

print testTree
```

7. 网页版

   当server处于开启状态时，可以通过ip:port(如：localhost:9000)打开网页版的分析器。



