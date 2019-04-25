import os
import json

from entries.RobomixContent import ContentPage
from entries.Day import *

from flask import Flask, request, render_template, send_from_directory, redirect, abort, Response

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 720

# For starting use
# cd robomix
# win: py -3 robomix.py
# macOs: python3 robomix.py


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
    title = 'Android developer, Software Engineer, 18+ yrs experience'
    return render_template('index.html', the_title=title)


@app.route('/ajax_content')
def suggestions():
    href = request.args.get('jsdata').split("#")[1]

    about = ContentPage('About', 'about.html')
    portfolio = ContentPage('Portfolio', 'content.html')
    # contacts = ContentPage('Contacts', 'content.html')

    unit_case = {
        'about': about,
        'portfolio': portfolio
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


@app.route('/sitemap.xml')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/schedule', methods=['GET'])
def get_object() -> str:

    monday_list = ['mathematics', 'history', 'physics']
    tuesday_list = ['history', 'mathematics', 'english']
    wednesday_list = ['physics', 'physical health']
    thursday_list = ['information technologies', 'computer science']
    friday_list = ['mathematics', 'information technologies']

    day_monday = Day('monday', monday_list)
    day_tuesday = Day('tuesday', tuesday_list)
    day_wednesday = Day('wednesday', wednesday_list)
    day_thursday = Day('thursday', thursday_list)
    day_friday = Day('friday', friday_list)

    all_days = {'monday':day_monday, 'tuesday':day_tuesday, 'wednesday':day_wednesday, 'thursday':day_thursday, 'friday':day_friday}

    monday_json = day_monday.get_json()
    tuesday_json = day_tuesday.get_json()
    wednesday_json = day_wednesday.get_json()
    thursday_json = day_thursday.get_json()
    friday_json = day_friday.get_json()

    all = [monday_json, tuesday_json, wednesday_json, thursday_json, friday_json]

    arguments = request.args
    arguments_day = arguments.get('day', 'empty', str)
    print('arg_day = ', arguments_day)

    result = make_json_from_list(all)

    # return all days if request does not have value 'day'
    if arguments_day == 'empty':
        return result

    # return day if request has value 'day'
    if all_days.__contains__(arguments_day):
        day = all_days.get(arguments_day)
        result = make_json_from_list([day.get_json()])
    else:
        # return error if we don have such day in list
        abort(Response('wrong argument "day". Expected one of each: "monday, tuesday, wednesday, thursday, friday" but '
                       'actual is ' + arguments_day, 400))

    return result


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
