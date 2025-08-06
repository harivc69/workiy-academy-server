from dotenv import load_dotenv
import os

# Load the appropriate .env file
env_mode = os.environ.get("APP_ENV", "dev")

if env_mode == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

# Check required vars
required = ["DB_NAME", "DB_USER", "DB_PASS", "DB_HOST"]
missing = [var for var in required if not os.getenv(var)]

if missing:
    raise EnvironmentError(f"❌ Missing environment variables: {', '.join(missing)}")

# ✅ Assign env variables to module-level variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Optional: expose env_mode
MODE = env_mode
