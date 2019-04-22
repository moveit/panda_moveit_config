^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package panda_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.7.2 (2019-04-22)
------------------
* removing unused attempts param (`#26 <https://github.com/ros-planning/panda_moveit_config/issues/26>`_)
* virtual joint quaternion->rpy
* fixing the virtual joint issue by adding the broadcaster (`#23 <https://github.com/ros-planning/panda_moveit_config/issues/23>`_)
* changing the end effector parent group (`#20 <https://github.com/ros-planning/panda_moveit_config/issues/20>`_)
  * changing the end effector parent group
  * changing virtual joint to floating for use with moveit_visual_tools
* Fix incorrect SRDF path (`#19 <https://github.com/ros-planning/panda_moveit_config/issues/19>`_)
* Contributors: Dave Coleman, Mike Lautman

0.7.1 (2018-12-10)
------------------
* CHOMP: remove "Hybrid" collision detector (`#16 <https://github.com/ros-planning/panda_moveit_config/pull/16>`_)
* Contributors: Robert Haschke

0.7.0 (2018-11-09)
------------------
* Initial release of panda_moveit_config into Melodic, including OMPL, CHOMP and STOMP configs
  We moved/merged this repo from https://github.com/frankaemika/franka_ros.
* Contributors: Dave Coleman, Florian Walch, Mike Lautman, Raghavender Sahdev
