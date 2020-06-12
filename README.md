# CoV Update Setu

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

I have made such arrangements that the script `scripts/main.py` would trigger itself off every day and send an email to the subscribers regarding the latest pandemic stats (active cases, confirmed cases, recovred cases and deceased cases) about their district.

## How to subscribe

You can subscribe to the service by opening an issue on this repository. Make sure to give following details in the description-
```json
"name": "xxx",
"email" : "xxx@xxx.xxx",
"district" : "xxx",
"state" : "xxx"
```

## Contributions

Are welcome.

## Courtesy

[covid19india/api](https://github.com/covid19india/api)
