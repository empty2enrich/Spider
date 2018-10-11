#!/usr/bin/python
# -*-coding:utf-8-*-

from urllib import request
from bs4 import BeautifulSoup, Tag

class RMRBSpider:
    def read_article(self, article_url):
        article = ArticleInfo()
        contents = []
        html = request.urlopen(article_url)
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all("div", id="detail_pop_content")
        for div in divs:
            contents.extend(div.contents)
        for content in contents:
            if isinstance(content, Tag):
                content_class = content['class']
                if content_class == ['title']:
                    article.title = content.getText()
                if content_class == ['subtitle']:
                    article.subtitle.append(content.getText())
                if content_class == ['detail_con']:
                    article.content += content.getText()
                if content_class == 'info clearfix'.split():
                    for child in content.contents:
                        if isinstance(child, Tag) and child['class'] == ['sha_left']:
                            article.describe.extend(child.getText().split())
        return article




class NewpapersInfo:
    def __init__(self):
        self.articles= []
        self.article_urls = []
        self.yestoday_news_url = []
        self.tomorrow_news_url = []
    pass

class ArticleInfo:
    def __init__(self):
        self.title = ""
        self.subtitle = []
        self.describe = []
        self.content = ""

if __name__ == "__main__":
    RMRBSpider().read_article("http://data.people.com.cn/rmrb/20181011/1/fa5cdcb51d564cc39e0d8766636f846e")