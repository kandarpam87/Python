import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)
import sys
sys.path.append(dir_path)

from log import *
from mymath import *
