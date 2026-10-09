#resources:(how to publish on turtlesim topics) https://note.com/hafnium/n/n80c7c3518ed8?hl=en
#Turtlesim Teleport service: https://docs.ros.org/en/melodic/api/turtlesim/html/srv/TeleportRelative.html
#teleport service easiest way:https://www.geeksforgeeks.org/python/turtle-setpos-and-turtle-goto-functions-in-python/
#ros1 moving in straight line : https://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
#converting imgs into commands for turtlesim: https://medium.com/@shilpajbhalerao/turtlesim-playground-cbc867924a8
#Turtlesim services: https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html
#Writing services: https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html
#!/usr/bin/env python3
import math
import rclpy
import time
from rclpy.node import Node
from turtlesim.msg import Pose
#from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportRelative ,TeleportAbsolute ,SetPen 
from formating import  image , formating , colors

image_pairs= formating(image)
PIXEL_SIZE = 0.5


class DrawPizza(Node):
    def __init__(self):
        super().__init__('turtle_draw')
        self.pose_ = None

        self.teleport_rel = self.create_client(TeleportRelative, '/turtle1/teleport_relative', 10)
        self.teleport_abs = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.pen_client= self.create_client(SetPen, '/turtle1/set_pen')



        self.timer_ = self.create_timer(0.01, self.draw)
    

    def move_forward_request(self,distance):
        #packing msg
        req = TeleportRelative.Request()
        #no rotations or any movement except in x_axis
        req.linear= float(distance)
        req.angular =0.0
        return self.teleport_rel.call_async(self.req)

    def teleport_to(self, x, y):
            req = TeleportAbsolute.Request()
            req.x = float(x)
            req.y = float(y)
            req.theta = 0.0  
            self.teleport_abs.call_async(req)
            time.sleep(0.02)

    def set_pen(self,rgb):
        req= SetPen.Request()
        req.r=rgb[0]
        req.g=rgb[1]
        req.b=rgb[2]
        req.width=15
        req.off=0
        return self.pen_client.call_async(self.req)
        

    def draw(self,image_pairs):
        start_x=2.0
        start_y=9.0
        self.teleport_to(start_x, start_y)

        for row in image_pairs:
            self.set_pen((0, 0, 0), off=1)
            new_y = start_y - ((row.index()-1) * PIXEL_SIZE)
            for count, color_code in row:
                
                rgb = colors[color_code]
                
                self.set_pen(rgb)
            
                distance = count * PIXEL_SIZE
                
                self.move_forward(distance)

        self.teleport_to(start_x,new_y)


def main(args=None):
    rclpy.init(args=args)
    node = DrawPizza()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
