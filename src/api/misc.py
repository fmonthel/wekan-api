from wekan_api import app

import util.response


@app.route('/status', methods=['GET'])
def status():
    """
    Endpoint to check the service's health.
    """
    return util.response.success({
        'status': 'OK',
    })
