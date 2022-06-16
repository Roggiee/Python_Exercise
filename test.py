import sys
from urllib import parse
print(parse.unquote(sys.argv[1]))
