import os
import sys


THIS_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(THIS_DIR, "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)
