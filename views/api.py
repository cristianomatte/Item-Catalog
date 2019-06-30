from flask import Blueprint, jsonify
from repository.sqlite import db_session
from model.category import Category
from model.item import Item


api = Blueprint('api', __name__)


@api.route('/v1/categories')
def get_categories():
    """Return a JSON with all categories and its items"""
    categories_payload = []

    for category in db_session.query(Category).all():
        # Get all items for the current category
        items_payload = [i.serialize for i in db_session.query(Item).
                         filter_by(category_id=category.id).all()]

        # Serialize the category and its items
        category_payload = category.serialize
        category_payload['Item'] = items_payload

        categories_payload.append(category_payload)

    return jsonify(Category=categories_payload)
