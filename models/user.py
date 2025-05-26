from database.db import get_connection
from flask import jsonify

# GET user information
def get_user_infor(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query, (user_id,)) 

        result = cursor.fetchone()
        if result:
            return jsonify({'message': 'success', 'data': result}), 200
        else:
            return jsonify({'message': 'User not found'}), 404

    except Exception as e:
        print(f"[ERROR] Lỗi khi truy vấn user_id {user_id}: {e}")
        return jsonify({'message': 'Can not find any user'}), 500


# UPDATE user information
def update_user_infor(user_id, data):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            UPDATE user
            SET password = %s,
                fullname = %s,
                address = %s,
                phone = %s,
                dateofbirth = %s
            WHERE id = %s
        """

        value = (
            data.get('password'),
            data.get('fullname'),
            data.get('address'),
            data.get('phone'),
            data.get('dateofbirth'),
            user_id
        )

        cursor.execute(query, value)
        conn.commit()

        if cursor.rowcount == 0:
            print("Không tìm thấy user với id:", user_id)
            return jsonify({'message': 'User not found or not updated'}), 404
        else:
            return jsonify({'message': 'success'}), 200

    except Exception as e:
        print("Error updating user:", e)
        return jsonify({'message': 'Error updating profile'}), 500


# DELETE user
def delete_user(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM user WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Không tìm thấy user với id:", user_id)
            return jsonify({'message': 'User not found'}), 404
        else:
            return jsonify({'message': 'success'}), 200

    except Exception as e:
        print("Error: Can not delete user:", e)
        return jsonify({'message': 'Error deleting user'}), 500
