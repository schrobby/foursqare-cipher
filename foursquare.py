# foursquare.py

class Cipher:
    def __init__(self, *keys):
        self.tables = self._make_tables(keys)

    def _make_tables(self, keys):
        alphabet = 'abcdefghiklmnopqrstuvwxyz'  # exclude 'j'
        keys = keys[:4]

        # remove repeated letters from keys
        keys = [''.join(dict.fromkeys(key)).lower() for key in keys]

        tables = [alphabet] * 4
        for i, key in enumerate(keys):
            tables[i] = key + ''.join(filter(lambda char: char not in key, alphabet))

        return tables

    def _find_position(self, char, table):
        pos = table.find(char)
        return (pos//5, pos%5)

    def _find_char(self, row, col, table):
        pos = 5*row + col
        return table[pos]

    def _crypt(self, lookup):
        ciphertext = self.ciphertext.lower()
        ciphertext = ciphertext + 'z' if len(ciphertext) % 2 else ciphertext

        # split ciphertext into brigrams
        bigrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

        cleartext = ''
        for gram in bigrams:
            row1, col1 = self._find_position(gram[0], self.tables[lookup[0]])
            row2, col2 = self._find_position(gram[1], self.tables[lookup[1]])

            cleartext += self._find_char(row1, col2, self.tables[lookup[2]])
            cleartext += self._find_char(row2, col1, self.tables[lookup[3]])

        return cleartext

    def encrypt(self, ciphertext):
        self.ciphertext = ciphertext

        # set table lookup sequence to encrypt
        return self._crypt([0, 3, 1, 2])

    def decrypt(self, ciphertext):
        self.ciphertext = ciphertext

        # set table lookup sequence to decrypt
        return self._crypt([1, 2, 0, 3])


if __name__ == '__main__':
    fsquare = Cipher('OUTCAST', 'TWOFACED', 'GRUDGE')

    encode = fsquare.encrypt('aforecloud')
    print(encode)

    decode = fsquare.decrypt(encode)
    print(decode)
