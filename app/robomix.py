from flask import Flask, request, render_template

app = Flask(__name__)

# For starting use
# cd app
# py -3 robomix.py
#


@app.route('/')
def hello():
    return "<h1 style='color:blue'>Hello world from Robomix!</h1>"


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the Web!')


@app.route('/v1', methods=['POST'])
def api_request() -> str:
    # getting headers -> request.headers.get('your-header-name')
    #

    # request.headers['your-header-name']
    headers = request.headers

    # GET
    arguments = request.args

    # POST
    forms = request.form

    #
    # Getting a data or a file from the request
    #
    # https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
    #
    # request.form['name']
    print(request)
    print(headers)
    print(arguments)
    print(forms)
    return "Test response"


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
