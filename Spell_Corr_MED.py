import numpy as np
import nltk
import pandas as pd
import pytrec_eval
from nltk.corpus import wordnet as wn


nltk.data.path.append('./NLTK_Data/')

# words = [n for n in wn.all_lemma_names()]
# print(len(words))
short_words = [n for n in wn.all_lemma_names() if len(n) <= 10 and n.find("_") == -1]
print("Number of records in dictionary ", len(short_words))


def min_ed_dist(target, source):
    target = [k for k in target]
    source = [k for k in source]
    sol = np.zeros((len(source), len(target)))

    sol[0] = [j for j in range(len(target))]
    sol[:, 0] = [j for j in range(len(source))]

    if target[1] != source[1]:
        sol[1, 1] = 2

    for c in range(1, len(target)):
        for r in range(1, len(source)):
            if target[c] != source[r]:
                sol[r, c] = min(sol[r-1, c], sol[r, c-1]) + 1
            else:
                sol[r, c] = sol[r-1, c-1]
    return sol[len(source)-1, len(target)-1]


corpus_df = pd.read_excel("C://Users//lavee//Documents//UWindsor//Courses//Winter'22//NLP//Assignment 1//corpus.xlsx")
corpus_df = corpus_df.head(500)
corpus_records = corpus_df.shape[0]
print("Number of records in corpus ", corpus_records)
corpus = corpus_df.to_records(index=False)
corpus = list(corpus)
# print(corpus)
# corpus = [("contry", "country"),
#           ("choped", "chopped"),
#           ("hell", "instagram")]

s1_list = []
s5_list = []
s10_list = []
count = 0
for w in corpus:
    word_distances = []
    count = count+1
    print(count)
    print(w)
    for n in short_words:
        word = (n, min_ed_dist("#"+n, "#"+w[0]))
        word_distances.append(word)
    sorted_word_distances = sorted(word_distances, key=lambda x: x[1])
    suggested_lov = []
    for i in range(0, 10):
        suggested_lov.append(sorted_word_distances[i])
    print(suggested_lov)
    if w[1] == suggested_lov[0][0]:
        s_1 = 1
    else:
        s_1 = 0
    # print("s_1", s_1)
    s1_list.append(s_1)
    s_5 = 0
    for i in range(0, 4):
        if w[1] == suggested_lov[i][0]:
            s_5 = 1
            break
    # print("s_5", s_5)
    s5_list.append(s_5)
    s_10 = 0
    for i in range(0, 9):
        if w[1] == suggested_lov[i][0]:
            s_10 = 1
            break
    # print("s_10", s_10)
    s10_list.append(s_10)

print("Average s@1 ", pytrec_eval.compute_aggregated_measure("gm", s1_list))
print("Average s@5 ", pytrec_eval.compute_aggregated_measure("gm", s5_list))
print("Average s@10 ", pytrec_eval.compute_aggregated_measure("gm", s10_list))

