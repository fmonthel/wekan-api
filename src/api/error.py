from wekan_api import app

import util.response


@app.errorhandler(404)
def not_found(error):
    """
    Generic response for a 404 error.
    """
    return util.response.error(
        status_code=404,
        message='The requested endpoint does not exist.',
        failure='failure_not_found',
    )


@app.errorhandler(500)
def internal_server_error(error):
    """
    Generic response for a 500 error.
    """
    return util.response.undefined_error()
