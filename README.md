# Spell Correction Using Minimum Edit Distance

## Introduction
The aim of an automatic spell correction system is to identify the incorrect words and suggest a correct word which is most similar to the incorrect word. The Minimum Edit Distance (MED) is one of the most popular method to find similar words. The MED algorithm uses 3 main operations (Insertion, Deletion and Substitution), to convert one word to another. In this project, we use the MED to find the average success rate on a spelling error corpus for first k words.

#### Example
Consider the word, "completly" from a corpus C and the corresponding correct word is "completely". Using MED, the first 5 words, with their minimum edit distance suggested from the dictionary D are: (completely, 1), (complexly, 2), (comely, 3), (complete, 3), (complexity, 3). Then s@1, will be 1. However, in case if the word appeared at 2nd or 3rd position then s@1 would be zero. For s@k to be 1, the correct word should appear in the first k suggestions. Otherwise, s@k is 0.

## Dataset
The datasets used are:
* [Birkbeck spelling error corpus](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/0643): This contains a list of misspelled words along with their correct spellings. This has been preprocessed manually and converted to an excel file available in corpus.xlsx.
* [Wordnet dictionary](https://wordnet.princeton.edu/): This contains a list of all english words against which we compare our misspelled words.

## Instructions to run the project
* Run the folloiwng command to clone the github repo
```bash
git clone https://github.com/laveenbhatia/Spell_Correction_Using_MED.git
```
* Run Spell_Corr_MED.py
