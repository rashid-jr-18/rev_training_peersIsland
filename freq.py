def countFreq(paragraph):
    freq={}
    Stop_found=False
    for r in paragraph:
        for word in r:
            word_lower=word.lower()
            
            if word_lower=="STOP":
                
                Stop_found=True
                break
            if len(word_lower) < 3:
                continue
            freq[word_lower]=freq.get(word_lower,0)+1
        if Stop_found:
            break
    return freq
    


paragraph=[
          ["hello","world","Hello"],
          ["this","is","a","test"],
        ["STOP","ignore","this","line"],
        ["should","not","be","processed"]
    ]
          
          
print(countFreq(paragraph))