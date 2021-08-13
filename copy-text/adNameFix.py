#! python3
# adNameFix formats AD names that have been copied to the clipboard in commonly supplied format of
# firstname surname, to the samAccountName format of 'firstname.surname' and copies those to the clipboard
# requires pyperclip: https://github.com/asweigart/pyperclip

import pyperclip

text = pyperclip.paste()
lines = text.split('\r\n\r\n')

def get_names(line_list):
    names = []
    for line in line_list:
        if len(line) > 0:
            line = line.strip()
            line = line.replace(' ', '.')
            line = line.replace('-', '.')
            line = line.lower()
            names.append(line)
    return names

ad_names = get_names(lines)
text = '\n'.join(ad_names )
pyperclip.copy(text)
