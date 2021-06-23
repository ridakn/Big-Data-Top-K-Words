set hive.merge.mapfiles=false;
set hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat;
set mapred.map.tasks = 250;
set mapred.reduce.tasks = 600;

DROP TABLE IF EXISTS theinputfile;
DROP TABLE IF EXISTS wordstrings_Table;

CREATE TABLE theinputfile (line String);
LOAD DATA INPATH 'BigData.txt' OVERWRITE INTO TABLE theinputfile;

CREATE TABLE wordstrings_Table (word String);

add file splitter.py;

INSERT OVERWRITE TABLE wordstrings_Table
SELECT TRANSFORM(line)
USING 'python splitter.py'
AS word
FROM theinputfile;

CREATE INDEX wordsindex ON TABLE 
wordstrings_Table (word)
AS 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler'
WITH DEFERRED REBUILD; 

SELECT word, count(*) AS count 
FROM wordstrings_Table 
GROUP BY word
SORT BY count DESC
LIMIT 100;

SELECT word, count(*) AS count
FROM wordstrings_Table
WHERE length(word) > 6
GROUP BY word
SORT BY count DESC
LIMIT 100;

DROP TABLE IF EXISTS theinputfile;
DROP TABLE IF EXISTS wordstrings_Table;