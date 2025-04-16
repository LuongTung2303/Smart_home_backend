# Model xử lý dữ liệu người dùng với truy vấn thủ công
from database.db import get_connection

def find_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
