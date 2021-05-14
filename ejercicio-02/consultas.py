from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generador2 import data_json 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///datos_json.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad docentes 
data = session.query(data_json).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python

# Obtener todos los registros de 
# la tabla docentes que tengan como valor en 
# el atributo especifico 

print("------Presentar todos los países del continente americano---------")


continente = session.query(data_json).filter(data_json.continent=="NA").all()
for p in continente:
    print(p.continent)

print("--------Presentar los países de Asía, ordenados por el atributo Dial.----------")

ordenado = session.query(data_json).filter(data_json.continent=="AS").order_by(data_json.dial).all()
for p in ordenado:
    print(p.dial, p.continent)

print("-------Presentar los lenguajes de cada país.-----------")

lenguaje = session.query(data_json).all()
for p in lenguaje:
    print(str(p.cldr) + " Idiomas = " + str(p.languages))


print("----Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa--------")

capitales = session.query(data_json).filter(data_json.continent=="EU").order_by(data_json.capital).all() 
for p in capitales:
    print(str(p.cldr) + " su Capital " + str(p.capital))


print("------Presentar todos los países que tengan en su cadena de nombre de país uador o en su cadena de capital ito.----------")

capitales = session.query(data_json).filter(or_(data_json.cldr.like("%uador"), data_json.capital.like("%ito"))).all()
for p in capitales:
    print(str(p.cldr) + " su Capital " + str(p.capital))
    