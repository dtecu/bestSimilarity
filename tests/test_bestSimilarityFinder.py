import os
import json

from src.bestsimilarity.bestSimilarityFinder import findBestSimilarity

def getDataAsList(fileName):
    with open(fileName, 'r') as file:
        allData = json.load(file)['data']
    return allData

def test_findBestSimilarity():
    with open(os.path.join('testData', 'dataForTesting.json'), 'r') as file:
        testData = json.load(file)['data']
    for item in testData:
        assert findBestSimilarity(item['reference'], item['other']) == item['top_result'], "Unexpected prediction"
