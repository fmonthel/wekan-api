from wekan_api import app
from wekan_api import db

import util.response


@app.route('/lists', methods=['GET'])
def lists():
    """
    Retrieve all lists.
    """
    try:
        lists = list(db.lists.find())
        return util.response.success({
            'lists': lists,
        })
    except:
        return util.response.undefined_error()


@app.route('/list/<list_id>', methods=['GET'])
def list_details(list_id):
    """
    Retrieve details for a single list by ID.
    """
    try:
        list = db.lists.find_one({'_id': list_id})
        return util.response.success({
            'list': list,
        })
    except:
        return util.response.undefined_error()


@app.route('/list/<list_id>/cards', methods=['GET'])
def list_cards(list_id):
    """
    Retrieve all cards associated with a list.
    """
    try:
        cards = list(db.cards.find({'listId': list_id}))
        return util.response.success({
            'cards': cards,
        })
    except:
        return util.response.undefined_error()
