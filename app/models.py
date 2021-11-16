from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(UserMixin,db.Model):
  __tablename__="users"
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255),unique = True,nullable = False)
  email  = db.Column(db.String(255),unique = True,nullable = False)
  secure_password = db.Column(db.String(255),nullable = False)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  products = db.relationship('Product', backref='user', lazy='dynamic')

  @property
  def set_password(self):
    raise AttributeError('You cannot read the password attribute')

  @set_password.setter
  def password(self, password):
    self.secure_password = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.secure_password,password) 
  
  def save_u(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def __repr__(self):
    return f'User {self.username}'

class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(55),nullable = False)
  short_description = db.Column(db.Text(), nullable = False)
  long_description = db.Column(db.Text(), nullable = False)
  price = db.Column(db.DECIMAL(10, 2))
  color = db.Column(db.String(),nullable=False)
  stock = db.Column(db.Integer,nullable=False)
  brand = db.Column(db.String(10),nullable=False)
  model = db.Column(db.String(10),nullable=False)  
  category = db.Column(db.String(255), index = True,nullable= False)
  img_1_path= db.Column(db.String())
  img_2_path= db.Column(db.String())
  img_3_path= db.Column(db.String())
  img_4_path= db.Column(db.String())
  time = db.Column(db.DateTime, default = datetime.utcnow)
  
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
  def save_p(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f'Product {self.name}'




