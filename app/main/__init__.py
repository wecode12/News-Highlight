# # from flask import Flask

# # # Initializing application
# # app = Flask(__name__)

# # from app import views
# from flask import Blueprint
# main = Blueprint('main',__name__)
# from . import views,errors
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors

