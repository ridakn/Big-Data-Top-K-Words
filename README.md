# Big-Data-Top-K-Words
Project to compare various techniques to find the top K words in a very large file i.e. different techniques to process Big Data.

## Introduction

<p align="justify">
In recent years, data has become very abundant due to the rapid increase of internet. It's consequently getting increasingly challenging to read, store and process large datasets; the input size is one of the key factors in determining how well or efficiently a program works and therefore, poses a problem and reduces efficiency the larger it gets. Being able to read, store and process huge amounts of data is the main problem of Big Data. Traditional database and data processing systems have been in place; however, the datasets are now so large that it's becoming difficult to manage this data efficiently. Apart from input size, there are various factors that affect how a program executes: the data structures used, the memory available and the algorithm used. This project focuses on analysing how these factors affect the performance for three datasets of different sizes i.e. three input sizes. </p>

## Aim

<p align="justify">
In this project, the main objective was to find the top K words in an input file where K is some integer pertaining to the frequency of each word i.e. how many times each word occurs in the text file and then print the top K most frequent words. Three text files were used as input, each of a different size: 400MB, 8GB and 32GB. Firstly, standard python technique is used, then MapReduce and Hive are used to showcase the improvement in performance for the same task. </p>

## Methods & Results

### Python

Case 1: Read entire file into memory and used loop to count top K words. <br>
Case 2: Read entire file into memory and used Python Counter for top K words. <br>
Case 3: Read file line by line and used loop to count top K words. <br>
Case 4: Read file line by line and used Python Counter for top K words. <br>
Case 5: Read file in chunks and processed in parallel to find top K words. <br>

<img width="752" alt="Screen Shot 2021-06-23 at 7 43 41 PM" src="https://user-images.githubusercontent.com/32781544/123127468-296c0b80-d3ff-11eb-97b9-25de9f2e9084.png">

### Map Reduce

Case 1: 1 Reducer <br>
Case 2: Many Reducers (96) <br>

Subcases: <br>
</t> Case A: Mapper & Reducer <br>
</t> Case B: Mapper, Reducer & Combiner <br>
</t> Case C: Mapper, Reducer, Combiner with Partitioner <br>
</t> Case D: Mapper, Reducer & Combiner using Compression of Text File <br>
  
 <img width="785" alt="Screen Shot 2021-06-23 at 7 57 53 PM" src="https://user-images.githubusercontent.com/32781544/123129901-27a34780-d401-11eb-9d88-84a3206bf052.png">
 
Case 3: Varying the number of reducers

<img width="730" alt="Screen Shot 2021-06-23 at 8 00 14 PM" src="https://user-images.githubusercontent.com/32781544/123130283-82d53a00-d401-11eb-8e1a-8bf38ebae74f.png">

### Hive

<img width="516" alt="Screen Shot 2021-06-23 at 8 01 19 PM" src="https://user-images.githubusercontent.com/32781544/123130530-ad26f780-d401-11eb-9c5f-f6e790b4c256.png">
<img width="583" alt="Screen Shot 2021-06-23 at 8 01 22 PM" src="https://user-images.githubusercontent.com/32781544/123130539-aef0bb00-d401-11eb-95eb-ed8f5c9c5b9c.png">

### Map Reduce VS Hive

<img width="449" alt="Screen Shot 2021-06-23 at 8 02 31 PM" src="https://user-images.githubusercontent.com/32781544/123130708-d8a9e200-d401-11eb-9756-955c8e645261.png">

## Conclusion

<img width="500" alt="Screen Shot 2021-06-23 at 8 02 34 PM" src="https://user-images.githubusercontent.com/32781544/123130740-e0698680-d401-11eb-83c3-f0ba902573aa.png">

