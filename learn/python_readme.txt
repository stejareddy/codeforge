#****python for machine learning****
#TOC-Table Of Content
#libraries
#httpserver
#django
#network
------------------------------------
#libraries
    - Numpy 
    - Pandas
    - Matplotlib
    - Scikit-learn
--------------------
#httpserver
$python3 -m http.server 8000        # creates a temp server for 8000 port
$python3 -m http.server <port> --directory /path/to/file        
$python3 manage.py runserver        # start and run django server
$python3 -m venv .venv          # create,activate,deactivate python virtual environment 
    | $source .venv/bin/activate        #activating the virtual environment
    | $deactivate       #exit out of virtual environment neatly 
-------------------------------------
#django 
$sudo apt-get install pip 
$pip install django 
$django-admin --version 
$django-admin startproject <projectname>
$django-admin startproject <projectname> .          # create project folder and then run this command inside it. 
$python3 manage.py runserver 
$python3 manage.py runserver &          #run in background 
---------------------
#network
netstat -tuln | grep LISTEN         #to find listening ports -tuln is tcp and udp ln is listing them all. 
fuser 8000/tcp          #find the pid of the known port



