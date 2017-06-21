#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by w23ta0 on 16-3-22

import base64
import hashlib

a=base64.b64encode("hello")
b=a.encode("hex")
print a
print b

a1=b.decode("hex")
b1=base64.b64decode(a1)
print a1
print b1





