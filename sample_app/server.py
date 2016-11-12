# -*- coding: utf-8 -*-
"""
Interface component.
"""
from __future__ import division, absolute_import, print_function, unicode_literals

import json
import logging

import flask

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


JSON_CONTENT = {"Content-Type": "application/json"}


def _exception_to_dict(exception):
    """Convert exception to an error object to be sent as response to APIs."""
    return {"error": {"type": type(exception).__name__,
                      "message": exception}}


class ApiError(Exception):
    """Base class for all JSON APIs exceptions.

    Attributes:
        message: exception message (inherited from Exception)
        status_code: corresponding HTTP status code.
        display_name: name of error class or None to use the class name.
        json: JSON-compatible representation.

    Args:
        message: exception message.
        extra_fields: additional fields to embed in error object.
    """

    status_code = 500
    display_name = None

    def __init__(self, message, **extra_fields):
        super(ApiError, self).__init__(message)
        self._extra = extra_fields

    @property
    def json(self):
        """JSON-compatible representation for the API exception."""
        error_object = _exception_to_dict(self)
        if self.display_name:
            error_object["error"]["type"] = self.display_name
        error_object["error"].update(self._extra)
        return error_object


class Server(object):
    """The Web Server.

    Args:
        args: server arguments that must have the following attributes:
            debug: run server in debug mode.
            host: the address to listen to connections.
            port: the server port.
    """

    _EXCEPTION_CODES = {
        TypeError: 400,
        ValueError: 400,
        ApiError: 500,
    }
    _EXCEPTION_DEFAULT_STATUS_CODE = 500

    def __init__(self, args):
        self._app = flask.Flask("sample_app")
        self._app.debug = args.debug
        self._host = args.host
        self._port = args.port
        self._sessions = {}

        for exception_type in self._EXCEPTION_CODES:
            self._app.register_error_handler(exception_type, self._exception_handler)

        self._app.add_url_rule("/", "sample_app",
                               lambda: flask.render_template("index.html", script="sample_app.js"))
        self._app.add_url_rule("/favicon.ico", "favicon",
                               lambda: self._app.send_static_file("favicon.ico"))

    def run(self):
        """Start the server."""
        self._app.run(self._host, self._port, use_reloader=False)

    def add_handler(self, route, handler, **options):
        """Add a function as handler for some route."""
        self._app.route(route, **options)(handler)

    def _exception_handler(self, exception):
        """Handle exceptions and send proper responses.

        Send a JSON representation of the exception, with the correct mime-type
        and HTTP status code.
        """
        logger.exception("Handler raised an exception")
        response = getattr(exception, "json", _exception_to_dict(exception))
        status_code = getattr(exception, "status_code",
                              self._EXCEPTION_CODES.get(type(exception),
                                                        self._EXCEPTION_DEFAULT_STATUS_CODE))
        return json.dumps(response), status_code, JSON_CONTENT
