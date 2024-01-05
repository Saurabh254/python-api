# Python-API (BeerData API)

## Description

The BeerData API is a dynamic and efficient application designed to provide users with seamless access to a diverse dataset of beer-related information.


## Table of Contents

- [Python-API (BeerData API)](#python-api-beerdata-api)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [API Endpoints](#api-endpoints)
    - [Method: GET](#method-get)
      - [Parameters:](#parameters)
    - [Method: GET](#method-get-1)
      - [Parameters:](#parameters-1)
    - [Method: GET](#method-get-2)
      - [Parameters:](#parameters-2)
    - [Method: GET](#method-get-3)
      - [Parameters:](#parameters-3)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Saurabh254/python-api.git
    ```
2. Navigate to the project directory
   ```shell
    cd python-api
    ```
3. Setting up virtual environment
   ```shell
    python -m venv virt
    source virt/bin/activate
    python -m pip install -r requirements.txt
    ```
## Usage

1. Run the app

```bash
uvicorn app.main:app
```
2. Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the app documentation

## API Endpoints

### Method: GET

#### Parameters:

  `/import/{page_number}`

 - Insert a page into the database along with its associated data.

### Method: GET

#### Parameters:

  `/remove/{page_number}`

  - page_number (int): The page number to be inserted.
Remove a page from the database along with its associated data.

### Method: GET

#### Parameters:

  `/page/{page_number}`

  - Retrieve information about a specific page of beer data.

### Method: GET

#### Parameters:

  `/{page_number}?abv={abv_value}&ibu={ibu_value}`

- page_number (int): Page number to be viewed.
- abv (float, optional): ABV value to be filtered. Defaults to None.
- ibu (int, optional): IBU value to be filtered. Defaults to None.

Dependencies
- Python 3.x
- FastAPI
- SQLAlchemy



# Contributing

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make changes and commit.
- Push your branch to your fork.
- Create a pull request.
