from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import abspath
from os import getcwd

db_name = 'ClubDeLectura.db'
app = Flask(__name__)
uri = 'sqlite:///{}/{}'.format(abspath(getcwd()), db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "gydasjhfuisuqtyy234897dshfbhsdfg83wt7"
db = SQLAlchemy(app)
