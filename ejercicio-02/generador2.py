from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///datos_json.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class data_json(Base):
    __tablename__ = 'paises'
    
    id= Column(Integer, primary_key=True)
    cldr = Column(String)
    capital = Column(String)
    continent = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    languages = Column(String)
    is_independent = Column(String)
    def _repr_(self):
        return "paises: cldr=%s capital=%s continent:%s dial:%s geoname:%s itu:%s languages:%s is_independent:%s" % (
                          self.cldr, 
                          self.capital, 
                          self.continent,
                          self.dial,
                          self.geoname,
                          self.itu,
                          self.languages,
                          self.is_independent)

Base.metadata.create_all(engine)


### CDLR display name