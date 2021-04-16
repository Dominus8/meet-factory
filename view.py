from app import app
from flask import render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import os
from models import Tag, Post


@app.route('/')
def index():
    files = os.listdir(path="D:\git_source\meet-factory\static\image\slider")
    category = Tag.query.all()


    for f in files:
        img = Image.open("static/image/slider/"+f)
        if img.size[0] != '1200':
            image = img.resize((1200, 600), Image.ANTIALIAS)
        image = image.save("static/image/slider/"+f)



#         print(img.size)
    return render_template('index.html', files=files, category=category)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
