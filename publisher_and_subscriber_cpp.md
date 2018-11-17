## Understanding Publisher and Subscirber(C++)

### - Publisher

```
#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

int _rate = 10;

int main(int argc, char **argv)
{

  ros::init(argc, argv, "node_name");

  ros::NodeHandle n;

  ros::Publisher pub  = n.advertise<msg_type>("topic_name", 1000);

  ros::Rate loop_rate(_rate);

  while (ros::ok())
  {
    std_msgs::String msg; # define pub msg 

    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());
    
    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    
  }

  return 0;
}
```

The difference bettween `ros::spinOnce` and `ros::spin()`, 

- `ros::spinOnce` won't stuck
- `ros::spin` stuck

## - Subscriber
```
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
```