from flask import Flask, render_template, request, redirect, url_for
from leaderpath_logic import LeaderPathWizard

app = Flask(__name__)
wizard = LeaderPathWizard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wizard', methods=['GET', 'POST'])
def wizard_step():
    if request.method == 'POST':
        user_data = request.form.get('user_input')
        wizard.process_input(user_data)
        
    if not wizard.current:
        return redirect(url_for('summary'))
        
    # Passing 'wizard=wizard' allows the sidebar to show live data
    return render_template('wizard.html', node=wizard.current, wizard=wizard)

@app.route('/summary')
def summary():
    return render_template('summary.html', wizard=wizard)

if __name__ == "__main__":
    app.run(debug=True)