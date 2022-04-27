import serial
import time
import webbrowser
for i in range(20):
    try:
        arduino = serial.Serial(port = f'COM{i}', baudrate = 115200, timeout = .1)
        print('Connected to arduino in COM', i)
        break
    except: pass

while True:
    try:
        cmd = arduino.readline()
        cmd = cmd[:-2].decode('UTF-8')
        print(cmd)
        if cmd == '1':
            webbrowser.open('https://classes.brilliantpala.org/learn/598/')
            print('Button 1 Pressed!!')
        elif cmd == '2':
            webbrowser.open('https://web.whatsapp.com/')
            print('Button 2 Pressed!!')
        elif cmd == '3':
            webbrowser.open('https://www.quora.com/')
            print('Button 3 Pressed!!')

    except UnicodeDecodeError:
        pass
