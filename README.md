# thaiwseg
Thaiwseg is word segmentation which based on Thai language, the project of a group of SIIT. We've tried to experiment and play around with the Thai language with using Python,Thai Dictionary and,Google translate. We created an algorithm to divide the text input into word segment.

* What we're developing right now: Improving the accurracy of diving and creating web interface with Flask in order to run it on a web server. Also comparing our result with github projects like "Cutkum" and "Deepcut"

# Requirement
Python 3.0 ++

CutKum

Deepcut

mTranslate

Fuzzywuzzy

Flask

# Detailed Install instructions

Create a virtual machine using virtualenv ( pip install virtualenv ) and run the whole project in a virtual environment 

Also, install these repositories:

* pip install cutkum
* pip install deepcut  and pip install docker
* pip install mtranslate   
* pip install fuzzywuzzy

- Easiest way to install is by creating a virtual environment. Install all the repositories above only when the virtualenv have been activated.
- Download the whole git folder as zip and unzip the files inside the virtual environment folder that you created.
- If Cutkum cannot find 'lstm.l6.d2.pb' , download and copy it to 'virtualenv/model/' directory.
- Copy the Main.py and thaidict.txt to the 'virtualenv/' directory. [ make sure both files are in the same Dir ]
- To run the file, open Terminal and move to the 'virtualenv/' directory. Then activate using 'source bin/activate' command. After that run python3 and type the necessary command.
- In the above mentioned directory type: python3 Real_gui.py and run it!
- After the GUI successfully loads type in the Thai sentence and press enter.


# Installation with pictures
Image is:
(https://preview.ibb.co/jBkhi7/Screen_Shot_2561_02_17_at_20_02_58.png)


# Coding Section

from mtranslate.core import translate

# Reference
[Flask](http://flask.pocoo.org)

[Thai Dictionary](https://github.com/pureexe/thai-wordlist)

[mTranslate/core](https://www.npmjs.com/package/@ngx-translate/core)

[DeepCut](https://github.com/rkcosmos/deepcut)

[CutKum](https://github.com/pucktada/cutkum)

[FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)



# Contributers 
* Punchok Kerdsiri -  https://github.com/punch872
* boycatbay - https://github.com/boycatbay
