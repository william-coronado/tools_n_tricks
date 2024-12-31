from faker import Faker
from faker.providers import BaseProvider
from rich import print
fake = Faker('en_AU')

# Create a user profile
def generate_user():
    Faker.seed(42)
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "job": fake.job(),
        "company": fake.company(),
        "credit_card": fake.credit_card_number()
    }

# Generate multiple users
users = [generate_user() for _ in range(5)]
print("Generated AU users:")
print(users)

# Use specific locales
fake_fr = Faker('fr_FR')
french_user = {
    "name": fake_fr.name(),
    "address": fake_fr.address()
}
print("Generated French user:")
print(french_user)

# Create custom providers
class CustomProvider(BaseProvider):
    def custom_value(self):
        return fake.random_element(['A', 'B', 'C'])

fake.add_provider(CustomProvider)