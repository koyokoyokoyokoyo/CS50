import re #check the re library: docs.python.org/3/library/re.html <-- inlcuding symbols for patterns(re.search)
#example:
email = input("what's your input? ")
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
##Note that + == 1 or more of the thing to the left, so [^@]+ works
#[] <-- set of characters allowed(included)
#{} <-- HOW MANY charcters would you want of the PREVIOUS RE
#a{3,5} <-- 3 to 5 instances of a
#a{4,}b <-- however many a's, followed by a singular b
#\w alphanumeric characters (so document for more of these, like \d, \D, \s, \S, etc...)
#(\w|\s) a group(). alphanumeric or whitespace
#(\w+\s)? can be there OR NOT, which is what ? does
#(?:...)
#(?P<capture_name>\+etc...) ?P<> gives a capture group a name
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    #last = matches.group(1)
    #first = matches.group(2)
    name = f"{first} {last}"
    #name = f"{first} {last}"
    #OR INSTEAD OF ALL OF THOSE
    #name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
#MAXIMUM simplicity, and the walrus operator
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#_________________________________________________________________________
url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(2)}") #group 2 BECAUSE (www\.) is grouped with (), so it technically group(1)

#ALTERNATIVE WAY WITH non-capturing versions (?:...)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    #removed $ to allow any symbol after the username
    print(f"Username: {matches.group(1)}")

                    ####note that there are also other functions to use with the re library####

    #re.sub(pattern, repl, string, count=0, flag=0) like re.sub(r"https://", "", url, re.IGNORECASE)
    #re.split(pattern, string, maxsplit=0, flags=0) <-- split a string using multiple characters
    #re.findall(pattern, string, flags=0) <-- allows you to find multiple copies of the same pattern in different places in a string