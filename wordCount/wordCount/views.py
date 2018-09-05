from django.http import HttpResponse
from django.shortcuts import render
import re
import operator


def home(request):
    return render(request, 'home.html', {'header': 'Word Count'})


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordList = re.findall(r"[\w']+", fulltext)
    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(wordDictionary)
    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordList), 'sortedWords': sortedWords})


def about(request):
    return render(request, 'about.html')