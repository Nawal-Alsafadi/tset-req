
from api.routes.myBluePrint import first_page_bp
from api.routes.myBluePrint import second_page_bp

def app_routes(app):
        app.register_blueprint(first_page_bp, url_prefix='/api')
        app.register_blueprint(second_page_bp, url_prefix='/api')

