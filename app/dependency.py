import json


def getDataFromBeerDataSet(page_number: int):
    """
    Retrieve beer data from a dataset for a specific page.

    Args:
        page_number (int): The page number for which to retrieve beer data.

    Returns:
        dict: A dictionary containing the beer data for the specified page.

    Raises:
        FileNotFoundError: If the dataset file for the given page_number is not found.

    Example Usage:
        - `getDataFromBeerDataSet(1)`: Retrieve beer data for page 1.

    Note:
        The dataset files should follow the naming convention 'beer_<page_number>.json',
        for example, 'beer_1.json' for page 1.

    Dataset Structure:
        The dataset file should contain a JSON-formatted representation of beer data.

    Example Dataset Structure:
        {
            "data": [
                {"beer_name": "Beer1", "abv": 5.0, "ibu": 30, ...},
                {"beer_name": "Beer2", "abv": 6.2, "ibu": 40, ...},
                ...
            ]
        }
    """
    try:
        # Search for the dataset file using the provided page_number
        # Example file name: beer_1.json
        with open(f"./app/beer-dataset/beer_{page_number}.json", 'r') as f:
            # Load the dataset and return it as a dictionary
            data = json.load(f)
            return data

    except FileNotFoundError:
        # Raise an exception if the dataset file is not found
        raise FileNotFoundError(
            f"Dataset file for page {page_number} not found.")
