import mysql.connector
from venv import logger

def save_data_into_DB(data):
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost')
        cursor = connection.cursor()
        query = "INSERT INTO `crawl_data`.`job_data` (`Title`, `Company_Name`, `Place`, `Deadline`, `Experience`, `Level`, `Salary`, `Education`, `Description`, `Requirement`, `Number_Employee`, `Source_Picture`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in data:
            cursor.execute(query, i)
        connection.commit()
        connection.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")