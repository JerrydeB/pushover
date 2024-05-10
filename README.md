# Pushover Python Package

## Install

1. Install the package with pip

```
pip install pushover_jb
```

2. Create a [Pushover](https://pushover.net) account.

3. Put your user key and api token in a file .env

```
PUSHOVER_USER_KEY=xxxxxxx
PUSHOVER_API_TOKEN=xxxxxxx
```

## Usage

```
import pushover_jb as po

po.send(
    message="This is the message", 
    title="Title", 
    priority=po.Priority.P2
)
```

### Functions:

send: sends a push notification

Arguments:
```
message (str): The message to be sent.
title (str, optional): The title of the message. Defaults to an empty string.
priority (Priority, optional): The priority of the message. Defaults to Priority.P3.
```
