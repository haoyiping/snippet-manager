import os, sys

pwd = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

sys.path.insert(0, os.getcwd())
