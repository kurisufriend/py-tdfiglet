#import discord

class tdf:
    def __init__(self):
        self.character_19 = None
        self.fix_string = None
        self.character_26 = None

class font:
    def __init__(self):
        self.font_name_length = None
        self.font_name = None
        self.font_type = None
        self.letter_spacing = None
        self.block_size = None
        self.characters_define = None


f = open("pittyx.tdf", "rb")
r = f.read()
f.close()
print(r[1:1+18])

"""
for b in r:
    print(b)
"""