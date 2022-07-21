from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer
from werkzeug.security import generate_password_hash

db_path = "sqlite:///ts.db"

# Instantiate the database
db = SQLAlchemy()

def setup_db(app):
    # A function to connect the db to flask
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

# Inititalize the database
def create_db():
    db.drop_all()
    db.create_all()

    mike = (User(
        email = 'jack@example.com',
        username = 'jack',
        password = generate_password_hash('123456789', 'pbkdf2:sha256'),
        age = 12
    ))

    mike.add()

    toy1 = Toy(name='Super Mario Bros', price=0.005, version='2010 model', image_link="https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
    toy2 = Toy(name='Lego', price=2.05, version='City theme', image_link="https://images.unsplash.com/photo-1587654780291-39c9404d746b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
    toy3 = Toy(name='Bunny', price=6.005, version='fur', image_link="https://images.unsplash.com/photo-1556012018-50c5c0da73bf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTJ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60")
    toy4 = Toy(name='Chuchu train', price=0.875, version='plastic', image_link="https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
    toy5 = Toy(name='Moschino', price=0.5255, version='moschino1.1', image_link="https://images.unsplash.com/photo-1530325553241-4f6e7690cf36?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8N3x8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=60")
    toy6 = Toy(name='Mamushka', price=0.5255, version='polypropylene', image_link="https://images.unsplash.com/photo-1613981948475-6e2407d8b589?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWF0cnlvc2hrYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60")


    toy6.add()
    toy5.add()
    toy2.add()
    toy4.add()
    toy5.add()
    toy6.add()

# User Model
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key = True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    age = Column(Integer)

    # Adds a new user to the database
    def add(self):
        db.session.add(self)
        db.session.commit()

    # Deletes a user from the database
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'age': self.age
        }

    def __repr__(self) -> str:
        return f"<id: {self.id} email: {self.email}>"


class Toy(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    price = Column(Integer)
    version = Column(String(10))
    image_link = Column(String)
    # category_id = Column(Integer, db.ForeignKey("category.id"), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

# class Category(db.Model):
#     id = Column(Integer, primary_key=True)
#     type = Column(String(20))
#     toys = db.relationship('Toy', backref='category')

