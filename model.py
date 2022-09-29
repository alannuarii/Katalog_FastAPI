from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base

class Catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_produk = Column(String(50))
    brand = Column(String(20))
    tahun_rilis = Column(String(5))
    prosesor = Column(String(20))
    penyimpanan = Column(String(20))
    ram = Column(String(10))
    ukuran_layar = Column(String(20))
    harga = Column(String(20))
    image = Column(String(30))

    def __repr__(self):
        return self.nama_produk