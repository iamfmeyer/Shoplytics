import pandas as pd
from faker import Faker
import random
import os
from src.config_loader import DATA_DIR, yaml_config

# Load configurations from YAML
num_records = yaml_config["processing"]["num_records"]
random_seed = yaml_config["processing"]["random_seed"]

# Initialize Faker and set random seed for reproducibility
Faker.seed(random_seed)
random.seed(random_seed)
fake = Faker()

# Set number of dummy records
NUM_RECORDS = 1000

# Create dummy data
data = []
for _ in range(NUM_RECORDS):
    data.append(
        {
            "order_id": fake.uuid4(),
            "customer_id": fake.uuid4(),
            "product": random.choice(["Smartphone", "Laptop", "Tablet", "Headphones"]),
            "amount": random.randint(50, 2000),
            "order_date": fake.date_this_year(),
            "region": random.choice(
                ["Europe", "Asia", "North America", "South America"]
            ),
        }
    )

# Save dummy data to DataFrame
df = pd.DataFrame(data)

# Make sure output directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Save data as CSV file
output_file = os.path.join(DATA_DIR, yaml_config["paths"]["input_file"])
df.to_csv(output_file, index=False)

print(f"Dummy data successfully written to {output_file}")
