# Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.
# Напишите Python скрипт, который:
# * Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
# * Импортирует необходимые модели данных.
# * Выводит название магазинов (shop), в которых представлены книги конкретного издателя, получая имя или идентификатор издателя (publisher), через `input(`).

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Sale, Stock

DSN = 'postgresql://postgres:postgres@localhost:5432/orm'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='РусКнига')
publisher2 = Publisher(name='NewBook')
publisher3 = Publisher(name='BestBook')

session.add([publisher1,publisher2,publisher3])
session.commit()

book1 = Book(title='Наука и техника', id_publisher='1')
book2 = Book(title='Роботы и женщины', id_publisher='1')
book3 = Book(title='Sun & planets', id_publisher='2')
book4 = Book(title='Letters in future', id_publisher='2')
book5 = Book(title='Hello from space', id_publisher='3')

session.add([book1,book2,book3,book4,book5])
session.commit()

shop1 = (name='кНигга')
shop2 = (name='AllIn')
shop3 = (name='Бумага и деньги')

session.add([shop1,shop2,shop3])
session.commit()

session.close()