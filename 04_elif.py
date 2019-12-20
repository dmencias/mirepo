# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:19:11 2019

@author: CEC
"""

aclNum = int(input("What is the IPv4 ACL number? "))

if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL. ")
elif aclNum >=100 and aclNum <= 199:
    print("this is a extended IPv4 ACL.!")
else:
    print("This is not a standard or extended ipv4 ACL")
