import pytest

from unittest.mock import patch
from fastapi import HTTPException
from fastapi.testclient import TestClient
from src.bestsimilarity.main import api

testClient = TestClient(api)

testString = "Just to test that this is what the stub function returns."

@patch('src.bestsimilarity.main.findBestSimilarity', return_value=testString)
def test_getBestSimilarityWithCorrectData(mock_findBestSimilarity):
    customerData = {
        "reference": "Higgs boson in particle physics",
        "other": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]
    }

    response = testClient.post("/bestSimilarity/", json=customerData)

    assert response.status_code == 200

    assert response.json() == {"top_result": testString}

    mock_findBestSimilarity.assert_called_once_with(customerData["reference"], customerData["other"])

def test_getBestSimilarityWithNoReference():
    input_data = {
        "reference": "",
        "other": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]
    }

    response = testClient.post("/bestSimilarity/", json=input_data)

    assert response.status_code == 400
    assert response.json() == {"detail": "No reference title in the request"}

def test_getBestSimilarityWithNoOtherTitles():
    input_data = {
        "reference": "Higgs boson in particle physics",
        "other": []
    }

    response = testClient.post("/bestSimilarity/", json=input_data)

    assert response.status_code == 400
    assert response.json() == {"detail": "No titles to match against the reference in the request"}
