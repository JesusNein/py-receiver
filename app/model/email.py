from mongoengine import *

class Email(Document):
    """
    How an email is stored in database.
    """
    to_addr     = StringField()
    from_addr   = StringField()
    created_on  = DateTimeField()
    subject     = StringField()
    body        = ListField()
    server      = StringField()

