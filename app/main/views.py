from flask import render_template, redirect, url_for,abort,request, flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Product
from .forms import UpdateProfile,ProductForm
from .. import db, photos


@main.route('/', methods = ['GET','POST'])
def index():
    form = ProductForm()
    products = Product.query.all()
    if form.validate_on_submit():
        name=form.name.data
        short_description = form.short_description.data
        long_description = form.long_description.data
        price = form.price.data
        color = form.color.data
        stock = form.stock.data
        brand = form.brand.data
        model = form.model.data
        category = form.category.data
        product = Product(name=name,short_description=short_description,long_description=long_description,price=price,color=color,stock=stock,brand=brand,model=model,category=category,user_id = current_user._get_current_object().id)
        product.save_p()
        
        flash(f'Your Product {name} has been added successfully', 'success')
        return redirect(url_for('main.index'))

    return render_template("index.html", products=products,form=form)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    products = Product.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,products=products)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))