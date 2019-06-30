from flask import Blueprint, render_template, make_response, redirect, url_for
from flask import session, request
from repository.sqlite import db_session
from repository.database import Database
from model.user import User
import random
import string
import json
import requests


auth = Blueprint('auth', __name__)
db = Database(db_session)

with open('client_secrets.json', 'r') as file:
    # Read facebook app id and secret from configuration file
    data = file.read()
    dictionary = json.loads(data)
    google_client_id = dictionary['google']['client_id']


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    """Logs an user in"""
    if request.method == 'POST':
        if not state_is_valid():
            response = make_response(json.dumps('Invalid state parameter.'),
                                     401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Get google access token from request and perform login
        access_token = request.data.decode('utf-8')
        if not access_token:
            # If no access token was provided, returns an error
            response = make_response(
                json.dumps('Access token not provided.'), 400)
            response.headers['Content-Type'] = 'application/json'
            return response

        return login_with_google(access_token)
    else:
        if 'user_id' in session:
            # If the user is already logged in, redirect to catalog
            return redirect(url_for('web.show_catalog_latest_items'))

        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in range(32))
        session['state'] = state
        return render_template('login.html', state=state)


@auth.route('/logout/')
def logout():
    """Logs out the user"""
    # Logout the user on google
    access_token = session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token={}' \
        .format(access_token)
    requests.get(url)

    # Remove all user information from session
    del session['user_id']
    del session['access_token']

    return redirect(url_for('web.show_catalog_latest_items'))


def state_is_valid():
    """Verifies if the request state is the same as the session one"""
    return request.args.get('state') == session['state']


def login_with_google(access_token):
    """Retrieve user information from Google to login"""
    # Get info about the access token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}') \
        .format(access_token)
    try:
        r = requests.get(url)
    except requests.RequestException:
        response = make_response(json.dumps('Error connecting to Google.'),
                                 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    body = r.content.decode('utf8')
    token_info = json.loads(body)

    # Verify that the access token was issued to this client
    if token_info['issued_to'] != google_client_id:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Get user info
    url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    params = {'access_token': access_token, 'alt': 'json'}
    try:
        r = requests.get(url, params=params)
    except requests.RequestException:
        response = make_response(json.dumps('Error connecting to Google.'),
                                 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    body = r.content.decode('utf8')
    user_info = json.loads(body)
    email = user_info['email']
    name = user_info['name']

    # Verify that required info was provided by Google
    if not email or not name:
        response = make_response(
            json.dumps('Incomplete user info from Google.'), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify if the user already exists and create a new one if not
    user = db.get_user_with_email(email)
    if not user:
        user = db.create_user(email, name)

    # Add user information to session
    session['user_id'] = user.id
    session['access_token'] = access_token

    return make_response('', 200)
