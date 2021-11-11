from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData

user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'ormar_my_shop_db'

URL_DATA_BASE = (
    f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}"
)
metadata = MetaData()
database = Database(URL_DATA_BASE)
engine = create_engine(URL_DATA_BASE)
