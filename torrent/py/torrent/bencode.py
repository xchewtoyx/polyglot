class Decoder(object):
    def __init__(self):
        self.readers = {
            'i': self.read_int,
            'd': self.read_dict,
            'l': self.read_list,
        }
        for digit in range(10):
            self.readers[str(digit)] = self.read_str

    def decode(self, data):
        length, value = self.read_token(data)
        return value

    def read_dict(self, data):
        assert data[0] == 'd'
        pos = 1
        values = {}
        while data[pos] != 'e':
            length, key = self.read_str(data[pos:])
            pos += length
            length, value = self.read_token(data[pos:])
            pos += length
            values[key] = value
        return pos + 1, values

    def read_int(self, data):
        assert data[0] == 'i'
        final_pos = data.find('e')
        value = int(data[1:final_pos])
        length = final_pos + 1
        return length, value

    def read_list(self, data):
        assert data[0] == 'l'
        pos = 1
        values = []
        while data[pos] != 'e':
            length, value = self.read_token(data[pos:])
            pos += length
            values.append(value)
        return pos+1, values

    def read_str(self, data):
        sep = data.find(':')
        length = int(data[:sep])
        value = data[sep+1:sep+length+1]
        return sep+length+1, value

    def read_token(self, data):
        marker = data[0]
        return self.readers[marker](data)
