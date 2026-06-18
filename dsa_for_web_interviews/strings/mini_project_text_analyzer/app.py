from collections import Counter


def analyze_text(filename):

    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.split()

    total_words = len(words)

    char_count = len(text)

    word_frequency = Counter(words)

    print("\nTEXT ANALYSIS")
    print("-" * 30)

    print("Total Words:", total_words)
    print("Total Characters:", char_count)

    print("\nTop 5 Frequent Words:")

    for word, count in word_frequency.most_common(5):
        print(f"{word}: {count}")


analyze_text("sample.txt")