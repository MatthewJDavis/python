import dns.resolver, sys

if len(sys.argv) < 2:
    print('Usage: python resolve.py [domain name]')
    sys.exit()

resolver = dns.resolver.Resolver()

answers = resolver.query(sys.argv[1], 'A')

for answer in answers:
    print(answer)
