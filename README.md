# Python email receiver

Receives SMTP mails and puts them in a MongoDB document.

## Development installation
Requirements:
  - [Virtualenv and pip](http://docs.python-guide.org/en/latest/starting/install/linux/).
  - Mutt. Text based email client.
  - [MongoDB](http://docs.mongodb.org/manual/administration/install-on-linux/).

First, create a new virtual environment:
```
$ virtualenv venv
```
Install required packages:
```
$ pip install -r requirements.txt
```
