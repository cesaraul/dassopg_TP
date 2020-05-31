import socket
import json
import os
import sys

import csv 
import time
import signal
import traceback

class Moneda:
    def __init__(self,nombre):
        self.nombre = nombre
        