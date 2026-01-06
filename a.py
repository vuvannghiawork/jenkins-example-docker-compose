import mysql.connector

try:
    connection = mysql.connector.connect(
        host='127.0.0.1', # Kết nối qua tunnel
        port=3306,
        user='root',
        password='nghia'
    )

    if connection.is_connected():
        print("Kết nối thành công đến MySQL trên PWD!")
        db_info = connection.get_server_info()
        print(f"Phiên bản MySQL: {db_info}")

except Exception as e:
    print(f"Lỗi kết nối: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()