import emoji
def main():
    userEmoji = input("Input: ")
    print(emoji.emojize(f"{userEmoji}", language="alias", variant="emoji_type"))
if __name__ == "__main__":
main()