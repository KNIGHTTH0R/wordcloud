from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re
with open("pg4300.txt") as f:
    lines = f.readlines()

text = "".join(lines)
after_splitting= re.split(r'[\n.()!, ""/]', text)
split_list = [x for x in after_splitting if len(x) > 0]
split_list_2 = split_list
freq = {}
stopwords = [u'and',u'I',u'his', u'the', u'of', u'to', u'a',u'you', u'is', u'are', u'in', u'as']
for w in split_list_2:
    if w in stopwords:
        continue
    else:
        w=str(w)
        w.replace("-","")
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1

"""maximum = max(freq, key=freq.get) 
print(maximum, freq[maximum])
for keys,values in freq.items():
        print keys,values """

wordcloud = WordCloud().generate_from_frequencies(wd.items())

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
