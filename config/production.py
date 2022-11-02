from dotenv import load_dotenv
from config.default import *

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('viking'),
    pw=os.getenv('dkagh1.'),
    url=os.getenv('localhost'),
    db=os.getenv('board'))