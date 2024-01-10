schema="gans_simple"   # name of the database you want to use here
host="localhost"        # to connect to your local server
user="root"
password="THISISNOTAPASSWORD" # your password!!!!
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'