from wtforms import Form, StringField, TextAreaField, FileField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    photos = FileField('photos')
