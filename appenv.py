from flask import Flask
from qreader import QReader


qreader_reader = QReader()
app = Flask(__name__)
