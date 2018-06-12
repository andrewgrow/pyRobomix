import os

from entries.RobomixContent import ContentPage

from flask import Flask, request, render_template, send_from_directory, redirect


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 720

# For starting use
# cd robomix
# py -3 robomix.py
#


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


# No cacheing at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/')
def index() -> 'html':
    title = 'Robomix: websites & mobile apps'
    return render_template('index.html', the_title=title)


@app.route('/ajax_content')
def suggestions():
    href = request.args.get('jsdata')

    about = ContentPage('About Us', 'about.html')
    portfolio = ContentPage('Portfolio', 'content.html')
    # contacts = ContentPage('Contacts', 'content.html')

    unit_case = {
        '#about': about,
        '#portfolio': portfolio
        # '#contacts': contacts
    }

    content = unit_case.get(href, about)

    return render_template(content.template, content_name=content.title)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results: '
    return render_template('results.html', the_title=title, the_letters=letters, the_phrase=phrase, the_results=results,)


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


@app.route('/entries')
def entry_page() -> 'html':
    return render_template('entries.html', the_title='Welcome to search4letters on the Web!')


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


@app.route('/sitemap.xml')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
