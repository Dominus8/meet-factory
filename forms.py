from wtforms import Form, StringField, TextAreaField, FileField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    image = FileField('Image')

class TagForm(Form):
    title = StringField('Заголовок категории')
    body = TextAreaField('Body')
    image = FileField('Image')

class SliderForm(Form):
    title = StringField('Заголовок слайда')
    body = TextAreaField('Body')
    image = FileField('Image')