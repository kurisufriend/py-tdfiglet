import sys

_CHARLIST= "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";



def char_lookup(c, font):
    for i in range(0, len(_CHARLIST) - 1):
        if _CHARLIST[i] == c and not(font.characters_define[i] == [b'0xFF', b'0xFF']):
            return i
    return None


class font:
    def __init__(self):
        self.font_name_length = None
        self.font_name = None
        self.font_type = None
        self.letter_spacing = None
        self.block_size = None
        self.characters_define = None
        self.data = None

class tdf:
    def __init__(self, f):
        self.fonts = []
        f.read(1) # character 19
        if not(f.read(18) == b"TheDraw FONTS file"): # fix string
            print("file is seemingly invalid")
            sys.exit(1)
        f.read(1) # character 26
#        while True: # just one for nao
        if not(f.read(4) == b'U\xaa\x00\xff'): # fix string
            return
        construction = font()
        construction.font_name_length = f.read(1)
        construction.font_name = f.read(12).decode("ascii")
        f.read(4)
        construction.font_type = f.read(1)
        construction.letter_spacing = f.read(1)
        construction.block_size = int.from_bytes(f.read(2), byteorder="little")
        construction.characters_define = [f.read(188)[x:x+5] for x in range(0, 188,2)]
        construction.data = f.read(construction.block_size)
        self.fonts.append(construction)



f = open("pittyx.tdf", "rb")
loaded = tdf(f)
f.close()

print(loaded.fonts[0].block_size)