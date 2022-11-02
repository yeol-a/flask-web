from dotenv import load_dotenv
from config.default import *

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    db=os.getenv('DB_NAME'))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe0\xd3x9\xfe\xbb\x14J\xd8\xf6\xff\xae\x19\xed\xac\x04'