import os

from flask import Flask, request, render_template, send_from_directory, redirect

app = Flask(__name__)

# For starting use
# cd robomix
# py -3 robomix.py
#


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/')
def index():
    return "<h1 style='color:blue'>Hello world from Robomix 2!</h1>"


@app.route('/search4',  methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results: '
    return render_template('results.html', the_title=title, the_letters=letters, the_phrase=phrase, the_results=results,)


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the Web!')


@app.route('/some_address')
def redirect_example() -> '301':
    """It is an example for a redirect"""
    return redirect('/', code=301)


@app.errorhandler(404)
def page_not_found(e) -> '404':
    return render_template('error_page.html', the_title='Page Not Found', the_message=e), 404


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
