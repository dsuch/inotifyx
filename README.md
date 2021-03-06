
**This fork of inotifyx is Python 3-friendly, works with both Python 2.7 and Python 3.4+.**

inotifyx is a simple Python binding to the Linux inotify file system event
monitoring API.

Documentation is provided in the module.  To get help, start an interactive
Python session and type:

>>> import inotifyx
>>> help(inotifyx)

You can also test out inotifyx easily.  The following command will print events
for /tmp:

  python -m inotifyx /tmp

Tests can be run via setup.py:

  ./setup.py test

Note that the module must be built and installed for tests to run correctly.
In the future, this requirement will be lifted.
