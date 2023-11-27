import requests
import re

# re is regular expression , it can search for patterns in

class WebCrawler:
    def __init__(self):
        # keeps a list of visited sites
        self.discovered_sites = []

    # BFS implementation
    def crawl(self,start_url):
        queue = [start_url]
        self.discovered_sites.append(start_url)
        while queue:
            test_url = queue.pop(0)
            print(test_url)
            # take raw html rep of visited sites to look for neighbours
            test_url_html = self.read_raw_html(test_url)
            for url in self.get_links_from_html(test_url_html):
                if url not in self.discovered_sites:
                    self.discovered_sites.append(url)
                    queue.append(url)

    def read_raw_html(self,url):
        raw_html = " "
        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass
        return raw_html

    def get_links_from_html(self,raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",raw_html)

if __name__=="__main__":
    crawler = WebCrawler()
    crawler.crawl("https://www.cnn.com")