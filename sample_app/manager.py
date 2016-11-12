# -*- coding: utf-8 -*-
"""
Manager component.
"""
from __future__ import division, absolute_import, print_function, unicode_literals

import logging

from . import server

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Application(object):
    """The application."""

    def __init__(self, args):
        self.server = server.Server(args)
        self.server.run()
