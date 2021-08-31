from flask_jwt_extended import jwt_required
from src import app

from . import admin_bp

@admin_bp.route('/admin/', methods=['GET'])
# @jwt_required
def admin():
    jsonify(message="Welcome! to the Data Science Learner")
    # return 'This is the Admin Blueprint'