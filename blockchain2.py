# This is the second version of my own blockchain

import os
import hashlib
import json
import binascii
import ecdsa
import base64
  
class block:
    transaction = []
    block = 0
    dict_transaction = 0
    def generate_private_key(self):
        private_key = ecdsa.SigningKey.generate(curve = ecdsa.SECP256k1)
        private_key_hex = binascii.hexlify(private_key.to_string()).decode("ascii")
        print(private_key_hex)
        return private_key_hex
    def generate_public_key(self, private_key_hex):
        private_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key()
        public_key_hex = binascii.hexlify(public_key.to_string()).decode("ascii")
        print(public_key_hex)
        return public_key_hex
    def verify_block(self, public_key, index):
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1) # the default is sha1
        BLOCK = self.open_block(index, True)
        block_transaction = {"adress1": BLOCK["block"]["transaction"]["adress1"], "amount": BLOCK["block"]["transaction"]["amount"], "adress2": BLOCK["block"]["transaction"]["adress2"]}
        mes = block_transaction
        user_data = json.dumps(mes).encode('utf-8')
        hashcode=hashlib.sha256(user_data).hexdigest()
        sig  = bytes(BLOCK["block"]["transaction"]["signature"], encoding='utf-8')
        data = base64.b64decode(sig)
        
        return vk.verify(data, bytes.fromhex(hashcode))

    def sign_block(self, private_key_hex):
        private_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
        public_key = private_key.get_verifying_key()
        sign_block = {"adress1": self.dict_transaction["adress1"], "amount": self.dict_transaction["amount"], "adress2": self.dict_transaction["adress2"]}
        sign_data = json.dumps(sign_block).encode('utf-8')
        hashcode=hashlib.sha256(sign_data).hexdigest()
        sig = private_key.sign(bytes.fromhex(hashcode))
        encoded = base64.b64encode(sig)
        str_sign_transaction = encoded.decode('UTF-8')
        #data = base64.b64decode(encoded)    -   возвращение записи к бинарнику
        self.dict_transaction['signature'] = str_sign_transaction 
    def len_index(self):
        self.len_index =  len(os.listdir(path="./blocks/"))
        print(self.len_index)
    def input_text(self, public_key):
        transaction_text = input().split(" ")
        self.dict_transaction = {"adress1":public_key, "amount": int(transaction_text[0]), "adress2": transaction_text[1], "signature":0}
        
    def open_block(self, index = 0, MODE=False):
        with open("blocks/" + str(index), "r") as read_file:
            data = json.load(read_file)
        if MODE == False:
            self.block = data
        else:
             return data   
    def write(self):
        len_index = len(os.listdir(path="./blocks/"))
        self.block["block"]["index"] = len_index
        with open("blocks/" + str(len_index), "w") as write_file:
            json.dump(self.block, write_file)
    def prov_len(self):
        if len(self.transaction) == 3:
            return False
        else:
            return True
    def edit_transaction(self):
        self.block["block"]["transaction"] = self.dict_transaction
    def hash_block(self, option = False):
        hash_object = hashlib.sha256(str(self.block["block"]).encode())
        if option == 0:
            self.block["hash"] = str(hash_object.hexdigest())
        else:
            return str(hash_object.hexdigest())
    def previos_hash(self):
        len_index = len(os.listdir(path="./blocks/")) - 1
        with open("blocks/" + str(len_index), "r") as read_file:
            data = json.load(read_file)
        self.block["block"]["previos_hash"] = data["hash"]
    def edit_nonse(self):
        i = 0
        len_hash = 2
        while True:
            i = i + 1
            self.block["block"]["nonse"] = i
            if self.hash_block(True)[0:len_hash:1] == "0" * len_hash:
                break
    def sbros(self):
        self.transaction = []
        self.block = 0
        self.len_index = ""
        
# b = block()
# while True:
#     b.open_block()
#     while b.prov_len():  
#         b.input_text()
#     b.edit_transaction()
#     b.edit_nonse()
#     b.previos_hash()
#     b.hash_block()
#     b.write()
#     b.sbros()
#     print("БЛОК СОЗДАН")
    
