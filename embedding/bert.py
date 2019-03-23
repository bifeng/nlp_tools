from bert_serving.client import BertClient
bc = BertClient(ip='192.168.1.97')
bc.encode(['吃饭没'])


# http://192.168.1.97:8889/sentence_sim/?ques1=吃饭没&吃饭没&ques2=你好
