class tdf:
    def __init__(self, f):
        self.fonts = []
        f.read(1)       # character 19
        if f.read(18) == b"TheDraw FONTS file"

class font:
    def __init__(self):
        self.font_name_length = None
        self.font_name = None
        self.font_type = None
        self.letter_spacing = None
        self.block_size = None
        self.characters_define = None
        self.data = None

f = open("pittyx.tdf", "rb")
loaded = tdf(f)
print(r[25:25+12])
f.close()

"""
for b in r:
    print(b)
"""