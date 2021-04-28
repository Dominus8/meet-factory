from flask import Blueprint, redirect, url_for, render_template, request
from models import *
from app import db, app
from flask_security import login_required
from PIL import Image

lending = Blueprint('lending', __name__, template_folder='templates')

@lending.route('/', methods=['POST', 'GET'])
def index():

    slides = Slider.query.all()

# обработка изображений в слайдере на главной странице
    for s in slides:
        img = Image.open("static/image/"+s.image)

        if img.size[0] != '1100':
            image = img.resize((1200, 501), Image.ANTIALIAS)
            image.save(r"static/image/slider/"+s.image)


        tag = Tag.query.filter(Tag.slug == 'Ливерные-колбасы-и-паштеты').first_or_404()
        liverwoods = tag.posts

        tag = Tag.query.filter(Tag.slug == 'Полукопченые-колбасы').first_or_404()
        semismoked = tag.posts

        tag = Tag.query.filter(Tag.slug == 'Колбасы-варёно-копчёные').first_or_404()
        boiledsmoked = tag.posts

        tag = Tag.query.filter(Tag.slug == 'Колбасы-варёные').first_or_404()
        boiled  = tag.posts

        tag = Tag.query.filter(Tag.slug == 'Сосиски-и-Сардельки').first_or_404()
        sausages = tag.posts

    return render_template('lending/index.html', liverwoods=liverwoods, semismoked=semismoked, boiledsmoked=boiledsmoked, boiled=boiled, sausages=sausages, slides=slides)