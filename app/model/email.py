from mongoengine import *
import datetime

class Email(Document):
    """
    How an email is stored in database.
    """
    to_addr     = StringField(db_field='to')
    from_addr   = StringField(db_field='from')
    created_on  = DateTimeField(default=datetime.datetime.now)
    subject     = StringField()
    body        = StringField()
    server      = ListField()
    read        = BooleanField(default=False)

