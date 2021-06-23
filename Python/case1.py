#Case 1: Read Entire File into RAM and then sort

import time
import re
import operator

# Clean item so that only English text remains
def clean_item(item):
    
    return ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \'\t])|(\w+:\/\/\S+)", " ", item).split())

# Print the top K words
def topKwords(K, count_all):
    for i in range(K):
        print(count_all[i])
        

if __name__ == '__main__':
    
    K = 10      # Some K value
    
    print("Case 1: Read Entire File into RAM and then sort dictionary")

    # Pick filename, uncomment the file to run
    
    filename = "dataset-400MB.txt"
    #filename = "dataset-8GB.txt"
    #filename = "Big Data.txt"

    start1 = time.time()
    
    words = {}
    
    # Opening entire file
    with open(filename) as f:
        reader = f.readlines()
    
    # Reading the contents and populating the dictionary
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
    
    # Sorting dictionary
    count_all = sorted(words.items(), key=operator.itemgetter(1), reverse = True)
    
    end2 = time.time()
    
    print("Reading file + adding words and frequency to dictionary took: ", end1 - start1)                   
    print("Sorting took: ", end2 - start2)
    print("Total execution time: ", end2 - start1)
    
    # Printing the words
    topKwords(K, count_all)



