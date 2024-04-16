import mysql.connector
connection = mysql.connector.connect(user = 'root', password = '123456',host = 'localhost')
cursor = connection.cursor()
queryy = "CREATE TABLE `crawl_data`.`TTNT_Task` (`Id` INT AUTO_INCREMENT,`Title` VARCHAR(255),`Company_Name` VARCHAR(255),`Time` VARCHAR(255),`City` VARCHAR(255),`Age` VARCHAR(255),`Sexual` VARCHAR(255),`Probation_Time` VARCHAR(255),`Work_Way` VARCHAR(255),`Job` VARCHAR(255),`Place` VARCHAR(255),`Number_Employee` VARCHAR(255),`Experience` VARCHAR(255),`Level` VARCHAR(255),`Salary` VARCHAR(255),`Education` VARCHAR(255),`Right` TEXT,`Description` TEXT,`Requirement` TEXT,`Deadline` VARCHAR(255),`Source_Picture` VARCHAR(255),PRIMARY KEY (id));"
cursor.execute(queryy)
