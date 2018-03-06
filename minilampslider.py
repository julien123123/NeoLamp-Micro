from neopixel import NeoPixel as npx
from machine import Pin
import time

np = npx(Pin(5), 32)


html = """ <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{text-align:center; width: 90%; margin: 0 auto; background-color: #311d3f; color: white;}h1{font-family: helvetica;}p{font-family: monospace;}.slidecontainer{width: 100%; text-align: center;}.slider{-webkit-appearance: none; width: 100%; height: 15px; border-radius: 5px; background: #d3d3d3; outline: none; opacity: 0.7; -webkit-transition: .2s; transition: opacity .2s;}.slider:hover{opacity: 1;}.slider::-webkit-slider-thumb{-webkit-appearance: none; appearance: none; width: 25px; height: 25px; border-radius: 50%; background: #4CAF50; cursor: pointer;}#R::-webkit-slider-thumb{background: red;}#B::-webkit-slider-thumb{background: blue;}.slider::-moz-range-thumb{width: 25px; height: 25px; border-radius: 50%; background: #4CAF50; cursor: pointer;}</style></head><body><h1>MiniLampe v0.1</h1><div class="slidecontainer"> <input type="range" min="0" max="255" value="50" class="slider" id="R"> <p><span id="c1"></span></p><input type="range" min="0" max="255" value="50" class="slider" id="G"> <p><span id="c2"></span></p><input type="range" min="0" max="255" value="50" class="slider" id="B"> <p><span id="c3"></span></p></div><script>var slider1=document.getElementById("R");var output1=document.getElementById("c1");output1.innerHTML=slider1.value;var slider2=document.getElementById("G");var output2=document.getElementById("c2");output2.innerHTML=slider2.value;var slider3=document.getElementById("B");var output3=document.getElementById("c3");output3.innerHTML=slider3.value;slider1.oninput=function(){var R=this.value output1.innerHTML=R; var xmlhttp=new XMLHttpRequest(); xmlhttp.open('POST', 'http://' + window.location.hostname, true) xmlhttp.send(R)}setInterval(values, 200);slider2.oninput=function(){var G=this.value output1.innerHTML=G; var xmlhttp=new XMLHttpRequest(); xmlhttp.open('POST', 'http://' + window.location.hostname, true) xmlhttp.send(G)}setInterval(values, 200);slider3.oninput=function(){var B=this.value output1.innerHTML=B; var xmlhttp=new XMLHttpRequest(); xmlhttp.open('POST', 'http://' + window.location.hostname, true) xmlhttp.send(B)s}setInterval(values, 200);</script></body></html> """

// The non-minified html code is in the html file

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    conn.sendall('HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type:text/html\r\n\r\n')
    request = str(request)
    red = request.find('R')
    green = request.find('G')
    blue = request.find('B')
    conn.sendall(html)
    conn.close()
    print(red,green,blue)
    for i in range(32):
        np[i] = (red, green, blue)
        np.write()
        time.sleep(0.1)
        
