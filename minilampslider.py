from neopixel import NeoPixel as npx
from machine import Pin
import time
import json

np = npx(Pin(5), 32)

html = """ <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{text-align:center; width: 90%; margin: 0 auto; background-color: #311d3f; color: white;}h1{font-family: helvetica;}p{font-family: monospace;}.slidecontainer{width: 100%; text-align: center;}.slider{-webkit-appearance: none; width: 100%; height: 15px; border-radius: 5px; background: #d3d3d3; outline: none; opacity: 0.7; -webkit-transition: .2s; transition: opacity .2s;}.slider:hover{opacity: 1;}.slider::-webkit-slider-thumb{-webkit-appearance: none; appearance: none; width: 25px; height: 25px; border-radius: 50%; background: #4CAF50; cursor: pointer;}#R::-webkit-slider-thumb{background: red;}#B::-webkit-slider-thumb{background: blue;}.slider::-moz-range-thumb{width: 25px; height: 25px; border-radius: 50%; background: #4CAF50; cursor: pointer;}</style></head><body><h1>MiniLampe v0.1</h1><div class="slidecontainer"> <input type="range" min="0" max="255" value="50" class="slider" id="R"> <p><span id="c1"></span></p><input type="range" min="0" max="255" value="50" class="slider" id="G"> <p><span id="c2"></span></p><input type="range" min="0" max="255" value="50" class="slider" id="B"> <p><span id="c3"></span></p></div><script>var slider1=document.getElementById("R");var output1=document.getElementById("c1");output1.innerHTML=slider1.value;var slider2=document.getElementById("G");var output2=document.getElementById("c2");output2.innerHTML=slider2.value;var slider3=document.getElementById("B");var output3=document.getElementById("c3");output3.innerHTML=slider3.value;slider1.oninput=function(){var rgb=getColors(); output1.innerHTML=rgb[0]; postColors(rgb);};slider2.oninput=function(){var rgb=getColors(); output2.innerHTML=rgb[1]; postColors(rgb);};slider3.oninput=function(){var rgb=getColors(); output3.innerHTML=rgb[2]; postColors(rgb);};getColors=function(){var rgb=new Array(slider1.value, slider2.value, slider3.value); return rgb;};postColors=function(rgb){var xmlhttp=new XMLHttpRequest(); var npxJSON='{"R":' + rgb[0] + ', "G":' + rgb[1] + ', "B":' + rgb[2] + '}'; xmlhttp.open('POST', 'http://' + window.location.hostname + '/npx', true); xmlhttp.setRequestHeader('Content-type', 'application/json'); xmlhttp.send(npxJSON);};</script></body></html> """
# The non-minified code is in the html file

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    print('addr')
    request = conn.recv(1024)
    request = str(request)
    print(request)
    #-------------------------------------------------------------------
    # Ned to find a betrer way to handle the POST response from client
    red = request.find('R=')
    green = request.find('G=')
    blue = request.find('B=')
    # -------------------------------------------------------------------
    conn.sendall(html)
    conn.close()
    print(red,green,blue)
    for i in range(32):
        np[i] = (red, green, blue)
        np.write()
        time.sleep(0.1)
        
