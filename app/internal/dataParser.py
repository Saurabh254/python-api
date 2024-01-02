

def camel_to_snake_singly(inputString: str):
    # converts the word from camel case to snake case
    # from nameDisplay to name-display
    result = [inputString[0].lower()]
    for symbol in inputString[1:]:
        if symbol.isupper():
            result.extend(['_', symbol.lower()])
        else:
            result.append(symbol)
    return ''.join(result)


def camel_to_snake(data):
    # converts the camel case keys name snake case keys
    if (type(data) == dict):
        _tempDict = {}
        for key, value in data.items():
            _tempDict[camel_to_snake_singly(key)] = camel_to_snake(value)
        return _tempDict
    else:
        return data
