
def remove_stop_words(sentences):
    res="" 

    fr=open("langauge_fundementels\\task\\operators\\readwrite\\stop_words.txt")
    
    stop_words=[line.rstrip("\n") for line in fr]
    cleaned_words=[ w for w in sentences.split(" ")if w not in stop_words]
    res=" ".join(cleaned_words)
    return res
sentence1="machine learning is a subset of ai"
sentence2="django is one of python framework"
print(remove_stop_words(sentence1))
print(remove_stop_words(sentence2))
assert remove_stop_words(sentence1)=="machine learning subset ai","test case failed"
assert remove_stop_words(sentence2)=="django one python framework","test case failed"
print("test case accepted")
