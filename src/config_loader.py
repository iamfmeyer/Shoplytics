from dotenv import load_dotenv
import os
import yaml


# Load .env file
load_dotenv()

# Load environment variables
BASE_DIR = os.getenv("BASE_DIR")
DATA_DIR = os.getenv("DATA_DIR")


# Load YAML configuration
def load_yaml_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


# Access YAML data
yaml_config = load_yaml_config()
INPUT_FILE = yaml_config["paths"]["input_file"]
OUTPUT_REVENUE_BY_REGION = yaml_config["paths"]["output_revenue_by_region"]
OUTPUT_TOP_PRODUCTS = yaml_config["paths"]["output_top_products"]
