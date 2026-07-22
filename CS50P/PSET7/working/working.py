#my solution for this was extremely stupid and the code looks demented, but hopefully it'll be much better in the future
import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        #the statement itself that needs to be matches
        if matches := re.search(r"([1-9]|10|11|12)(\:([0-5][0-9]))? (AM|PM) to ([1-9]|10|11|12)(\:([0-5][0-9]))? (AM|PM)", s):
            if matches.group(4) == "AM":
                before = int(matches.group(1))
                if matches.group(3):
                    beforeM = int(matches.group(3))
                else:
                    beforeM = 00
                if matches.group(5) != "12":
                    after = int(matches.group(5))
                    after += 12
                    if matches.group(7):
                        afterM = int(matches.group(7))
                    else:
                        afterM = 00
                #check for 12 am
                if matches.group(1) == 12:
                    return (f"00:{beforeM:02} to {after:02}:{afterM:02}")
                else:
                    return (f"{before:02}:{beforeM:02} to {after:02}:{afterM:02}")

            elif matches.group(4) == "PM":
                before = int(matches.group(5))
                if matches.group(7):
                    beforeM = int(matches.group(7))
                else:
                    beforeM = 00
                if matches.group(1) != 12:
                    after = int(matches.group(1))
                    after += 12
                    if matches.group(3):
                        afterM = int(matches.group(3))
                    else:
                        afterM = 00
                #check for 12 am
                if matches.group(5) == 12:
                    return (f"{after:02}:{afterM:02} to 00:{beforeM:02}")
                else:
                    return (f"{after:02}:{afterM:02} to {before:02}:{beforeM:02}")

        else:
            raise ValueError

    except ValueError:
        print("Inavlid Syntax!")
        sys.exit()


if __name__ == "__main__":
    main()