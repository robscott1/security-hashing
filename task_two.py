import base64
from time import time

import bcrypt as bcrypt

from HashObject import HashObject
from nltk.corpus import words
import nltk

class PasswordTool:

    def __init__(self, file):
        self.file = file
        self.hashes = self.read_file()
        self.groups_by_salt = self.group_by_salt()
        self.words_list = list(filter(lambda x: 10 >= len(x) >= 6, words.words()))

    def run(self):
        self.crack()
        print("\nResults...")
        for h in self.hashes:
            print(f"{h.user} --> {h.cracked_word}")

    def crack(self):
        start = time()
        for group in self.groups_by_salt.values():
            for word in self.words_list:
                for hash_obj in group:
                    real_hash = f"$2b${hash_obj.work_factor}$" \
                                f"{hash_obj.salt}" \
                                f"{hash_obj.hash_value}"
                    my_hash = self._hash(hash_obj, word).decode("utf-8")
                    if real_hash == my_hash:
                        end = time()
                        print(f"Hash hit: {hash_obj.user} --> {word} ({end - start})")
                        hash_obj.cracked_word = word
                        start = time()




    def group_by_salt(self):
        result = {}
        for h in self.hashes:
            if h.salt not in result:
                result[h.salt] = [h]
            else:
                hash_list = result.get(h.salt)
                hash_list.append(h)
        return result

    def _hash(self, hash_obj, word):
        salt = f"$2b${hash_obj.work_factor}${hash_obj.salt}".encode()
        word = bytes(word.encode())
        pw = bcrypt.hashpw(word, salt)

        return pw


    def read_file(self):
        hashes = []
        with open(self.file, 'r') as r:
            line = r.readline()
            while line:
                hash_obj = HashObject.process_txt(line)
                hashes.append(hash_obj)
                line = r.readline()
        return hashes





if __name__ == "__main__":
    tool = PasswordTool("shadow-file")
    tool.run()