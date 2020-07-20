from urllib.parse import urlparse

from newspaper import Article, news_pool

class Citation():
    def __init__(self, url):
        self.extract_info(url)

    def extract_info(self, url):
        article = Article(url)
        article.download()
        article.parse()
        print("========================")
        print(url)
        parsed_uri = urlparse(url)
        print(parsed_uri.netloc)
        print(article.authors)
        print(article.title)
        print(article.publish_date)
        print("\n")

def sources(urls):
    for url in urls:
        Citation(url)
    
    

sources(["https://gen.medium.com/we-dont-view-you-as-americans-that-s-the-bottom-line-c084c7fe8edd?source=topic_page---------------------------20",
"https://www.economist.com/middle-east-and-africa/2020/07/18/covid-19-has-throttled-south-africas-economy", 
"https://www.economist.com/business/2020/07/18/the-varying-american-fortunes-of-grindr-and-blued"])