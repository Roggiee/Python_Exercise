alias urldecode='python3 -c "import sys;from urllib import parse;print(parse.unquote(sys.argv[1]))"'

for f in "$@"
do
    newName=$(urldecode "$f")
    mv "$f" "$newName"
done