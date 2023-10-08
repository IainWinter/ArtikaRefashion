from database import *

def init_tables():
	query_direct('''
        CREATE TABLE IF NOT EXISTS users (
			wallet_id    VARCHAR(128) PRIMARY KEY,
			user_name    VARCHAR(256) NOT NULL,
			user_address VARCHAR(512) NOT NULL,
			user_is_designer INT NOT NULL
        );
    ''')

	db_commit()

def _user_get_count(wallet_id):
	return query_get_count("SELECT COUNT(*) FROM users WHERE wallet_id = ?", (wallet_id, ))

def user_link_wallet(wallet_id, is_designer):
	# if there is no account, create one
	if _user_get_count(wallet_id) == 0:
		query("INSERT INTO users (wallet_id, user_name, user_address, user_is_designer) VALUES (?, ?, ?, ?)", (wallet_id, "", "", int(is_designer)))
		db_commit()

	# otherwise, do nothing

	return { "status": "ok" }

def user_set_info(wallet_id, user_name, user_address):
	# make sure that the user does exist
	if _user_get_count(wallet_id) == 0:
		return { "error": "there is no account with this wallet" }

	query("UPDATE users SET user_name = ?, user_address = ? WHERE wallet_id = ?", (user_name, user_address, wallet_id))
	db_commit()

	return { "status": "ok" }

def user_get_info(wallet_id):
	# make sure that the user does exist
	if _user_get_count(wallet_id) == 0:
		return { "error": "there is no account with this wallet" }
	
	return query_get("SELECT user_name, user_address FROM users WHERE wallet_id = ?", (wallet_id, ))


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