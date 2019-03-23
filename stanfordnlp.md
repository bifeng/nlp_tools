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















