import requests
import json

# Call the URL
url = "https://trends.google.com/trends/api/dailytrends"
querystring = {"hl":"en-US","tz":"-60","geo":"US","ns":"15"}

# Get Data
response = requests.request("GET", url, params=querystring)
r = response.text
data = r.replace(")]}',","")
api = json.loads(data)
trends = api['default']['trendingSearchesDays']



for trend in trends:
    date = trend['formattedDate']
    topics = trend['trendingSearches']
    
    for topic in topics:
        
        title = topic['title']['query']
        #print(title+',')
        rank = topic['formattedTraffic']
        tags = topic['relatedQueries']
        for tag in tags:
            keywords = tag['query']
            #print('#'+keywords.replace(" ", ""))
            print(keywords+',')
        img = topic['image']
        articles = topic['articles']
        for article in articles:
            article_title = article['title']
            
            link = article['url']
            snippet = article['snippet']
        #print(article_title+',')
        




    