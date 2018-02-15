# thaiwseg
Thaiwseg is word segmentation which based on Thai language, the project of a group of SIIT. We've tried to experiment and play around with the Thai language with using Python,Thai Dictionary and,Google translate. We created an algorithm to divide the text input into word segment.

*what we're developing right now is trying to improve the accurracy of diving and create web interface with Flask in order to runs on web server and also to see the process and compare our result with github project like "Cutkum" and "Deep cut"

# Requirement
Python 3.0 ++

CutKum

Deepcut

mTranslate

Fuzzywuzzy

Flask

# Install instructions

You could either (1) Create a virtual machine using virtualenv ( pip install virtualenv ) and run the whole project in a virtual environment or (2) install Anaconda python and run it.


Also, install these repositories:

pip install cutkum
pip install deepcut  (requires Keras)
pip install mtranslate   (already inside the project folder)

# Coding Section

from mtranslate.core import translate



# Reference
[Flask][http://flask.pocoo.org]

[Thai Dictionary](https://github.com/pureexe/thai-wordlist)

[mTranslate/core](https://www.npmjs.com/package/@ngx-translate/core)

[DeepCut](https://github.com/rkcosmos/deepcut)

[CutKum][https://github.com/pucktada/cutkum]

[FuzzyWuzzy][https://github.com/seatgeek/fuzzywuzzy]
