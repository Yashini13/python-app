from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        amount = float(request.form['amount'])
        expenses.append({'item': item, 'amount': amount})
    total = sum(e['amount'] for e in expenses)
    return render_template('index.html', expenses=expenses, total=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
