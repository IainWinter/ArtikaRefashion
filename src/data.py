from database import *

def init_tables():
	query_direct('''
        CREATE TABLE IF NOT EXISTS users (
			user_wallet_id  VARCHAR(128) PRIMARY KEY AUTOINCREMENT,
			user_name       VARCHAR(256) NOT NULL,
			user_address    VARCHAR(512) NOT NULL
        );
    ''')

	db_commit()

def _user_get_count(wallet_id):
	return query_get_count("SELECT COUNT(*) FROM users WHERE user_wallet_id = ?", (wallet_id, ))

def user_create(wallet_id):
	# make sure that the user doesnt exist
	if _user_get_count(wallet_id) == 1:
		return { "error", "account already exists" }

	query("INSERT INTO users (user_wallet_id, user_name, user_address) VALUES (?, ?, ?)", (wallet_id, "", ""))

	return { "status", "ok" }

def user_set_info(wallet_id, user_name, user_address):
	# make sure that the user does exist
	if _user_get_count(wallet_id) == 0:
		return { "error", "there is no account with this wallet" }

	query("UPDATE users SET user_name = ?, user_address = ? WHERE wallet_id = ?", (user_name, user_address, wallet_id))

	return { "status", "ok" }

# assumes that the session_id is the first arg in the list 'args'
def with_session(func, args):
	user_id = get_user_id_from_session_token(args[0])
	if user_id == -1: 
		return { "error": "invalid session" }

	# replace session_id with user_id, to use list expansion
	args[0] = user_id
	return func(*args)

def print_all_tables():
	users          = query_get("SELECT * FROM users", ())
	categories     = query_get("SELECT * FROM categories", ())
	blocks         = query_get("SELECT * FROM blocks", ())
	block_notes    = query_get("SELECT * FROM block_notes", ())
	session_tokens = query_get("SELECT * FROM session_tokens", ())

	print(users)
	print(categories)
	print(blocks)
	print(block_notes)
	print(session_tokens)