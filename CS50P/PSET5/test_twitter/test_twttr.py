from twttr import twitter
def main():
    test_twttr()

def test_twttr():
    assert twitter("twitter") == "twttr"

if __name__ == "__main__":
    main()