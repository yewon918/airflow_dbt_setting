#!/bin/bash

# Initialize Airflow DB if not exists
if [ ! -f "/opt/airflow/airflow.db" ]; then
    echo "Initializing Airflow DB..."
    airflow db init
fi

# Create admin user automatically (optional)
airflow users create \
    --username admin \
    --firstname admin \
    --lastname user \
    --email admin@example.com \
    --role Admin \
    --password admin || true

# Run the service command (webserver / scheduler)
exec "$@"
