from flask_frozen import Freezer
from app import app

# app = Flask(__name__)
freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    yield 'index', {}
    
if __name__ == '__main__':
    # dev
    # app.run(debug=True)
    freezer.freeze()
