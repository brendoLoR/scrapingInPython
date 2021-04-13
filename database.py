import mysql.connector

def connect(db):
    mysqldb = mysql.connector.connect(
        host = 'localhost',
        database = db,
        user = 'root',
        charset = 'utf8'
    )

    return mysqldb

def close(db):
    db.close()

def insert(db, table, columns, values):
    mysqldb = connect(db)
    dbcursor = mysqldb.cursor()
    sql = "INSERT IGNORE INTO "+str(table).replace("\'", "")+" "+str(columns).replace("\'", "")+" VALUES (%s, %s, %s, %s)"
    val = values
    dbcursor.execute(sql, val)
    mysqldb.commit()

    return dbcursor.lastrowid

"""
CREATE TABLE `scrapingdb`.`jobs_offers` ( `JOB_ID` INT NOT NULL AUTO_INCREMENT COMMENT 'PRIMARY KEY' ,
`SITE_ID` INT NOT NULL DEFAULT '0' COMMENT 'KEY OF SITE ID ON SITE_TEBLE' , `COMPANY_NAME` TEXT CHARACTER
SET ascii COLLATE ascii_general_ci NULL DEFAULT NULL COMMENT 'COMPANY NAME OF JOB OFFER' ,
`SKILLS` TEXT CHARACTER SET armscii8 COLLATE armscii8_general_ci NULL DEFAULT NULL , `PUBLISHED_DATE` DATETIME NOT NULL
DEFAULT CURRENT_TIMESTAMP , `APPLY_LINK` TEXT NULL DEFAULT NULL COMMENT 'LINK TO APPLY BUTTON' ,
PRIMARY KEY (`JOB_ID`, `SITE_ID`)) ENGINE = InnoDB;

CREATE TABLE `scrapingdb`.`site_table` ( `SITE_ID` INT NOT NULL AUTO_INCREMENT COMMENT 'SITE_ID' ,
`SITE_NAME` TEXT NOT NULL , `SITE_LINK` TEXT NOT NULL , `SITE_TAGS` TEXT CHARACTER SET armscii8 
COLLATE armscii8_general_ci NOT NULL , `SITE_CLASSES` TEXT CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL ,
`SITE_KEYWORD` TEXT CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL , PRIMARY KEY (`SITE_ID`)) ENGINE = InnoDB; 
"""