from sqlalchemy import create_engine, orm, insert
from sqlalchemy.orm import sessionmaker, registry
from datetime import datetime
from schema import Base, Available, Style, Beer, Category, getBeerModel
from dataParser import camel_to_snake_dict
from pprint import pprint

_datajson = {
    "currentPage": 1,
    "numberOfPages": 603,
    "totalResults": 30121,
    "data": [
        {
            "id": "tmEthz",
            "name": "\"Admiral\" Stache",
            "nameDisplay": "\"Admiral\" Stache",
            "description": "Milwaukee Brewing Co’s take on a classic European style. Baltic Porters are the stronger lager fermented cousin of the classic London Porter. The higher strength and cold fermentation help to create a smooth, less fruity porter, rich in roasted malt flavors and aromas. The “Admiral” Stache has a deep brown hue with a light caramel head. Toffee and milk chocolate dominate the flavor with subtle hints of dried fruit. One month of aging in Bourbon Barrels imparted a layer of vanilla and oak.\r\n\r\nWe first developed this beer in 2007. Our first attempted batch of beer at the 2nd street location was a Baltic Porter. What we ended up with became known as “Shake Down Nut Brown”. You can guess what went wrong from there… But, so many things right! Every year that has gone by, the beer has gotten a little bit stronger, in flavor and alcohol.\r\n\r\nWe use a black malt for the dark rich color and an extra special malt for the dried fruit flavors. Baltic Porters are fermented cold with a lager yeast. That long slow maturation creates a smooth flavor profile. The anticipation of the bourbon barrel aging it the most exciting part of this brew process. We want that oak character with hints of bourbon, we use 3rd run barrels for this result. Each batch has been slightly different from the last.",
            "abv": "7",
            "ibu": "23",
            "glasswareId": 5,
            "srmId": 37,
            "availableId": 4,
            "styleId": 104,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/tmEthz/upload_3Jl1St-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "originalGravity": "1.071",
            "createDate": "2012-09-09 13:35:27",
            "updateDate": "2016-11-11 14:23:06",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 37,
                "name": "37",
                "hex": "3F0708"
            },
            "available": {
                "id": 4,
                "name": "Seasonal",
                "description": "Available at the same time of year, every year."
            },
            "style": {
                "id": 104,
                "categoryId": 9,
                "category": {
                    "id": 9,
                    "name": "Other Lager",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Baltic-Style Porter",
                "shortName": "Baltic Porter",
                "description": "A true smooth cold-fermented and cold lagered beer, brewed with lager yeast. Black to very deep ruby/garnet in color. Overall, Baltic Porters have a very smooth lagered character with distinctive caramelized sugars, licorice and chocolate-like character of roasted malts and dark sugars. Roasted dark malts should not contribute bitterness, or astringent roast character. A low degree of smokiness from malt may be evident. Debitterized roast malts are best used for this style. Because of its alcoholic strength, aroma may include gentle (low) lager fruitiness (berries, grapes, plums, not banana; ale-like fruitiness from warm temperature fermentation is not appropriate), complex alcohols, cocoa-like, roast malt (and sometimes coffee-like roast barley, yet not bitter). Hop aroma is very low, though a hint of floral or sweet hop aroma can complement aromatics and flavor without dominance. Baltic Porters are not hop bitter dominated and expressed as low to medium-low. Baltic porters range from having medium to full body complemented with a medium-low to medium level of malty sweetness. No butterscotch-like diacetyl or sweet corn-like dimethylsulfide (DMS) should be apparent in aroma or flavor.",
                "ibuMin": "35",
                "ibuMax": "40",
                "abvMin": "7.5",
                "abvMax": "9",
                "srmMin": "40",
                "srmMax": "40",
                "ogMin": "1.072",
                "fgMin": "1.016",
                "fgMax": "1.022",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:41:46"
            }
        },
        {
            "id": "mwTzYN",
            "name": "\"I'm Idaho!\" XPA",
            "nameDisplay": "\"I'm Idaho!\" XPA",
            "description": "This beer might be light in color but it's definitely flavour fuelled! We wanted to showcase tropical American hops in this XPA, and among them the new hop variety Idaho 7.",
            "abv": "4.8",
            "ibu": "40",
            "styleId": 25,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/mwTzYN/upload_79fUJ5-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2018-07-11 19:38:21",
            "updateDate": "2018-07-11 19:39:17",
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
        },
        {
            "id": "WfTRD1",
            "name": "#1 Brown Brett Braggot",
            "nameDisplay": "#1 Brown Brett Braggot",
            "description": "This beer started its life as a brown ale that just wanted to be a bit more. Our farmer Rally, who picks up spent grains also happens to have a pretty thriving bee business. He transports his hives from state to state pollinating large crops for farms as far south as Georgia peach orchards and up north to Maine for Blueberry fields. Having just returned from a blueberry pollination in Maine and looking to sell off some of his honey we jumped on close to 200 lbs of this liquid gold and added it to the brown ale during secondary fermentation. Also added to the Disco funk tank was a blend of yeast, one a Belgian Saison Yeast and the other, our buddy Brettanomyces (aka Brett). This wild yeast strain adds that slight Belgian Funk to our tank and get’s the disco party started.",
            "abv": "6",
            "ibu": "18",
            "styleId": 147,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/WfTRD1/upload_pvShMp-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2015-03-29 15:12:57",
            "updateDate": "2015-12-17 23:07:31",
            "style": {
                "id": 147,
                "categoryId": 12,
                "category": {
                    "id": 12,
                    "name": "Mead, Cider, & Perry",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Braggot",
                "shortName": "Braggot",
                "description": "A harmonious blend of mead and beer, with the distinctive characteristics of both. A wide range of results are possible, depending on the base style of beer, variety of honey and overall sweetness and strength. Beer flavors tend to somewhat mask typical honey flavors found in other meads.",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:48:30"
            }
        },
        {
            "id": "uLkd3a",
            "name": "#2 Brett Golden Sour",
            "nameDisplay": "#2 Brett Golden Sour",
            "description": "This beer had a long weekend in our brew kettle allowing beer bugs (Pediococcus and Latcobacillus) to get down get down and do their sour thang. While yeast strains eat sugar and produce alcohol beer bugs eat sugar and produce acids. This gives sour beers their puckering power. After letting the bugs play in the sweet wort pool we boil the beer and add a touch of earthy hops. Disco Pig #2 Brett Golden Sour is 100% Brett fermented to replicate as closely as possible what a traditional Belgian wild fermented sour beer should be!",
            "abv": "6.5",
            "ibu": "9",
            "styleId": 36,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/uLkd3a/upload_dag3lM-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2015-03-29 15:10:51",
            "updateDate": "2015-12-18 00:22:07",
            "style": {
                "id": 36,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Golden or Blonde Ale",
                "shortName": "Blonde",
                "description": "Golden or Blonde ales are straw to golden blonde in color. They have a crisp, dry palate, light to medium body, and light malt sweetness. Low to medium hop aroma may be present but does not dominate. Bitterness is low to medium. Fruity esters may be perceived but do not predominate. Diacetyl should not be perceived. Chill haze should be absent.",
                "ibuMin": "15",
                "ibuMax": "25",
                "abvMin": "4",
                "abvMax": "5",
                "srmMin": "3",
                "srmMax": "7",
                "ogMin": "1.045",
                "fgMin": "1.008",
                "fgMax": "1.016",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:27:26"
            }
        },
        {
            "id": "hB0QeO",
            "name": "#9",
            "nameDisplay": "#9",
            "description": "Not quite pale ale.  A beer cloaked in secrecy.  An ale whose mysterious unusual palate will swirl across your tongue and ask more questions than it answers.\r\n\r\nA sort of dry, crisp, fruity, refreshing, not-quite pale ale.  #9 is really impossible to describe because there's never been anything else quite like it.  Our secret ingredient introduces a most unusual aroma which is balanced with residual sweetness.",
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
        },
        {
            "id": "5qG8kT",
            "name": "#duckface Blonde",
            "nameDisplay": "#duckface Blonde",
            "description": "A crisp and refreshing blonde ale.  The bright citrus notes and delightful malt balance make this the perfect beer to relax with on a long summer.  \r\n\r\nMade with lemongrass.",
            "abv": "4.3",
            "ibu": "19",
            "styleId": 124,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/5qG8kT/upload_o7PK06-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2017-09-18 22:26:46",
            "updateDate": "2018-03-15 21:19:14",
            "style": {
                "id": 124,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Herb and Spice Beer",
                "shortName": "Spice Beer",
                "description": "Herb beers use herbs or spices (derived from roots, seeds, fruits, vegetable, flowers, etc.) other than or in addition to hops to create a distinct (ranging from subtle to intense) character, though individual characters of herbs and/or spices used may not always be identifiable. Under hopping often, but not always, allows the spice or herb to contribute to the flavor profile. Positive evaluations are significantly based on perceived balance of flavors. Note: Chili-flavored beers that emphasize heat rather than chili flavor should be entered as a \"spiced\" beer.  A statement by the brewer explaining what herbs or spices are used is essential in order for fair assessment in competitions. Specifying a style upon which the beer is based may help evaluation. If this beer is a classic style with an herb or spice, the brewer should specify the classic style. If no Chocolate or Coffee category exists in a competition, then chocolate and coffee beers should be entered in this category.",
                "ibuMin": "5",
                "ibuMax": "70",
                "abvMin": "2.5",
                "abvMax": "12",
                "srmMin": "5",
                "srmMax": "50",
                "ogMin": "1.03",
                "fgMin": "1.006",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:44:45"
            }
        },
        {
            "id": "KZPL21",
            "name": "#InsertStupidApplePunHere",
            "nameDisplay": "#InsertStupidApplePunHere",
            "description": "Pi or Pie? 3.14 Anyone? \r\n\r\nEnough with the apple puns already!\r\n\r\nMichigan apple cider meets locally produced honey, dates, demerara sugar from Guyana, muscovado sugar from Mauritius, spices and graham flavors.",
            "abv": "14",
            "styleId": 148,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/KZPL21/upload_SQjelk-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2018-11-27 19:30:54",
            "updateDate": "2018-11-27 19:31:26",
            "style": {
                "id": 148,
                "categoryId": 12,
                "category": {
                    "id": 12,
                    "name": "Mead, Cider, & Perry",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Open Category Mead",
                "shortName": "Mead",
                "description": "This mead should exhibit the character of all of the ingredients in varying degrees, and should show a good blending or balance between the various flavor elements. Whatever ingredients are included, the result should be identifiable as a honey-based fermented beverage.",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:48:35"
            }
        },
        {
            "id": "m8f62Y",
            "name": "#KoLSCH",
            "nameDisplay": "#KoLSCH",
            "description": "Social Media have revolutionized human interaction ... and for all their pro's and con's, they cannot be overlooked for their power to give a platform to be heard, a voice to the otherwise voiceless. \r\n\r\nAs a nod to this, we bring you \"#KÖLSCH\" Köln-style Ale. We start by stripping our water down to the bare essentials then rebuild it to match the mineral content of the water in Köln, Germany. Then we add in tons of German Pilsner malts and eine kleine menge of German Perle and Tettnang hops. Easy going, crisp and refreshing!",
            "abv": "4.8",
            "ibu": "27",
            "glasswareId": 4,
            "srmId": 3,
            "availableId": 1,
            "styleId": 45,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/m8f62Y/upload_IHiHKI-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "foodPairings": "Fish & chips, chicken fingers, dilly dippers ... anything fried!",
            "servingTemperature": "very_cold",
            "servingTemperatureDisplay": "Very Cold - (0-4C/32-39F)",
            "originalGravity": "1.045",
            "createDate": "2016-06-21 16:27:40",
            "updateDate": "2016-06-23 15:36:35",
            "glass": {
                "id": 4,
                "name": "Pilsner",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 3,
                "name": "3",
                "hex": "FFCA5A"
            },
            "available": {
                "id": 1,
                "name": "Year Round",
                "description": "Available year round as a staple beer."
            },
            "style": {
                "id": 45,
                "categoryId": 4,
                "category": {
                    "id": 4,
                    "name": "German Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "German-Style Kölsch / Köln-Style Kölsch",
                "shortName": "Kölsch",
                "description": "Kölsch is warm fermented and aged at cold temperatures (German ale or alt-style beer). Kölsch is characterized by a golden to straw color and a slightly dry, subtly sweet softness on the palate, yet crisp. Good, dense head retention is desirable. Light pearapple-Riesling wine-like fruitiness may be apparent, but is not necessary for this style. Caramel character should not be evident. The body is light to medium-light. This beer has low hop flavor and aroma with medium bitterness. Wheat can be used in brewing this beer. Ale yeast is used for fermentation, though lager yeast is sometimes used in the bottle or final cold conditioning process. Fruity esters should be minimally perceived, if at all. Chill haze should be absent.",
                "ibuMin": "18",
                "ibuMax": "25",
                "abvMin": "4.8",
                "abvMax": "5.3",
                "srmMin": "4",
                "srmMax": "6",
                "ogMin": "1.042",
                "fgMin": "1.006",
                "fgMax": "1.01",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:29:04"
            }
        },
        {
            "id": "R61vnh",
            "name": "#Merica!",
            "nameDisplay": "#Merica!",
            "description": "SURLY NATION, 'TIS FOR THEE, SWEET BEER OF LIBERTY!\r\nLight gold in color, #Merica! is an old-school pre-Prohibition American Lager that was brewed in 2015 for the Annual D4th of July party put on by the Minneapolis-based punk band Dillinger Four. One of the only beer styles truly born in the U.S.A, pre-Prohibition American Lagers used corn as an integral part of the flavor profile, rather than as a simple substitute for barley malt. The flaked corn used in #Merica! comes across as a subtle, fresh corn flavor, while soft hop aromatics come from Warrior and Willamette hops, which add a mild fruity, herbal character that stays in the background. #Merica! is perfect for a hot summer day and celebrating the country’s birthday and 21 years of Dillinger Four.",
            "abv": "5",
            "availableId": 4,
            "styleId": 93,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/R61vnh/upload_Pz78yV-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "originalGravity": "1.053",
            "createDate": "2016-06-20 14:26:27",
            "updateDate": "2018-08-08 05:00:09",
            "available": {
                "id": 4,
                "name": "Seasonal",
                "description": "Available at the same time of year, every year."
            },
            "style": {
                "id": 93,
                "categoryId": 8,
                "category": {
                    "id": 8,
                    "name": "North American Lager",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "American-Style Lager",
                "shortName": "American Lager",
                "description": "Light in body and very light to straw in color, American lagers are very clean and crisp and aggressively carbonated. Flavor components should b e subtle and complex, with no one ingredient dominating the others. Malt sweetness is light to mild. Corn, rice, or other grain or sugar adjuncts are often used. Hop bitterness, flavor and aroma are negligible to very light. Light fruity esters are acceptable. Chill haze and diacetyl should be absent.",
                "ibuMin": "5",
                "ibuMax": "13",
                "abvMin": "3.8",
                "abvMax": "5",
                "srmMin": "2",
                "srmMax": "4",
                "ogMin": "1.04",
                "fgMin": "1.006",
                "fgMax": "1.01",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:39:26"
            }
        },
        {
            "id": "Tx1Y4D",
            "name": "#NOFILTER IPA",
            "nameDisplay": "#NOFILTER IPA",
            "description": "Juicy New England style IPA dry hopped with a massive amount of citra and mosaic hops.",
            "abv": "7",
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/Tx1Y4D/upload_oZCVc7-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2017-04-14 18:08:31",
            "updateDate": "2017-05-10 14:35:35",
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "1cn2gt",
            "name": "#NoGlutenCollusion - Cherry",
            "nameDisplay": "#NoGlutenCollusion - Cherry",
            "description": "Our #NoGlutenCollusion is a light beer made with rice and corn and flavored with cherries and lime.",
            "abv": "6.9",
            "ibu": "10",
            "styleId": 127,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/1cn2gt/upload_2XZEls-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2018-07-27 18:32:54",
            "updateDate": "2018-07-27 18:33:12",
            "style": {
                "id": 127,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Gluten-Free Beer",
                "shortName": "Gluten-Free Beer",
                "description": "A beer (lager, ale or other) that is made from fermentable sugars, grains and converted carbohydrates. Ingredients do not contain gluten, in other words zero gluten (No barley, wheat, spelt, oats, rye, etc). May or may not contain malted grains that do not contain gluten. Brewers may or may not design and identify these beers along other style guidelines with regard to flavor, aroma and appearance profile. The beer's overall balance and character should be based on its own merits and not necessarily compared with traditional styles of beer. In competitions, brewers identify ingredients and fermentation type. NOTE: These guidelines do not supersede any government regulations. Wine, mead, flavored malt beverages or beverages other than beer as defined by the TTB (U.S. Trade and Tax Bureau) are not considered \"gluten-free beer\" under these guidelines.",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:45:08"
            }
        },
        {
            "id": "zrbNet",
            "name": "#NOHOLDSIE Holdsie Da Deuce",
            "nameDisplay": "#NOHOLDSIE Holdsie Da Deuce",
            "description": "Rye Tripel aged in red Wine Barrels",
            "abv": "8.2",
            "availableId": 2,
            "styleId": 59,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/zrbNet/upload_NO3CdZ-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2014-11-26 20:13:19",
            "updateDate": "2015-12-17 19:00:42",
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 59,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Tripel",
                "shortName": "Belgian Tripel",
                "description": "Tripels are often characterized by a complex, sometimes mild spicy character. Clove-like phenolic flavor and aroma may be evident at extremely low levels. Yeast-generated  fruity esters, including banana, are also common, but not necessary. These pale/light-colored ales may finish sweet, though any sweet finish should be light. The beer is characteristically medium and clean in body with an equalizing hop/malt balance and a perception of medium to medium high hop bitterness. Traditional Belgian Tripels are often well attenuated. Brewing sugar may be used to lighten the perception of body. Its sweetness will come from very pale malts. There should not be character from any roasted or dark malts. Low hop flavor is acceptable. Alcohol strength and flavor should be perceived as evident. Head retention is dense and mousse-like. Chill haze is acceptable at low serving temperatures. Traditional Tripels are bottle conditioned, may exhibit slight yeast haze but the yeast should not be intentionally roused. Oxidative character if evident in aged Tripels should be mild and pleasant.",
                "ibuMin": "20",
                "ibuMax": "45",
                "abvMin": "7",
                "abvMax": "10",
                "srmMin": "4",
                "srmMax": "9",
                "ogMin": "1.07",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:31:50"
            }
        },
        {
            "id": "EV2zxl",
            "name": "#NOHOLDSIE Holdsie San",
            "nameDisplay": "#NOHOLDSIE Holdsie San",
            "description": "Rye Tripel aged in Bourbon Barrels",
            "abv": "8.2",
            "availableId": 2,
            "styleId": 59,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/EV2zxl/upload_3mwAdV-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2014-11-26 20:15:35",
            "updateDate": "2015-12-17 20:03:28",
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 59,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Tripel",
                "shortName": "Belgian Tripel",
                "description": "Tripels are often characterized by a complex, sometimes mild spicy character. Clove-like phenolic flavor and aroma may be evident at extremely low levels. Yeast-generated  fruity esters, including banana, are also common, but not necessary. These pale/light-colored ales may finish sweet, though any sweet finish should be light. The beer is characteristically medium and clean in body with an equalizing hop/malt balance and a perception of medium to medium high hop bitterness. Traditional Belgian Tripels are often well attenuated. Brewing sugar may be used to lighten the perception of body. Its sweetness will come from very pale malts. There should not be character from any roasted or dark malts. Low hop flavor is acceptable. Alcohol strength and flavor should be perceived as evident. Head retention is dense and mousse-like. Chill haze is acceptable at low serving temperatures. Traditional Tripels are bottle conditioned, may exhibit slight yeast haze but the yeast should not be intentionally roused. Oxidative character if evident in aged Tripels should be mild and pleasant.",
                "ibuMin": "20",
                "ibuMax": "45",
                "abvMin": "7",
                "abvMax": "10",
                "srmMin": "4",
                "srmMax": "9",
                "ogMin": "1.07",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:31:50"
            }
        },
        {
            "id": "qdUTFp",
            "name": "#Ultrafresh",
            "nameDisplay": "#Ultrafresh",
            "description": "DDH Double IPA w/ Vic Secret, Azacca, and Simcoe Hops.",
            "abv": "8.3",
            "styleId": 31,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/qdUTFp/upload_pdCfkb-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2018-07-23 15:41:27",
            "updateDate": "2018-07-23 15:42:36",
            "style": {
                "id": 31,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Imperial or Double India Pale Ale",
                "shortName": "Imperial IPA",
                "description": "Imperial or Double India Pale Ales have intense hop bitterness, flavor and aroma. Alcohol content is medium-high to high and notably evident. They range from deep golden to medium copper in color. The style may use any variety of hops. Though the hop character is intense it's balanced with complex alcohol flavors, moderate to high fruity esters and medium to high malt character. Hop character should be fresh and lively and should not be harsh in quality. The use of large amounts of hops may cause a degree of appropriate hop haze. Imperial or Double India Pale Ales have medium-high to full body. Diacetyl should not be perceived. The intention of this style of beer is to exhibit the fresh and bright character of hops. Oxidative character and aged character should not be present.",
                "ibuMin": "65",
                "ibuMax": "100",
                "abvMin": "7.5",
                "abvMax": "10.5",
                "srmMin": "5",
                "srmMax": "13",
                "ogMin": "1.075",
                "fgMin": "1.012",
                "fgMax": "1.02",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:46"
            }
        },
        {
            "id": "cBKBoK",
            "name": "#‎NOHOLDSIE‬ Holdsie Uno",
            "nameDisplay": "#‎NOHOLDSIE‬ Holdsie Uno",
            "description": "Rye Tripel aged in White Wine Barrels",
            "abv": "8.2",
            "availableId": 2,
            "styleId": 59,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/cBKBoK/upload_TEDqCp-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2014-11-26 20:14:57",
            "updateDate": "2015-12-17 20:03:28",
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 59,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Tripel",
                "shortName": "Belgian Tripel",
                "description": "Tripels are often characterized by a complex, sometimes mild spicy character. Clove-like phenolic flavor and aroma may be evident at extremely low levels. Yeast-generated  fruity esters, including banana, are also common, but not necessary. These pale/light-colored ales may finish sweet, though any sweet finish should be light. The beer is characteristically medium and clean in body with an equalizing hop/malt balance and a perception of medium to medium high hop bitterness. Traditional Belgian Tripels are often well attenuated. Brewing sugar may be used to lighten the perception of body. Its sweetness will come from very pale malts. There should not be character from any roasted or dark malts. Low hop flavor is acceptable. Alcohol strength and flavor should be perceived as evident. Head retention is dense and mousse-like. Chill haze is acceptable at low serving temperatures. Traditional Tripels are bottle conditioned, may exhibit slight yeast haze but the yeast should not be intentionally roused. Oxidative character if evident in aged Tripels should be mild and pleasant.",
                "ibuMin": "20",
                "ibuMax": "45",
                "abvMin": "7",
                "abvMax": "10",
                "srmMin": "4",
                "srmMax": "9",
                "ogMin": "1.07",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:31:50"
            }
        },
        {
            "id": "OquPH6",
            "name": "$Texas",
            "nameDisplay": "$Texas",
            "description": "Double NEIPA dry hopped with Hallertau Blanc, HBC-431, and El Dorado.",
            "abv": "8.2",
            "ibu": "58",
            "styleId": 31,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/OquPH6/upload_SamTfN-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2019-06-14 12:34:02",
            "updateDate": "2019-06-14 12:34:29",
            "style": {
                "id": 31,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Imperial or Double India Pale Ale",
                "shortName": "Imperial IPA",
                "description": "Imperial or Double India Pale Ales have intense hop bitterness, flavor and aroma. Alcohol content is medium-high to high and notably evident. They range from deep golden to medium copper in color. The style may use any variety of hops. Though the hop character is intense it's balanced with complex alcohol flavors, moderate to high fruity esters and medium to high malt character. Hop character should be fresh and lively and should not be harsh in quality. The use of large amounts of hops may cause a degree of appropriate hop haze. Imperial or Double India Pale Ales have medium-high to full body. Diacetyl should not be perceived. The intention of this style of beer is to exhibit the fresh and bright character of hops. Oxidative character and aged character should not be present.",
                "ibuMin": "65",
                "ibuMax": "100",
                "abvMin": "7.5",
                "abvMax": "10.5",
                "srmMin": "5",
                "srmMax": "13",
                "ogMin": "1.075",
                "fgMin": "1.012",
                "fgMax": "1.02",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:46"
            }
        },
        {
            "id": "8wyzkj",
            "name": "'79 Series: Chocolate Peanut Butter Porter",
            "nameDisplay": "'79 Series: Chocolate Peanut Butter Porter",
            "description": "The second installment of the ’79 Series is a Chocolate Peanut Butter Porter, featuring liquid coco and roasted peanuts, for a rich chocolate flavor.",
            "abv": "8.4",
            "ibu": "38",
            "srmId": 41,
            "styleId": 158,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/8wyzkj/upload_0Fm2f6-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2019-03-09 13:46:45",
            "updateDate": "2019-03-09 13:47:28",
            "srm": {
                "id": 41,
                "name": "Over 40",
                "hex": "000000"
            },
            "style": {
                "id": 158,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style Imperial Porter",
                "shortName": "American Imperial Porter",
                "description": "American-style imperial porters are black in color. No roast barley or strong burnt/astringent black malt character should be perceived. Medium malt, caramel and cocoa-like sweetness. Hop bitterness is perceived at a medium-low to medium level. Hop flavor and aroma may vary from being low to medium-high. This is a full bodied beer. Ale-like fruity esters should be evident but not overpowering and compliment hop character and malt derived sweetness. Diacetyl (butterscotch) levels should be absent.",
                "ibuMin": "35",
                "ibuMax": "50",
                "abvMin": "5.5",
                "abvMax": "9.5",
                "srmMin": "40",
                "srmMax": "40",
                "ogMin": "1.08",
                "ogMax": "1.1",
                "fgMin": "1.02",
                "fgMax": "1.03",
                "createDate": "2013-08-10 12:42:51",
                "updateDate": "2015-04-07 15:49:32"
            }
        },
        {
            "id": "NuwQdp",
            "name": "'Bout 'Effin Time",
            "nameDisplay": "'Bout 'Effin Time",
            "description": "Our popular West Coast IPA, but turned up to 11 and bursting with hop flavour.",
            "abv": "8.5",
            "ibu": "75",
            "styleId": 31,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/NuwQdp/upload_fo6tyE-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2019-06-03 14:17:13",
            "updateDate": "2019-06-03 14:17:57",
            "style": {
                "id": 31,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Imperial or Double India Pale Ale",
                "shortName": "Imperial IPA",
                "description": "Imperial or Double India Pale Ales have intense hop bitterness, flavor and aroma. Alcohol content is medium-high to high and notably evident. They range from deep golden to medium copper in color. The style may use any variety of hops. Though the hop character is intense it's balanced with complex alcohol flavors, moderate to high fruity esters and medium to high malt character. Hop character should be fresh and lively and should not be harsh in quality. The use of large amounts of hops may cause a degree of appropriate hop haze. Imperial or Double India Pale Ales have medium-high to full body. Diacetyl should not be perceived. The intention of this style of beer is to exhibit the fresh and bright character of hops. Oxidative character and aged character should not be present.",
                "ibuMin": "65",
                "ibuMax": "100",
                "abvMin": "7.5",
                "abvMax": "10.5",
                "srmMin": "5",
                "srmMax": "13",
                "ogMin": "1.075",
                "fgMin": "1.012",
                "fgMax": "1.02",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:46"
            }
        },
        {
            "id": "ZQzj1u",
            "name": "'Lil Griz",
            "nameDisplay": "'Lil Griz",
            "description": "Deliberately blazing our own trail, we brewed this barrel aged brown ale believing there is room for a new craft beer category: “Sessionable Bourbon Barrel Aged Beers”. Weighing in at 6.8% ABV ( Alc. 6.8% by Vol. ), the rich chocolate notes & creaminess of the flaked oats easily justify this beer bringing home a FoBAB medal this year. We hope you enjoy the ‘Lil Griz.",
            "abv": "6.8",
            "ibu": "34",
            "styleId": 37,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/ZQzj1u/upload_0hoJ8r-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2015-02-25 14:30:03",
            "updateDate": "2015-12-17 22:55:35",
            "style": {
                "id": 37,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style Brown Ale",
                "shortName": "American Brown",
                "description": "American brown ales range from deep copper to brown in color. Roasted malt caramel-like and chocolate-like characters should be of medium intensity in both flavor and aroma. American brown ales have evident low to medium hop flavor and aroma, medium to high hop bitterness, and a medium body. Estery and fruity-ester characters should be subdued. Diacetyl should not be perceived. Chill haze is allowable at cold temperatures.",
                "ibuMin": "25",
                "ibuMax": "45",
                "abvMin": "4",
                "abvMax": "6.4",
                "srmMin": "15",
                "srmMax": "26",
                "ogMin": "1.04",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:27:35"
            }
        },
        {
            "id": "sBTXRJ",
            "name": "'Merica",
            "nameDisplay": "'Merica",
            "description": "Merica is a single malt, single hop farmhouse ale. It’s brewed with floor malted pilsner and 3lbs per bbl Nelson Sauvin hops. The beer is conditioned with 2 brett strains and wine yeast. The Nelson hops provide white wine flavors while Brettanomyces add a juicy quality to the beer.",
            "abv": "7.5",
            "ibu": "30",
            "styleId": 72,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/sBTXRJ/upload_OFYowQ-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2013-02-22 13:04:53",
            "updateDate": "2018-08-13 15:18:57",
            "style": {
                "id": 72,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "French & Belgian-Style Saison",
                "shortName": "Saison",
                "description": "Beers in this category are golden to deep amber in color. There may be quite a variety of characters within this style. Generally: They are light to medium in body. Malt aroma is low to medium-low. Esters are medium to high in  aroma, while, complex alcohols, herbs, spices, low Brettanomyces character and even clove and smoke-like phenolics may or may not be evident in the overall balanced beer. Hop aroma and flavor may be at low to medium levels. Malt flavor is low but provides foundation for the overall balance. Hop bitterness is moderate to moderately assertive. Herb and/or spice flavors, including black pepper-like notes, may or may not be evident. Fruitiness from fermentation is generally in character. A balanced small amount of sour or acidic flavors is acceptable when in balance with other components. Earthy, cellar-like, musty aromas are okay. Diacetyl should not be perceived. Chill or slight yeast haze is okay. Often bottle conditioned with some yeast character and high carbonation. French & Belgian-Style Saison may have Brettanomyces characters that are slightly acidity, fruity, horsey, goaty and/or leather-like.",
                "ibuMin": "20",
                "ibuMax": "40",
                "abvMin": "4.5",
                "abvMax": "8.5",
                "srmMin": "4",
                "srmMax": "14",
                "ogMin": "1.055",
                "fgMin": "1.004",
                "fgMax": "1.016",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:34:55"
            }
        },
        {
            "id": "7WoDkH",
            "name": "'Merican",
            "nameDisplay": "'Merican",
            "abv": "5.8",
            "glasswareId": 5,
            "styleId": 32,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/7WoDkH/upload_JsZsYY-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2013-11-01 12:36:31",
            "updateDate": "2015-12-17 06:41:04",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "style": {
                "id": 32,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style Amber/Red Ale",
                "shortName": "Amber",
                "description": "American amber/red ales range from light copper to light brown in color. They are characterized by American-variety hops used to produce the perception of medium hop bitterness, flavor, and medium aroma. Amber ales have medium-high to high maltiness with medium to low caramel character. They should have medium to medium-high body. The style may have low levels of fruityester flavor and aroma. Diacetyl can be either absent or barely perceived at very low levels. Chill haze is allowable at cold temperatures. Slight yeast haze is acceptable for bottle-conditioned products.",
                "ibuMin": "30",
                "ibuMax": "40",
                "abvMin": "4.5",
                "abvMax": "6",
                "srmMin": "11",
                "srmMax": "18",
                "ogMin": "1.048",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:52"
            }
        },
        {
            "id": "c4f2KE",
            "name": "'Murican Pilsner",
            "nameDisplay": "'Murican Pilsner",
            "abv": "5.5",
            "glasswareId": 4,
            "styleId": 98,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/c4f2KE/upload_jjKJ7g-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2013-08-19 11:58:12",
            "updateDate": "2015-12-17 06:02:53",
            "glass": {
                "id": 4,
                "name": "Pilsner",
                "createDate": "2012-01-03 02:41:33"
            },
            "style": {
                "id": 98,
                "categoryId": 8,
                "category": {
                    "id": 8,
                    "name": "North American Lager",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "American-Style Pilsener",
                "shortName": "American Pilsener",
                "description": "This classic and unique pre-Prohibition American-style Pilsener is straw to deep gold in color. Hop bitterness, flavor and aroma are medium to high, and use of noble-type hops for flavor and aroma is preferred. Up to 25 percent corn and/or rice in the grist should be used. Malt flavor and aroma are medium. This is a light-medium to medium-bodied beer. Sweet corn-like dimethylsulfide (DMS), fruity esters and American hop-derived citrus flavors or aromas should not be perceived. Diacetyl is not acceptable. There should be no chill haze. Competition organizers may wish to subcategorize this style into rice and corn subcategories.",
                "ibuMin": "25",
                "ibuMax": "40",
                "abvMin": "5",
                "abvMax": "6",
                "srmMin": "3",
                "srmMax": "6",
                "ogMin": "1.045",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:40:08"
            }
        },
        {
            "id": "EPLPz5",
            "name": "'n Toeback",
            "nameDisplay": "'n Toeback",
            "description": "'n Toeback is a top fermenting 'Kempense Quattro'.\r\nLegend says that after drinking a toeback quattro one of the 'Wildemannen' takes the Sint-Katharina church of Hoogstraten out for a walk. He can carry a 105 meter tower, weighing 100 metric tons on his back! A magic beer, that 'toeback'!",
            "abv": "9.5",
            "styleId": 63,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/EPLPz5/upload_WLs95w-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2012-11-06 12:28:06",
            "updateDate": "2015-12-16 19:40:08",
            "style": {
                "id": 63,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Pale Strong Ale",
                "shortName": "Belgian Pale Strong",
                "description": "Belgian pale strong ales are pale to golden in color with relatively light body for a beer of its alcoholic strength. Often brewed with light colored Belgian \"candy\" sugar, these beers are well attenuated. The perception of hop bitterness is medium-low to medium -high, with hop flavor and aroma also in this range. These beers are highly attenuated and have a perceptively deceiving high alcoholic character-being light to medium bodied rather than full bodied. The intensity of malt character should be low to medium, often surviving along with a complex fruitiness. Very little or no diacetyl is perceived. Herbs and spices are sometimes used to delicately flavor these strong ales. Low levels of phenolic spiciness from yeast byproducts may also be perceived. Chill haze is allowable at cold temperatures.",
                "ibuMin": "20",
                "ibuMax": "50",
                "abvMin": "7",
                "abvMax": "11",
                "srmMin": "4",
                "srmMax": "10",
                "ogMin": "1.064",
                "fgMin": "1.012",
                "fgMax": "1.024",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:32:16"
            }
        },
        {
            "id": "IkRF2B",
            "name": "'Nother Day in Paradise",
            "nameDisplay": "'Nother Day in Paradise",
            "availableId": 3,
            "styleId": 125,
            "isOrganic": "N",
            "isRetired": "Y",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/IkRF2B/upload_pe8G4j-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2012-03-30 12:27:35",
            "updateDate": "2018-11-02 02:13:07",
            "available": {
                "id": 3,
                "name": "Not Available",
                "description": "Beer is not currently available."
            },
            "style": {
                "id": 125,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Specialty Beer",
                "shortName": "Specialty",
                "description": "These beers are brewed using unusual fermentable sugars, grains and starches that contribute to alcohol content other than, or in addition to, malted barley. Nuts generally have some degree of fermentables, thus beers brewed with nuts would appropriately be entered in this category. The distinctive characters of these special ingredients should be evident either in the aroma, flavor or overall balance of the beer, but not necessarily in overpowering quantities. For example, maple syrup or potatoes would be considered unusual. Rice, corn, or wheat are not considered unusual. Special ingredients must be listed when competing. A statement by the brewer explaining the special nature of the beer, ingredient(s) and achieved character is essential in order for fair assessment in competitions. If this beer is a classic style with some specialty ingredient(s), the brewer should also specify the classic style. Guidelines for competing: Spiced beers using unusual fermentables should be entered in the experimental category. Fruit beers using unusual fermentables should be entered in the fruit beer category.",
                "ibuMax": "100",
                "abvMin": "2.5",
                "abvMax": "25",
                "srmMin": "1",
                "srmMax": "100",
                "ogMin": "1.03",
                "fgMin": "1.006",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:44:53"
            }
        },
        {
            "id": "SBjSb9",
            "name": "'Pack & Brass",
            "nameDisplay": "'Pack & Brass",
            "description": "A delectable combination of coffee and hops. We had our friends at Black and Brass Coffee Co. in Honesdale roast up some wonderful Yirgacheffe coffee beans. We then added those to an IPA dry hopped generously with Chinook, Simcoe, and Citra. The end result is a wonderfully balanced beer in which the coffee and hops meld into one.",
            "abv": "6.8",
            "ibu": "55",
            "availableId": 2,
            "styleId": 123,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/SBjSb9/upload_Xz72TA-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "originalGravity": "1.065",
            "createDate": "2019-06-03 16:03:16",
            "updateDate": "2019-06-03 18:05:34",
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 123,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Coffee-Flavored Beer",
                "shortName": "Coffee Beer",
                "description": "Coffee beers use coffee in any of its forms other than or in addition to hops to create a distinct (ranging from subtle to intense) character. Under hopping allows coffee to contribute to the flavor profile while not becoming excessively bitter. If this beer is a classic style with coffee flavor, the brewer should specify the classic style.",
                "ibuMin": "15",
                "ibuMax": "40",
                "abvMin": "2.5",
                "abvMax": "12",
                "srmMin": "8",
                "srmMax": "50",
                "ogMin": "1.03",
                "fgMin": "1.006",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:44:40"
            }
        },
        {
            "id": "i51yaD",
            "name": "'t Smisje Kirst",
            "nameDisplay": "'t Smisje Kirst",
            "abv": "11",
            "styleId": 64,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/i51yaD/upload_1WsEQd-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2014-07-14 19:55:57",
            "updateDate": "2015-12-17 15:18:38",
            "style": {
                "id": 64,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Dark Strong Ale",
                "shortName": "Belgian Dark Strong",
                "description": "Belgian dark strong ales are amber to dark brown in color. Often, though not always, brewed with dark Belgian \"candy\" sugar, these beers can be well attenuated, ranging from medium to full-bodied. The perception of hop bitterness is low to medium, with hop flavor and aroma also in this range. Fruity complexity along with the soft flavors of roasted malts add distinct character. The alcohol strength of these beers can often be deceiving to the senses. The intensity of malt character can be rich, creamy, and sweet with intensities ranging from medium to high. Very little or no diacetyl is perceived. Herbs and spices are sometimes used to delicately flavor these strong ales. Low levels of phenolic spiciness from yeast byproducts may also be perceived. Chill haze is allowable at cold temperatures.",
                "ibuMin": "20",
                "ibuMax": "50",
                "abvMin": "7",
                "abvMax": "11",
                "srmMin": "9",
                "srmMax": "35",
                "ogMin": "1.064",
                "fgMin": "1.012",
                "fgMax": "1.024",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:32:23"
            }
        },
        {
            "id": "qbRV90",
            "name": "'tis the Saison",
            "nameDisplay": "'tis the Saison",
            "description": "A Saison brewed with rye malt and three types of peppercorn.  This is Bart’s first NoDable Series brew so come out and enjoy!",
            "abv": "7",
            "ibu": "30",
            "glasswareId": 5,
            "srmId": 7,
            "availableId": 2,
            "styleId": 72,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/qbRV90/upload_OhEPYR-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2012-04-11 01:58:50",
            "updateDate": "2015-12-16 16:20:18",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 7,
                "name": "7",
                "hex": "F39C00"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 72,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "French & Belgian-Style Saison",
                "shortName": "Saison",
                "description": "Beers in this category are golden to deep amber in color. There may be quite a variety of characters within this style. Generally: They are light to medium in body. Malt aroma is low to medium-low. Esters are medium to high in  aroma, while, complex alcohols, herbs, spices, low Brettanomyces character and even clove and smoke-like phenolics may or may not be evident in the overall balanced beer. Hop aroma and flavor may be at low to medium levels. Malt flavor is low but provides foundation for the overall balance. Hop bitterness is moderate to moderately assertive. Herb and/or spice flavors, including black pepper-like notes, may or may not be evident. Fruitiness from fermentation is generally in character. A balanced small amount of sour or acidic flavors is acceptable when in balance with other components. Earthy, cellar-like, musty aromas are okay. Diacetyl should not be perceived. Chill or slight yeast haze is okay. Often bottle conditioned with some yeast character and high carbonation. French & Belgian-Style Saison may have Brettanomyces characters that are slightly acidity, fruity, horsey, goaty and/or leather-like.",
                "ibuMin": "20",
                "ibuMax": "40",
                "abvMin": "4.5",
                "abvMax": "8.5",
                "srmMin": "4",
                "srmMax": "14",
                "ogMin": "1.055",
                "fgMin": "1.004",
                "fgMax": "1.016",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:34:55"
            }
        },
        {
            "id": "GMWSAD",
            "name": "(401) India Pale Ale",
            "nameDisplay": "(401) India Pale Ale",
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/GMWSAD/upload_3dlRGl-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2013-07-22 23:17:15",
            "updateDate": "2015-12-17 04:43:34",
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "tciJOF",
            "name": "(512) ALT",
            "nameDisplay": "(512) ALT",
            "description": "(512) ALT is a German-style amber ale that is fermented cooler than typical ales and cold conditioned like a lager. ALT means \"old\" in German and refers to a beer style made using ale yeast after many German brewers had switched to newly discovered lager yeast. This ale has a very smooth, yet pronounced, hop bitterness with a malty backbone and a characteristic German yeast character. Made with 98% Organic 2-row and Munch malts and US noble hops.",
            "abv": "6",
            "ibu": "36",
            "glasswareId": 5,
            "srmId": 21,
            "availableId": 5,
            "styleId": 55,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/tciJOF/upload_cdbSIJ-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 05:20:58",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 21,
                "name": "21",
                "hex": "952D00"
            },
            "available": {
                "id": 5,
                "name": "Spring",
                "description": "Available during the spring months."
            },
            "style": {
                "id": 55,
                "categoryId": 4,
                "category": {
                    "id": 4,
                    "name": "German Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "German-Style Altbier",
                "shortName": "Altbier",
                "description": "German-Style Altbiers are copper to dark brown ales, originally from the Düsseldorf area. No chill haze should be perceived. A variety of malts including wheat may be used to produce medium-low to medium malt aroma. Fruityester aroma can be low. No diacetyl aroma should be perceived. Hop aroma is low to medium. A variety of malts including wheat may be used to produce medium-low to medium level malty flavor. Hop flavor is low to medium. Hop bitterness is medium to very high (although the 25 to 35 IBU range is more normal for the majority of Altbiers from Düsseldorf). Fruity-ester flavors can be low. No diacetyl should be perceived. The overall impression is clean, crisp, and flavorful often with a dry finish. Body is medium.",
                "ibuMin": "25",
                "ibuMax": "52",
                "abvMin": "4.3",
                "abvMax": "5.5",
                "srmMin": "11",
                "srmMax": "19",
                "ogMin": "1.044",
                "fgMin": "1.008",
                "fgMax": "1.014",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 17:08:31"
            }
        },
        {
            "id": "6PPnT2",
            "name": "(512) Black IPA",
            "nameDisplay": "(512) Black IPA",
            "description": "An entirely new creation from organic 2-row, organic Crystal 60 and Carafa III, a huskless black malt that gives this beer it’s black color with notes of coffee and chicory without any tannic bitterness. The hop additions are many and generous, featuring Apollo, Horizon, and Nugget, clocking the beer in at 70 IBU. Over 11 pounds per batch of Nugget hops are added directly to the fermenter yielding a resiny herbal and spicy aroma. A hybrid style for dark beer fans who love hops.",
            "abv": "7.5",
            "ibu": "70",
            "glasswareId": 5,
            "srmId": 41,
            "availableId": 5,
            "styleId": 125,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/6PPnT2/upload_Cnl1UJ-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 07:13:40",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 41,
                "name": "Over 40",
                "hex": "000000"
            },
            "available": {
                "id": 5,
                "name": "Spring",
                "description": "Available during the spring months."
            },
            "style": {
                "id": 125,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Specialty Beer",
                "shortName": "Specialty",
                "description": "These beers are brewed using unusual fermentable sugars, grains and starches that contribute to alcohol content other than, or in addition to, malted barley. Nuts generally have some degree of fermentables, thus beers brewed with nuts would appropriately be entered in this category. The distinctive characters of these special ingredients should be evident either in the aroma, flavor or overall balance of the beer, but not necessarily in overpowering quantities. For example, maple syrup or potatoes would be considered unusual. Rice, corn, or wheat are not considered unusual. Special ingredients must be listed when competing. A statement by the brewer explaining the special nature of the beer, ingredient(s) and achieved character is essential in order for fair assessment in competitions. If this beer is a classic style with some specialty ingredient(s), the brewer should also specify the classic style. Guidelines for competing: Spiced beers using unusual fermentables should be entered in the experimental category. Fruit beers using unusual fermentables should be entered in the fruit beer category.",
                "ibuMax": "100",
                "abvMin": "2.5",
                "abvMax": "25",
                "srmMin": "1",
                "srmMax": "100",
                "ogMin": "1.03",
                "fgMin": "1.006",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:44:53"
            }
        },
        {
            "id": "VwR7Xg",
            "name": "(512) Bruin (A.K.A. Brown Bear)",
            "nameDisplay": "(512) Bruin (A.K.A. Brown Bear)",
            "description": "At once cuddly and ferocious, (512) BRUIN combines a smooth, rich maltiness and mahogany color with a solid hop backbone and stealthy 7.6% alcohol. Made with Organic 2 Row and Munich malts, plus Chocolate and Crystal malts, domestic hops, and a touch of molasses, this brew has notes of raisins, dark sugars, and cocoa, and pairs perfectly with food and the crisp fall air.",
            "abv": "7.6",
            "ibu": "30",
            "glasswareId": 5,
            "srmId": 21,
            "availableId": 7,
            "styleId": 37,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/VwR7Xg/upload_MiNs9j-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 05:30:35",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 21,
                "name": "21",
                "hex": "952D00"
            },
            "available": {
                "id": 7,
                "name": "Fall",
                "description": "Available during the fall months."
            },
            "style": {
                "id": 37,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style Brown Ale",
                "shortName": "American Brown",
                "description": "American brown ales range from deep copper to brown in color. Roasted malt caramel-like and chocolate-like characters should be of medium intensity in both flavor and aroma. American brown ales have evident low to medium hop flavor and aroma, medium to high hop bitterness, and a medium body. Estery and fruity-ester characters should be subdued. Diacetyl should not be perceived. Chill haze is allowable at cold temperatures.",
                "ibuMin": "25",
                "ibuMax": "45",
                "abvMin": "4",
                "abvMax": "6.4",
                "srmMin": "15",
                "srmMax": "26",
                "ogMin": "1.04",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:27:35"
            }
        },
        {
            "id": "SqP18Z",
            "name": "(512) Cascabel Cream Stout",
            "nameDisplay": "(512) Cascabel Cream Stout",
            "description": "Smooth and roasty, and black as night, (512) Cascabel Cream Stout is brewed to a hair under 6% abv using almost 90% Organic Two Row and Crystal Malts, Chocolate Malt, and Roasted Barley. Non-fermentable Brewers Lactose is added for lasting sweetness, and over 20 pounds of Guajillo Chiles are added to warm you up when the night gets “chile”.",
            "abv": "6",
            "ibu": "20",
            "glasswareId": 5,
            "srmId": 41,
            "availableId": 8,
            "styleId": 20,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/SqP18Z/upload_8FxcuW-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cool",
            "servingTemperatureDisplay": "Cool - (8-12C/45-54F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 06:24:47",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 41,
                "name": "Over 40",
                "hex": "000000"
            },
            "available": {
                "id": 8,
                "name": "Winter",
                "description": "Available during the winter months."
            },
            "style": {
                "id": 20,
                "categoryId": 1,
                "category": {
                    "id": 1,
                    "name": "British Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Sweet or Cream Stout",
                "shortName": "Sweet Stout",
                "description": "Sweet stouts, also referred to as cream stouts, have less roasted bitter flavor and a full-bodied mouthfeel. The style can be given more body with milk sugar (lactose) before bottling. Malt sweetness, chocolate, and caramel flavor should dominate the flavor profile and contribute to the aroma. Hops should balance and suppress some of the sweetness without contributing apparent flavor or aroma. The overall impression should be sweet and full-bodied.",
                "ibuMin": "15",
                "ibuMax": "25",
                "abvMin": "3",
                "abvMax": "6",
                "srmMin": "40",
                "srmMax": "40",
                "ogMin": "1.045",
                "fgMin": "1.012",
                "fgMax": "1.02",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:24:41"
            }
        },
        {
            "id": "SV7JCk",
            "name": "(512) FIVE",
            "nameDisplay": "(512) FIVE",
            "description": "(512) FIVE is the culmination of our experience thus far and features a lineup of some of our favorite ingredients. Organic American two-row and English Maris Otter malts lay the foundation, while a generous dose of English roasted barley, black malt and chocolate malt create layers of roasty, dark complexity. American and Belgian crystal malts give balance and depth to the roasted character. Multiple additions of UK Fuggle hops impart an earthy, spicy finish to this deep, dark Imperial Stout.",
            "abv": "10.1",
            "ibu": "45",
            "glasswareId": 6,
            "srmId": 41,
            "availableId": 8,
            "styleId": 43,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/SV7JCk/upload_RNljF3-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cool",
            "servingTemperatureDisplay": "Cool - (8-12C/45-54F)",
            "createDate": "2015-06-19 16:03:18",
            "updateDate": "2015-12-18 02:19:48",
            "glass": {
                "id": 6,
                "name": "Snifter",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 41,
                "name": "Over 40",
                "hex": "000000"
            },
            "available": {
                "id": 8,
                "name": "Winter",
                "description": "Available during the winter months."
            },
            "style": {
                "id": 43,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style Imperial Stout",
                "shortName": "American Imperial Stout",
                "description": "Black in color, American-style imperial stouts typically have a high alcohol content. Generally characterized as very robust. The extremely rich malty flavor and aroma are balanced with assertive hopping and fruity-ester characteristics. Bitterness should be moderately high to very high and balanced with full sweet malt character. Roasted malt astringency and bitterness can be moderately perceived but should not overwhelm the overall character. Hop aroma is usually moderately-high to overwhelmingly hop-floral, -citrus or -herbal. Diacetyl (butterscotch) levels should be absent.",
                "ibuMin": "50",
                "ibuMax": "80",
                "abvMin": "7",
                "abvMax": "12",
                "srmMin": "40",
                "srmMax": "40",
                "ogMin": "1.08",
                "fgMin": "1.02",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:28:49"
            }
        },
        {
            "id": "oJFZwK",
            "name": "(512) FOUR",
            "nameDisplay": "(512) FOUR",
            "description": "For our 4th anniversary, we turned to one of our greatest inspirations, the rich brewing tradition of Great Britain.\r\n\r\n(512) FOUR is a classic English-style Strong Ale. The biscuity Maris Otter and caramelly Crystal malts contribute notes of toast, toffee, and dried fruits, which are perfectly balanced with a blend of authentic UK Fuggle and East Kent Golding hops. Dry-hopped with Northdown, (512) FOUR is a complex and satisfying ale.",
            "abv": "7.5",
            "ibu": "35",
            "glasswareId": 5,
            "srmId": 8,
            "availableId": 2,
            "styleId": 14,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/oJFZwK/upload_B40pzO-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2013-10-07 22:14:45",
            "updateDate": "2015-12-17 06:36:42",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 8,
                "name": "8",
                "hex": "EA8F00"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 14,
                "categoryId": 1,
                "category": {
                    "id": 1,
                    "name": "British Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Strong Ale",
                "shortName": "Strong Ale",
                "description": "Light amber to mid-range brown in color, strong ales are medium to full bodied with a malty sweetness and may have low levels of roast malt character. Hop aroma should be minimal and flavor can vary from none to medium in character intensity. Fruity-ester flavors and aromas can contribute to the character of this ale. Bitterness should be minimal but evident and balanced with malt and/or caramel-like sweetness. Alcohol types can be varied and complex. A rich, often sweet and complex estery character may be evident. Very low levels of diacetyl are acceptable. Chill haze is acceptable at low temperatures. (This style may often be split into two categories, strong and very strong.)",
                "ibuMin": "30",
                "ibuMax": "65",
                "abvMin": "7",
                "abvMax": "11",
                "srmMin": "8",
                "srmMax": "21",
                "ogMin": "1.06",
                "fgMin": "1.014",
                "fgMax": "1.04",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:21:05"
            }
        },
        {
            "id": "ezGh5N",
            "name": "(512) IPA",
            "nameDisplay": "(512) IPA",
            "description": "(512) India Pale Ale is a big, aggressively dry-hopped American IPA with smooth bitterness (~65 IBU) balanced by medium maltiness. Organic 2-row malted barley, loads of hops, and great Austin water create an ale with apricot and vanilla aromatics that lure you in for more.",
            "abv": "7",
            "ibu": "65",
            "glasswareId": 5,
            "srmId": 8,
            "availableId": 1,
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/ezGh5N/upload_r8SNni-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 04:42:39",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 8,
                "name": "8",
                "hex": "EA8F00"
            },
            "available": {
                "id": 1,
                "name": "Year Round",
                "description": "Available year round as a staple beer."
            },
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "s8rdpK",
            "name": "(512) ONE",
            "nameDisplay": "(512) ONE (2009)",
            "description": "Our first anniversary release is a Belgian-style strong ale that is amber in color, with a light to medium body. Subtle malt sweetness is balanced with just enough hops. Soft honey aromas lead the way into rich raisin and mildly spicy, cake-like flavors. Made with 80% Organic Malted Barley, Belgian Specialty grains, Forbidden Fruit yeast, domestic hops and Round Rock local wildflower honey, this beer’s strength can be deceiving.",
            "abv": "8",
            "ibu": "22",
            "glasswareId": 8,
            "srmId": 8,
            "availableId": 2,
            "styleId": 63,
            "isOrganic": "N",
            "isRetired": "N",
            "year": 2009,
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/s8rdpK/upload_seL9LP-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-13 20:15:42",
            "updateDate": "2015-12-16 15:16:19",
            "glass": {
                "id": 8,
                "name": "Tulip",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 8,
                "name": "8",
                "hex": "EA8F00"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 63,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Pale Strong Ale",
                "shortName": "Belgian Pale Strong",
                "description": "Belgian pale strong ales are pale to golden in color with relatively light body for a beer of its alcoholic strength. Often brewed with light colored Belgian \"candy\" sugar, these beers are well attenuated. The perception of hop bitterness is medium-low to medium -high, with hop flavor and aroma also in this range. These beers are highly attenuated and have a perceptively deceiving high alcoholic character-being light to medium bodied rather than full bodied. The intensity of malt character should be low to medium, often surviving along with a complex fruitiness. Very little or no diacetyl is perceived. Herbs and spices are sometimes used to delicately flavor these strong ales. Low levels of phenolic spiciness from yeast byproducts may also be perceived. Chill haze is allowable at cold temperatures.",
                "ibuMin": "20",
                "ibuMax": "50",
                "abvMin": "7",
                "abvMax": "11",
                "srmMin": "4",
                "srmMax": "10",
                "ogMin": "1.064",
                "fgMin": "1.012",
                "fgMax": "1.024",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:32:16"
            }
        },
        {
            "id": "2fXsvw",
            "name": "(512) Pale",
            "nameDisplay": "(512) Pale",
            "description": "(512) Pale is a copper colored American Pale Ale that balances earthy hop bitterness and bright hop flavor with a rich malty body. Made with Organic 2-row malt and US grown hops like all (512) ales, this beer is refreshing and not to be missed.",
            "abv": "6",
            "ibu": "30",
            "glasswareId": 5,
            "srmId": 7,
            "availableId": 1,
            "styleId": 25,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/2fXsvw/upload_c0Trtt-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 05:31:49",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 7,
                "name": "7",
                "hex": "F39C00"
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
        },
        {
            "id": "NZYBId",
            "name": "(512) Peach Sour",
            "nameDisplay": "(512) Peach Sour (2014)",
            "description": "We produced Peach Sour using a sour mash technique. We encouraged the naturally occurring wild yeast and bacteria that come in with the organic barley and wheat to spontaneously ferment at warm temperatures over a three day period. Fermentation was completed in stainless and racked to a 1,000 gallon Foeder (large oak barrel) for aging. After being on the wood for two months, we added 200 pounds of fresh peaches and allowed it to age another 12 months before packaging it for you. We hope you enjoy!",
            "abv": "6.2",
            "ibu": "8",
            "glasswareId": 8,
            "availableId": 2,
            "styleId": 136,
            "isOrganic": "N",
            "isRetired": "N",
            "year": 2014,
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/NZYBId/upload_fZwIL9-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cool",
            "servingTemperatureDisplay": "Cool - (8-12C/45-54F)",
            "createDate": "2014-10-28 13:32:24",
            "updateDate": "2015-12-17 19:22:18",
            "glass": {
                "id": 8,
                "name": "Tulip",
                "createDate": "2012-01-03 02:41:33"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 136,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Wood- and Barrel-Aged Sour Beer",
                "shortName": "BBL Aged Sour",
                "description": "A wood- or barrel-aged sour beer is any lager, ale or hybrid beer, either a traditional style or a unique experimental beer that has been aged for a period of time in a wooden barrel or in contact with wood and has developed a bacterial induced natural acidity. This beer is aged in wood with the intention of introducing the micro flora present in the wood. Sometimes wood aging is intended to impart the particularly unique character of the wood, but wood-aged is not necessarily synonymous with imparting wood-flavors. Wood character can be characterized as a complex blend of vanillin and unique wood character. Wood-derived character can also be characterized by flavors of the product that was in the barrel during prior use. These wood-derived flavors, if present in this style, can be very low in character and barely perceived or evident or assertive as wood-derived flavors. Any degree of woodderived flavors should be in balance with other beer character. Fruit and herb/spiced versions may take on the hue, flavors and aromas of added ingredients.  Usually bacteria and \"wild\" yeasts fermentation contributes complex esters and results in a dry to very dry beer. Ultimately a balance of flavor, aroma and mouthfeel are sought with the marriage of acidity, complex esters, and new beer with wood and/or barrel flavors. Beers in this style may or may not have Brettanomyces character.  Brewers when entering this category should specify type of barrel used and any other special treatment or ingredients used. Competition managers may create style subcategories to differentiate between high alcohol and low alcohol beers and very dark and lighter colored beer as well as for fruit beers and non-fruit beers. Competitions may develop guidelines requesting brewers to specify what kind of wood (new or used oak, other wood varieties). The brewer may be asked to explain the special nature (wood used, base beer style(s) and achieved character) of the beer.",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:46:56"
            }
        },
        {
            "id": "9O3QPg",
            "name": "(512) SIX",
            "nameDisplay": "(512) SIX",
            "description": "(512) SIX is a Belgian Style Dubbel with as many organic Belgian ingredients as possible. Castle Pale, Special B and Cara-Munich lend unique Belgian terrior based flavors of dark fruits like plum, raisin and chocolate. Candi sugar cranks the alcohol without increasing the body. This low hopped malty beast from the dungeons of (512) will make a cold day warmer and our 6th Anniversary event one for the books.",
            "abv": "7.5",
            "ibu": "25",
            "glasswareId": 8,
            "srmId": 28,
            "availableId": 2,
            "styleId": 58,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/9O3QPg/upload_GIORHy-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cool",
            "servingTemperatureDisplay": "Cool - (8-12C/45-54F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 05:41:29",
            "glass": {
                "id": 8,
                "name": "Tulip",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 28,
                "name": "28",
                "hex": "6A0E00"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 58,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Dubbel",
                "shortName": "Belgian Dubbel",
                "description": "This medium-bodied, red to dark brown colored ale has a malty sweetness and chocolate-like caramel aroma. A light hop flavor and/or aroma is acceptable. Dubbels are also characterized by low-medium to medium bitterness. No diacetyl is acceptable. Yeastgenerated fruity esters (especially banana) are appropriate at low levels. Head retention is dense and mousse-like. Chill haze is acceptable at low serving temperatures. Often bottle conditioned a slight yeast haze and flavor may be evident.",
                "ibuMin": "20",
                "ibuMax": "30",
                "abvMin": "6.25",
                "abvMax": "7.5",
                "srmMin": "16",
                "srmMax": "36",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.016",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:31:45"
            }
        },
        {
            "id": "A78JSF",
            "name": "(512) THREE",
            "nameDisplay": "(512) THREE",
            "description": "For our 3rd Anniversary release we knew we had to pull out all the stops. Please welcome to the family… (512) THREE Belgian Style Tripel! Brewed in the spirit of the abbey ales of Belgium, (512) THREE pours a deep golden with a dense, creamy white head. The authentic Belgian yeast strain produces a complex, spicy palate that balances ripe fruity esters with bready malts and firm but subtle hops. Our house-made liquid invert sugar contributes an effervescent mouthfeel that finishes smooth and silky but enticingly dry, barely betraying its nearly 9.5% ABV/VOL!",
            "abv": "9.5",
            "ibu": "22",
            "glasswareId": 5,
            "srmId": 10,
            "availableId": 2,
            "styleId": 59,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/A78JSF/upload_COtQzI-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-09 18:45:11",
            "updateDate": "2015-12-16 15:12:37",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 10,
                "name": "10",
                "hex": "DE7C00"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 59,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style Tripel",
                "shortName": "Belgian Tripel",
                "description": "Tripels are often characterized by a complex, sometimes mild spicy character. Clove-like phenolic flavor and aroma may be evident at extremely low levels. Yeast-generated  fruity esters, including banana, are also common, but not necessary. These pale/light-colored ales may finish sweet, though any sweet finish should be light. The beer is characteristically medium and clean in body with an equalizing hop/malt balance and a perception of medium to medium high hop bitterness. Traditional Belgian Tripels are often well attenuated. Brewing sugar may be used to lighten the perception of body. Its sweetness will come from very pale malts. There should not be character from any roasted or dark malts. Low hop flavor is acceptable. Alcohol strength and flavor should be perceived as evident. Head retention is dense and mousse-like. Chill haze is acceptable at low serving temperatures. Traditional Tripels are bottle conditioned, may exhibit slight yeast haze but the yeast should not be intentionally roused. Oxidative character if evident in aged Tripels should be mild and pleasant.",
                "ibuMin": "20",
                "ibuMax": "45",
                "abvMin": "7",
                "abvMax": "10",
                "srmMin": "4",
                "srmMax": "9",
                "ogMin": "1.07",
                "fgMin": "1.01",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:31:50"
            }
        },
        {
            "id": "X4KcGF",
            "name": "(512) TWO",
            "nameDisplay": "(512) TWO",
            "description": "We went all out on the hops for our 2nd Anniversary release, a Double IPA. Eight varieties of hops (including Glacier, Horizon, Nugget, and Columbus) spread out over 10 different additions (including whole-leaf Simcoe and Nugget in the grant, and 2 separate dry-hoppings!) add up to 99 IBUs of pure hoppy goodness . A solid malt backbone supports the smooth bitterness, complex flavors, and intoxicating aroma. And like all (512) ales, this one is made using over 80% USDA certified organic ingredients.",
            "abv": "9",
            "ibu": "99",
            "glasswareId": 5,
            "srmId": 9,
            "availableId": 6,
            "styleId": 31,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/X4KcGF/upload_Zcoan4-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 05:20:12",
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
                "id": 6,
                "name": "Summer",
                "description": "Available during the summer months."
            },
            "style": {
                "id": 31,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "Imperial or Double India Pale Ale",
                "shortName": "Imperial IPA",
                "description": "Imperial or Double India Pale Ales have intense hop bitterness, flavor and aroma. Alcohol content is medium-high to high and notably evident. They range from deep golden to medium copper in color. The style may use any variety of hops. Though the hop character is intense it's balanced with complex alcohol flavors, moderate to high fruity esters and medium to high malt character. Hop character should be fresh and lively and should not be harsh in quality. The use of large amounts of hops may cause a degree of appropriate hop haze. Imperial or Double India Pale Ales have medium-high to full body. Diacetyl should not be perceived. The intention of this style of beer is to exhibit the fresh and bright character of hops. Oxidative character and aged character should not be present.",
                "ibuMin": "65",
                "ibuMax": "100",
                "abvMin": "7.5",
                "abvMax": "10.5",
                "srmMin": "5",
                "srmMax": "13",
                "ogMin": "1.075",
                "fgMin": "1.012",
                "fgMax": "1.02",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:46"
            }
        },
        {
            "id": "USaRyl",
            "name": "(512) Whiskey Barrel Double Pecan Porter",
            "nameDisplay": "(512) Whiskey Barrel Double Pecan Porter",
            "description": "(512) Double Pecan Porter is a robust porter accented by locally grown roasted pecans and subtly enhanced by aging in recently emptied oak whiskey barrels. For the first ever bottling, only one 200L barrel was bottled. Notes of chocolate, coffee and pecan marry with the subtle flavors of vanilla and whiskey to make this a wonderful winter warmer worth sharing and savoring. We sincerely hope you enjoy every sip.",
            "abv": "9.5",
            "ibu": "30",
            "glasswareId": 5,
            "srmId": 41,
            "availableId": 2,
            "styleId": 135,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/USaRyl/upload_1rXpCX-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-13 20:20:15",
            "updateDate": "2015-12-16 15:01:21",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 41,
                "name": "Over 40",
                "hex": "000000"
            },
            "available": {
                "id": 2,
                "name": "Limited",
                "description": "Limited availability."
            },
            "style": {
                "id": 135,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Wood- and Barrel-Aged Strong Beer",
                "shortName": "BBL Aged Strong",
                "description": "Any strong classic style or unique, experimental style of beer can be wood or barrel-aged for a period of time in a wooden barrel or in contact with wood. This beer is aged with the intention of imparting the particularly unique character of the wood and/or what has previously been in the barrel. New wood character can be characterized as a complex blend of vanillin and unique wood character but wood aged is not necessarily synonymous with imparting wood-flavors. Used sherry, rum, bourbon, scotch, port, wine and other barrels are often used, imparting complexity and uniqueness to beer. Ultimately a balance of flavor, aroma and mouthfeel are sought with the marriage of new beer with wood and/or barrel flavors. Primary character of the beer style may or may not be apparent. Sour wood-aged beer of any color is outlined in other categories. Beers in this style may or may not have Brettanomyces character. The brewer must explain the special nature of the beer to allow for accurate judging. Comments could include: type of wood used (new or old, oak or other wood type), type of barrel used (new, port/ whiskey/ wine/ sherry/ other), base beer style or achieved character. Beer entries not accompanied by this information will be at a disadvantage during judging.",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:46:50"
            }
        },
        {
            "id": "bXwskR",
            "name": "(512) White IPA",
            "nameDisplay": "(512) White IPA",
            "description": "Refreshingly light, this Belgian inspired India Pale Ale delivers hot weather satisfaction with pronounced hop character and flavor. Built like a Belgian wheat beer, but brewed, hopped and finished  like an IPA, two classic brewing cultures collide in this delightful creation that is both sessionable and amazingly flavorful.",
            "abv": "5.3",
            "ibu": "55",
            "glasswareId": 5,
            "srmId": 4,
            "availableId": 6,
            "styleId": 30,
            "isOrganic": "Y",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/bXwskR/upload_0m1DZl-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2015-06-19 15:35:51",
            "updateDate": "2015-12-18 03:47:26",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 4,
                "name": "4",
                "hex": "FFBF42"
            },
            "available": {
                "id": 6,
                "name": "Summer",
                "description": "Available during the summer months."
            },
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "XnPVIo",
            "name": "(512) Wild Bear",
            "nameDisplay": "(512) Wild Bear",
            "description": "(512)’s first excursion into the world of so-called wild fermentation, Wild Bear’s origins lie in our Fall seasonal, BRUIN. After primary fermentation, we added Brettanomyces yeast and Pediococcus bacteria cultures, and aged the blend in new oak barrels for over 10 months. This combination of wild “bugs” and barrel aging gives (512) Wild Bear a complex and enticing aroma of tart cherries, oak, and a touch of barnyard “funkiness”, a crisp, tart flavor that will intensify with age, and an effervescent, oaky finish that leaves the palate clean. More recent versions are aged in one of our 45HL Foeder for 24 months.",
            "abv": "8.5",
            "ibu": "9",
            "glasswareId": 8,
            "availableId": 4,
            "styleId": 125,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/XnPVIo/upload_XCxTBJ-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-09 18:44:37",
            "updateDate": "2015-12-16 14:31:48",
            "glass": {
                "id": 8,
                "name": "Tulip",
                "createDate": "2012-01-03 02:41:33"
            },
            "available": {
                "id": 4,
                "name": "Seasonal",
                "description": "Available at the same time of year, every year."
            },
            "style": {
                "id": 125,
                "categoryId": 11,
                "category": {
                    "id": 11,
                    "name": "Hybrid/mixed Beer",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Specialty Beer",
                "shortName": "Specialty",
                "description": "These beers are brewed using unusual fermentable sugars, grains and starches that contribute to alcohol content other than, or in addition to, malted barley. Nuts generally have some degree of fermentables, thus beers brewed with nuts would appropriately be entered in this category. The distinctive characters of these special ingredients should be evident either in the aroma, flavor or overall balance of the beer, but not necessarily in overpowering quantities. For example, maple syrup or potatoes would be considered unusual. Rice, corn, or wheat are not considered unusual. Special ingredients must be listed when competing. A statement by the brewer explaining the special nature of the beer, ingredient(s) and achieved character is essential in order for fair assessment in competitions. If this beer is a classic style with some specialty ingredient(s), the brewer should also specify the classic style. Guidelines for competing: Spiced beers using unusual fermentables should be entered in the experimental category. Fruit beers using unusual fermentables should be entered in the fruit beer category.",
                "ibuMax": "100",
                "abvMin": "2.5",
                "abvMax": "25",
                "srmMin": "1",
                "srmMax": "100",
                "ogMin": "1.03",
                "fgMin": "1.006",
                "fgMax": "1.03",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:44:53"
            }
        },
        {
            "id": "QLp4mV",
            "name": "(512) Wit",
            "nameDisplay": "(512) Wit",
            "description": "Made in the style of the Belgian wheat beers that are so refreshing, (512) Wit is a hazy ale spiced with coriander and domestic grapefruit peel. 50% US Organic 2-row malted barley and 50% US unmalted wheat and oats make this a light, crisp ale well suited for any occasion.",
            "abv": "5.1",
            "ibu": "10",
            "glasswareId": 5,
            "srmId": 5,
            "availableId": 1,
            "styleId": 65,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/QLp4mV/upload_FfMhAC-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2012-01-03 02:42:36",
            "updateDate": "2015-12-16 04:38:26",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 5,
                "name": "5",
                "hex": "FBB123"
            },
            "available": {
                "id": 1,
                "name": "Year Round",
                "description": "Available year round as a staple beer."
            },
            "style": {
                "id": 65,
                "categoryId": 5,
                "category": {
                    "id": 5,
                    "name": "Belgian And French Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "Belgian-Style White (or Wit) / Belgian-Style Wheat",
                "shortName": "Witbier",
                "description": "Belgian white ales are very pale in color and are brewed using unmalted wheat and malted barley and are spiced with coriander and orange peel. Coriander and light orange peel aroma should be perceived as such or as an unidentified spiciness. Phenolic spiciness and yeast flavors may be evident at mild levels. These beers are traditionally bottle conditioned and served cloudy. An unfiltered starch and yeast haze should be part of the appearance. The low to medium body should have some degree of creaminess from wheat starch. The style is further characterized by the use of noble-type hops to achieve low hop bitterness and little to no apparent hop flavor. This beer has no diacetyl and a low to medium fruity-ester level. Mild acidity is appropriate.",
                "ibuMin": "10",
                "ibuMax": "17",
                "abvMin": "4.8",
                "abvMax": "5.2",
                "srmMin": "2",
                "srmMax": "4",
                "ogMin": "1.044",
                "fgMin": "1.006",
                "fgMax": "1.01",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:32:30"
            }
        },
        {
            "id": "jj8YRF",
            "name": "(860) India Pale Ale",
            "nameDisplay": "(860) India Pale Ale",
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/jj8YRF/upload_BwXlKY-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2013-09-15 19:48:52",
            "updateDate": "2015-12-17 05:37:37",
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "thTbY7",
            "name": "(904) Weissguy",
            "nameDisplay": "(904) Weissguy",
            "description": "A traditional Bavarian style Hefeweissen, notes of clove, orange and coriander along with a cloudy yeast character make this a summer favorite.",
            "abv": "4.4",
            "ibu": "19",
            "glasswareId": 9,
            "srmId": 4,
            "styleId": 48,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/thTbY7/upload_jxcOpY-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2012-02-17 13:08:40",
            "updateDate": "2015-12-16 15:32:04",
            "glass": {
                "id": 9,
                "name": "Weizen",
                "createDate": "2012-01-03 02:41:33"
            },
            "srm": {
                "id": 4,
                "name": "4",
                "hex": "FFBF42"
            },
            "style": {
                "id": 48,
                "categoryId": 4,
                "category": {
                    "id": 4,
                    "name": "German Origin Ales",
                    "createDate": "2012-03-21 20:06:46"
                },
                "name": "South German-Style Hefeweizen / Hefeweissbier",
                "shortName": "Hefeweizen",
                "description": "The aroma and flavor of a Weissbier with yeast is decidedly fruity and phenolic. The phenolic characteristics are often described as clove-, nutmeg-like, mildly smoke-like or even vanilla-like. Banana-like esters should be present at low to medium-high levels. These beers are made with at least 50 percent malted wheat, and hop rates are quite low. Hop flavor and aroma are absent or present at very low levels. Weissbier is well attenuated and very highly carbonated and a medium to full bodied beer. The color is very pale to pale amber. Because yeast is present, the beer will have yeast flavor and a characteristically fuller mouthfeel and may be appropriately very cloudy. No diacetyl should be perceived.",
                "ibuMin": "10",
                "ibuMax": "15",
                "abvMin": "4.9",
                "abvMax": "5.5",
                "srmMin": "3",
                "srmMax": "9",
                "ogMin": "1.047",
                "fgMin": "1.008",
                "fgMax": "1.016",
                "createDate": "2012-03-21 20:06:46",
                "updateDate": "2015-04-07 15:29:27"
            }
        },
        {
            "id": "FLkbzq",
            "name": "(KU)Jenga Smash",
            "nameDisplay": "(KU)Jenga Smash",
            "description": "IPA Collab w/ Two Stones Brewpub.",
            "abv": "7.7",
            "glasswareId": 5,
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/FLkbzq/upload_BfrB6Y-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "servingTemperature": "cold",
            "servingTemperatureDisplay": "Cold - (4-7C/39-45F)",
            "createDate": "2015-07-08 13:24:18",
            "updateDate": "2016-08-30 12:32:29",
            "glass": {
                "id": 5,
                "name": "Pint",
                "createDate": "2012-01-03 02:41:33"
            },
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "dVJb5O",
            "name": "(No) Pumpkin",
            "nameDisplay": "(No) Pumpkin",
            "description": "NO Pumpkin IPA is a Fall Seasonal IPA that is flavored without the use of pumpkin, or spices. That's right NO PUMPKIN in the beer! We feel that this trend, and these particular flavors are gross in beer and many other pumpkin infused items you will be experiencing this fall. The real flavor from this IPA comes from the hops not some useless squash. There are fruity notes of blackeberry, boysenberry and grape. So enjoy your pumpkin spice, chai, mocha, latte this fall, but when you and your palette needs a break from pumpkin invasion grab a Sloop NO Pumpkin.",
            "abv": "6",
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/dVJb5O/upload_YxDKP8-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "createDate": "2018-10-11 16:26:23",
            "updateDate": "2018-10-11 16:27:17",
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        },
        {
            "id": "3BSrTW",
            "name": "(Take The) Causeway IPA",
            "nameDisplay": "(Take The) Causeway IPA",
            "description": "Copious amounts of Citra and Simcoe hops are used throughout the brewing process in this American India Pale Ale. From first-wort to bittering, flavor, aroma and dry hops, an artful combination of just two extraordinary hops leads to an explosively hoppy finish on the palate. These hops are hard for us to get our hands on, so get it while you can.",
            "abv": "7.5",
            "ibu": "56",
            "availableId": 1,
            "styleId": 30,
            "isOrganic": "N",
            "isRetired": "N",
            "labels": {
                "icon": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-icon.png",
                "medium": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-medium.png",
                "large": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-large.png",
                "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-contentAwareIcon.png",
                "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-contentAwareMedium.png",
                "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/3BSrTW/upload_rltPd8-contentAwareLarge.png"
            },
            "status": "verified",
            "statusDisplay": "Verified",
            "originalGravity": "1.069",
            "createDate": "2015-03-11 18:58:53",
            "updateDate": "2019-04-24 20:05:01",
            "available": {
                "id": 1,
                "name": "Year Round",
                "description": "Available year round as a staple beer."
            },
            "style": {
                "id": 30,
                "categoryId": 3,
                "category": {
                    "id": 3,
                    "name": "North American Origin Ales",
                    "createDate": "2012-03-21 20:06:45"
                },
                "name": "American-Style India Pale Ale",
                "shortName": "American IPA",
                "description": "American-style India pale ales are perceived to have medium-high to intense hop bitterness, flavor and aroma with medium-high alcohol content. The style is further characterized by floral, fruity, citrus-like, piney, resinous, or sulfur-like American-variety hop character. Note that one or more of these American-variety hop characters is the perceived end, but the hop characters may be a result of the skillful use of hops of other national origins. The use of water with high mineral content results in a crisp, dry beer. This pale gold to deep copper-colored ale has a full, flowery hop aroma and may have a strong hop flavor (in addition to the perception of hop bitterness). India pale ales possess medium maltiness which contributes to a medium body. Fruity-ester flavors and aromas are moderate to very strong. Diacetyl can be absent or may be perceived at very low levels. Chill and/or hop haze is allowable at cold temperatures. (English and citrus-like American hops are considered enough of a distinction justifying separate American-style IPA and English-style IPA categories or subcategories. Hops of other origins may be used for bitterness or approximating traditional American or English character. See English-style India Pale Ale",
                "ibuMin": "50",
                "ibuMax": "70",
                "abvMin": "6.3",
                "abvMax": "7.5",
                "srmMin": "6",
                "srmMax": "14",
                "ogMin": "1.06",
                "fgMin": "1.012",
                "fgMax": "1.018",
                "createDate": "2012-03-21 20:06:45",
                "updateDate": "2015-04-07 15:26:37"
            }
        }
    ],
    "status": "success"
}

# with the actual URI for your database
DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/api'
engine = create_engine(DATABASE_URI)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

beerHead = getBeerModel(Base, 'beer_1')(**_datajson)
for item in _datajson['data']:
    _models = []
    style = Style(**item['style'])
    _models.append(style)
    category = Category(**item['style']['category'])
    # item['style']['category'] = category
    _models.append(category)
    if available in item.keys():
        available = Available(**item['available'])
        _models.append(available)

    beerHead = getBeerModel('beer_1')(**_datajson)
    _models.append(beerHead)
    beer = Beer(**item, parent=beerHead)
    _models.append(beer)


session.add(_models)

# # Commit the changes
session.commit()

# Close the session
session.close()
