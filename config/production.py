from dotenv import load_dotenv
from config.default import *

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('viking'),
    pw=os.getenv('dkagh1.'),
    url=os.getenv('localhost'),
    db=os.getenv('board'))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe0\xd3x9\xfe\xbb\x14J\xd8\xf6\xff\xae\x19\xed\xac\x04'