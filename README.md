# thaiwseg
Thaiwseg is word segmentation which based on Thai language, the project of a group of SIIT. We've tried to experiment and play around with the Thai language with using module like Pythainlp,Thai Dictionary and,mtranslate. We created an algorithm to divide the text input into word segment.

We noticed several methods of achieving this task across the internet and came up with the conclusion that Machine learning methods out perform any 'Stand alone Python' algorithm. Thai Language is far too complex than matching words from the dictionary for segmentation.

In this version (v0.9) we compared the top performing methods like Deepcut, Cutkum (coming in v1.0),PythaiNlp with a python algorithm based word segmenter. 

In the future versions we plan to implement a Machine learning algorithm (using Tensorflow).

# Requirement
Python 3.0 ++

Deepcut

Pythainlp

mTranslate

Fuzzywuzzy

Flask

# Detailed Install instructions

Create a virtual machine using virtualenv ( pip install virtualenv ) and run the whole project in a virtual environment 

Also, install these repositories:
```python
pip install cutkum
```
```python
pip install deepcut  and pip install docker
```
```python
pip install pythainlp
```
```python
pip install mtranslate   
```
```python
pip install fuzzywuzzy
```

- Easiest way to install is by creating a virtual environment. Install all the repositories above only when the virtualenv have been activated.
- Download the whole git folder as zip and unzip the files inside the virtual environment folder that you created.
- If Cutkum cannot find 'lstm.l6.d2.pb' , download and copy it to 'virtualenv/model/' directory.
- Copy the Main.py and thaidict.txt to the 'virtualenv/' directory. [ make sure both files are in the same Dir ]
- To run the file, open Terminal and move to the 'virtualenv/' directory. Then activate using 'source bin/activate' command. After that run python3 and type the necessary command.
- In the above mentioned directory type: python3 Real_gui.py and run it!
- After the GUI successfully loads type in the Thai sentence and press enter.
- IF YOU HAVE ANY ISSUES RUNNING THE FILE PLEASE RAISE AN ISSUE

# Installation video:

 [Install guide]https://www.youtube.com/watch?v=iDxvAWlIR-w


# Coding Section
how to import each modules
```python
from mtranslate.core import translate
import deepcut
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from mtranslate.core import translate
from pythainlp import *
```

# Reference
[Flask](http://flask.pocoo.org)

[Thai Dictionary](https://github.com/pureexe/thai-wordlist)

[mTranslate](https://www.npmjs.com/package/@ngx-translate/core)

[DeepCut](https://github.com/rkcosmos/deepcut)

[CutKum](https://github.com/pucktada/cutkum)

[FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)



# Contributers 
* Punchok Kerdsiri -  https://github.com/punch872
* boycatbay - https://github.com/boycatbay
