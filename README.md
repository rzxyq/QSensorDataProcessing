# Q Sensor Django Backend 

## Setup (for Macs)
NOTE: postgreSQL is necessary for this application 

**qsensorserver_db** is the name of the database postgreSQL database should have if one wishes to store data locally.  

##### Q Sensor 
To use this framework, a Q sensor must be connected via Bluetooth 

##### Running the server 
To run the server, one should navigate to the root directory of the backend, and run: 

`source venv/bin/activate` to activate the virtual environment packaged with this backend


Then, one should run 
`python manage.py migrate` followed by 
`python manage.py runserver` 


##### `screen` Command Line Argument and `.screenrc` 
To actually retrieve data from the Q sensor, the following file must be saved in the root (~) directory of the user:

`.screenrc` 

This file must contain the following line: 

`logfile flush 0.1` 

The above line causes any logfile created by the argument `screen` to be updated every tenth of a second (thus keeping the data we track locally up-to-date)

The final command line argument to run on the **DESKTOP (~/Desktop)** of the user is: 

`screen -L /dev/tty.AffectivaQ-v2-2072-SPP 1000` 

This causes screen to record data via the Q sensor's Bluetooth port and make a logfile called `screenlog.0` on the Desktop


##### Python Script to Run on the Desktop 
This backend contains a Python script `qsensorpost.py` within the /data_ directory of the backend.  This script should be copied to the **desktop (~/Desktop)** of the user.  It should be run from the desktop through the bash command: 

`python qsensorpost.py` 

This python scripts reads the last line of the developing log file on the Desktop, sends a POST request to the server running in order to update the Q sensor data on the server, and loops continuously.  


##### Viewing the Data

The data a Q sensor session is viewable at URL: 

`http://127.0.0.1:8000/data/result_view` 

To begin data acquisition, the button "GET DATA" should be pressed, and the data from the Q sensor will be mapped on a line graph on that URL's page. 

 
