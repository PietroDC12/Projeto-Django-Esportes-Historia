from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

#cd ./scripts/
#python secret_key_generator.py
#copiar o resultado e colar em .env