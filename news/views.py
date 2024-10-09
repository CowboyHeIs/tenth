from django.shortcuts import render
print('View file')
import feedparser

def get_news():
    feed_url = "https://jogja.ataranews.com/rss/pariwisata-budaya.xml"
    feed = feedparser.parse(feed_url)
    return feed.entries

def news_view(request):
    articles = get_news()
    return render(request, 'news.html', {'articles': articles})