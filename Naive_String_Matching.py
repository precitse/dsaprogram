# ...existing code...
def naive_string_matching(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    if m == 0:
        print(f"Pattern is empty — matches at every index from 0 to {n}")
        for i in range(n + 1):
            print(f"Pattern found at index {i}")
        return

    if m > n:
        print("No match found (pattern longer than text).")
        return

    matches = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)

    if not matches:
        print("No match found.")
    else:
        for idx in matches:
            print(f"Pattern found at index {idx}")


if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    naive_string_matching(text, pattern)
