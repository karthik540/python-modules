import urllib.request
import random

def downloadImage(url):
    fileName = str(random.randint(1 , 10^4)) + '.jpg'
    urllib.request.urlretrieve(url , fileName)

if __name__ == "__main__":
    downloadImage("https://i.ytimg.com/vi/hT_nvWreIhg/maxresdefault.jpg")