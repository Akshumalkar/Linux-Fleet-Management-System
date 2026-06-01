def node_dashboard_template(node_name: str, instance: str):
    return {
        "dashboard": {
            "title": f"Node Dashboard - {node_name}",
            "tags": ["fleet", "node"],
            "timezone": "browser",
            "panels": [
                {
                    "title": "CPU Usage",
                    "type": "timeseries",
                    "targets": [
                        {
                            "expr": f"rate(node_cpu_seconds_total{{instance='{instance}'}}[1m])"
                        }
                    ]
                },
                {
                    "title": "Memory Available",
                    "type": "timeseries",
                    "targets": [
                        {
                            "expr": f"node_memory_MemAvailable_bytes{{instance='{instance}'}}"
                        }
                    ]
                },
                {
                    "title": "Disk Available",
                    "type": "timeseries",
                    "targets": [
                        {
                            "expr": f"node_filesystem_avail_bytes{{instance='{instance}'}}"
                        }
                    ]
                }
            ]
        },
        "overwrite": True
    }