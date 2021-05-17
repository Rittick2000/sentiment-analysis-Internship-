import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
text=open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
tokenization_word=word_tokenize(cleaned_text,"english")
final_words=[]
for i in tokenization_word:
    if i not in stopwords.words('english'):
        final_words.append(i)
emotion_list=[]
with open('emotions.txt','r') as f:
    for line in f:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion=map(str,clear_line.split(':'))
        if word in final_words:
            emotion_list.append(emotion)
# print(emotion_list)
w=Counter(emotion_list)
# print(w)

def sentiment_analyse(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Nutral Sentiment")
sentiment_analyse(cleaned_text)

fig,axl=plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()