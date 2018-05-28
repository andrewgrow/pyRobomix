from flask import Flask, request

app = Flask(__name__)

# For starting use
# py -3 robomix.py
#

@app.route('/')
def hello():
    return "<h1 style='color:blue'>Hello There 4!</h1>"


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
