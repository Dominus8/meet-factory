from wtforms import Form, StringField, TextAreaField, FileField


class PostForm(Form):
    title = StringField('Название товара')
    body = TextAreaField('Информация о товаре')
    image = FileField('Изображение товара')

class TagForm(Form):
    title = StringField('Заголовок категории')
    body = TextAreaField('Описание категории')
    image = FileField('Изображение')

class SliderForm(Form):
    title = StringField('Заголовок слайда')
    body = TextAreaField('Текст на слайде')
    image = FileField('Изображение на слайде')