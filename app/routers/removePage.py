from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..internal.database import get_db, Beer


router = APIRouter(
    prefix="/remove",
    tags=["remove"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Page not found"}}
)


@router.get('/{page_number}', tags=['remove'])
async def remove_page_from_db(page_number: int, db: Session = Depends(get_db)):
    """
    Remove a page from the database along with its associated data.

    Parameters:
    - page_number: The page number to be removed.

    Dependencies:
    - db: SQLAlchemy Session, obtained through the `get_db` function.

    Returns:
    - {"status": "success", "result": "Deleted Successfully"}: If the page is successfully deleted.
    - {"status": "failed", "result": "Page doesn't exist in db "}: If the page doesn't exist in the database.
    """

    # Query the Beer table to get the Beer instance with the specified currentPage
    beer_instance = db.query(Beer).filter(
        Beer.currentPage == page_number).first()

    # Check if the Beer instance exists
    if beer_instance:
        # Retrieve associated BeerData instances
        beer_data_instances = beer_instance.data

        # Loop through and delete each associated BeerData instance
        for beer_data_instance in beer_data_instances:
            db.delete(beer_data_instance)

         # Delete the Beer instance
        db.delete(beer_instance)

        # Commit the changes to the database
        db.commit()

        # Return success message
        return {"status": "success", "result": "Deleted Successfully"}

    # Return failure message if the page doesn't exist
    return {"status": "failed", "result": "Page doesn't exist in db "}
