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
from rclpy.node import Node
from turtlesim.msg import Pose
#from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportRelative ,SetPen
from formating import  image , formating , colors

image_pairs= formating(image)
PIXEL_SIZE = 0.5


class DrawPizza(Node):
    def __init__(self):
        super().__init__('turtle')
        self.pose_ = None

        self.control_client = self.create_client(TeleportRelative, '/turtle1/teleport_relative', 10)
        self.pen_client= self.create_client(SetPen, '/turtle1/set_pen')



        self.timer_ = self.create_timer(0.01, self.draw)
    

    def move_forward_request(self,distance):
        #packing msg
        req = TeleportRelative().Request()
        #no rotations or any movement except in x_axis
        req.linear= float(distance)
        req.angular =0.0
        return self.cli.call_async(self.req)
        

    def set_pen(self):
        pass

    def draw(self,image_pairs):
        for row in image_pairs:
            for count, color_code in row:
                
                rgb = colors[color_code]
                
                self.set_pen(rgb)
            
                distance = count * PIXEL_SIZE
                
                self.move_forward(distance)



def main(args=None):
    rclpy.init(args=args)
    node = DrawPizza()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
