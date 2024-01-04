from fastapi import APIRouter, HTTPException
from ..dependency import getDataFromBeerDataSet

# Defining APIRouter for the /page endpoint
router = APIRouter(
    prefix="/page",
    tags=["page"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get('/{page_number}', tags=['page'])
async def render_page(page_number: int, abv: float = None, ibu: int = None):
    """
    Retrieve information about a specific page of beer data with optional ABV and IBU filters.

    Args:
        page_number (int): Page number to be viewed.
        abv (float, optional): ABV value to filter by. Defaults to None.
        ibu (int, optional): IBU value to filter by. Defaults to None.

    Raises:
        HTTPException: Raised when the desired page is not available.

    Returns:
        dict: JSON object containing the requested beer data.

    Example Usage:
        - `/page/1`: Retrieve all data for page 1.
        - `/page/2?abv=5.0`: Retrieve data for page 2 with ABV filter.
        - `/page/3?ibu=30`: Retrieve data for page 3 with IBU filter.
        - `/page/4?abv=5.0&ibu=30`: Retrieve data for page 4 with both ABV and IBU filters.
    """
    try:
        # Fetch the JSON object data for the specified page
        data = getDataFromBeerDataSet(page_number)

        # If ABV and IBU values are not defined, return the entire data
        if abv is None and ibu is None:
            return data

    except Exception as e:
        # Raise an HTTPException if getDataFromBeerDataSet is unable to parse the page data
        raise HTTPException(status_code=404, detail="Page not found")

    # Initialize a list to store matching objects based on ABV and IBU filters
    new_data = []

    # Parse data based on ABV and IBU values
    if ibu and abv:
        for item in data['data']:
            if 'abv' in item.keys() and float(item['abv']) == abv:
                if 'ibu' in item.keys() and int(item['ibu']) == ibu:
                    new_data.append(item)
    else:
        if abv:
            for item in data['data']:
                if 'abv' in item.keys() and float(item['abv']) == abv:
                    new_data.append(item)
        elif ibu:
            for item in data['data']:
                if 'ibu' in item.keys() and int(item['ibu']) == ibu:
                    new_data.append(item)

    # Construct the resulting object
    result_data = {
        "currentPage": page_number,
        "resultLength": len(new_data),
        "data": new_data,
        "status": "success"
    }

    return result_data
