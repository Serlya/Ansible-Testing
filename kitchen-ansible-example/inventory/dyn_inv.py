#!/usr/bin/env python
# coding=utf-8
import json

aa = {
    "tomcat-servers": {
        "hosts": ['192.168.0.99'],
    }
}

print json.dumps(aa, indent=4)
