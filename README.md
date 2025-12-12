# airflow_dbt_setting
Airflow, dbt 도커 컴포즈 환경 설정

디렉토리 구조

project-root/
│
├── docker/
│   └── docker-compose.yml
│
├── dockerfiles/
│   └── airflow_dbt/
│       ├── Dockerfile
│       └── requirements.txt
│
├── airflow/
│   ├── dags/
│   │   └── example_dbt_dag.py
│   ├── logs/
│   └── plugins/
│
└── dbt/
    ├── project/
    │   ├── models/
    │   │   └── core
    │   │   └── staging
    │   └── dbt_project.yml
    └── profiles.yml
