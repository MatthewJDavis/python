import time
''' Output text one char at a time with a sleep in between for testing builds in CI '''

text = 'this is a bit of a long line of text and would make the linter very very sad :('
doubled = text * 2
start = time.time()

for char in doubled:
    print(char)
    time.sleep(1)

finish = time.time()

print(f'Build took {finish - start:.2} to complete.')