import sys

sys.path.append("./EyesBot")
import ccxt
import ta
import pandas as pd
from utilities.spot_ftx import SpotFtx
from utilities.custom_indicators import VMC
from datetime import datetime
import time
import json