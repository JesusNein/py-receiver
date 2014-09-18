import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view
from app.model import email

@route("(address)@(host)", address=".+")
def START(message, address=None, host=None):
    mail = email.Email()
    mail.to_addr = message['To']
    mail.from_addr = message['From']
    mail.subject = message['Subject']
    mail.body = message.body()
    mail.server = message.Peer
    mail.save()

