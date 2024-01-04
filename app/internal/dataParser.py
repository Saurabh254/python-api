import json

# A predefined set of keys to identify fields containing JSON data
key_set = ['srm', 'style', 'labels', 'glass', 'available', 'beerVariation']


def parseDictToJsonString(Model, data_json):
    """
    Convert JSON data containing certain fields into SQLAlchemy model instances.

    Args:
        Model (SQLAlchemy model): The SQLAlchemy model class for which instances will be created.
        data_json (list[dict]): A list of dictionaries containing JSON data.

    Returns:
        list[Model]: A list of SQLAlchemy model instances created from the input JSON data.

    Example Usage:
        - `parseDictToJsonString(YourModel, [{"field1": "value1", "labels": {"key": "value"}}])`

    Note:
        - The function expects a predefined set of keys (`key_set`) that identify fields
          containing JSON data. It will convert the identified fields into JSON strings
          before creating SQLAlchemy model instances.

    Example:
        - If the input data_json contains a dictionary with a 'labels' key,
          the value of the 'labels' key will be converted into a JSON string before creating the model instance.

    Args:
        Model (SQLAlchemy model): The SQLAlchemy model class for which instances will be created.
        data_json (list[dict]): A list of dictionaries containing JSON data.

    Returns:
        list[Model]: A list of SQLAlchemy model instances created from the input JSON data.
    """
    data_model_list = []

    for item in data_json:
        for key in key_set:
            if key in item.keys():
                # Convert the field value to a JSON string
                item[key] = json.dumps(item[key])

        # Create an instance of the specified SQLAlchemy model and append it to the result list
        data_model_list.append(Model(**item))

    return data_model_list
