from environs import Env

env = Env()
env.read_env()

API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")
ID_ARCHIVE = env.str("ID_ARCHIVE")
