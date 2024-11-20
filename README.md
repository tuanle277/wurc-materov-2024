
# wurc-materov-2024

Create a new workspace:
`mkdir -p ~/ros2_ws/src`
then `cd ~/ros2_ws/src`

`src` is where the packages as folders are. Add in the materov folder/package sent above in it (it will be pushed later). Within it
+ `setup.py`: take a look at the entry_points list that allows putting up nodes. More comments in the file
+ `materov` folder: contains all the python files, each contains a node. More comments in the file. Right now we have 3 nodes mentioned above. 

To run:
+ `colcon build` (run this everytime after changing the node codes) in `ros2_ws` to create the necessary files/folders. 
+ `source install/setup.bash` (only need to run this once for each terminal instance)
+ `ros2 run <package_name> <node name>`
+ in our case: `ros2 run materov  <node name>`

Refer to these guides to start writing: https://docs.ros.org/en/humble/Tutorials/.
Learn some basic things like: node, message types, topics, publisher/subscriber (all in python).

Credit to Kevin Le
