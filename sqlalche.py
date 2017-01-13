#-*- coding:utf8 -*-


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
    id = Column(Integer, primary_key=True)
    name = Column(Integer())
    fullname = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                        self.name, self.fullname, self.password)



if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine("mysql://root:root@192.168.1.88/tornadodb",encoding='utf8', echo=True)
    Base.metadata.create_all(engine)

