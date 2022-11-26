import rclpy
from rclpy.node import Node

import serial

from std_msgs.msg import String

class HeadMoveSub(Node):

    def __init__(self):
        super().__init__('head_move_sub')
        self.subscription = self.create_subscription(String, 'head_move', self.move_callback, 10)
        self.subscription

    def move_callback(self, msg):
        print(msg)
        global pubHS


        if msg.data == "up":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x01)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x01)+chr(104)+chr(57))
            ser.flush()
            return

        if msg.data == "middle":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x01)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x01)+chr(104)+chr(47))
            ser.flush()
            return

        if msg.data == "down":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x01)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x01)+chr(104)+chr(37))
            ser.flush()
            return

        if msg.data == "left":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x00)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x00)+chr(32)+chr(31))
            ser.flush()
            return

        if msg.data == "center":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x00)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x00)+chr(24)+chr(42))
            ser.flush()
            return

        if msg.data == "right":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x00)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x00)+chr(40)+chr(60))
            ser.flush()
            return

        if msg.data == "turnoff":
            ser = serial.Serial('/dev/ttyACM0')
            ser.write(chr(0xAA))
            ser.flush()
            ser.write(chr(0x87)+chr(0x00)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x00)+chr(0)+chr(0))
            ser.flush()
            ser.write(chr(0x87)+chr(0x01)+chr(0x0a)+chr(0x00))
            ser.flush()
            ser.write(chr(0x84)+chr(0x01)+chr(0)+chr(0))
            ser.flush()


def main():        
    
    rclpy.init()
    head_move_sub = HeadMoveSub()
    rclpy.spin(head_move_sub)

    head_move_sub.destroy_node()
    rclpy.shudown()
   

if __name__ == '__main__':        
    main()