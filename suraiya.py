import pickle
from bs4 import BeautifulSoup

def get_data():
    with open('facebookappreview.html') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    
    mainList = soup.find('div', jsname = 'fk8dgd')
    reviewList = mainList.findAll('span', jsname = 'fbQN7e')
    starList = mainList.findAll('div', class_ = 'pf5lIe')

    text = []
    sentiment = []
    for review, star in zip(reviewList, starList):
        negCount = len(star.findAll('div', class_ = 'L0jl5e bUWb7c'))
        s = True if negCount < 3 else False
        sentiment.append(s)
        text.append(review)
    
    return (text, sentiment)

if __name__ == "__main__":
    text, sentiment = get_data()
    print(len(sentiment))
