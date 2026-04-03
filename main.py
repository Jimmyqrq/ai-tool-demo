def summarize(text):
    return "Summary: " + text[:50]

def rewrite(text):
    return "Rewritten: " + text

text = input("Enter text: ")

print(summarize(text))
print(rewrite(text))
