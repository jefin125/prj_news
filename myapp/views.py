from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key='b1bb9b9002aa4684aac5d790af45a0d8')
    headLines = newsapi.get_top_headlines(sources='cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc , img)

    return render(request, "main/index.html", context={"mylist": mylist})



