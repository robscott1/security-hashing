import base64


class HashObject:

    def __init__(self, user, work_factor, salt, hash_value):
        self.user = user
        self.work_factor = work_factor
        self.salt = salt
        self.hash_value = hash_value
        self.cracked_word = None

    @classmethod
    def process_txt(cls, txt):
        txt = txt.rstrip("\n")
        blocks = txt.split("$")
        user = blocks[0]
        work_factor = blocks[2]
        salt, hash_value = blocks[3][:22], blocks[3][22:]
        processed_txt = {
            "user": user,
            "work_factor": work_factor,
            "salt": salt,
            "hash_value": hash_value
        }
        return HashObject(**processed_txt)

    def set_cracked_word(self, word):
        self.cracked_word = word



