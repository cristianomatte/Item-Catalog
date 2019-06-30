from flask import Blueprint, render_template, request, redirect, url_for
from flask import session, flash
from repository.sqlite import db_session
from repository.database import Database
from model.category import Category
from model.item import Item
from views.utils import login_required, ownership_required
import random
import string
import json


web = Blueprint('web', __name__)
db = Database(db_session)


@web.route('/')
@web.route('/categories/')
def show_catalog_latest_items():
    """Display a list with the most recent items"""
    categories = db.get_all_categories()
    items = db.get_latest_items()

    return render_template(
        'catalog.html',
        title='Latest Items',
        categories=categories,
        items=items)


@web.route('/categories/<int:category_id>/items/')
def show_category_items(category_id):
    """Display a list of items of a category"""
    categories = db.get_all_categories()
    category = db.get_category_by_id(category_id)
    items = db.get_category_items(category)

    return render_template(
        'catalog.html',
        title='{} ({} items)'.format(category.name, len(items)),
        categories=categories,
        items=items,
        category=category)


@web.route('/categories/<int:category_id>/items/<int:item_id>')
def show_item(category_id, item_id):
    """Display an item information"""
    category = db.get_category_by_id(category_id)
    item = db.get_item_from_category(category, item_id)

    return render_template('item.html', item=item)


@web.route('/categories/items/new', methods=['GET', 'POST'])
def create_item():
    """Creates a new item"""
    return create_item_for_category(None)


@login_required
@web.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
def create_item_for_category(category_id):
    """Creates a new item with a default category selected"""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        # Ensure that all fields where filled
        if not name or not description or not category_id:
            flash('Please fill all form fields.')
            url = url_for('web.create_item')
            return redirect(url)

        db.create_item(name, description, category_id, session['user_id'])

        if category_id:
            url = url_for('web.show_category_items', category_id=category_id)
        else:
            url = url_for('web.show_catalog_latest_items')

        flash('Item successfully added!')
        return redirect(url)
    else:
        category = db.get_category_by_id(category_id)
        categories = db.get_all_categories()
        return render_template(
            'new_item.html',
            categories=categories,
            default_category=category)


@web.route('/categories/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
@login_required
@ownership_required
def edit_item(category_id, item_id):
    """Edits an item"""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        # Ensure that all fields where filled
        if not name or not description or not category_id:
            flash('Please fill all form fields.')
            url = url_for(
                'web.edit_item',
                category_id=category_id,
                item_id=item_id)
            return redirect(url)

        # Get item from database and update its fields
        item = db.get_item_by_id(item_id)
        item.name = name
        item.description = description
        item.category = db.get_category_by_id(category_id)
        db.update_item(item)

        flash('Item successfully edited!')
        return redirect(url_for(
            'web.show_item',
            category_id=category_id,
            item_id=item_id))
    else:
        categories = db.get_all_categories()
        item = db.get_item_by_id(item_id)
        return render_template('edit_item.html',
                               item=item,
                               categories=categories)


@web.route('/categories/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
@login_required
@ownership_required
def delete_item(category_id, item_id):
    """Deletes an item"""
    if request.method == 'POST':
        db.delete_item(item_id)
        flash('Item successfully deleted!')
        return redirect(url_for('web.show_category_items',
                                category_id=category_id))
    else:
        return render_template('delete_item.html', item_id=item_id)
