# Flask App Installation

This is to show how to install & run Flask App in Debug mode.

## Installation

This repo comes with the virtual environment (located as `venv`) folder for ease of installation process.

- First active the virtual environment by running:
> . venv/bin/activate

- Then simply run:

		pip install -r requirements.txt
		
Once all the required packages installation finishes successfully, we will move on to run the server.

## Starting the server

To start the server run the following command:

	FLASK_APP=app.py python -m flask run
	
To run the app with Debug mode & accessible in LAN:

	FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0