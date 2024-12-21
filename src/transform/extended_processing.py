import pandas as pd
import os
from src.config_loader import DATA_DIR, yaml_config

# Ensure the output directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load paths from YAML configuration
input_file = os.path.join(DATA_DIR, yaml_config["paths"]["input_file"])
output_file_product_region = os.path.join(
    DATA_DIR, yaml_config["paths"]["output_revenue_by_region"]
)
output_file_top_products = os.path.join(
    DATA_DIR, yaml_config["paths"]["output_top_products"]
)

# Read CSV file
df = pd.read_csv(input_file)

# Ensure output path exists
output_dir = "./data"
if not os.path.exists(output_dir):
    os.makedir(output_dir)


# 1. Revenue by product and region

pdf_revenue_by_product_and_region = (
    df.groupby(["region", "product"])["amount"].sum().reset_index()
)

# Save as parquet file
output_file_product_region = os.path.join(
    output_dir, "revenue_by_product_and_region.parquet"
)
pdf_revenue_by_product_and_region.to_parquet(output_file_product_region, index=False)


# 2. Top product by region
pdf_top_products_by_region = (
    df.groupby(["region", "product"])["amount"]
    .sum()
    .reset_index()
    .sort_values(["region", "amount"], ascending=[True, False])
    .groupby("region")
    .head(1)
)

# Save as parquet file
pdf_top_products_by_region.to_parquet(output_file_top_products, index=False)


print(f"Revenue by product and region saved to {output_file_product_region}")
print(f"Top products by region saved to {output_file_top_products}")
