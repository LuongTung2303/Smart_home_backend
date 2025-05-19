# Model xử lý dữ liệu người dùng với truy vấn thủ công
from database.db import get_connection

def get_user_infor(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
def update_user_infor(user_id, data):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
def delete_user(user_id):
    pass