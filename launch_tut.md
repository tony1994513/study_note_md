## Setup launch
```
<?xml version="1.0"?>
<launch>
    <node name="setup_baxter_left_hand_camera" pkg="birl_kitting_experiment" type="setup_baxter_left_hand_camera.py" />

    <arg name="marker_size" default="6.0" />
    <arg name="max_new_marker_error" default="0.08" />
    <arg name="max_track_error" default="0.2" />
    <arg name="cam_image_topic" default="/cameras/left_hand_camera/image" />
    <arg name="cam_info_topic" default="/cameras/left_hand_camera/camera_info" />
    <arg name="output_frame" default="/left_hand_camera" />
    <arg name="bundle_files" default="$(find birl_kitting_experiment)/bundles/pan_stand_0_1_2_3.xml $(find birl_kitting_experiment)/bundles/pan_stand_box_8_9_10_12.xml $(find birl_kitting_experiment)/bundles/package_box_4_5.xml $(find birl_kitting_experiment)/bundles/ink_box_13_14.xml $(find birl_kitting_experiment)/bundles/pencil_case_11_15.xml $(find birl_kitting_experiment)/bundles/weight_box_18_19.xml $(find birl_kitting_experiment)/bundles/tape_dispenser_22_23.xml $(find birl_kitting_experiment)/bundles/drink_20_21.xml $(find birl_kitting_experiment)/bundles/drink_24_25.xml" />


    <node name="ar_track_alvar" pkg="ar_track_alvar" type="findMarkerBundlesNoKinect" respawn="false" output="screen"
        args="$(arg marker_size) $(arg max_new_marker_error) $(arg max_track_error) $(arg cam_image_topic) $(arg cam_info_topic) $(arg output_frame) $(arg bundle_files)" />

   <node name="publishMarkersInfo" pkg="birl_kitting_experiment" type="alvar_marker_to_baxter_picking_pose.py" />

</launch>
```