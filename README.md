# cli-dslink-python
DSA CLI based in python

I would like to do this in python3, but the released dslink sdk
does not support python3 yet. We should try to switch to python3
when they have their next release.

### Current Functionality
Just getting started...

greet - Displays "Hello, World!"

### Goals for the Project
The goal for this CLI is to be able to do the following
* ls - list nodes starting from any base path
    * -l - list details about the nodes, including value?
* cd - change the current directory
* invoke - invoke an action with parameters (interactively ask for parms?)
* set - set the value of the node
* subscribe - blocking command that watches the value of a node
    * -r - subscribe to a whole "directory" of nodes

### Testing
```bash
$ virtualenv venv
$ . venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ pip install -r test_requirements.txt
(venv)$ nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
```

##### Related Projects
CLI written in dart: https://github.com/IOT-DSA/dslink-dart-shell
