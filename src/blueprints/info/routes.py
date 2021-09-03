from flask_jwt_extended import jwt_required
from flask import jsonify

from . import info_bp


recent_projects = {
    'project1': {
        'title': 'TS&A',
        'description': 'Web app that consume some Azure Cognitive Services as the API in order to provide an translator, that is capable to convert text to speech and run apect-based analysis.',
        'tools': [
            'Flask for back-end',
            'Azure Cognitive Services',
            'JQuery/Ajax',
            'HTML5/CSS3'
        ],
        'image': 'image1'
    },
    'project2': {
        'title': 'TS&A',
        'description': 'Web app that consume some Azure Cognitive Services as the API in order to provide an translator, that is capable to convert text to speech and run apect-based analysis.',
        'tools': [
            'Flask for back-end',
            'Azure Cognitive Services',
            'JQuery/Ajax',
            'HTML5/CSS3'
        ],
        'image': 'image1'
    }, 
    'project3': {
        'title': 'TS&A',
        'description': 'Web app that consume some Azure Cognitive Services as the API in order to provide an translator, that is capable to convert text to speech and run apect-based analysis.',
        'tools': [
            'Flask for back-end',
            'Azure Cognitive Services',
            'JQuery/Ajax',
            'HTML5/CSS3'
        ],
        'image': 'image1'
    }, 
    'project4': {
        'title': 'TS&A',
        'description': 'Web app that consume some Azure Cognitive Services as the API in order to provide an translator, that is capable to convert text to speech and run apect-based analysis.',
        'tools': [
            'Flask for back-end',
            'Azure Cognitive Services',
            'JQuery/Ajax',
            'HTML5/CSS3'
        ],
        'image': 'image1'
    }
}

awards = {
    'award1': {
        'title': 'Expo',
        'description': 'Awarded by MEP for classify and participate in the Costa Rica National Expo-Engineering in November 2018 and November 2019'        
    },
    'award2': {
        'title': 'Expo',
        'description': 'Awarded by MEP for classify and participate in the Costa Rica National Expo-Engineering in November 2018 and November 2019'        
    },
    'award3': {
        'title': 'Expo',
        'description': 'Awarded by MEP for classify and participate in the Costa Rica National Expo-Engineering in November 2018 and November 2019'        
    },
    'award4': {
        'title': 'Expo',
        'description': 'Awarded by MEP for classify and participate in the Costa Rica National Expo-Engineering in November 2018 and November 2019'        
    }
}

info = {
    'user1': {
        'description': 'I want to discover things that take me to new places.',
        'about_me': 'Hi there! I am Jafet Mora, a young Software Developer with a high interest in learn, build and share experiences. Generally I enjoy discovering technologies and new things from which I can learn, interact with, and of course have a good time creating code. You can know a little more about me by scrolling down, I hope you enjoy it. :)',
        'resume': 'resume.pdf',
        'phone': '+50671445897',
        'email': 'jafet.moraugalde15@gmail.com',
        'direction': 'Alajuela',
        'linkedin': 'linkedin-link',
        'github': 'github-link',
        'instagram': 'insta-link',
        'facebook': 'facebook-link',        
    }
}


@info_bp.route('/user-info/', methods=['GET'])
def user_info():
    return jsonify(
        response = info
    )
    
    
@info_bp.route('/user-projects/', methods=['GET'])
def user_projects():
    return jsonify(
        response = recent_projects
    )
    

@info_bp.route('/user-awards/', methods=['GET'])
def user_awards():
    return jsonify(
        response = awards
    )