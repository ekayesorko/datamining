import pickle
from bs4 import BeautifulSoup


with open('facebookappreview.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
 
mainList = soup.find('div', jsname = 'fk8dgd')
reviewList = mainList.findAll('span', jsname = 'fbQN7e')
starList = mainList.findAll('div', class_ = 'pf5lIe')
print(len(reviewList))
arr = [0,0,0,0,0]
storageArray = []
 
for review, star in zip(reviewList, starList):
    negCount = len(star.findAll('div', class_ = 'L0jl5e bUWb7c'))
    posCount = 5 - negCount
    reviewtype = posCount > 3
    arr[posCount - 1] += 1
    reviewString = review.text
    totalReview = (reviewString, reviewtype)
    storageArray.append(totalReview)
    #print(reviewString, 5 - negCount, sep = "\n")
print(storageArray)
pickle.dump(storageArray, open("MessengerReview.p",'wb'))
anotherStorageArray = pickle.load(open("MessengerReview.p","rb"))
print(len(anotherStorageArray))
print(arr)