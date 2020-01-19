from urllib.request import urlopen


def get_sha(url):
    with urlopen(url) as sha:
        sha_words = []
        for line in sha:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                sha_words.append(word)
    return sha_words


def print_items(items):
    for item in items:
        print(item)


def main():
    versionList = {'2019.1.5', '2019.1.4', '2019.1.3', '2019.1.2', '2019.1.1', '2019.1'}

    for version in versionList:
        url = 'https://download.jetbrains.com/teamcity/TeamCity-{}.tar.gz.sha256'.format(version)
        print_items(get_sha(url))


if __name__ == '__main__':
    main()
