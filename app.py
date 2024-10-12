from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for the query page
@app.route('/query')
def query():
    return render_template('query.html')

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route to handle form submission and redirect to result page
@app.route('/submit_query', methods=['POST'])
def submit_query():
    # Get the 'query' parameter from the form data
    query = request.form.get('query')
    # Redirect to the result page and pass the query
    return redirect(url_for('result', query=query))

# Route to display the result
@app.route('/result')
def result():
    # Get the query from the URL parameters
    query = request.args.get('query')
    return render_template('result.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)













