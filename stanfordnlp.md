more refer:

http://fancyerii.github.io/2019/02/26/stanfordnlp/





https://github.com/stanfordnlp/stanfordnlp

Chinese (traditional)  [download](http://nlp.stanford.edu/software/conll_2018/zh_gsd_models.zip) 0.1.0 



refer:

https://stackoverflow.com/questions/29542569/stanford-nlp-corenlp-dont-do-sentence-split-for-chinese



### install 

without or with cuda

```
conda install pytorch-cpu torchvision-cpu -c pytorch
conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
```

https://pytorch.org/

[Win10下 Java环境变量配置](https://www.cnblogs.com/cnwutianhao/p/5487758.html)

[Access to Java Stanford CoreNLP Server](https://github.com/stanfordnlp/stanfordnlp#access-to-java-stanford-corenlp-server) 



[Make torch dependency optional, just use the Java Stanford CoreNLP Server](https://github.com/stanfordnlp/stanfordnlp/issues/54)

1. Force installing the package by ignoring all dependencies with: `pip install --no-deps stanfordnlp`
2. Create a `requirements.txt` file manually with all required packages except `torch` (see end of reply);
3. Run `pip install -r requirements.txt` to install everything but `torch`.

`requirements.txt` file:

```
numpy
protobuf
requests
tqdm
...
```



### chinese

CoreNLP Client Options: https://stanfordnlp.github.io/stanfordnlp/corenlp_client.html

#### properties

[StanfordCoreNLP-chinese.properties](https://github.com/stanfordnlp/CoreNLP/blob/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-chinese.properties) 

default: `ssplit.boundaryTokenRegex = [.。]|[!?！？]+`

maybe have to replaced the Chinese punctuation with its Unicode formats: `[.\u3002]|[!?\uFF01\uFF1F]+`



#### encoding problem

https://github.com/stanfordnlp/stanfordnlp/issues/53





### update

client.py

```python
class CoreNLPClient(RobustService):
...
	def update(self, doc, annotators=None, properties=None):
        if properties is None:
            properties = self.default_properties
            properties.update({
                'annotators': ','.join(annotators or self.default_annotators),
                'inputFormat': 'serialized',
                'outputFormat': 'serialized',
                'serializer': 'edu.stanford.nlp.pipeline.ProtobufAnnotationSerializer'
            })
```



### tokensregex/semgrex/tregrex/__regex

https://nlp.stanford.edu/software/tokensregex.html

https://stanfordnlp.github.io/CoreNLP/tokensregex.html

client.py

```python
class CoreNLPClient(RobustService):
...
    def tokensregex(self, text, pattern, filter=False, to_words=False, annotators=None, properties=None):
        # this is required for some reason
        matches = self.__regex('/tokensregex', text, pattern, filter, annotators, properties)
        if to_words:
            matches = regex_matches_to_indexed_words(matches)
        return matches

    def semgrex(self, text, pattern, filter=False, to_words=False, annotators=None, properties=None):
        matches = self.__regex('/semgrex', text, pattern, filter, annotators, properties)
        if to_words:
            matches = regex_matches_to_indexed_words(matches)
        return matches

    def tregrex(self, text, pattern, filter=False, annotators=None, properties=None):
        return self.__regex('/tregex', text, pattern, filter, annotators, properties)

    def __regex(self, path, text, pattern, filter, annotators=None, properties=None):
        """Send a regex-related request to the CoreNLP server.
        :param (str | unicode) path: the path for the regex endpoint
        :param text: raw text for the CoreNLPServer to apply the regex
        :param (str | unicode) pattern: regex pattern
        :param (bool) filter: option to filter sentences that contain matches, if false returns matches
        :param properties: option to filter sentences that contain matches, if false returns matches
        :return: request result
        """
        ...
```



### RegexNERAnnotator

https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/RegexNERAnnotator.html

https://github.com/stanfordnlp/CoreNLP/blob/master/src/edu/stanford/nlp/ie/regexp/RegexNERSequenceClassifier.java

This class adds NER information to an annotation using the <u>RegexNERSequenceClassifier</u>. Adds NER information to each CoreLabel as a NamedEntityTagAnnotation.

> RegexNERSequenceClassifier
>
>  * This class isn't implemented very efficiently, since every regex is evaluated at every token position.
>  * So it can and does get quite slow if you have a lot of patterns in your NER rules.
>  * {@code TokensRegex} is a more general framework to provide the functionality of this class.
>  * But at present we still use this class.
>
> 
>
>    // This is pretty deathly slow. It loops over each entry, and then loops over each document token for it.
>     // We could gain by compiling into disjunctions patterns for the same class with the same priorities and restrictions?





### TokensRegexNERAnnotator 

https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/TokensRegexNERAnnotator.html

TokensRegexNERAnnotator labels tokens with types based on a simple manual mapping from regular expressions to the types of the entities they are meant to describe. 

The user provides a file formatted as follows:

```python
regex1	TYPE	overwritableType1,Type2...		priority
```

where each argument is tab-separated, and the last two arguments are optional. Several regexes can be associated with a single type. In the case where multiple regexes match a phrase, the priority ranking (higher priority is favored) is used to choose between the possible types. When the priority is the same, then longer matches are favored. 

```python
The first column regex may follow one of two formats:

1. A TokensRegex expression (marked by starting with "( " and ending with " )". See TokenSequencePattern for TokensRegex syntax. 
Example: ( /University/ /of/ [ {ner:LOCATION} ] ) SCHOOL
2. a sequence of regex, each separated by whitespace (matching "\s+"). 
Example: Stanford SCHOOL 
The regex will match if the successive regex match a sequence of tokens in the input. Spaces can only be used to separate regular expression tokens; within tokens \s or similar non-space representations need to be used instead. 
Notes: Following Java regex conventions, some characters in the file need to be escaped. Only a single backslash should be used though, as these are not String literals. The input to RegexNER will have already been tokenized. So, for example, with our usual English tokenization, things like genitives and commas at the end of words will be separated in the input and matched as a separate token.
```

TokensRegexNERAnnotator is similar to [`RegexNERAnnotator`](https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/RegexNERAnnotator.html) but uses TokensRegex as the underlying library for matching regular expressions. This allows for more flexibility in the types of expressions matched as well as utilizing any optimization that is included in the TokensRegex library.

Main differences from [`RegexNERAnnotator`](https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/RegexNERAnnotator.html):

- Supports annotation of fields other than the `NamedEntityTagAnnotation` field
- Supports both TokensRegex patterns and patterns over the text of the tokens
- <u>When NER annotation can be overwritten based on the original NER labels. The rules for when the new NER labels are used are given below:</u> 
  If the found expression overlaps with a previous NER phrase, then the NER labels are not replaced. 
  *Example*: Old NER phrase: `The ABC Company`, Found Phrase: `ABC => `Old NER labels are not replaced. 
  If the found expression has inconsistent NER tags among the tokens, then the NER labels are replaced. 
  *Example*: Old NER phrase: `The/O ABC/MISC Company/ORG => The/ORG ABC/ORG Company/ORG`
- How `validpospattern` is handled for POS tags is specified by `PosMatchType`
- By default, there is no `validPosPattern`
- By default, both O and MISC is always replaced



Configuration:

| Field                       | Description                                                  | Default                                             |
| --------------------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| `mapping`                   | Comma separated list of mapping files to use                 | `edu/stanford/nlp/models/kbp/regexner_caseless.tab` |
| `mapping.header`            | Comma separated list of header fields (or `true` if header is specified in the file) | pattern,ner,overwrite,priority,group                |
| `mapping.field.<fieldname>` | Class mapping for annotation fields other than ner           |                                                     |
| `commonWords`               | Comma separated list of files for common words to not annotate (in case your mapping isn't very clean) |                                                     |
| `backgroundSymbol`          | Comma separated list of NER labels to always replace         | `O,MISC`                                            |
| `posmatchtype`              | How should `validpospattern` be used to match the POS of the tokens. `MATCH_ALL_TOKENS` - All tokens has to match. `MATCH_AT_LEAST_ONE_TOKEN` - At least one token has to match. `MATCH_ONE_TOKEN_PHRASE_ONLY` - Only has to match for one token phrases. | `MATCH_AT_LEAST_ONE_TOKEN`                          |
| `validpospattern`           | Regular expression pattern for matching POS tags.            |                                                     |
| `noDefaultOverwriteLabels`  | Comma separated list of output types for which default NER labels are not overwritten. For these types, only if the matched expression has NER type matching the specified overwriteableType for the regex will the NER type be overwritten. |                                                     |
| `ignoreCase`                | If true, case is ignored                                     | `false`                                             |
| `verbose`                   | If true, turns on extra debugging messages.                  | `false`                                             |

Example of properties:

```python
    "regexner.mapping": "edu/stanford/nlp/models/kbp/chinese/gazetteers/cn_regexner_mapping.tab;path/custom_regexner_mapping_ner.tab"
    ...
    "regexner.commonWords":...
    ....
    "regexner.ignoreCase": "true"
```





### regexner

https://stanfordnlp.github.io/CoreNLP/ner.html#regexner-rules-format

https://stanfordnlp.github.io/CoreNLP/ner.html#customizing-the-fine-grained-ner

https://nlp.stanford.edu/software/regexner.html good example!

[How to manage a label with more than one type in regexner](https://github.com/stanfordnlp/CoreNLP/issues/428)



refer:

https://github.com/stanfordnlp/CoreNLP/issues/495



custom  for regexner:

```python
    "regexner.mapping": "edu/stanford/nlp/models/kbp/chinese/gazetteers/cn_regexner_mapping.tab;path/custom_regexner_mapping_ner.tab"
```

Here is an example entry in `custom_regexner_mapping_ner.tab`:

```
london	CITY	LOCATION		3.0
```

The first field has text to match and the second field has the entity category to assign. (Note that you *must* have a **tab** character between the text and the category. Other spaces will not do.)

In a little more detail now, the first field is not just matched as <u>a string</u>, but as <u>a sequence of one or more space-separated patterns</u>. That is, CoreNLP divides text into tokens and each whitespace-separated pattern in the first field has to match against successive tokens in the text. Each pattern is a (standard Java) regular expression. If the regular expressions match a sequence of tokens, the tokens will be relabeled as the category in the second column. Providing that you avoid certain special characters, a pattern can just be <u>a regular String</u>, and so you can use RegexNER as a gazetteer. However, you can also do somewhat fancier things once you know that you can match regular expressions. 

The third column means that existing LOCATION tags can be overwritten as CITY. RegexNER will not overwrite an existing entity assignment, unless you give it permission in a third tab-separated column, which contains <u>a comma-separated list of entity types</u> that can be overwritten. Only the non-entity O label can always be overwritten, but you can specify extra entity tags which can always be overwritten as well.

The fourth column can be used to give rules a priority.  If <u>multiple rules match</u>, the result is undefined unless you give the rules a priority. There are <u>two tabs</u> between the entity label and the priority. Rules with no explicitly given priority have priority 1.0.



regex confict (无法复现): such as multiple entity rules will decide by probability, should resolved by the priority column. 

```python
登陆 失败	KEY_WORD		3.0
登陆	KEY_WORD		
失败	KEY_WORD		
```



### ner

https://stanfordnlp.github.io/CoreNLP/ner.html

https://stanfordnlp.github.io/CoreNLP/regexner.html

https://nlp.stanford.edu/software/crf-faq.html

https://github.com/stanfordnlp/CoreNLP/blob/master/src/edu/stanford/nlp/ie/NERClassifierCombiner.java

ner - edu.stanford.nlp.pipeline.NERCombinerAnnotator

regexner - TokensRegexNERAnnotator is  run as a sub-annotator of  a comprehensive named entity recognition process by the NERCombinerAnnotator



NERClassifierCombiner, this annotator will run several named entity recognizers and then combine their results but it can run just <u>a single annotator</u> or <u>only rule-based quantity NER</u>.

<u>Named entities</u> are recognized using <u>a combination of three CRF sequence taggers</u> trained on various corpora, including CoNLL, ACE, MUC, and ERE corpora. <u>Numerical entities</u> are recognized using <u>a rule-based system</u>.



### segmenter

https://nlp.stanford.edu/software/segmenter-faq.html

custom dict for segmenter:

```python
    "segment.serDictionary": "edu/stanford/nlp/models/segmenter/chinese/dict-chris6.ser.gz,path/custom_segment_dict.txt",
```



### annotator

https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/Annotator.html

We extensively use Properties objects to configure each Annotator. In particular, CoreNLP has most of its properties in an informal namespace with properties names like "parse.maxlen" to specify that a property only applies to a parser annotator. There can also be global properties; they should not have any periods in their names. Each Annotator knows its own name; we assume these don't collide badly, though possibly two parsers could share the "parse.*" namespace. An Annotator should have a constructor that simply takes a Properties object. At this point, the Annotator should expect to be getting properties in namespaces. The classes that annotators call (like a concrete parser, tagger, or whatever) mainly expect properties not in namespaces. In general the annotator should subset the passed in properties to keep only global properties and ones in its own namespace, and then strip the namespace prefix from the latter properties.



### annotator dependencies

https://stanfordnlp.github.io/CoreNLP/annotators.html#annotator-dependencies



### without server

https://github.com/stanfordnlp/CoreNLP/issues/701

https://textminingonline.com/dive-into-nltk-part-vi-add-stanford-word-segmenter-interface-for-python-nltk

http://www.52nlp.cn/python%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86%E5%AE%9E%E8%B7%B5-%E5%9C%A8nltk%E4%B8%AD%E4%BD%BF%E7%94%A8%E6%96%AF%E5%9D%A6%E7%A6%8F%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%99%A8

The best you could do is make java calls with `subprocess`. 

method 1 - nltk

http://www.nltk.org/_modules/

tokenizer/tag/parse



method 2 - jpype

jvm_path = jpype.getDefaultJVMPath()
jvm_args = ["-Xmx1g", "-Djava.ext.dirs=%s" % ('/usr/local/share/stanford_nltk/stanford-segmenter-2015-12-09/')]
jpype.startJVM(jvm_path, jvm_args[0], jvm_args[1])

AR_Segmenter = jpype.JClass('edu.stanford.nlp.international.arabic.process.ArabicSegmenter')
Properties = jpype.JClass('java.util.Properties')

options = Properties()
options.setProperty('orthoOptions','removeProMarker')
options.setProperty('loadClassifier',ARClassifierData)
ARSegmenter = AR_Segmenter(options)
if ARSegmenter.flags.loadClassifier:
ARSegmenter.loadSegmenter(ARSegmenter.flags.loadClassifier, options)



method 3 - 

I have met the same problem and resolved by Queue technology. Basic idea is, to create multiple Docker containers and give them the different role. A container used as Input, this container just get the input strings and put them into RabbitMQ queue. On the other side of the queue, there are multiple containers used as workers, each of them doing the job that loading analysis process program (which is the code in showing console of this article). And then, these workers put the results to another queue in RabbitMQ, and on the other side of this queue, there is a container used as Output. This system architecture used to process multiple messages in parallel.



### dedicated-server

https://stanfordnlp.github.io/CoreNLP/corenlp-server.html#dedicated-server



### close port

http://www.nltk.org/_modules/nltk/parse/corenlp.html

```python
def try_port(port=0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))

    p = sock.getsockname()[1]
    sock.close()

    return p

...

        if port is None:
            try:
                port = try_port(9000)
            except socket.error:
                port = try_port()
                corenlp_options.append(str(port))
        else:
            try_port(port)
```



### bash/python (star/stop server)

refer: https://pastebin.com/j1mGFYV1

```bash
#!/bin/bash
#
# A script to start/stop the CoreNLP server on port 80, made
# in particular for the configuration running at corenlp.run.
# This script should be placed into:
#
#   /etc/init.d/corenlp
#
# To run it at startup, link to the script using:
#
#   ln -s /etc/init.d/conenlp /etc/rc.2/S75corenlp
#
# Usage:
#
#    service corenlp [start|stop]
#    ./corenlp [start|stop]
# 

#
# Set this to the username you would like to use to run the server.
# Make sure that this user can authbind to port 80!
#
SERVER_USER="nlp"
CORENLP_DIR="/opt/corenlp"


do_start()
{
  if [ -e "$CORENLP_DIR/corenlp.shutdown" ]; then
    echo "CoreNLP server is already running!"
    echo "If you are sure this is a mistake, delete the file:"
    echo "$CORENLP_DIR/corenlp.shutdown"
  else
    export CLASSPATH=""
    for JAR in `find "$CORENLP_DIR" -name "*.jar"`; do
      CLASSPATH="$CLASSPATH:$JAR"
    done
    nohup su "$SERVER_USER" -c "/usr/bin/authbind --deep java -Djava.net.preferIPv4Stack=true -Xms2048m -Xmx4096m -XX:MaxNewSize=1024m  -Djava.io.tmpdir="$CORENLP_DIR" -cp "$CLASSPATH" -mx15g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 80 -timeout 650000 " \
      > "$CORENLP_DIR/stdout.log" 2> "$CORENLP_DIR/stderr.log" &
    echo "CoreNLP server started."
  fi  
}

do_stop() 
{
  if [ ! -e "$CORENLP_DIR/corenlp.shutdown" ]; then
    echo "CoreNLP server is not running"
  else
    KEY=`cat "$CORENLP_DIR/corenlp.shutdown"`
    curl "localhost/shutdown?key=$KEY"
    echo "CoreNLP server stopped"
  fi
}

do_restart()
{
  do_stop
  sleep 3
  do_start
}

case $1 in
start) do_start
;;
stop) do_stop
;;
restart) do_restart
;;
esac
```

Code explain:

`-Djava.io.tmpdir=`   default parameters, which is the `/tmp/` in Linux, `C:\Users\登录用户~1\AppData\Local\Temp\` in Windows.

```bash
-e file
    True if file exists. 
```

https://stackoverflow.com/questions/321348/bash-if-a-vs-e-option



#### stop server

https://stanfordnlp.github.io/CoreNLP/corenlp-server.html#stopping-the-server

https://stackoverflow.com/questions/46298404/standard-way-to-start-and-stop-stanfordcorenlp-server-in-python

https://stackoverflow.com/questions/45886128/unable-to-set-up-my-own-stanford-corenlp-server-with-error-could-not-delete-shu

```python
# linux
import requests
from commands import getoutput
import tempfile
tempfile.gettempdir()
# /tmp

url = "http://localhost:9000/shutdown?"
shutdown_key = getoutput("cat /tmp/corenlp.shutdown")
r = requests.post(url,data="",params={"key": shutdown_key})
```

```python
# windows
import requests
from commands import getoutput
import tempfile
tempfile.gettempdir()
# C:/Users/登录用户~1/AppData/Local/Temp

url = "http://localhost:9000/shutdown?"
shutdown_key = getoutput("type C:/Users/登录用户~1/AppData/Local/Temp/corenlp.shutdown")
r = requests.post(url,data="",params={"key": shutdown_key})
```



### Memory/Batching To Maximize Pipeline Speed

https://stanfordnlp.github.io/CoreNLP/memory-time.html



https://github.com/stanfordnlp/stanfordnlp



### some useful functions

```
	...
    # get the first token of the first sentence
    print('---')
    print('first token of first sentence')
    token = sentence.token[0]
    print(token.word)
    print(token.originalText)
    print(token.lemma)
    ...
    
client.start()
client.update(annotators=None, properties=None)
client.stop()
```



### Question

https://stanfordnlp.github.io/CoreNLP/faq.html



#### dynamically-add-properties-to-stanfordcorenlp-annotator-or-pipeline

https://stackoverflow.com/questions/46194378/dynamically-add-properties-to-stanfordcorenlp-annotator-or-pipeline

https://stackoverflow.com/questions/26245422/stanford-corenlp-use-partial-existing-annotation

It sounds like you want to build a first pipeline, run it on a set of documents, clear the memory, and then build a second pipeline and run it on the set of documents.

If you run the second pipeline on the same set of Annotations, it will just pick up where the first pipeline finished. But you need to set `enforceRequirements` to `false` so the second pipeline won't crash. Also after you are done using the first pipeline you should run `StanfordCoreNLP.clearAnnotatorPool();` to get rid of the models or you won't solve the memory issue.



#### how to deal with conflict between ner model and regexner ?























