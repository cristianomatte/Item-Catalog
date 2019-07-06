from sqlalchemy import create_engine, desc
from model.category import Category
from model.item import Item
from model.user import User


class Database:
    """Database performs commands and queries on a SQL database"""

    def __init__(self, db_session):
        self.db_session = db_session()

    def get_user_with_email(self, email):
        try:
            return self.db_session.query(User).filter_by(email=email).one()
        except:
            return None

    def create_user(self, email, name):
        try:
            user = User(name=name, email=email)
            self.db_session.add(user)
            self.db_session.commit()

            user = self.db_session.query(User).filter_by(email=email).one()
            return user
        except:
            return None

    def get_latest_items(self):
        return self.db_session.query(Item).order_by(desc(Item.last_update)) \
            .limit(10).all()

    def get_all_categories(self):
        try:
            return self.db_session.query(Category).all()
        except:
            return None

    def get_category_by_id(self, category_id):
        try:
            return self.db_session.query(Category).filter_by(id=category_id) \
                .one()
        except:
            return None

    def get_category_items(self, category):
        try:
            return self.db_session.query(Item) \
                .filter_by(category_id=category.id).all()
        except:
            return None

    def get_item_from_category(self, category, item_id):
        try:
            return self.db_session.query(Item). \
                filter_by(category_id=category.id, id=item_id).one()
        except:
            return None

    def get_item_by_id(self, item_id):
        try:
            return self.db_session.query(Item).filter_by(id=item_id).one()
        except:
            return None

    def create_item(self, name, description, category_id, owner_id):
        item = Item(
            name=name,
            description=description,
            category_id=category_id,
            owner_id=owner_id)
        self.db_session.add(item)
        self.db_session.commit()

    def update_item(self, item):
        self.db_session.add(item)
        self.db_session.commit()

    def delete_item(self, item_id):
        item = self.db_session.query(Item).filter_by(id=item_id).one()
        self.db_session.delete(item)
        self.db_session.commit()
