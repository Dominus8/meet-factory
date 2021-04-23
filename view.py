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

    for s in slides:
        img = Image.open("static/image/"+s.image)

        if img.size[0] != '1100':
            image = img.resize((1200, 601), Image.ANTIALIAS)
            image.save(r"static/image/slider/"+s.image)

    for t in category:
        img = Image.open("static/image/"+t.image)

        if img.size[0] != '285':
            image = img.resize((286, 286), Image.ANTIALIAS)
            image.save(r"static/image/tagimage/"+t.image)

    return render_template('index.html', category=category, slides=slides)

@app.route('/adm', methods=['POST', 'GET'])
@login_required
def adm(*args, **kwargs):
    posts=Post.query.all()
    tags=Tag.query.all()
    slides=Slider.query.all()
    d=list(dict(request.args).values())

    if d==['Создать товар']:
        return redirect(url_for('create_post'))


    if d==['Создать категорию']:
        return redirect(url_for('create_tag'))


    if d==['Создать слайд']:
        return redirect(url_for('create_slide'))

    return render_template('adm.html', posts=posts, tags=tags, slides=slides)


@app.route('/adm/createpost', methods=['POST', 'GET'])
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
        return redirect(url_for('adm'))
    form = PostForm()

    return render_template('create.html', form=form)


@app.route('/adm/createslide', methods=['POST', 'GET'])
@login_required

def create_slide():
    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = photos.save(request.files['image'])
        try:
            slide = Slider(title=title, body=body, image=image)
            db.session.add(slide)
            db.session.commit()
        except:
            print('база не смогла')
        return redirect(url_for('adm'))
    form = SliderForm()

    return render_template('createSlide.html', form=form)


@app.route('/adm/creattag', methods=['POST', 'GET'])
@login_required

def create_tag():
    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = photos.save(request.files['image'])
        try:
            tag = Tag(name=title, subtitle=body, image=image)
            db.session.add(tag)
            db.session.commit()
        except:
            print('база не смогла')
        return redirect(url_for('adm'))
    form = TagForm()

    return render_template('createTag.html', form=form)


@app.route('/where')
def where():
    return render_template('where.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404