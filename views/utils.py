from functools import wraps
from flask import session, redirect, url_for, flash
from repository.sqlite import db_session
from repository.database import Database


db = Database(db_session)


def login_required(f):
    """Verifiy if there is a logged user and redirect to login page if not"""
    @wraps(f)
    def wrapper(*args, **kwds):
        if "user_id" not in session:
            flash('Please login to create, edit and remove items.')
            return redirect(url_for('auth.login'))
        return f(*args, **kwds)
    return wrapper


def ownership_required(f):
    """Verify if the current logged user is the owner of the selected item"""
    @wraps(f)
    def wrapper(*args, **kwds):
        item_id = kwds["item_id"]
        item = db.get_item_by_id(item_id)

        if item.owner_id != session['user_id']:
            flash('You can only modify items created by you.')
            return redirect(url_for('web.show_item',
                                    category_id=item.category_id,
                                    item_id=item_id))

        return f(*args, **kwds)
    return wrapper
