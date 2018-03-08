# NeoLamp-Micro
Mini neopixel lamp controlled by a website hosted on an ESP8266 runing Micropython


## THIS code is almost working!
The only thing that I need to figure out is how to handle the POST request response in micropython. 
It looks something like this:

    b'POST /npx HTTP/1.1\r\nHost: 192.xxx.xxx.xxx\r\nConnection: keep-alive\r\nContent-Length: 27\r\nOrigin: http://192.168.0.110\r\nUser-Agent: Mozilla/5.0 (X11; CrOS x86_64 10323.46.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.107 Safari/537.36\r\nContent-type: application/json\r\nAccept: */*\r\nReferer: http://192.xxx.xxx.xxx/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: fr,en;q=0.9,fr-CA;q=0.8\r\n\r\n{"R":114, "G":120, "B":236}'
Only the dictionary at the end is important to me, but I don't know how to extract it using micropython.
I'm thinking og using the urequests library, but I don't know anything about it.
