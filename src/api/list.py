from wekan_api import app
from wekan_api import db

import util.response


@app.route('/lists', methods=['GET'])
def lists():
    """
    Retrieve all lists.
    """
    try:
        all_lists = list(db.lists.find())
        return util.response.success({
            'lists': all_lists,
        })
    except:
        return util.response.undefined_error()


@app.route('/list/<list_id>', methods=['GET'])
def list_details(list_id):
    """
    Retrieve details for a single list by ID.
    """
    try:
        details = db.lists.find_one({'_id': list_id})

        if not details:
            return util.response.error(
                status_code=404,
                message='The specified list ID does not exist.',
                failure='failure_nonexistent_list',
            )

        return util.response.success({
            'list': details,
        })
    except:
        return util.response.undefined_error()


@app.route('/list/<list_id>/cards', methods=['GET'])
def list_cards(list_id):
    """
    Retrieve all cards associated with a list.
    """
    try:
        if not db.lists.find_one({'_id': list_id}):
            return util.response.error(
                status_code=404,
                message='The specified list ID does not exist.',
                failure='failure_nonexistent_list',
            )

        cards = list(db.cards.find({'listId': list_id}))
        return util.response.success({
            'cards': cards,
        })
    except:
        return util.response.undefined_error()
