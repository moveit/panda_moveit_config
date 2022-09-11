^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package panda_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.1 (2022-09-11)
------------------
* Update to franka_description 0.10.0 (`#119 <https://github.com/ros-planning/panda_moveit_config/issues/119>`_)
* Example use of ns parameter in sensors.yaml (`#88 <https://github.com/ros-planning/panda_moveit_config/issues/88>`_)
* Drop link8 from ACM as this link doesn't have any collision model anymore
* srdf: Use loop macros to reduce code redundancy
* Unify calls to xacro
* Contributors: Matt Droter, Robert Haschke, Tim Redick

0.8.0 (2022-09-01)
------------------
* Thorough rework based on franka_description 0.9.1 (using fine and coarse collision models)
  The internal robot controller uses coarse collision models for self-collision checking.
  In MoveIt, these coarse models should be used for self-collision checking only as well.
  Particularly, these coarse models should not be used for collision checking with the environment.
