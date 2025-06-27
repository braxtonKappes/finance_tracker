from passlib.context import CryptContext

# Create the password context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Replace this with the password you want to hash
plain_password = "my_secure_password"

# Generate the hashed password
hashed_password = pwd_context.hash(plain_password)

# Output the result
print(f"Plain Password: {plain_password}")
print(f"Hashed Password: {hashed_password}")
