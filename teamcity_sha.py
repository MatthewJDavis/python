from urllib.request import urlopen


def get_sha(url):
    with urlopen(url) as sha:
        sha_words = []
        for line in sha:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                sha_words.append(word)
    return sha_words


versionList = {'2019.1.5', '2019.1.4', '2019.1.3', '2019.1.2', '2019.1.1', '2019.1'}

for version in versionList:
    url = 'https://download.jetbrains.com/teamcity/TeamCity-{}.tar.gz.sha256'.format(version)
    get_sha(url)

