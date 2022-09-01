^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package panda_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.0 (2022-09-01)
------------------
* Thorough rework based on franka_description 0.9.1 (using fine and coarse collision models)
  The internal robot controller uses coarse collision models for self-collision checking.
  In MoveIt, these coarse models should be used for self-collision checking only as well.
  Particularly, these coarse models should not be used for collision checking with the environment.
