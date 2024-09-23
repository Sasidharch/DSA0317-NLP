import re

def demonstrate_regex():
    # Sample text for demonstration
    text = """
    Alice was beginning to get very tired of sitting by her sister on the bank,
    and of having nothing to do: once or twice she had peeped into the book her
    sister was reading, but it had no pictures or conversations in it, 'and what
    is the use of a book,' thought Alice, 'without pictures or conversations?'
    """

    # 1. Basic Matching
    pattern = r'Alice'
    match = re.search(pattern, text)
    if match:
        print(f"Found '{match.group()}' at position {match.start()}")
    else:
        print("No match found for 'Alice'")

    # 2. Matching with Wildcards
    pattern = r'Alice.*book'
    match = re.search(pattern, text)
    if match:
        print(f"Found pattern '{match.group()}' that starts with 'Alice' and ends with 'book'")
    else:
        print("No match found for 'Alice.*book'")

    # 3. Finding All Matches
    pattern = r'\b[A-Za-z]{4,}\b'  # Matches words with 4 or more letters
    matches = re.findall(pattern, text)
    print(f"Words with 4 or more letters: {matches}")

    # 4. Substituting Text
    pattern = r'\bAlice\b'
    replaced_text = re.sub(pattern, 'Bob', text)
    print("Text after replacing 'Alice' with 'Bob':")
    print(replaced_text)

    # 5. Splitting Text
    pattern = r'\s+'  # Splitting on any whitespace
    words = re.split(pattern, text)
    print(f"Words split from text: {words[:10]}")  # Print only the first 10 words for brevity

if __name__ == "__main__":
    demonstrate_regex()
