
import requests

def getConnectionsData(url):
    answersJson = requests.get(url).json()
    categories = [[] for i in range(4)]
    currCategory = 0
    for category in answersJson['categories']:
        for card in category['cards']:
            categories[currCategory].append(card['content'])
        currCategory = currCategory + 1

    return categories

def getWordleData(url):
    answerJson = requests.get(url).json()
    return answerJson['solution']

def getMiniCrosswordData(url):
    answerJson = requests.get(url).json()
    solution = []
    currRow = -1
    for char in answerJson['body'][0]['cells']:
        if (char):
            if (int(char['clues'][0]) != currRow):
                currRow = char['clues'][0]
                solution.append(char['answer'])
            else:
                solution[currRow] = solution[currRow] + char['answer']

    return solution