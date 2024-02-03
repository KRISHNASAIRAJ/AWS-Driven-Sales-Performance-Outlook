import boto3
import random
import time
from decimal import Decimal

session = boto3.Session(profile_name='default', region_name='ap-southeast-2')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('AWS-Driven-Sales-Performance-Outlook-Table') 

def generate_order_data():
    order_id = str(random.randint(1, 10000))
    product_name = random.choice(['Microtek 1250SW', 'Base 180', 'Aaron 1860', 'LivFast 1000SW', 'Microtek JUMBO 3000'])
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(6000.0, 30000.0), 2)))
    
    return {
        'order_id': order_id,   
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }

def insert_into_dynamodb(data):
    try:
        table.put_item(Item=data)
        print(f"Inserted Data: {data}")
    except Exception as e:
        print(f"Error inserting Data: {str(e)}")

if __name__ == '__main__':
    try:
        while True:
            data = generate_order_data()
            insert_into_dynamodb(data)
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nScript stopped by User")