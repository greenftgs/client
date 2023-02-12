from connect import db
from models import Publisher, Book, Shop, Sale, Stock


publisher1 = Publisher(name='РусКнига')
publisher2 = Publisher(name='NewBook')
publisher3 = Publisher(name='BestBook')

session.add([publisher1, publisher2, publisher3])
session.commit()

book1 = Book(title='Наука и техника', id_publisher='1')
book2 = Book(title='Роботы и женщины', id_publisher='1')
book3 = Book(title='Sun & planets', id_publisher='2')
book4 = Book(title='Letters in future', id_publisher='2')
book5 = Book(title='Hello from space', id_publisher='3')

session.add([book1, book2, book3, book4, book5])
session.commit()

shop1 = Shop(name='кНигга')
shop2 = Shop(name='AllIn')
shop3 = Shop(name='Бумага и деньги')

session.add([shop1, shop2, shop3])
session.commit()

stock1 = Stock(id_shop='1', id_book='1', count='53')
stock2 = Stock(id_shop='1', id_book='2', count='13')
stock3 = Stock(id_shop='1', id_book='3', count='3')
stock4 = Stock(id_shop='1', id_book='4', count='43')
stock5 = Stock(id_shop='1', id_book='5', count='31')
stock6 = Stock(id_shop='2', id_book='2', count='123')
stock7 = Stock(id_shop='2', id_book='5', count='13')
stock8 = Stock(id_shop='3', id_book='4', count='33')

session.add([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8])
session.commit()

sale1 = Sale(id_stock='1', count='14', price='123.21', date_sale='2019-01-08')
sale2 = Sale(id_stock='1', count='34', price='5323.23', date_sale='2021-06-18')
sale3 = Sale(id_stock='1', count='44', price='11123.26', date_sale='2022-02-28')
sale4 = Sale(id_stock='2', count='14', price='11623.29', date_sale='2012-03-18')
sale5 = Sale(id_stock='3', count='14', price='723.22', date_sale='2021-09-02')
sale6 = Sale(id_stock='4', count='46', price='11123.43', date_sale='2020-08-09')
sale7 = Sale(id_stock='5', count='34', price='6523.43', date_sale='2021-04-30')
sale8 = Sale(id_stock='7', count='14', price='1723.33', date_sale='2020-01-07')
sale9 = Sale(id_stock='8', count='34', price='90023.73', date_sale='2019-12-28')
sale10 = Sale(id_stock='7', count='84', price='100123.03', date_sale='2018-03-18')

session.add([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10])
session.commit()


db.close()
