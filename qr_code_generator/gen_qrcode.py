#this code generates a QR code so that you can connect to
#to the wifi network indicated on "ssid" and "password"

import wifi_qrcode_generator.generator as qr
from PIL import Image

ssid= "inserttheIDofyourwifi"
password="insertpasswordofyourwifi"
security= "WPA"

from wifi_qrcode_generator.generator import wifi_qrcode
qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save("wifi_qrcode.png")
Image.open("wifi_qrcode.png")

