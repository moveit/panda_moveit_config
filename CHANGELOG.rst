^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package panda_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.7.8 (2022-09-11)
------------------
* Update to franka_description 0.10.0 (`#119 <https://github.com/ros-planning/panda_moveit_config/issues/119>`_)
* Contributors: Matt Droter, Robert Haschke

0.7.7 (2022-09-01)
------------------
* Thorough rework based on franka_description 0.9.1 (using fine and coarse collision models)
  The internal robot controller uses coarse collision models for self-collision checking.
  In MoveIt, these coarse models should be used for self-collision checking only as well.
  Particularly, these coarse models should not be used for collision checking with the environment.
* Adapt ACM configuration to Melodic
  Melodic's srdfdom/MoveIt don't support tags <disable_default_collisions> and <enable_collisions>.
* Remove adapter ResolveConstraintFrames
  as it's not implemented in Melodic
