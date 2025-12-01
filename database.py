def vulnerable_login(conn, username, password):
    cursor = conn.cursor()
    # SQL Injection explícito
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    return cursor.fetchall()
