from pydantic import BaseModel

class Catalog(BaseModel):
    id = int
    nama_produk = str
    brand = str
    tahun_rilis = str
    prosesor = str
    penyimpanan = str
    ram = str
    ukuran_layar = str
    harga = str
    image = str

    class Config:
        orm_mode = True