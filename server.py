import os
from flask import Flask


PORT = int(os.environ['PORT'])
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello Dockerfile'

app.run(debug=True, host='0.0.0.0', port=PORT)
