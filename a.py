# # import mysql.connector

# # try:
# #     connection = mysql.connector.connect(
# #         host='127.0.0.1', # Kết nối qua tunnel
# #         port=3306,
# #         user='root',
# #         password='nghia'
# #     )

# #     if connection.is_connected():
# #         print("Kết nối thành công đến MySQL trên PWD!")
# #         db_info = connection.get_server_info()
# #         print(f"Phiên bản MySQL: {db_info}")

# # except Exception as e:
# #     print(f"Lỗi kết nối: {e}")

# # finally:
# #     if 'connection' in locals() and connection.is_connected():
# #         connection.close()


# from sshtunnel import SSHTunnelForwarder
# import pymysql
# import os 


# # --- Thông tin SSH ---
# SSH_HOST = "direct.labs.play-with-docker.com"
# SSH_USER = "ip172-18-0-44-d5eaflol2o9000e2i3pg" # Đây là phần trước chữ @
# # Lưu ý: PWD thường sử dụng SSH Key, nếu bạn dùng mật khẩu hãy thêm tham số ssh_password

# # --- Thông tin MySQL (bên trong mạng Docker) ---
# MYSQL_HOST = "172.20.0.3" # IP nội bộ của container MySQL
# MYSQL_PORT = 3306
# MYSQL_USER = "test_user"
# MYSQL_PASS = "test_user"
# MYSQL_DB   = "nghia"

# # Thiết lập SSH Tunnel
# with SSHTunnelForwarder(
#     (SSH_HOST, 22),
#     ssh_username=SSH_USER,
#    ssh_pkey=os.path.expanduser("~/.ssh/id_ed25519"),
#     remote_bind_address=(MYSQL_HOST, MYSQL_PORT)
# ) as tunnel:

#     print(f"Tunnel đang chạy tại cổng: {tunnel.local_bind_port}")

#     # Kết nối tới MySQL thông qua cổng local của Tunnel
#     connection = pymysql.connect(
#         host='127.0.0.1',
#         user=MYSQL_USER,
#         password=MYSQL_PASS,
#         db=MYSQL_DB,
#         port=tunnel.local_bind_port
#     )

#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT VERSION();")
#             result = cursor.fetchone()
#             print(f"Kết nối thành công! Phiên bản MySQL: {result}")
#     finally:
#         connection.close()