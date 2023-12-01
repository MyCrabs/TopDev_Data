import mysql.connector
connection = mysql.connector.connect(user = 'root', password = '123456',host = 'localhost')
cursor = connection.cursor()
query = "CREATE TABLE `test`.`test_table1` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`City` VARCHAR(45) NULL,`Title` VARCHAR(45) NULL,PRIMARY KEY (`ID`))"
query_insert1 = "INSERT INTO `test`.`test_table` (`ID`, `Name`, `City`, `Title`) VALUES ('2', 'Trình', 'Quảng Bình', 'huhu');"
query_delete = "delete from `test`.`test_table` where id = '1'"
query_insert2 = "insert into `test`.`test_table` (`ID`, `Name`, `City`, `Title`) VALUES (%s,%s,%s,%s);"
queryy = "CREATE TABLE `test`.`test_table3` (`id` INT AUTO_INCREMENT,`title` VARCHAR(255),`company_name` VARCHAR(255),`venue` VARCHAR(255),`date` VARCHAR(255),`exp_year` VARCHAR(255),`level` VARCHAR(255),`salary` VARCHAR(255),`edu` VARCHAR(255),`src_pic` VARCHAR(255),PRIMARY KEY (id));"
#cursor.execute(querry) => Neu tao bang thi khong can commit
#>>Update connection
# val =[
#     ('3', 'Cường Còi', 'Hà Tịnh', 'Ngẩn'),
#     ('4', 'Trung Gian', 'Huế', 'hehe')
# ]
# for i in val:
#     cursor.execute(querry_insert2,i)
# connection.commit() # Lam viec thay doi du lieu phai co dong commit
cursor.execute(queryy)
