#Case 4: Read line by line so only single line is stored in RAM + COUNTER

from collections import Counter 
import time
import re
    
# Clean item so that only English text remains
def clean_item(item):
    
    return ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \'\t])|(\w+:\/\/\S+)", " ", item).split())

if __name__ == '__main__':
    
    K = 10      # Some K value
    
    print("Case 4: Read line by line so only single line is stored in RAM using COUNTER")
    
    # Pick filename, uncomment the file to run
    
    filename = "dataset-400MB.txt"
    #filename = "dataset-8GB.txt"
    #filename = "Big Data.txt"
    
    start1 = time.time()
    
    words = {}
    
    # Reading line by line
    with open(filename) as reader:
        for line in reader:
            cleanitem = clean_item(line)
            for w in cleanitem.split():
                if w != "'":
                    if w in words:
                        words[w] += 1
                    else: 
                        words[w] = 1
    
    end1 = time.time()
    
    start2 = time.time()
    
    # Sorting with counter
    count_all = Counter(words)
    
    end2 = time.time()
    
    print("Reading file + adding words and frequency to dictionary took: ", end1 - start1) 
    print("Sorting took: ", end2 - start2)
    print("Total execution time: ", end2 - start1)

    
    #Print top K words
    topKwords = count_all.most_common(K)
    print(topKwords)
    

