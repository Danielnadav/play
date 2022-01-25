from urllib.request import urlretrieve
from urllib.parse import urlencode
mydict = {'q': "Title"}
qstr = urlencode(mydict)
# str resolves to: 'q=whee%21+Stanford%21%21%21&something=else'
thing = urlretrieve("https://www.duckduckgo.com/?" + qstr)