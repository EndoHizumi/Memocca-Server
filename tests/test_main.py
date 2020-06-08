import unittest
from unittest import mock

import main as sticky_server


class testAuthorize(unittest.TestCase):

    @mock.patch('flask.request')
    @mock.patch('models.io_util.set_response_json')
    def test_authorize(self, mock_request, mock_set_response_json):
        mock_request.cookie.get.return_value = 'accesstoken'
        sticky_server.authorize()
        mock_set_response_json.assert_not_called()
