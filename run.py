import flask_cors
from classifyLyric import app
from flask_cors import CORS
CORS(app=app)
app.run(host="0.0.0.0", port=8081, debug=True)