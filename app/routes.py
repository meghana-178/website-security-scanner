# Placeholder for app/routes.py
from flask import Blueprint, render_template, request
from .utils import scan_website

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        result = scan_website(url)
    return render_template('index.html', result=result)
