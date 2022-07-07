import struct

class ImuSample:
    PACK_FORMAT = '<hhh'
    PACK_SIZE = 6

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @classmethod
    def from_bytes(cls, b):
        x, y, z = struct.unpack_from(ImuSample.PACK_FORMAT, b)
        return cls(x=x, y=y, z=z)

    def get_xyz(self):
        return self.__x, self.__y, self.__z

    def __bytes__(self):
        buffer = bytearray(ImuSample.PACK_SIZE)
        struct.pack_into(
            ImuSample.PACK_FORMAT,
            buffer, 0,
            self.__x, self.__y, self.__z
        )
        return bytes(buffer)

    def __str__(self):
        # return f'({self.__x}, {self.__y}, {self.__z})'
        return f'{self.get_xyz()}'


# unit test
if __name__ == "__main__":
    d = ImuSample.from_bytes(b'\x01\x02\x03\x04\x05\x06')
    print(d)