import os.path
from flask import Flask, request, send_from_directory
from flask import render_template

application = Flask(__name__, static_url_path='')

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

@application.route("/")
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)
    #return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/zuoye/")
def assignment():
    return application.send_static_file('assignment/index.html')
    #content = get_file('assignment.html')
    #return Response(content, mimetype="text/html")
    #return "<h1 style='color:blue'>Zuo Ye!</h1>"

@application.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='assignment', filename=filename)

@application.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return application.send_static_file(path)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
