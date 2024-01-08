from flask import Blueprint

from api.models.myModels import getString
from api.models.myModels import getString2



first_page_bp = Blueprint('first_page_bp', __name__)
first_page_bp.route('fisrt-page-route', methods=['GET'])(getString)

second_page_bp = Blueprint('second_page_bp', __name__)
second_page_bp.route('secind-page-route', methods=['GET'])(getString2)
