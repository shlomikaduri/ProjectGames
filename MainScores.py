'''
This function is run server that read text file Scores.txt, the server is running and listen read the file content each web refresh.
in order to open the page, all you need is to open the web browser and go to http://127.0.0.1:5000/ after running the program
'''
from flask import Flask, render_template
import Utils

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        score = open("Scores.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)