import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from connect import db

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'Издательство: {self.name}, номер: {self.id_publisher}'


class Book(Base):
    __tablename__ = "book"

    id_book = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    title = sq.Column(sq.String(length=140), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id_publisher"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Книга: {self.title}, номер: {self.id_book}'


class Shop(Base):
    __tablename__ = "shop"

    id_shop = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
        return f'Магазин: {self.name}, номер: {self.id_book}'


class Stock(Base):
    __tablename__ = "stock"

    id_stock = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id_shop"), nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'Наличие: номер книги - {self.id_book}, магазин - {self.id_shop}, количество - {self.count}'


class Sale(Base):
    __tablename__ = "sale"

    id_sale = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id_stock"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Продано: номер продажи - {self.id_sale}, номер на складе - {self.id_stock}, ' \
               f'количество - {self.count}, дата продажи - {self.date_sale}, стоимость - {self.price}'


def create_tables(engine):
    Base.metadata.create_all(engine)


create_tables(engine)

db.close()
