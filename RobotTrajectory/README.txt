Code developed by Nikhil Jawade
Student ID - 210987533

**************************************************************************************************
					    ABOUT
**************************************************************************************************

This is a ROS package that automatically generate point-to-point cubic trajectories connecting 
pairs of randomly generated points. For successful execution of the ROS program, several 
instructions needs to be followed (see the following section).



**************************************************************************************************
				 INSTRUCTIONS TO BE FOLLOWED
**************************************************************************************************

1. Open 'Terminal'

2. Unzip the file 'ar_week5_test.zip' using following command:
   	$ unzip ar_week5_test.zip -d ~/catkin_ws/src/

4. Run following set of commands in the same sequence:
	$ cd ~/catkin_ws			-Move to your catkin workspace

	$ catkin_make				-Compiles the catkin package that was programmed

	$ roscore				-Starts Master, Parameters and rosout

5. Run the 'launch.xml' in new 'Terminal' which will execute all the nodes required to run the ROS 
   program successfully:
	$ source ./devel/setup.bash		-Source your environment setup file
		
	$ roslaunch ar_week5_test launch.xml	-Runs 'launch.xml'

	
