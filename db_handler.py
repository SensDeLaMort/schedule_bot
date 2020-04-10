import sqlite3


class Handler:
	conn = None
	c = None

	def __init__(self):
		self.conn = sqlite3.connect('users.db', check_same_thread = False)
		self.c = self.conn.cursor()


	def get_user(self, id):
		sql_query = 'SELECT * FROM users WHERE id={0}'.format(id)
		self.c.execute(sql_query)
		return(self.c.fetchone())


	def add_user(self, id, group, sub, faculty):
		sql_query = 'INSERT INTO users ("id", "group", "sub", "faculty") VALUES ({0}, {1}, {2}, "{3}")'.format(id, group, sub, faculty)
		self.c.execute(sql_query)
		self.conn.commit()
