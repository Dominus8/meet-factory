from flask import Blueprint, redirect, url_for, render_template, request
from models import *
from .forms import PostForm
from app import db, app
from flask_security import login_required
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image

posts = Blueprint('posts', __name__, template_folder='templates')

# Загрузка файлов

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


# создание поста

@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
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
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index(*args, **kwargs):
    q = request.args.get('q')
    page = request.args.get('page')
    s = request.args.get('slug')
    tags = Tag.query.all()


    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))  # .all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    if s:
        tag = Tag.query.filter(Tag.slug == s).first_or_404()
        posts = tag.posts

    pages = posts.paginate(page=page, per_page=10)


    return render_template('posts/index.html', posts=posts, pages=pages, tags=tags,)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    img = Image.open("static/image/"+post.image)
    if img.size[0] != '450':
        image = img.resize((450, 450), Image.ANTIALIAS)
    image = image.save("static/image/"+post.image)
    return render_template('posts/post_detail.html', post=post, tags=tags, image=image)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)

