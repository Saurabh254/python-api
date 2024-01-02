from fastapi import APIRouter
import json
import pathlib
from fastapi.logger import logger
from ..dependency import getDataFromBeerDataSet
from fastapi import HTTPException
from pprint import pprint


# defining APIRouter for the /page endpoint
router = APIRouter(
    prefix="/page",
    tags=["page"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get('/{page_number}', tags=['page'])
async def render_page(page_number: int, abv: float = None, ibu: int = None):
    """_summary_

    Args:
        page_number (int): Page number to be viewed
        abv (float, optional): abv value to be filtered. Defaults to None.
        ibu (int, optional): ibu value to be filter. Defaults to None.

    Raises:
        HTTPException: Exception will raised when the desire page is not available

    Returns:
        _type_: json object
    """

    try:
        # fetch the jsonObject data
        data = getDataFromBeerDataSet(page_number)
        # if abv and ibu values ain't defined well return the data
        if (abv == None and ibu == None):
            return data
    # exception will occur if getDataFromBeerDataSet unable to parse the page data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")

    # for storing the matching objects
    newData = []

    # parsing data on the basis of ibu and abv value
    if ibu and abv:
        for item in data['data']:
            if 'abv' in item.keys() and float(item['abv']) == abv:
                if 'ibu' in item.keys() and int(item['ibu']) == ibu:
                    newData.append(item)
    else:
        if abv:
            for item in data['data']:
                if 'abv' in item.keys() and float(item['abv']) == abv:
                    newData.append(item)
        elif ibu:
            for item in data['data']:
                if 'ibu' in item.keys() and int(item['ibu']) == ibu:
                    newData.append(item)

    # resulting object
    _data = {
        "currentPage": page_number,
        "resultLength": len(newData),
        "data": newData,
        "status": "success"
    }

    return _data
