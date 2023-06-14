cmake_minimum_required(VERSION 3.22)
project(panda_moveit_config)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config ros1 DESTINATION share/${PROJECT_NAME})
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})

ament_package()
