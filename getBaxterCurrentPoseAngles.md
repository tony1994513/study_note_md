## Get Baxter en-effector current pose and angle

```
limb = 'right'
limb_interface = baxter_interface.limb.Limb(limb) 

current_pose_dic = limb_interface.endpoint_pose() # get pose in dic
current_pose_list = [ current_pose_dic['position'].x,  # convert to list
                    current_pose_dic['position'].y,
                    current_pose_dic['position'].z,
                    current_pose_dic['orientation'].x,
                    current_pose_dic['orientation'].y,
                    current_pose_dic['orientation'].z,
                    current_pose_dic['orientation'].w]

current_angles = [limb_interface.joint_angle(joint) for joint in limb_interface.joint_names()]    # get current angles and name
```