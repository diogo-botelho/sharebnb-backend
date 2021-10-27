from typing import Optional
from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField
from wtforms.validators import regexp

class FileForm(FlaskForm):
    """Form for adding file."""
    image = FileField(u'Image File')
    description = TextAreaField(u'Image Description')