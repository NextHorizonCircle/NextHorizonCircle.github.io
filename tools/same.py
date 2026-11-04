# prints SAME if index.html already holds the same app parts as the newly built file
import re, sys
g = lambda s, i: re.search(r'id="' + i + r'"[^>]*>(.*?)</script>', s, re.S).group(1)
a, b = open(sys.argv[1]).read(), open(sys.argv[2]).read()
print("SAME" if all(g(a, i) == g(b, i) for i in ["pc-vault", "pc-app", "pc-boot"]) else "DIFF")
