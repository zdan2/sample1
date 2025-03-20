from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    # SelectField,  # 使われていないインポートを削除
    # RadioField,
    # DateField,
    # DateTimeField,
    # IntegerField,
    # DecimalField,
    # FloatField,
    # BooleanField,
    # HiddenField,
    # MultipleFileField,
    # FileField
)
from wtforms.validators import DataRequired, Email, Length, EqualTo  # 使われていないインポートを削除、EqualToは残す


class UserInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8, max=255),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password', validators=[  # DataRequiredとLengthは維持
        DataRequired(), Length(min=8, max=255)  # 閉じ括弧を追加
    ])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=255)])
    city = StringField('City', validators=[DataRequired(), Length(max=255)])
    state = StringField('State', validators=[DataRequired(), Length(max=255)])
    zip = StringField('Zip', validators=[DataRequired(), Length(max=10)])
    country = StringField('Country', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit')