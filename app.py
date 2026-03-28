from flask import Flask, render_template

app = Flask(__name__)


# 2
@app.route('/age')
def age_page():
    age = 18
    return render_template('age.html', age=age)


if __name__ == '__main__':
    app.run(debug=True)
