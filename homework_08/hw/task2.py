"""
Write a wrapper class TableData for database table, that when initialized with database name and table acts as
collection object (implements Collection protocol). Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
len(presidents) will give current amount of rows in presidents table in database
presidents['Yeltsin'] should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in table changed after you created collection
instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record, then go
to the next one, until records are exhausted. When writing tests, it's not always neccessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file.
"""
import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def __contains__(self, value):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT COUNT (*) FROM {} where name=:name".format(TableData.scrub(self.table_name)), {"name": value})
        (ln,) = self.cursor.fetchall()[0]
        self.conn.close()
        return ln > 0
    
    @staticmethod
    def scrub(table_name):
        return ''.join( chr for chr in table_name if chr.isalnum() )
    
    def __getitem__(self, item):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * from {} where name=:name".format(TableData.scrub(self.table_name))  , {"name": item})
        while row := self.cursor.fetchone():
            self.conn.close()
            return row

    def __iter__(self):
        """Probably not the optimal solution to close connection at the end of iterations,
        but maybe it will be enough to add notice of such behavior to documentation in order to avoid possible
        confusions. and give advise to user to call Instance.conn_close() if they not going to iterate
        until the end of table.
        """
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * from {}'.format(TableData.scrub(self.table_name)))
        colnames = self.cursor.description
        while row := self.cursor.fetchone():
            retdict = {}
            for i, col in enumerate(colnames):
                retdict[col[0]] = row[i]
            yield retdict
        self.conn.close()

    def __len__(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT COUNT (*) FROM {}'.format(TableData.scrub(self.table_name)))
        (ln,) = self.cursor.fetchall()[0]
        self.conn.close()
        return int(ln)

    def conn_close(self):
        self.conn.close()
