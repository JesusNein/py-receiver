from mongoengine import *

class Notification(Document):
    """
    A notification as it is checked by the system
    """
    company     = ReferenceField()
