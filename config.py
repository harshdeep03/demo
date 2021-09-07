import pymysql
import aws_credentials as rds
conn = pymysql.connect(
        host= demodb.ctr1nhto2rau.ap-south-1.rds.amazonaws.com, #endpoint link
        port = 3306, # 3306
        user = admin, # admin
        password = 12345678, #adminadmin
        db = demodb, #test
        
        )
