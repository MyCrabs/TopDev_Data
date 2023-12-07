import mysql.connector
connection = mysql.connector.connect(user = 'root', password = '123456',host = 'localhost')
cursor = connection.cursor()
query = "CREATE TABLE `test`.`test_table1` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`City` VARCHAR(45) NULL,`Title` VARCHAR(45) NULL,PRIMARY KEY (`ID`))"
query_insert1 = "INSERT INTO `test`.`test_table` (`ID`, `Name`, `City`, `Title`) VALUES ('2', 'Trình', 'Quảng Bình', 'huhu');"
query_delete = "delete from `test`.`test_table` where id = '1'"
query_insert2 = "insert into `test`.`test_table` (`ID`, `Name`, `City`, `Title`) VALUES (%s,%s,%s,%s);"
queryy = "CREATE TABLE `crawl_data`.`job_data` (`id` INT AUTO_INCREMENT,`Title` VARCHAR(255),`Company_Name` VARCHAR(255),`Place` VARCHAR(255),`Deadline` VARCHAR(255),`Experience` VARCHAR(255),`Level` VARCHAR(255),`Salary` VARCHAR(255),`Education` VARCHAR(255),`Description` VARCHAR(1000),`Requirement` VARCHAR(1000),`Number_Employee` VARCHAR(255),`Source_Picture` VARCHAR(255),PRIMARY KEY (id));"
cursor.execute(queryy)
