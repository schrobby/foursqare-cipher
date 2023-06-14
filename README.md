# foursqare-cipher
Python implemention of the four-square cipher. Read the [article on Wikipedia](https://en.wikipedia.org/wiki/Four-square_cipher) if you want to learn more.

## Usage
This package runs without any dependencies whatsoever. 
```
import foursquare

cipher = foursquare.Cipher('DIDNT', 'READ', 'TLDR')
encode = cipher.encrypt('secretmessage')
decode = cipher.decrypt(decode)
```

Unlike the reference implementation on Wikipedia, up to 4 keys can be provided when creating a `Cipher` object. If you would only like to encode the 2nd and 3rd alphabet table, set the corresponding argument to an empty string:
```
cipher = foursquare.Cipher('', 'READ', 'TLDR', '')
```
