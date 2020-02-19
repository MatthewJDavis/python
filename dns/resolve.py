import dns.resolver

resolver = dns.resolver.Resolver()

answers = resolver.query('matthewdavis111.com', 'A')

for answer in answers:
    print(answer)