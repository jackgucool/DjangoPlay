__author__ = 'yiminggu'

import MySQLdb


class mydb:
    host    =   "localhost"
    user    =   "testuser"
    passwd  =   "testpass"
    db    =   "test"

    def __init__(self):
        self.connection = MySQLdb.connect(
            host = self.host,
            user = self.user,
        )
