

### segmenter

https://nlp.stanford.edu/software/segmenter.html

https://nlp.stanford.edu/software/segmenter-faq.html

chinese:

the CRF-based Chinese Word Segmenter

Two models with two different segmentation standards are included: [Chinese Penn Treebank standard](http://www.cis.upenn.edu/~chinese/segguide.3rd.ch.pdf) and [Peking University standard](http://sighan.cs.uchicago.edu/bakeoff2005/data/pku_spec.pdf).



the CRF-Lex Chinese Word Segmenter 



>  Huihsin Tseng, Pichuan Chang, Galen Andrew, Daniel Jurafsky and Christopher Manning. 2005. [*A Conditional Random Field Word Segmenter*](http://nlp.stanford.edu/pubs/sighan2005.pdf). In Fourth SIGHAN Workshop on Chinese Language Processing.

> Pi-Chuan Chang, Michel Galley and Chris Manning. 2008. [*Optimizing Chinese Word Segmentation for Machine Translation Performance*](http://nlp.stanford.edu/pubs/acl-wmt08-cws.pdf). In WMT.



### pos

https://nlp.stanford.edu/software/tagger.html

https://nlp.stanford.edu/software/pos-tagger-faq.html

the log-linear part-of-speech taggers

- Chinese: the [Penn Chinese Treebank](http://www.cis.upenn.edu/~chinese/).

> Kristina Toutanova and Christopher D. Manning. 2000. [Enriching the Knowledge Sources Used in a Maximum Entropy Part-of-Speech Tagger](http://nlp.stanford.edu/~manning/papers/emnlp2000.pdf). In *Proceedings of the Joint SIGDAT Conference on Empirical Methods in Natural Language Processing and Very Large Corpora (EMNLP/VLC-2000)*, pp. 63-70.
>
> Kristina Toutanova, Dan Klein, Christopher Manning, and Yoram Singer. 2003. [Feature-Rich Part-of-Speech Tagging with a Cyclic Dependency Network](http://nlp.stanford.edu/~manning/papers/tagging.pdf). In *Proceedings of HLT-NAACL 2003*, pp. 252-259.



### ner

https://nlp.stanford.edu/software/CRF-NER.html

https://nlp.stanford.edu/software/crf-faq.html

We also provide Chinese models built from <u>the Ontonotes Chinese named entity data</u>. There are two models, one using distributional similarity clusters and one without. 

 (CRF models were pioneered by [Lafferty, McCallum, and Pereira (2001)](http://www.cis.upenn.edu/~pereira/papers/crf.pdf); see [Sutton and McCallum (2006)](http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf) or [Sutton and McCallum (2010)](http://arxiv.org/pdf/1011.4088v1) for more comprehensible introductions.)

> Jenny Rose Finkel, Trond Grenager, and Christopher Manning. 2005. Incorporating Non-local Information into Information Extraction Systems by Gibbs Sampling. *Proceedings of the 43nd Annual Meeting of the Association for Computational Linguistics (ACL 2005),* pp. 363-370. [`http://nlp.stanford.edu/~manning/papers/gibbscrf3.pdf`](http://nlp.stanford.edu/~manning/papers/gibbscrf3.pdf)



### kbp (relation extraction)

There are descriptions of the sentence level statistical model, semgrex rules, and tokensregex rules in the write up for our [2016 TAC-KBP submission](https://nlp.stanford.edu/pubs/zhang2016stanford.pdf). 



### Pattern-based Information Extraction and Diagnostics

https://nlp.stanford.edu/software/patternslearning.html

This software provides code for two components:

- [Learning entities](https://nlp.stanford.edu/software/patternslearning.html#bootstrap) from unlabeled text starting with seed sets using patterns in an iterative fashion
- [Visualizing and diagnosing](https://nlp.stanford.edu/software/patternslearning.html#viz) the output from one to two systems.



**Algorithm**: bootstrapped pattern-based learning.

> Improved Pattern Learning for Bootstrapped Entity Extraction. [Sonal Gupta](http://www.cs.stanford.edu/people/sonal/) and [Christopher D. Manning](http://nlp.stanford.edu/~manning/). In Proceedings of the Eighteenth Conference on Computational Natural Language Learning (CoNLL). 2014.[[pdf](http://nlp.stanford.edu/pubs/gupta14evalpatterns.pdf); [Supplementary](http://nlp.stanford.edu/pubs/gupta14evalpatterns-supplemental.pdf); [bib](http://nlp.stanford.edu/pubs/gupta14evalpatterns.bib)]



### coref

https://stanfordnlp.github.io/CoreNLP/coref.html









