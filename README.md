# GCP IoT — IoT Device Integration with Google Cloud Platform

Repository with two practical approaches for sending data from IoT devices to **Google BigQuery** using Google Cloud Platform. Each approach uses a different communication protocol, allowing you to compare their advantages depending on the use case.

---

## Available Architectures

### 1. `http - bigquery` — Ingestion via HTTP and Cloud Functions

Devices send data through **HTTP/HTTPS** requests to a **Google Cloud Function**, which acts as the entry point and handles inserting records into BigQuery.

```
IoT Device
     │
     │  HTTP POST (JSON payload)
     ▼
Cloud Function (GCP)
     │
     │  Streaming insert
     ▼
BigQuery (target table)
```

**When to use it:** devices with stable connectivity, simple REST integrations, low sending frequency.

---

### 2. `mqtt - bigquery` — Ingestion via MQTT broker

Devices publish messages to an **MQTT broker**. A subscriber picks up the messages and inserts them into BigQuery.

```
IoT Device
     │
     │  MQTT publish (topic)
     ▼
MQTT Broker
     │
     │  subscribe + callback
     ▼
Python Client (subscriber)
     │
     │  Streaming insert
     ▼
BigQuery (target table)
```

**When to use it:** resource-constrained devices, unstable networks, high message frequency, pub/sub architectures.

---

## Requirements

- Python 3.8+
- Active project on [Google Cloud Platform](https://console.cloud.google.com/)
- Service account with BigQuery permissions (`roles/bigquery.dataEditor`)
- Dataset and table in BigQuery created beforehand
- For MQTT: accessible broker (e.g. local [Mosquitto](https://mosquitto.org/) or [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/))

---

## Repository Structure

```
gcp_iot/
├── http - bigquery/        # HTTP approach with Cloud Functions
│   ├── main.py             # Cloud Function code
│   ├── http_cloud_function.py           # Device simulator client
│   └── requirements.txt
│
├── mqtt - bigquery/        # MQTT approach with broker
│   ├── mqtt_subscriber_bigquery.py       # Subscriber that inserts into BigQuery
│   ├── mqtt_publisher_bigquery.py        # Device simulator publisher
│   └── requirements.txt
│
└── .gitignore
```
