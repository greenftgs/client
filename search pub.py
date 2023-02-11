from connect import db
from models import Publisher, Book, Shop, Stock

for c in db.query(Publisher).all():
    print(c)


def get_shops(publisher):
    if search_pub.isdigit():
        publisher = db.query(Shop).\
            join(Stock, Stock.id_stock == Shop.id_shop).\
            join(Book, Book.id_book == Stock.id_book).\
            join(Publisher, Publisher.id_publisher == Book.id_publisher).\
            filter(Publisher.id_publisher == int(search_pub)).all()
    else:
        publisher = db.query(Shop). \
            join(Stock, Stock.id_stock == Shop.id_shop). \
            join(Book, Book.id_book == Stock.id_book). \
            join(Publisher, Publisher.id_publisher == Book.id_publisher). \
            filter(Publisher.name == search_pub)
    return publisher


if __name__ == '__main__':
    search_pub = input('Введите имя или id издателя для поиска книг в магазине: ').lower()
    print(get_shops(publisher))

db.close()
