# 🖥️ Linux Fleet Management System

A scalable and distributed Linux Fleet Management System designed for real-time monitoring, observability, and centralized control of multiple Linux servers using a lightweight agent-based architecture.

---

## 🚀 Project Description

The Linux Fleet Management System enables administrators to monitor and manage multiple Linux machines from a single dashboard. It collects real-time system metrics such as CPU usage, memory consumption, disk utilization, and network activity from distributed agents installed on each server.

The system ensures efficient infrastructure monitoring, quick anomaly detection, and improved operational visibility across all connected machines.

---

## 🎯 Key Features

- Real-time monitoring of multiple Linux servers
- CPU, RAM, Disk, and Network usage tracking
- Lightweight Python-based monitoring agent
- Centralized web dashboard for visualization
- Secure API communication between agent and backend
- Scalable architecture for large server fleets
- Health status monitoring and alerts
- Docker support for easy deployment

---

## 🏗️ System Architecture

Frontend (React Dashboard)
        ↓
Backend (FastAPI Server)
        ↓
Linux Agents (Multiple Servers)
        ↓
System Metrics Collection (CPU, RAM, Disk, Network)

---

## 🛠️ Tech Stack

Frontend:
- React.js
- Axios
- Tailwind CSS (optional)

Backend:
- FastAPI (Python)
- Uvicorn
- Pydantic

Database:
- PostgreSQL

Agent:
- Python (psutil, requests)

DevOps:
- Docker
- Docker Compose
- Linux (Ubuntu/CentOS)

---

## 📁 Project Structure

fleet-management/
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── package.json
│
├── agent/
│   └── linux_agent.py
│
├── docker-compose.yml
└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/linux-fleet-management.git
cd linux-fleet-management
