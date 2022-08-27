Code developed by Nikhil Jawade

******************************************************************************************************
                                             ABOUT
******************************************************************************************************

This is a ROS package that simulates a simple computational model of social human-robot interaction.
For successful execution of the ROS program, several instructions needs to be followed (see the following section).



*****************************************************************************************************
                                     INSTRUCTIONS TO BE FOLLOWED
*****************************************************************************************************

1. Open 'Terminal'

2. Unzip the file 'ar_week5_test.zip' using following command:
    $ unzip cr_week8_test.zip -d ~/catkin_ws/src/

3. Run the following set of commands to give the execute permission to the required scripts:
    $ cd ~/catkin_ws/src/cr_week8_test/scripts/	- Move to the folder where scripts exist

    $ chmod +x interaction_generator.py		- Execute permission to interaction_generator.py

    $ chmod +x perception_filter.py		- Execute permission to perception_filter.py

    $ chmod +x robot_controller.py		- Execute permission to robot_controller.py

    $ chmod +x robot_expression_prediction.py	- Execute permission to expression_prediction.py

4. Run following set of commands in the same sequence:
    $ cd ~/catkin_ws			- Move to your catkin workspace

    $ catkin_make				- Compiles the catkin package that was programmed

    $ roscore					- Starts Master, Parameters and rosout

5. Run the 'launch' file in new 'Terminal' which will execute all the nodes required to run the ROS 
   program successfully:
    $ source ./devel/setup.bash					- Source your environment setup file
	
    $ roslaunch cr_week8_test human_robot_interaction.launch	- Runs 'human_robot_interaction.launch'

6. To see the what values sent in messages, we will run 'rostopic echo' to print the messages on screen.
   For that, you need to open 4 new Terminals and run following command on each of them:
    $ source ./devel/setup.bash				- Source your environment setup file
	
   Once you source the setup on all 4 Terminals, run following 'rostopic echo' commands on each
   Terminal:

    $ rostopic echo /object_info			- 'object_info' message on 1st Terminal

    $ rostopic echo /human_info				- 'human_info' message on 2nd Terminal

    $ rostopic echo /perceived_info			- 'perceived_info' message on 3rd Terminal

    $ rostopic echo /robot_info				- 'robot_info' message on 3rd Terminal




	
