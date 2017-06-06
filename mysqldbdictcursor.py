import MySQLdb.cursors
MySQLdb.connect(host='...', cursorclass=MySQLdb.cursors.DictCursor)

###

import MySQLdb
db = MySQLdb.connect(host='...', db='...', user='...t', passwd='...')

list_cursor = db.cursor()
dict_cursor = db.cursor(MySQLdb.cursors.DictCursor)
