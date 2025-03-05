From the directory where this README.md file resides (that is: bestSimilarity directory), please run the following command:

poetry run uvicorn src.bestsimilarity.main:api

in order to start the uvicorn server that waits for POST requests. Requests to this server can then be done in the local browser at: http://127.0.0.1:8000/docs


In order to run the tests, please run the following (from the same top directory):

poetry run pytest

Please notice that for the getBestSimilarity function of the main module, we run a unit test (by mocking the findBestSimilarity function). We do this mainly to test the API.

However, for the findBestSimilarity in bestSimilarityFinder module, we run a functional test, because we are interested to also see how well it finds the similarities. The data we test on is placed in the dataForTesting.json file under tests directory.

I also added a directory testData which contains some data I created manually to test the functionality of findBestSimilarity function. In some of the few examples I purposely tried to confuse it. However, it detected the similarities pretty well.
