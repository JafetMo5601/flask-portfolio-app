from flask_jwt_extended import jwt_required
from flask import jsonify

from . import admin_bp


@admin_bp.route('/admin/', methods=['GET'])
@jwt_required()
def admin():
    return jsonify(
        message='This is the Admin Blueprint'
    )
