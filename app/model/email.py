from mongoengine import *
import datetime

class Email(Document):
    """
    How an email is stored in database.
    """
    identifier  = StringField()
    to_addr     = StringField(db_field='to')
    from_addr   = StringField(db_field='from')
    received_on = DateTimeField(default=datetime.datetime.now)
    subject     = StringField()
    body        = StringField()
    server      = ListField()
    status      = StringField()

