import json


def getDataFromBeerDataSet(page_number: int):

    # Search for the give dataset
    # example file name: beer_1.json
    with open(f"./app/beer-dataset/beer_{page_number}.json", 'r') as f:
        # loads the data set and get a json string
        data = json.load(f)

        return data
