refer: <br>http://ufal.mff.cuni.cz/conll2009-st/task-description.html



### Install

http://code.google.com/p/mate-tools/ 下载:<br>srl-4.31.tgz<br>CoNLL2009-ST-Chinese-ALL.anna-3.3.parser.model<br>CoNLL2009-ST-Chinese-ALL.anna-3.3.postagger.model<br>CoNLL2009-ST-Chinese-ALL.anna-3.3.srl-4.1.srl.model<br>将模型移至srl-4.31.tgz对应的model目录。

https://nlp.stanford.edu/software/segmenter.shtml 下载:<br>stanford-segmenter-2018-10-16.zip<br>将stanford-segmenter-2018-10-16.zip的data目录下ctb.gz、ctb.prop、dict-chris6.ser.gz及dict文件夹移至srl-4.31.tgz对应的data目录。

修改srl-4.31.tgz的scripts目录下run_http_server.sh对应的语言设置、模型及数据的路径信息。

示例：

[mate-tools](https://github.com/bifeng/nlp_tools/raw/master/chinese_srl)

### Output



核心的语义角色: <br>A0-5 六种，A0 通常表示动作的施事，A1通常表示动作的影响等，A2-5 根据谓语动词不同会有不同的语义含义。

附加语义角色(15种)：<br>ADV adverbial, default tag ( 附加的，默认标记 )
BNE beneﬁciary ( 受益人 )
CND condition ( 条件 )
DIR direction ( 方向 )
DGR degree ( 程度 )
EXT extent ( 扩展 )
FRQ frequency ( 频率 )
LOC locative ( 地点 )
MNR manner ( 方式 )
PRP purpose or reason ( 目的或原因 )
TMP temporal ( 时间 )
TPC topic ( 主题 )
CRD coordinated arguments ( 并列参数 )
PRD predicate ( 谓语动词 )
PSR possessor ( 持有者 )<br>PSE possessee ( 被持有 )















