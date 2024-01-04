from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..internal.database import get_db, Beer, BeerData
from ..dependency import getDataFromBeerDataSet
from ..internal.dataParser import parseDictToJsonString

router = APIRouter(
    prefix="/import",
    tags=["import"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Page not found"}}
)


@router.get('/{page_number}', tags=['import'])
async def insert_page_into_db(page_number: int, db: Session = Depends(get_db)):
    """
    Insert a page into the database along with its associated data.

    Parameters:
    - page_number: The page number to be inserted.

    Dependencies:
    - db: SQLAlchemy Session, obtained through the `get_db` function.

    Returns:
    - {"status": "success", "result": "Page Added"}: If the page is successfully inserted.
    - {"status": "success", "result": "page exists"}: If the page already exists in the database.
    - {"status": "failed", "result": <error_message>}: If an exception occurs during the insertion process.
    """
    # Check if the page already exists in the database
    if not db.query(Beer).filter(Beer.currentPage == page_number).scalar():
        try:
            # Get data for the page from an external source
            beers = getDataFromBeerDataSet(page_number)

            # Convert BeerData instances to JSON strings
            beers['data'] = parseDictToJsonString(BeerData, beers['data'])

            # Add the new Beer instance to the database
            db.add(Beer(**beers))

            # Commit the changes to the database
            db.commit()

            # Return success message
            return {"status": "success", "result": "Page Added"}
        except Exception as e:
            # Print the exception and return failure message
            print(e)
            return {"status": "failed", "result": str(e)}
    else:
        # Return success message if the page already exists
        return {"status": "success", "result": "page exists"}
