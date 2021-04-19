import base64
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, block_size=16):
        if block_size < 2 or block_size > 255:
            raise AESCipher.InvalidBlockSizeError('The block size must be between 2 and 255, inclusive')
        self.block_size = block_size
        self.key = "2949382094230487"
        self.iv = 'dkghepfowntislqn'
        self.pad = ""

    def encrypt(self, raw):
        raw = self.__pad(raw) #Default zero based bytes[16]
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw.encode()))

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return self.__unpad(cipher.decrypt(enc).decode("utf-8")).strip(" ")

    def __pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

    @staticmethod
    def __unpad(s):
        return s[:-ord(s[len(s)-1:])]