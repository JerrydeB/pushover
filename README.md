# Pushover Python Package

## Install

1. Install the package with pip

```
pip install pushover-jb
```

2. Create a [Pushover](https://pushover.net) account.

3. Put your user key and api token in a file .env

```
PUSHOVER_USER_KEY=xxxxxxx
PUSHOVER_API_TOKEN=xxxxxxx
```

## Usage

```
from pushover_jb import message as pom

pom.send(
    message="This is the message", 
    title="Title", 
    priority=pom.Priority.P2
)
```

### Functions:

send: sends a push notification

**Arguments**
```
message (str): The message to be sent.
title (str, optional): The title of the message. Defaults to an empty string.
priority (Priority, optional): The priority of the message. Defaults to Priority.P3.
```

**Priority**

Can be P1, P2, P3 or P4. P1 being the highest priority. Please check out the 
Pushover [priority docs](https://pushover.net/api#priority) for more information 
on what it means.
