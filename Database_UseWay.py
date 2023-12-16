import mysql.connector
connection = mysql.connector.connect(user = 'root', password = '123456',host = 'localhost')
cursor = connection.cursor()
queryy = "CREATE TABLE `crawl_data`.`job_data` (`Id` INT AUTO_INCREMENT,`Title` VARCHAR(255),`Company_Name` VARCHAR(255),`Job` VARCHAR(255),`Place` VARCHAR(255),`Number_Employee` VARCHAR(255),`Experience` VARCHAR(255),`Level` VARCHAR(255),`Salary` VARCHAR(255),`Education` VARCHAR(255),`Description` VARCHAR(2000),`Requirement` VARCHAR(2000),`Deadline` VARCHAR(255),`Source_Picture` VARCHAR(255),PRIMARY KEY (id));"
cursor.execute(queryy)
