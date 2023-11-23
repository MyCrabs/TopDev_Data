import mysql.connector
connection = mysql.connector.connect(user='root', password='123456', host='localhost')
cursor = connection.cursor()
cursor.execute("SELECT * FROM test.test_table3")
data_from_DB = cursor.fetchall()
connection.close()

info = [1, 'Nhân Viên IT - Lập Trình Viên Java (Spring Boot) - Quận 12', 'Công Ty Tnhh Aegona', 'TP.HCM', '25/11/2023', 'Yêu cầu kinh nghiệm', 'Chuyên viên- nhân viên', '1 - 50 triệu', 'Đại học', 'https://cdn1.vieclam24h.vn/images/default/2023/11/02/LG tròn đỏ trắng_169890869871.png']
