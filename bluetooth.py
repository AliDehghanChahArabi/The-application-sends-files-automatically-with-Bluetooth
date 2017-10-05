import os

while True :
    print ("Install pi-bluetooth")
    os.system("sudo apt-get install pi-bluetooth")
    print ("Install bluetooth bluez")
    os.system("sudo apt-get install bluetooth bluez")
    print ("Install bluez python-bluez")
    os.system("sudo apt-get install bluez python-bluez")
    print ("hciconfig hci0 piscan")
    os.system("sudo hciconfig hci0 piscan")
    print ("hciconfig hci0 name 'raspberrypi'")
    os.system("sudo hciconfig hci0 name 'raspberrypi'")
    print ("Scan Blt")
    os.system("sudo python /usr/share/doc/python-bluez/examples/simple/inquiry.py")

    with open("blt.txt", "r") as file :
        id_blt = file.read()
        file.close()

    print (id_blt)

    print ("Send File apk client")
    os.system("ussp-push %s@12 /home/pi/Desktop/client.apk client.apk" % (id_blt))
