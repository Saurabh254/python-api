from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date, Float, Column
from typing import Optional
from sqlalchemy.dialects.postgresql import JSON


'''
schema based on page 1, 2 and 3
'''


class Base(DeclarativeBase):
    pass


class BeerData(Base):
    __tablename__ = "beer_data"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    beer_currentPage: Mapped[int] = mapped_column(
        Integer, ForeignKey(f'beer_page.currentPage'))
    name: Mapped[Optional[str]]
    nameDisplay: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    abv: Mapped[Optional[str]]
    ibu: Mapped[Optional[str]]
    glasswareId: Mapped[Optional[int]]
    glass: Mapped[Optional[str]]
    styleId: Mapped[Optional[int]]
    srmId: Mapped[Optional[int]]
    availableId: Mapped[Optional[int]]
    year: Mapped[Optional[int]]
    isOrganic: Mapped[Optional[str]]
    isRetired: Mapped[Optional[str]]
    labels: Mapped[Optional[str]]
    status: Mapped[Optional[str]]
    statusDisplay: Mapped[Optional[str]]
    servingTemperature: Mapped[Optional[str]]
    servingTemperatureDisplay: Mapped[Optional[str]]
    foodPairings: Mapped[Optional[str]]
    createDate: Mapped[Optional[Date]] = mapped_column(Date)
    updateDate: Mapped[Optional[Date]] = mapped_column(Date)
    style: Mapped[Optional[str]]
    srm = Column(JSON)
    available: Mapped[Optional[str]]
    originalGravity: Mapped[Optional[float]]
    beerVariationId: Mapped[Optional[str]]
    beerVariation = Column(JSON)
    beer = relationship('Beer', back_populates='data')


class Beer(Base):
    __tablename__ = 'beer_page'
    currentPage: Mapped[int] = mapped_column(Integer, primary_key=True)
    numberOfPages: Mapped[int]
    totalResults: Mapped[int]
    data: Mapped[list[BeerData]] = relationship(
        'BeerData', back_populates='beer', cascade='all, delete-orphan')
    status: Mapped[Optional[str]]
