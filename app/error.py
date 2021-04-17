from flask import render_template
from app import app

@app.errorhandler(404)
def four_oh_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('four_oh_four.html'), 404