# Sample chat service

Python micro service sample

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the service and how to install them

```
apt-get install python3 python3-pip

pip3 install virtualenv
```

## Installing
Clonning repository
```
git clone https://github.com/averdier/py_sample_chat_service
```

Installing requirements

```
cd py_sample_chat_service/

virtualenv env
source env/bin/activate
pip install -r requirements.txt

deactivate
```

## Usage
Commands for start HTTP REST service
```
cd py_sample_chat_service/

source env/bin/activate
python runserver.py
```
