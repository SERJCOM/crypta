from blockchain2 import block

b = block()
flag = 0

def set_flag_menu():
    menu_flag = int(input("введи номер: 1 - настройка, 0 - майнинг"))
    return menu_flag
    
flag = set_flag_menu()

private_key = 0
public_key = 0
while True:
    if flag == 1:
        private_key = b.generate_private_key()
        public_key = b.generate_public_key(private_key)
        flag = 0
    if flag == 0:
        b.open_block()
        b.input_text(public_key)
        b.sign_block(private_key)
        b.edit_transaction()
        b.previos_hash()
        b.sign_block(private_key)
        b.edit_nonse()
        b.hash_block()
        b.write()
    #b.verify_block(public_key, 14)
    b.sbros()
    
    print("БЛОК СОЗДАН")