from sqlalchemy import create_engine, orm, insert
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from schema import Glass, Base, Srm, Available, Style, Beer, Category
from app.internal.dataParser import camel_to_snake
from pprint import pprint


heh = {
    "id": "hB0QeO",
    "name": "#9",
    "nameDisplay": "#9",
    "description": "Not quite pale ale.  A beer cloaked in secrecy.  An ale whose mysterious unusual palate will swirl across your tongue and ask more objectquestions than it answers.\r\n\r\nA sort of dry, crisp, fruity, refreshing, not-quite pale ale.  #9 is really impossible to describe because there's never been anything else quite like it.  Our secret ingredient introduces a most unusual aroma which is balanced with residual sweetness.",
    "abv": "5.1",
    "ibu": "20",
    "glasswareId": 5,
    "srmId": 9,
    "availableId": 1,
    "styleId": 25,
    "isOrganic": "N",
    "isRetired": "N",
    "labels": {
          "icon": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-icon.png",
          "medium": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-medium.png",
          "large": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-large.png",
          "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-contentAwareIcon.png",
          "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-contentAwareMedium.png",
          "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/hB0QeO/upload_tI37PC-contentAwareLarge.png"
    },
    "status": "verified",
    "statusDisplay": "Verified",
    "servingTemperature": "cold",
    "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
    "originalGravity": "1.048",
    "createDate": "2012-01-03 02:42:36",
    "updateDate": "2015-12-15 23:21:11",
    "glass": {
        "id": 5,
        "name": "Pint",
        "createDate": "2012-01-03 02:41:33"
    },
    "srm": {
        "id": 9,
        "name": "9",
        "hex": "E58500"
    },
    "available": {
        "id": 1,
        "name": "Year Round",
        "description": "Available year round as a staple beer."
    },
    "style": {
        "id": 25,
        "categoryId": 3,
        "category": {
            "id": 3,
            "name": "North American Origin Ales",
            "createDate": "2012-03-21 20:06:45"
        },
        "name": "American-Style Pale Ale",
        "shortName": "American Pale",
        "description": "American pale ales range from deep golden to copper in color. The style is characterized by fruity, floral and citrus-like American-variety hop character producing medium to medium-high hop bitterness, flavor, and aroma. Note that the \"traditional\" style of this beer has its origins with certain floral, fruity, citrus-like, piney, resinous, or sulfur-like American hop varietals. One or more of these hop characters is the perceived end, but the perceived hop characters may be a result of the skillful use of hops of other national origins. American pale ales have medium body and low to medium maltiness. Low caramel character is allowable. Fruity-ester flavor and aroma should be moderate to strong. Diacetyl should be absent or present at very low levels. Chill haze is allowable at cold temperatures.",
        "ibuMin": "30",
        "ibuMax": "42",
        "abvMin": "4.5",
        "abvMax": "5.6",
        "srmMin": "6",
        "srmMax": "14",
        "ogMin": "1.044",
        "fgMin": "1.008",
        "fgMax": "1.014",
        "createDate": "2012-03-21 20:06:45",
        "updateDate": "2015-04-07 15:25:18"
    }
}

heh = camel_to_snake(heh)
# with the actual URI for your database
DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/api'
engine = create_engine(DATABASE_URI)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the database
glass = Glass(**heh["glass"])
srm = Srm(**heh['srm'])
available = Available(**heh["available"])
category = Category(**heh["style"]['category'])
heh['style']['category'] = category
style = Style(**heh["style"])
session.add_all([glass, srm, available, style])

heh["glass"] = glass
heh["srm"] = srm
heh["available"] = available
heh["style"] = style

beer = Beer(**heh)

session.add(beer)

# # Commit the changes
session.commit()

# Close the session
session.close()
