from wekan_api import app
from wekan_api import db

import util.response


@app.route('/cards', methods=['GET'])
def cards():
    """
    Retrieve all cards.
    """
    try:
        all_cards = list(db.cards.find())
        return util.response.success({
            'cards': all_cards,
        })
    except:
        return util.response.undefined_error()


@app.route('/card/<card_id>', methods=['GET'])
def card_details(card_id):
    """
    Retrieve details for a single card by ID.
    """
    try:
        card = db.cards.find_one({'_id': card_id})

        if not card:
            return util.response.error(
                status_code=404,
                message='The specified card ID does not exist.',
                failure='failure_nonexistent_card',
            )

        return util.response.success({
            'card': card,
        })
    except:
        return util.response.undefined_error()
