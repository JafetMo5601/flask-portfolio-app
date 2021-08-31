from . import info_bp

@info_bp.route('/info/', methods=['GET'])
def info():
    return 'This is the Info Blueprint'