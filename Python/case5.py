#Case 5: Read files in chunks then using counter

import time
import re
import os
import collections
import concurrent.futures 

# Clean item so that only English text remains
def clean_item(item):
    
    return ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \'\t])|(\w+:\/\/\S+)", " ", item).split())


# Save output words into a text file
def save_topKwords(filename, K, topKwords):
    name = filename.split(".")
    fname = name[0] + "_TOP_" + str(K) + "_WORDS.txt"
    f = open(fname, 'w')
    f.write("Frequency \t Word \n")
    for word in topKwords:
        f.write('{0[1]}\t\t{0[0]}\n'.format(word))

    
if __name__ == '__main__':
    
    K = 10    # Some K value
    
    print("Case 5: Read files in chunks then use counter")
        
    # Pick filename, uncomment the file to run
    
    filename = "dataset-400MB.txt"
    #filename = "dataset-8GB.txt"
    #filename = "Big Data.txt"
    
    result_list = []
    
    start1 = time.time()
    
    # Pick a Chunk Size, uncomment to run
    
    chunk_size = int(100 * 1024 * 1000)     # 100 MB
    #chunk_size = int(50 * 1024 * 1000)     # 50 MB
    #chunk_size = int(200 * 1024 * 1000)    # 200 MB
    
    # Divide the files and make them into chunks of size chunk_size
    def make_chunks(chunk_size):
        
        if not os.path.exists('Parts_of_'+ filename):
            os.makedirs('Parts_of_'+ filename)
    
        reader = open(filename, 'rb')
        
        p = 0
        
        while True:
            lines = reader.read(chunk_size)
            if not lines:
                break
            p += 1
            fname = 'Parts_of_'+ filename+'/part_' + str(p)
            file_object  = open(fname, 'wb')
            file_object.write(lines)
            file_object.close()  
            
        return p
    
    # Total chunks made
    totalfiles = make_chunks(chunk_size)
    filenames = ['part_' + str(i) for i in range(1, totalfiles+1)]
    
    end1 = time.time()
    
    print("Dividing file into chunks and storing individual files: ", end1 - start1)  
    
    start2 = time.time()
    
    # Process each chunk
    def read_chunks(number):
        
        words = {}
        partnumber = 1
        fname = 'Parts_of_'+ filename+'/part_' + str(partnumber)
        
        with open(fname) as reader:
            for line in reader:
                cleanitem = clean_item(line)
                for w in cleanitem.split():
                    if w != "'":
                        if w in words:
                            words[w] += 1
                        else: 
                            words[w] = 1
        
        return words
    
    count_all = collections.Counter()
    
    # Parallel Execution of the files
    with concurrent.futures.ProcessPoolExecutor() as executor:      
        for result in executor.map(read_chunks, filenames):
            count_all.update(result)  
    
    
    end2 = time.time()
    
    print("Parallel Execution took: ", end2 - start2)
    print("Total execution time: ", end2 - start1)
    
    #Print top K words
    topKwords = count_all.most_common(K)
    print(topKwords)
    
    # Save the top K words
    save_topKwords(filename, K, topKwords)
    
