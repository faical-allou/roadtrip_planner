from flask import Flask, abort, flash, redirect, render_template, request, url_for, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route("/")
def hello():
    return render_template('./homepage.html', name = "Hello")

@app.route("/homepage.html")
def homepage_html():
    return render_template('./homepage.html', name = "Hello")

@app.route('/<path:filename>', methods=['GET'])
def display_static(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 80.
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('ON_HEROKU'):
        app.run(host='0.0.0.0', port=port)
    else :
        app.run(host='localhost', port=port)