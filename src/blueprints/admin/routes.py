from flask_jwt_extended import jwt_required
from flask import jsonify, request

from . import admin_bp
    
    
# @admin_bp.route('/add-project/', methods=['POST'])
# @jwt_required()
# def add_project():
    
#     project_info = request.json
#     #Update the DB
    
#     return jsonify(
#         response = 'The project info is the following:\n'
#         + 'Title: ' + project_info['title'] + '\n' 
#         + 'Description: ' + project_info['description'] + '\n' 
#         + 'Image_path: ' + project_info['image'] + '\n' 
#         + 'Tools: ' + ' '.join(project_info['tools']) + '\n' 
#     )
    

