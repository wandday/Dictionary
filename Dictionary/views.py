from django.shortcuts import render
import requests
import bs4

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_search(request):
    words = request.GET['word']

    answer1 = requests.get('https://www.dictionary.com/browse/'+words)
    answer2 = requests.get('https://www.thesaurus.com/browse/'+words)

    if answer1:
        soup1 = bs4.BeautifulSoup(answer1.text, 'lxml')
        word_meanings = soup1.find_all('div', {'value': '1'})
        word_meaning = word_meanings[0].getText()

    else:
        words = 'Sorry, the meaning of '+ words +' could not be found'
        word_meanings = ''
        word_meaning = ''

    if answer2:
        soup2 = bs4.BeautifulSoup(answer2.text, 'lxml')

        synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
        synon = []
        for items in synonyms[0:]:
            item = items.text.strip()
            synon.append(item) 
        synonym = synon

        antonyms = soup2.find_all('a', {'class': 'css-pc0050 eh475bn0'})
        anton = []
        for items in antonyms[0:]:
            item = items.text.strip()
            anton.append(item)
        antonym = anton

    else:
        synonym = ''
        antonym = ''

    search_result = {
        'words': words,
        'word_meaning': word_meaning,
    } 

    return render(request, 'word_search.html', {'search_result':search_result, 'synonym':synonym, 'antonym': antonym} )


