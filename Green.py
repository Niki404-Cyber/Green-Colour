import os, sys
try:
    __import__("easyso").bnsbuy()
except Exception as e:
    exit(str(e))
