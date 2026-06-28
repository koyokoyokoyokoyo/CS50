from random import choice #now we can just write choice instead of random.choice repeatedly.
import sys #another module, sys.

#this means, if sys.argv has less than two arguments, so for e.g. just argv[0] and nothing for argv[1]
if len(sys.argv) < 2: 
    sys.exit("blah blah blah" )
#more than one word. 'James Bond' instead of just 'James'
elif > 2:
    sys.exit("too many")
print("Hello, my name is", sys.argv[1])

for arg in sys.argv[1:]: #[] to determine when you want to start. this is slicing
    print("Hello, my name is," arg)

PACKAGES
#pip is a package manager. it allows packages to be run
#"pip install cowsay" in terminal, for example.
#APIs. Application Programming Interface
#You can install via pip a library called 'requests', which will connect you with the API.
#It allows you to make web/internet requests using code, allowing you to act like a browser.
import requests
import sys
import json
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(json.dumps(response.json()), indent=2)
#.dumps, where s is for string. this just pretty prints the json dictionary in a nice, more understandable format
o = response.json()
for result in o["results"]:
    print(result["trackName"])
#from FILENAME import FUNCTION < importing fucntions form your own personal file
#for your file, it is BEST to use if __name__ == etc OR ELSE your code will not work :(

#########extra note from lesson5:
if not isinstance(variable, (int,float)): # isinstance(v, t) is a native python function 
    raise TypeError("must be of type int or float")