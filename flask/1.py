from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html' , title = 'the home page')

@app.route('/about')
def about():
    return render_template('about.html', title = 'the about page')

if(__name__ == '__main__'):
    app.run(debug=True , port=3000 )