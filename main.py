# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books "
# #                "(id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)")
#
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

####################################################################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# db.create_all()

# new_book = Books(title="Harry Potter", author="JK Rowling", rating=9.3)
#
# db.session.add(new_book)
# db.session.commit()

## READ All Records
all_books = db.session.query(Books).all()
print(all_books)

## Read A Particular Record By Query
book = Books.query.filter_by(title="Harry Potter").first()
print(book)

## Update A Particular Record By Query
book_to_update = Books.query.filter_by(title="Harry Potter and the Chamber of Secrets").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
book_to_update.rating = 9.3
db.session.commit()


## Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Books.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

## Delete A Particular Record By PRIMARY KEY
## You can also delete by querying for a particular value e.g. by title or one of the other properties.
book_id = 1
book_to_delete = Books.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
