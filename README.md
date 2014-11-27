Filenardo
=========

Simple file server made using Tornado

How to
=========
The idea is from the ``SimpleHTTPServer.py`` that comes with Python, but it is not made to have lot of people asking it at the same time.

[Tornado][1] in the other hand is excellent, and made for serving lot of stuff :D So why not using a simple file to call Tornado help us ?

Just run

``filenardo.py --help `` and you will get that:

``--path`` is the path of your folder, default is the actual folder where the script runs.

``--url`` the url which you will use, default is 127.0.0.1

``--port`` the port number, default is 8888

example:

``python filenardo.py --path=/some/where --url=192.168.1.2 --port=8888``

Why the name
=========
Hein?

[1]: https://github.com/facebook/tornado
