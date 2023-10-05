pip install python-dotenv

create  .env file in root directory and add .env in git ignore

# create secure secret key
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())


--------------------------------------------settings.py-----------------------------------------

from dotenv import load_dotenv
load_dotenv()
import ast

SECRET_KEY = str(os.getenv('SECRET_KEY'))
DEBUG = (ast.literal_eval(os.getenv('DEBUG')))
