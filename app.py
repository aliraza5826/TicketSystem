from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock ticket data
tickets = {
    12345: {'subject': 'Issue with login', 'status': 'Open', 'description': 'User is unable to login with their credentials.'},
    67890: {'subject': 'Payment error', 'status': 'Closed', 'description': 'Payment gateway is not responding.'}
}

@app.route('/')
def home():
    return render_template('home.html', tickets=tickets)

@app.route('/ticket/<int:ticket_id>')
def view_ticket(ticket_id):
    ticket = tickets.get(ticket_id)
    if not ticket:
        return redirect(url_for('home'))
    return render_template('view_ticket.html', ticket=ticket, ticket_id=ticket_id)

@app.route('/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        ticket_id = max(tickets.keys(), default=0) + 1
        subject = request.form['subject']
        description = request.form['description']
        tickets[ticket_id] = {'subject': subject, 'status': 'Open', 'description': description}
        return redirect(url_for('home'))
    return render_template('create_ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
