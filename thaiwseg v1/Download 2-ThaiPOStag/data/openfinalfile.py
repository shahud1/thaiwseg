import subprocess
import os


path_to_notepad = '/Applications/TextEdit.app'
path_to_file = '/Users/shahud/PycharmProjects/ProjectPOS/data/segmentedtext.TAGGED'

subprocess.call([path_to_notepad, path_to_file])
