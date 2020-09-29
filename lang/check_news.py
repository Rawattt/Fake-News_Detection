#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sys
from nltk import word_tokenize
from nltk.corpus import stopwords


# In[15]:


def _calLanguageRatio(text):
    
    languages_ratios = {}
    
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens]

    
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) 

    return languages_ratios


# In[24]:


def detectEnglishLanguage(text):
    ratios = _calLanguageRatio(text)

    most_rated_language = max(ratios, key=ratios.get)

    return 'english' == most_rated_language


# In[25]:


if __name__ == '__main__':
    a = 'this is a test text. it will be used to check if our function can recognise this string is in english language'
    detectEnglishLanguage(a)


# In[ ]:




