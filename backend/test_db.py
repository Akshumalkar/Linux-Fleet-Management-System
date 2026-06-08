from sqlalchemy import create_engine

DATABASE_URL = "postgresql://fleetadmin:fleetpass@localhost:5432/fleetdb"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("✅ Database Connected Successfully")
    connection.close()

except Exception as e:
    print("❌ Error:", e)