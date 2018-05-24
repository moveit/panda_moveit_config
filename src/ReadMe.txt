ReadMe for testing CHOMP Plans with obstacles
---------------------------------------------

**Pre-requisites:**
moveit package installed from source from: https://github.com/ros-planning/moveit

_collision_scene_1.py :_ a complex simulated environment (with 4 obstacles) to test that CHOMP plans around obstacles.

_collision_scene_2.py :_ a simple simulated environment (with 1 obstacle) to test that CHOMP plans around obstacles. One can vary the position/size of the obstacle to do any kind of planning.

To **run the CHOMP planner**, do the following in two seperate terminals:
1. roslaunch panda_moveit_config demo_chomp.launch
2. python collision_scene_test_1.py OR python collision_scene_test_2.py
