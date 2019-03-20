import requests
from bs4 import BeautifulSoup
import os

class Get10k():
    def __init__(self):
        self.basepage = "https://www.sec.gov{}"
        self.homepage = "https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&owner=exclude&action=getcompany"

    def getFilingsPage(self, stock_name):
        soup = self.parsePage(self.homepage.format(stock_name))
        base = soup.find(text='10-K')
        form = str(base.find_next()).split("\"")[3]
        return form

    def parsePage(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def getFormsPage(self, form):
        soup = self.parsePage(self.basepage.format(form))
        filingDateLookup = soup.find(text='Filing Date')
        filingDate = filingDateLookup.find_next().text
        form10kLookup = soup.find_all('tr')
        form10kList = form10kLookup[1].find('a')
        form10k = str(form10kList).split("\"")[1]
        return form10k

    def saveHtml(self, form10k):
        soup = str(self.parsePage(self.basepage.format(form10k)))
        script_dir = os.path.dirname(__file__)
        rel_path = "templates/form.html"
        abs_file_path = os.path.join(script_dir, rel_path)
        file_ = open(abs_file_path, 'w')
        file_.write(soup)
        file_.close()


    def main(self, company):
        self.saveHtml(self.getFormsPage(self.getFilingsPage(company)))
        


    



