from app import app, db
from flask import render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import os
from models import Tag, Post, Slider
from flask_security import login_required
from forms import *

@app.route('/')
def index():
    
    category = Tag.query.all()
    slides = Slider.query.all()


    return render_template('index.html', category=category, slides=slides)


@app.route('/create', methods=['POST', 'GET'])
@login_required

def create_post():

    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = photos.save(request.files['image'])
        try:
            post = Post(title=title, body=body, image=image)
            db.session.add(post)
            db.session.commit()
        except:
            print('база не смогла')
        return redirect(url_for('index'))
    form = PostForm()

    return render_template('create.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
