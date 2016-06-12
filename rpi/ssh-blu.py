import sys
import serial

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate = 9600)

def send_signal(signal):
    if(signal == "3"):
        print "TURN RIGHT!"
        bluetoothSerial.write("r")
    elif(signal == "4"):
        print "MOVE FORWARD!"
        bluetoothSerial.write("f")
    elif(signal == "5"):
        print "TURN LEFT!"
        bluetoothSerial.write("l")
    else:
        print "DON'T MOVE!"
        bluetoothSerial.write("x")
    return 1

if __name__ == "__main__":
    send_signal(sys.argv[1])
    print "hello ssh!"