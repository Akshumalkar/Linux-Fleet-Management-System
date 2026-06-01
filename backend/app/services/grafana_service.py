import requests
from app.dashboards.templates.node_dashboard import node_dashboard_template

GRAFANA_URL = "http://localhost:3000"
API_KEY = "YOUR_GRAFANA_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def create_dashboard_for_node(node_name: str, instance: str):
    dashboard_json = node_dashboard_template(node_name, instance)

    response = requests.post(
        f"{GRAFANA_URL}/api/dashboards/db",
        json=dashboard_json,
        headers=headers
    )

    return response.json()