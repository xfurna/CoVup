# CoV Updates Setu
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Because services that have `setu` in their names are rad' cool.

## This repository

```bash
├── meta.json
├── README.md
├── scripts
│   ├── main.py
└── templates
    ├── announce.txt
    └── subscribers.txt
```

I have made such arrangements (using [WayScript](https://wayscript.com/)) that the script `scripts/main.py` would trigger itself off every day and send an email to all the subscribers regarding the latest CoV pandemic stats about their district (like active cases, confirmed cases, recovered cases and deceased cases).

## How to subscribe

You can subscribe to the service by opening an issue on this repository. Make sure to give following details in the description-
```json
"name": "xxx",
"email" : "xxx@xxx.xxx",
"district" : "xxx",
"state" : "xxx"
```

If you have privacy concerns, you can share your details with me on [telegram](https://t.me/evi1haxor), privately.

**Note:** You can make muliple subscriptions too.

## Contributions

Are welcome.

<hr>

**Courtesy:** [covid19india/api](https://github.com/covid19india/api)
