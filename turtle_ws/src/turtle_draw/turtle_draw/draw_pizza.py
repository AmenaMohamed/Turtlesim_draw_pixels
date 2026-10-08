#resources:(how to publish on turtlesim topics) https://note.com/hafnium/n/n80c7c3518ed8?hl=en
#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from formating import  image , formating , colors

image_pairs= formating(image)
PIXEL_SIZE = 0.5


class DrawPizza(Node):
    def __init__(self):
        super().__init__('turtle')
        self.pose_ = None

        self.cmd_vel_pub_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        self.pose_sub_ = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10
        )

        self.timer_ = self.create_timer(0.01, self.draw)
    
    def pose_callback(self, msg):
        
        self.pose_ = msg
    def move_forward(self):
        pass

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
