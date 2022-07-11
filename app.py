from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html', pagetitle='Flask server home page')
@app.route('/priya')
def priya():
	return render_template('priya.html', pagetitle='About Priya')
if __name__ == '__main__':
	app.run(debug=True)
