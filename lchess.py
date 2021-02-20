import re
coord  = r'([a-h][1-8])'
pawn   = r'^' + coord + '$' # regular pawn move. Ex: e4
knight = r'^N' + coord + '{1,2}$' # regular knight move
bishop = r'^B' + coord + '{1,2}$' # regular bishop move
rook   = r'^R' + coord + '{1,2}$' # regular rook move
queen   = r'^Q' + coord + '{1,2}$' # regular queen move
king   = r'^K' + coord + '{1,2}$' # regular king move
test = input()

if (re.match(pawn, test) != None):
    print("Regular pawn move: " + re.match(pawn, test).string)
elif (re.match(knight, test)):
    print("Regular knight move: " + re.match(knight, test).string)
elif (re.match(bishop, test)):
    print("Regular bishop move: " + re.match(bishop, test).string)
elif (re.match(rook, test)):
    print("Regular rook move: " + re.match(rook, test).string)
elif (re.match(queen, test)):
    print("Regular queen move: " + re.match(queen, test).string)
elif (re.match(king, test)):
    print("Regular king move: " + re.match(king, test).string)
else:
    print("Not recognized")