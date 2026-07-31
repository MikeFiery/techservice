import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")


def conectar():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "techservice_db")
        )
    except mysql.connector.Error as erro:
        raise RuntimeError(
            "Não foi possível conectar ao MySQL. Verifique o ficheiro .env "
            "e confirme que o servidor MySQL está a correr no host configurado."
        ) from erro