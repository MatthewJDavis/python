#! python3
# adNameFix formats AD names that have been copied to the clipboard in commonly supplied format of
# firstname surname, to the samAccountName format of 'firstname.surname' and copies those to the clipboard
# requires pyperclip: https://github.com/asweigart/pyperclip

import pyperclip

text = pyperclip.paste()

lines = text.split('\r\n')
samAcctName = []

for i in range(len(lines)):
    if i == len(lines) -1 and len(lines[i]) > 0:
        print('end of list')
        lines[i] = "'" + lines[i].replace(' ', '.') + "'" # replace the space with a full stop adds quotes. End of file so we don't need the comma
        samAcctName.append(lines[i])
    elif len(lines[i]) > 0:
        lines[i] = "'" + lines[i].replace(' ', '.') + "'" + ","  # replace the space with a full stop adds quotes and comma to lines
        samAcctName.append(lines[i])
    else:
        print(f'No data found at line: {i}')

text = '\n'.join(samAcctName)

pyperclip.copy(text)


