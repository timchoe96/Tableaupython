
import pandas as pd    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
#reading excel file 

data = pd.read_excel("articles.xlsx")

#summary of data

data.describe()
data.info()

#counting number of articles per source 

data.groupby(by = ["source_id"])['article_id'].count()


#counting number of reactions per publisher 

data.groupby(by=["source_id"])["engagement_reaction_count"].sum()


#drop unecessary column 

data = data.drop("engagement_comment_plugin_count",axis=1)


#create keyword flag for article title and create new column with confirmation of keyword       
#create keyword finder function 

def keywordFlag(word):
    
    keyword_flag = []

    for x in data["title"]:
        try:
            if word in x:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
            
    return keyword_flag

keywordflag = keywordFlag("murder")

#add new column to the dataframe

data["keyword_flag"] = pd.Series(keywordflag)
 

#the polarity_scores method returns a dictionary with 3 scores split between positive, negative and neutral, indicating 
# how positive or negative a certian string phrase is, in this case we will judge the article titles 
#extract the scores and make a new dataframe column for each category 

title_neg_sentiment = []
title_pos_sentiment =[]
title_neu_sentiment = []

for x in data["title"]:
    try:
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(x)
        title_neg_sentiment.append(sent["neg"])
        title_pos_sentiment.append(sent["pos"])
        title_neu_sentiment.append(sent["neu"])
    except:
        title_neg_sentiment.append(0)
        title_pos_sentiment.append(0)
        title_neu_sentiment.append(0)

data["keyword_flag"]

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment =pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data["title_neg_sentiment"] = title_neg_sentiment
data["title_pos_sentiment"] = title_pos_sentiment
data["title_neu_sentiment"] = title_neu_sentiment

data.to_excel("blogme_clean.xlsx",sheet_name="blogmedata",index=False)



