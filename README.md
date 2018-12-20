# cs598kgk
final project

This is a flask project and can be run using the following commands

$ export FLASK_APP=start.py
$ flask run

and then visiting

http://127.0.0.1:5000/.

One thing to note, in getting the program to run on pythonanywhere, I set some of the file paths to be full file paths. This will cause problems when attempting to run locally.

The program was hosted for a time at http://keydex.pythonanywhere.com/

There is a known bug where sometimes the js timer doesn't properly start. This will cause some buttons to get stuck as disabled. Using inspect element and removing the disabled property from the buttons fixes this problem.
