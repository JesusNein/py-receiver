# This file contains python variables that configure Lamson for email processing.
import logging

# You may add additional parameters such as `username' and `password' if your
# relay server requires authentication, `starttls' (boolean) or `ssl' (boolean)
# for secure connections.
relay_config = {'host': 'localhost', 'port': 8825}

receiver_config = {'host': 'localhost', 'port': 8823}

database_config = {
        'table'     : 'quadrum',
        'username'  : 'YOURUSERNAME',
        'password'  : 'YOURPASSWORD'
}

handlers = ['app.handlers.main']

router_defaults = {'host': 'test\\.com'}

template_config = {'dir': 'app', 'module': 'templates'}

# the config/boot.py will turn these values into variables set in settings
