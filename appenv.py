import openpyxl
import datetime
from flask import Flask
from cv2 import QRCodeDetector
from pyzbar.pyzbar import decode
from qreader import QReader


qreader_reader, cv2_reader, pyzbar_reader = QReader(), QRCodeDetector(), decode
app = Flask(__name__)
