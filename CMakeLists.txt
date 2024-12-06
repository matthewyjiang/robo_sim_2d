cmake_minimum_required(VERSION 2.8.3)
project(robo_sim_2d)
find_package(catkin REQUIRED COMPONENTS 
roscpp
rospy
std_msgs
message_generation
)
catkin_python_setup()

add_service_files(
  FILES
  AddRobot.srv
  ApplyForceForward.srv
)

# Generate messages
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)


include_directories(include ${catkin_INCLUDE_DIRS})


catkin_install_python(PROGRAMS
  scripts/main.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

