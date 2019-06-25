from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''<!DOCTYPE html>

            <html>
                <head>
                    <style>
                        form {{
                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }}
                        textarea {{
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        }}
                    </style>
                </head>
                <body>
                    <form action="" method="POST">
                        <l>Rotate by:</l><input type="text" name="rot" value="0" required>
                        <textarea rows="4" cols="50" name="text" required>{0}</textarea>
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>'''

@app.route("/")
def index():
    return form.format()

@app.route("/", methods=['POST'])
def encrypt():
    #rot = request.args.get('rot')
    rot = request.form["rot"]
    #text = request.args.get('text')
    text = request.form['text']
    #print(rot)
    #print(rotate_string(text, rot))
    return form.format(rotate_string(text, int(rot)))

app.run()