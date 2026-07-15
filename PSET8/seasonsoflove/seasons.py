from datetime import date, datetime, timedelta
import inflect
p = inflect.engine()
import sys

def main():
    try:
        calculate()
    except ValueError:
        sys.exit("Invalid date")


def validate_date(BirthDate):
    try:
        temp = datetime.strptime(BirthDate, "%Y-%m-%d")
    except ValueError:
        raise ValueError
    else:
        BirthDate = temp
        return BirthDate

def calculate():
    date1 = input("Date Of Birth: ")
    date1 = validate_date(date1)
    #current date
    today = (date.today()).isoformat()
    today = validate_date(today)
    diff = today - date1
    diff = diff.total_seconds() / 60
    diff = int(diff)
    print(f"{p.number_to_words(diff)} {p.plural_noun('minute', diff)}")


if __name__ == "__main__":
    main()