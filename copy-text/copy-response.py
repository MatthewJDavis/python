#! python3
# copy-response.py a program the copies a response template to the clipboard
# requires pyperclip: https://github.com/asweigart/pyperclip
# py -m virtualenv env, .\env\Scripts\activate on Windows or source env/bin/activate

# Dictionary of responses
ResponseList = {'thanks': 'Thank you for the email. \n\nMatthew',
            'return': 'I am on holiday at the moment and will reply on my return',
            'outOfOffice': 'I am currently out of the office.'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [response] - copy response to clipboard')
    sys.exit()

response = sys.argv[1]  # first command line arg is the response name

if response in ResponseList:
    pyperclip.copy(ResponseList[response])
    print('Password for ' + response + ' copied to clipboard')
else:
    print('There is no response named ' + response)
