from bs4 import BeautifulSoup
import requests

def crawl(url_initial , tag_name , atr_name , atr_value , url_final = '' , page_no = 1 , isFullUrl = False):
    for i in range(page_no):
        if(isFullUrl):
            source_code = requests.get(url_initial)
        else:
            source_code = requests.get(url_initial + str(i) + url_final)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text , 'html.parser')
        data = []
        for link in soup.find_all(tag_name , {atr_name : atr_value}):
            data.append(link.string)
    return data

###     Crawling repo list in github
if __name__ == "__main__":
    url_initial = 'https://github.com/karthik540?tab=repositories'
    #url_final = '&qid=1559539678&ref=sr_pg_2'
    #page_no = 5
    tag_name = 'a'
    atr_name= 'itemprop'
    atr_value = 'name codeRepository'
    #print(crawl(url_initial , tag_name , atr_name , atr_value , url_final , page_no))
    print(crawl(url_initial , tag_name , atr_name , atr_value , isFullUrl= True))