# Dictionary: Count word occurrences in a given text and store them in a dictionary.

from collections import Counter

def CWO(text):
    words = text.lower().split()  
    WC = Counter(words)  
    return dict(WC)  

text = "My Name is Md Naim Ahammed."
WC = CWO(text)
print(WC)
