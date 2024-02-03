# AWS-Driven-Sales-Performance-Outlook

The Project aims to establish a robust data pipeline for tracking and analyzing sales performance using various AWS services. The process involves creating a DynamoDB database, implementing Change Data Capture (CDC), utilizing Kinesis streams, and finally, storing and querying the data in Amazon Athena.

![Architecture](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/fea78b73-0f89-4d76-8771-e4e844a5bda0)


## Technology Used
* Python
* DynamoDB
* DynamoDB Stream(CDC)
* Kinesis Stream
* Kinesis Filehose
* Event Bridge Pipe(For Stream Ingestion)
* Kinesis Firehose(To Batch Streaming)
* Lambda
* Athena
* S3

## Features

* Data Generation Script
  * A Python script has been provided to generate synthetic sales data.
  * The script uses the boto3 library to connect with DynamoDB.
  * The file is included in the repository(mock_data_generator_for_dynamodb.py)


* DynamoDB Setup
  * A DynamoDB database named sales-performance-outlook is created.
  * Implemented Change Data Capture (CDC) for tracking updates and deletions in records.
 ![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/81d6ad2f-7bc7-43ba-af85-939d5d744467)
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/3ffbbf09-75e4-4940-aa68-f480558abee4)


  
  * Established a DynamoDB table named Orders-data-table with order_id as the key.
  * Enabled DynamoDB stream to capture changes in the table(sales-performance-outlook), specifying what data to capture (old/new item).
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/0490fe17-0bc0-49a8-a6e0-16c7e41c691a)


* Kinesis Stream
  * Created a Kinesis stream named kinesis-sales-order to collect streaming data.
  * Similar to Kafka, Kinesis uses shards for partitioning data streams.
  * Read from Starting position of source data
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/7653827f-405e-4b25-9c9e-b4cd5da6e8d4)
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/1599fe3c-e9e8-4bee-8c8d-95138e631a23)



* Event Bridge Integration
  * Configured an Event Bridge pipe to integrate DynamoDB and Kinesis stream.
  * Specified DynamoDB as the source and Kinesis stream as the destination, sharding data based on the eventID.
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/cc5a9ce3-ab65-4dba-ac97-35e5cc6e0e4a)


* Kinesis Firehose
  * Implemented Kinesis Firehose for processing streaming data as batch data.
  * Kinesis Firehose buffer interval 15sec
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/f7ef64c3-8aee-40a7-b9da-27722b202415)
  * Used a Lambda function for data transformation, decoding and parsing DynamoDB strings into JSON with newline characters.
  * Configured buffer time for efficient data processing.
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/8905c7a8-63e5-4fb4-bd8e-cffdcb9029da)


* Glue
  * Created Catalog named aws-driven-sales-performance-outlook-catlog which uses crawler to get metadata of data in various data sources
  * Which creates table based on the schema of the data and further it can be used by Athena for analytical purpose
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/6b24c0ca-56ec-4bd8-8352-73d070886f6c)
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/db0d1211-99f0-4bbc-9055-e5c0b853e708)



* S3 Storage and Crawler
  * Set up S3 as the destination for Kinesis Firehose, storing transformed data in files.
  * S3 Collect buffer interval 60sec
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/e4b19b33-0f37-420a-a990-74e4a10917a3)
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/abda9849-be22-4163-bd2e-f8575fa187ca)


  * Created a crawler with a JSON classifier to identify raw data patterns in the S3 bucket.
  * Ran the crawler with an output file prefix of outlook_ to create a table in the sales-data-catalog database.
  * "$.order_id,$.product_name,$.quantity,$.price" (classifier pattern)json
  * So the classifier avoids the crawler to scan the raw data violating pattern
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/2fdb5c44-18e8-43b0-b595-310e167a85d8)


* Athena Query
  * Utilized AWS Athena, a serverless analytical service, to query the data stored in the sales-data-catalog table.
  * Athena enables seamless querying of data without the need for a dedicated infrastructure.
![image](https://github.com/KRISHNASAIRAJ/AWS-Driven-Sales-Performance-Outlook/assets/90061814/3e35de8f-b8e2-4d37-9e82-703307bbd7e4)


* Permissions Management
  * Added necessary permissions to IAM users for DynamoDB, Kinesis, and Event Bridge.


## Key Outcomes
* The project follows a comprehensive data pipeline architecture to capture, process, and analyze sales data efficiently.
* The inclusion of CDC ensures that changes in records are tracked, providing a complete view of sales performance over time.
* The use of serverless services like Athena and Lambda minimizes infrastructure management efforts.
* The project showcases the integration of multiple AWS services for a seamless end-to-end data processing and analytics solution.
