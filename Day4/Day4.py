
def is_valid_passphrase(text):
    return len(text) == len(set(text))


def contains_no_anagrams(text):
    for idx, word in enumerate(text):
        word_ = list(word)
        word_.sort()
        text[idx] = str(word_)

    return is_valid_passphrase(text)


if __name__ == "__main__":
    with open("input.txt") as f:
        passphrases = f.readlines()

    split_pass = [passphrase.split() for passphrase in passphrases]

    print(sum(is_valid_passphrase(text) for text in split_pass))

    print(sum(contains_no_anagrams(text) for text in split_pass))

