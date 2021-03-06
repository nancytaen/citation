from datetime import date
from urllib.parse import urlparse

from newspaper import Article, news_pool
import spacy


class Citation:
    """
    represents one citation from an url
    """
    def __init__(self, url, is_test=False):
        if not is_test:
            self.extract_info(url)

    def extract_info(self, url):
        """
        extract relevant info using newspaper3k and urlparse
        """
        self.url = url
        parsed_uri = urlparse(url).netloc.split('.', 2)
        self.website = parsed_uri[0] if parsed_uri[0] != 'www' else parsed_uri[1]
        article = Article(url)
        article.download()
        article.parse()
        self.authors = article.authors
        self.title = article.title
        self.date = article.publish_date
        self.is_name = self.is_name()

    def is_name(self):
        """
        assess if the author(s) is people or corporate
        return true if people's names
        """
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.authors[0])
        for t in doc.ents:
            if (t.label_ == "PERSON"):
                return True
        return False

    def format(self):
        """
        format info into IEEE citation
        """
        # format authors & date
        self.format_authors()
        self.format_date()
        today = date.today().strftime("%B %d, %Y")

        citation = """{} "{}", {}{}. [Online], Available: {}. [Accessed {}].""".format(
            self.authors, self.title, self.website.capitalize(), self.date, self.url, today)
        return citation
    
    def format_authors(self):
        """
        format authors e.g. Aaron Gell -> A. Gell,

        """
        authors = ""
        # first/middle name initials + last name if people
        if self.is_name:
            for author in self.authors:
                names = author.split(' ')
                for i in range(len(names) - 1):
                    authors += names[i][0] + ". "
                authors += names[-1]
        # simply append if corporate
        else:
            for i in range(len(self.authors)):
                authors += self.authors[i]
        if authors:
            authors += ","
        self.authors = authors
    
    def format_date(self):
        """
        format date into Month Date, Year
        """
        if self.date:
            self.date = ", " + self.date.strftime('%B %d, %Y')
    