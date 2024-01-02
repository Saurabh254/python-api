from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped


Base = declarative_base()


class Glass(Base):
    __tablename__ = 'glasses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_date = Column(DateTime)


class Srm(Base):
    __tablename__ = 'srms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hex = Column(String)


class Available(Base):
    __tablename__ = 'availables'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_date = Column(DateTime)


class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True)
    category_id = mapped_column(Integer, ForeignKey('categories.id'))
    name = Column(String)
    short_name = Column(String)
    description = Column(String)
    ibu_min = Column(Float)
    ibu_max = Column(Float)
    abv_min = Column(Float)
    abv_max = Column(Float)
    srm_min = Column(Float)
    srm_max = Column(Float)
    og_min = Column(Float)
    fg_min = Column(Float)
    fg_max = Column(Float)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    category = relationship('Category')


class Beer(Base):
    __tablename__ = 'beers'
    id = Column(String, primary_key=True)
    name = Column(String)
    name_display = Column(String)
    description = Column(String)
    abv = Column(Float)
    ibu = Column(Integer)
    glassware_id = mapped_column(Integer, ForeignKey('glasses.id'))
    srm_id = mapped_column(Integer, ForeignKey('srms.id'))
    available_id = mapped_column(Integer, ForeignKey('availables.id'))
    style_id = mapped_column(Integer, ForeignKey('styles.id'))
    labels = Column(JSON)
    is_organic = Column(String)
    is_retired = Column(String)
    status = Column(String)
    status_display = Column(String)
    serving_temperature = Column(String)
    serving_temperature_display = Column(String)
    original_gravity = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)

    glass = relationship('Glass')
    srm = relationship('Srm')
    available = relationship('Available')
    style = relationship('Style')
