from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Product
from .forms import UpdateProfile
from .. import db, photos

@main.route('/')
def index():
    products = Product.query.all()

    return render_template("index.html", products=products)


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