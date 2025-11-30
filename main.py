from fastapi import FastAPI
import mysql.connector.pooling
import logging
import os

app = FastAPI()

# Logging setup
logging.basicConfig(
    filename="incident.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Create DB connection pool using ENV
db_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="app_pool",
    pool_size=int(os.getenv("DB_POOL_SIZE", 2)),
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME"),
)

# Ensure table exists on startup
@app.on_event("startup")
def start():
    conn = None
    try:
        conn = db_pool.get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS traffic_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                value INT
            )
        """)
        logging.info("Table ready")
    except Exception as e:
        logging.error(e)
    finally:
        if conn:
            conn.close()

# API endpoint
@app.get("/db")
def db():
    conn = None
    try:
        conn = db_pool.get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO traffic_log(value) VALUES (1)")
        cur.execute("SELECT SUM(value) FROM traffic_log")
        s = cur.fetchone()
        return {"sum": s}
    except Exception as e:
        logging.error(e)
        raise e
    finally:
        if conn:
            conn.close()
