from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter()
def allcaps(string):
    return string.upper()

@app.template_filter()
def reverse(whatever):
    try:
        whatever = eval(whatever)
    except NameError as e:
        print("Assuming string!")
    return whatever[::-1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cap/<string>')
def cap(string = None):
    return render_template('index.html', string = string)

@app.route('/rev/<string>')
def rev(string = None):
    return render_template('index.html', rev = string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)