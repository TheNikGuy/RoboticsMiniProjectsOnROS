Code developed by Nikhil Jawade
Student ID - 210987533

******************************************************************************************************
                                             ABOUT
******************************************************************************************************

This is a ROS package that will automatically generate Cartesian space movements of the end-effector
of the Panda robot manipulator: the end-effector will "draw" squares of different sizes on the x-y
Cartesian plane, starting from a given robot configuration. For successful execution of the ROS
program, several instructions needs to be followed (see the following section).



*****************************************************************************************************
                                     INSTRUCTIONS TO BE FOLLOWED
*****************************************************************************************************

1. Open 'Terminal'

2. In the src fodler of your catkin workspace install the following repository:
    $ git clone -b melodic-devel https://github.com/ros-planning/panda_moveit_config.git

    $ rosdep update

    $ rosdep install --from-paths . --ignore-src -r -y

    $ cd ..

    $ catkin_make

3. Unzip the file 'ar_week10_test.zip' using following command:
    $ unzip ar_week10_test.zip -d ~/catkin_ws/src/

4. Run the following set of commands to give the execute permission to the required scripts:
    $ cd ~/catkin_ws/src/ar_week10_test/scripts/	- Move to the folder where scripts exist

    $ chmod +x square_size_generator.py		- Execute permission to interaction_generator.py

    $ chmod +x move_panda_square.py		- Execute permission to perception_filter.py

5. Run following set of commands in the same sequence:
    $ cd ~/catkin_ws				- Move to your catkin workspace

    $ catkin_make				- Compiles the catkin package that was programmed

    $ roscore					- Starts Master, Parameters and rosout

5. Run the 'launch' file in new 'Terminal' which will run the RVIZ successfully:
    $ source ./devel/setup.bash				- Source your environment setup file
	
    $ roslaunch panda_moveit_config demo.launch		- Runs 'panda_moveit_config demo.launch'

6. Now run the necessary scripts and rqt_plot:

   For that, you need to open 3 new Terminals and run following command on each of them:
    $ source ./devel/setup.bash				- Source your environment setup file
	
   Once you source the setup on all 3 Terminals, run following commands on each Terminal:

    $ rosrun ar_week10_test square_size_generator.py	- Run 'square_size_generator.py' on 1st Terminal

    $ rosrun ar_week10_test move_panda_square.py	- Run 'square_size_generator.py' on 2nd Terminal

    $ rosrun rqt_plot rqt_plot				- Run the rqt_plot on 3rd Terminal

   When the rqt_plot is up and running, you manually need to add 'joint_space/positions[0]' to 'joint_space/positions[6]' and adjust the x-y axis ranges.
	
