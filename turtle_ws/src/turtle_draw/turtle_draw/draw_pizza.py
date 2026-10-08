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

    def move_forward(self,distance):
        #packing msg
        vel_msg = Twist()
        speed=2
        #no rotations or any movement except in x_axis
        vel_msg.linear.x = abs(speed)

        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        t0 = rclpy.Time.now().to_sec()
        current_distance = 0
        while(current_distance < distance):
             #Publish the velocity
             self.cmd_vel_pub_.publish(vel_msg)
             #Takes actual time to velocity calculus
             t1=rclpy.Time.now().to_sec()
             #Calculates distancePoseStamped
             current_distance= speed*(t1-t0)
             #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        self.cmd_vel_pub_.publish(vel_msg)
        

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
