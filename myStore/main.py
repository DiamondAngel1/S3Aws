#!/usr/bin/env python3
import os
import subprocess
import boto3
from datetime import datetime

# Налаштування
DB_CONTAINER = "postgres"   # ім'я контейнера
DB_NAME = "mydb"
DB_USER = "postgres"
S3_BUCKET = "my-backup-bucket"
BACKUP_DIR = "/tmp"

# Формуємо ім'я файлу
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"{BACKUP_DIR}/{DB_NAME}_{timestamp}.sql"

# Виконуємо pg_dump всередині контейнера
with open(backup_file, "w") as f:
    subprocess.run([
        "docker", "exec", DB_CONTAINER,
        "pg_dump", "-U", DB_USER, DB_NAME
    ], stdout=f, check=True)

# Завантажуємо на S3
s3 = boto3.client("s3")
s3.upload_file(backup_file, S3_BUCKET, os.path.basename(backup_file))

print(f"Backup {backup_file} uploaded to s3://{S3_BUCKET}/")
