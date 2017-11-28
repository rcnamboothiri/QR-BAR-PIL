from pyqrcode import QRCode
import sys
url = QRCode("This is too much")
url.svg('uca.svg', scale=10)