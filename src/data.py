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

	query_direct('''
		CREATE TABLE IF NOT EXISTS work_ad (
			owner_wallet_id VARCHAR(128) PRIMARY KEY,
			name VARCHAR(256) NOT NULL,
			img VARCHAR(256) NOT NULL,
			est_price INT NOT NULL
		);
	''')
		
	query_direct('''
		CREATE TABLE IF NOT EXISTS orders (
			work_ad_id INT PRIMARY KEY,
			user_wallet_id VARCHAR(128) NOT NULL,
			response INT DEFAULT NULL
		);
    ''')

	db_commit()

def _user_exists(wallet_id):
	return query_get_count("SELECT COUNT(*) FROM users WHERE wallet_id = ?", (wallet_id, )) == 1

def _work_ad_exists(work_ad_id):
	return query_get_count("SELECT COUNT(*) FROM work_ad WHERE id = ?", (work_ad_id, )) == 1

def _order_exists(order_id):
	return query_get_count("SELECT COUNT(*) FROM orders WHERE id = ?", (order_id, )) == 1

def user_link_wallet(wallet_id, is_designer):
	if not _user_exists(wallet_id):
		query("INSERT INTO users (wallet_id, user_name, user_address, user_is_designer) VALUES (?, ?, ?, ?)", (wallet_id, "", "", int(is_designer)))
		db_commit()

	# otherwise, do nothing

	return { "status": "ok" }

def user_set_info(wallet_id, user_name, user_address):
	if not _user_exists(wallet_id):
		return { "error": "there is no account with this wallet" }

	query("UPDATE users SET user_name = ?, user_address = ? WHERE wallet_id = ?", (user_name, user_address, wallet_id))
	db_commit()

	return { "status": "ok" }

def user_get_info(wallet_id):
	if not _user_exists(wallet_id):
		return { "error": "there is no account with this wallet" }
	
	return query_get("SELECT user_name, user_address FROM users WHERE wallet_id = ?", (wallet_id, ))

def designer_create_work_ad(wallet_id, name, description, img, price):
	if not _user_exists(wallet_id):
		return { "error": "there is no account with this wallet" }
	
	query("INSERT INTO work_ad (owner_wallet_id, name, description, img, est_price) VALUES (?, ?, ?, ?, ?)", (wallet_id, name, description, img, price))

	return { "status": "ok" }

def designer_delete_work_ad(wallet_id, work_ad_id):
	query("DELETE FROM work_ad WHERE owner_wallet_id = ? AND id = ?", (wallet_id, work_ad_id))

	return { "status": "ok" }

def user_create_work_item(wallet_id, work_ad_id):
	if not _user_exists(wallet_id):
		return { "error": "there is no account with this wallet" }

	if not _work_ad_exists(work_ad_id):
		return { "error": "there is no work ad with this id" }

	query("INSERT INTO work_items (work_ad_id, user_wallet_id) VALUES (?, ?)", (work_ad_id, wallet_id))

	return { "status": "ok" }

def designer_respond_to_work_item(designer_wallet_id, work_order_id, will_do_the_work_boolean):
	if not _user_exists(designer_wallet_id):
		return { "error": "there is no account with this wallet" }

	if not _order_exists(work_order_id):
		return { "error": "there is no order with this id" }
	
	query("UPDATE orders SET response = ? WHERE id = ?", (will_do_the_work_boolean, work_order_id))

	return { "status": "ok" }

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