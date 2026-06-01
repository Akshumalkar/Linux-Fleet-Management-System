from fastapi import FastAPI
import time
import psycopg2

from app.database import engine
from app.models import Base
from app.routers import nodes
from app.services.grafana_service import create_dashboard_for_node

app = FastAPI()


@app.on_event("startup")
async def startup():
    max_retries = 30

    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                host="db",
                port=5432,
                user="postgres",
                password="postgres",
                dbname="fleetdb"
            )

            conn.close()
            break

        except psycopg2.OperationalError:
            if i == max_retries - 1:
                raise

            time.sleep(1)

    Base.metadata.create_all(bind=engine)

app.include_router(nodes.router)

@app.get("/")
def root():
    return {"message": "API Running"}


@app.post("/nodes")
def add_node(hostname: str, ip_address: str):
    node = {
        "id": len(nodes) + 1,
        "hostname": hostname,
        "ip_address": ip_address
    }

    nodes.append(node)

    return node

@app.post("/nodes")
def add_node(hostname: str, ip_address: str):
    node = {
        "id": len(nodes) + 1,
        "hostname": hostname,
        "ip_address": ip_address
    }

    nodes.append(node)

    # 🔥 NEW: Auto create Grafana dashboard
    try:
        create_dashboard_for_node(
            node_name=hostname,
            instance=ip_address + ":9100"
        )
    except Exception as e:
        print("Grafana dashboard creation failed:", e)

    return node

@app.get("/nodes")
def get_nodes():
    return nodes