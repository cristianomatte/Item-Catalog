# Catalog App

A CRUD catalog site of sports' items.

## Requirements

For running this project, you will need the [Vagrant virtual machine](https://github.com/udacity/fullstack-nanodegree-vm) provided by Udacity. Follow the instructions on the link to run your virtual machine.

This project is written in Python 3.

## Running

Copy all the files of the project to the `/vagrant/catalog/` directory of the virtual machine repository. Start and connect to the virtual machine with the following commands:

```bash
vagrant up
vagrant ssh
```

From the virtual machine, go to the catalog directory.

```bash
cd /vagrant/catalog
```

Then, install the dependencies required by the project.

```bash
sudo pip3 install -r requirements.txt
```

Create and populate the database.

```bash
python3 lots_of_items.py
```

Finally, run the project.

```bash
python3 application.py
```

The Catalog App is available at the URL http://localhost:8000.

## Endpoints

### Web endpoints
- `/login` - log in the user
- `/logout` - log out the user
- `/categories` - show a list with the most recent items
- `/categories/<int:category_id>/items/` - show the items of a category
- `/categories/<int:category_id>/items/<int:item_id>` - show an item information
- `/categories/items/new` - create a new item
- `/categories/<int:category_id>/items/new` - create a new item with a predefined category
- `/categories/<int:category_id>/items/<int:item_id>/edit` - edit an item
- `/categories/<int:category_id>/items/<int:item_id>/delete` - delete an item

### API endpoint
- `/v1/categories/` - returns a json with all categories and its items