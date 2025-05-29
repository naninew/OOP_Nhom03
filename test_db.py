import psycopg2
import ProtectedData


def test_db():
    DB_info = ProtectedData.getDatabaseKey()
    conn = psycopg2.connect(
        database=DB_info["DB_NAME"],
        password=DB_info["DB_PASS"],
        user=DB_info["DB_USER"],
        host=DB_info["DB_HOST"],
        port=DB_info["DB_PORT"],
    )
    print("Connected successfully")
    cur = conn.cursor()
    cur.execute("SELECT * FROM card")
    rows = cur.fetchall()
    for data in rows:
        print(*data)
    conn.close()


# test_db()
# ---------------------------------------------------
from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))
A = "???"
try:
    A = gateway.entry_point.SayHello("Ma Ngoc Thang")
except:
    print("Error when connecting with database")
print("-------")
print(A)
print("-------")
