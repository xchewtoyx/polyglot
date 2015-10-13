from torrent.bencode import Decoder

def loads(bencode_string):
    decoder = Decoder()
    return decoder.decode(bencode_string)
