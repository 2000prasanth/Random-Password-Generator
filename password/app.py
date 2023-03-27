from flask import Flask, render_template, request
import random
import string


port1=int(input("Enter a port value between 5000 and 9000 : "))
#Running the program multiple times on the same port seems to give error
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    special = int(request.form['special'])
    numbers = int(request.form['numbers'])

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Create a pool of characters based on user input
    pool = ''
    if special > 0:
        pool += symbols
    if numbers > 0:
        pool += digits
    remaining = length - special - numbers
    if remaining > 0:
        pool += lower + upper

    # Generate the password
    password = ''.join(random.choices(pool, k=length))

    return render_template('generate.html', password=password)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=port1)
