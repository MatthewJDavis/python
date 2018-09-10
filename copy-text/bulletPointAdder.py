#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line on the clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)