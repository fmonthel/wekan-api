from wekan_api import app
from wekan_api import db

import util.response


@app.route('/boards', methods=['GET'])
def boards():
    """
    Retrieve all boards.
    """
    try:
        all_boards = list(db.boards.find())
        return util.response.success({
            'boards': all_boards,
        })
    except:
        return util.response.undefined_error()


@app.route('/board/<board_id>', methods=['GET'])
def board_details(board_id):
    """
    Retrieve details for a single board by ID.
    """
    try:
        board = db.boards.find_one({'_id': board_id})

        if not board:
            return util.response.error(
                status_code=404,
                message='The specified board ID does not exist.',
                failure='failure_nonexistent_board',
            )

        return util.response.success({
            'board': board,
        })
    except:
        return util.response.undefined_error()


@app.route('/board/<board_id>/lists', methods=['GET'])
def board_lists(board_id):
    """
    Retrieve all lists associated with a board.
    """
    try:
        if not db.boards.find_one({'_id': board_id}):
            return util.response.error(
                status_code=404,
                message='The specified board ID does not exist.',
                failure='failure_nonexistent_board',
            )

        lists = list(db.lists.find({'boardId': board_id}))
        return util.response.success({
            'lists': lists,
        })
    except:
        return util.response.undefined_error()


@app.route('/board/<board_id>/cards', methods=['GET'])
def board_cards(board_id):
    """
    Retrieve all cards associated with a board.
    """
    try:
        if not db.boards.find_one({'_id': board_id}):
            return util.response.error(
                status_code=404,
                message='The specified board ID does not exist.',
                failure='failure_nonexistent_board',
            )

        cards = list(db.cards.find({'boardId': board_id}))
        return util.response.success({
            'cards': cards,
        })
    except:
        return util.response.undefined_error()
