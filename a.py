#!/usr/bin/python
# -*- coding: utf-8 -*-

import hymlab.text as ht

# 論文に対する文書集合に対するベクトル
tc = ht.TextCollection("tex_text")
tfidf = ht.TfIdf(tc).tf_idf()
sim = ht.Similarity(tfidf)

# クエリに対するベクトル
tc_s = ht.TextCollection([u"えーっとえー焦げじゃんネットワークを作った使った音声検索でえー未知語の検索結果が知りたいです"])
tf = ht.TfIdf(tc_s).tf()[0]

# 結果を表示
res = sim.most_similarity_by_feature(tf)
for sim in res:
    print u"file A : %s" %  sim.vsm1.text.path
    print u"file B : %s" %  sim.vsm2.text.path
    print u"similarity : %s" %  sim.similarity
    print "\n"

