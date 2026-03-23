# GCP IoT — Integración de dispositivos IoT con Google Cloud Platform

Repositorio con dos aproximaciones prácticas para enviar datos desde dispositivos IoT a **Google BigQuery** usando Google Cloud Platform. Cada enfoque usa un protocolo de comunicación diferente, lo que permite comparar sus ventajas según el caso de uso.

---

## Arquitecturas disponibles

### 1. `http - bigquery` — Ingesta vía HTTP y Cloud Functions

Los dispositivos envían datos mediante peticiones **HTTP/HTTPS** a una **Google Cloud Function**, que actúa como punto de entrada y se encarga de insertar los registros en BigQuery.

```
Dispositivo IoT
     │
     │  HTTP POST (JSON payload)
     ▼
Cloud Function (GCP)
     │
     │  Streaming insert
     ▼
BigQuery (tabla destino)
```

**Cuándo usarlo:** dispositivos con conectividad estable, integraciones REST sencillas, baja frecuencia de envío.

---

### 2. `mqtt - bigquery` — Ingesta vía broker MQTT

Los dispositivos publican mensajes en un **broker MQTT**. Un suscriptor recoge los mensajes y los inserta en BigQuery.

```
Dispositivo IoT
     │
     │  MQTT publish (topic)
     ▼
Broker MQTT
     │
     │  subscribe + callback
     ▼
Cliente Python (suscriptor)
     │
     │  Streaming insert
     ▼
BigQuery (tabla destino)
```

**Cuándo usarlo:** dispositivos con recursos limitados, redes poco estables, alta frecuencia de mensajes, arquitecturas pub/sub.

---

## Requisitos

- Python 3.8+
- Proyecto activo en [Google Cloud Platform](https://console.cloud.google.com/)
- Cuenta de servicio con permisos sobre BigQuery (`roles/bigquery.dataEditor`)
- Dataset y tabla en BigQuery creados previamente
- Para MQTT: broker accesible (p.ej. [Mosquitto](https://mosquitto.org/) local o [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/))

---

## Estructura del repositorio

```
gcp_iot/
├── http - bigquery/        # Enfoque HTTP con Cloud Functions
│   ├── main.py             # Código de la Cloud Function
│   ├── http_cloud_function.py           # Cliente simulador de dispositivo
│   └── requirements.txt
│
├── mqtt - bigquery/        # Enfoque MQTT con broker
│   ├── mqtt_subscriber_bigquery.py       # Suscriptor que inserta en BigQuery
│   ├── mqtt_publisher_bigquery.py        # Publicador simulador de dispositivo
│   └── requirements.txt
│
└── .gitignore
```
