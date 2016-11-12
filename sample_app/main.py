# -*- coding: utf-8 -*-
"""
Flask ReactJS Bootstrap package.
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import argparse
import logging
import sys

import sample_app
from . import manager


logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

DESCRIPTION = "Flask ReactJS Bootstrap Software"


# This variable stores our Application instance. It is defined in module level
# to be easily accessible from debugging consoles.
app = None  # pylint: disable=invalid-name


def _parse_args(argv):
    """Parses command-line arguments."""
    opts = argparse.ArgumentParser(prog=argv[0], description=DESCRIPTION)
    opts.add_argument("-v", "--version",
                      action="version",
                      version=sample_app.__version__,
                      help="show the version number and exit")

    server_opts = opts.add_argument_group("Web server options")
    server_opts.add_argument("--host",
                             default="0.0.0.0",
                             help="address to listen for connections (default: %(default)s)")
    server_opts.add_argument("-p", "--port",
                             type=int,
                             default=8080,
                             help="server port number (default: %(default)s)")

    debug_opts = opts.add_argument_group("Debugging and development options")
    debug_opts.add_argument("-d", "--debug",
                            action="store_true",
                            help="run application in debug mode")

    return opts.parse_args(argv[1:])


def main(argv=None):
    """The software entry point."""
    args = _parse_args(argv or sys.argv)

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    global app  # pylint: disable=global-statement,invalid-name
    app = manager.Application(args)
