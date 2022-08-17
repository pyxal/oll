#!/bin/bash/python3

hlp = """
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CFOP-OLL Trainer V3.0                                         #
# Made by Pyxal                                                 #
#                                                               #
# Recap: train cases one after another without reoccurrence     #
# Training: train cases with random occurrence                  #
#                                                               #
# All cases selected in recap mode by default                   #
# Arguments can be parsed to train the corresponding cases      #
# in training mode:                                             #
#                                                               #
#    Arg                 Description                            #
#                                                               #
#    Sune                All edges oriented cases               #
#    T                   T-shape cases                          #
#    Squares             Square cases                           #
#    Corners             All Cornors oriented cases             #
#    Lightning           Lightning cases                        #
#    P                   P-shape cases                          #
#    C                   C-shape cases                          #
#    Fish                Fish-shape cases                       #
#    L                   L-shape cases                          #
#    W                   W-shape cases                          #
#    I                   I-shape cases                          #
#    Knights             Knight Move cases                      #
#    Awkward             Awkward-shape cases                    #
#    Dot                 Dot cases                              #
#    1 - 57              Specific case                          #
#                                                               #
#    Train               switch to training mode                #
#                        with all cases                         #
#                                                               #
#    Gallery             show case gallery (not windows)        #
#                        combineable with other args            #
#                        to show corresponding cases            #
#                                                               #
#                                                               #
# While training, the following inputs can be used:             #
#                                                               #
#    a, alg              show alg                               #
#    c, case             show case (not windows)                #
#    h, help             show this help message                 #
#    e, exit             exit                                   #
#                                                               #
#                                                               #
# Idea and scrambles borrowed from bestsiteever.ru/oll          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

# imports
from platform import machine
from random import choice, sample
from sys import argv


def main():
    # help message
    if len(argv) == 2:
        if argv[1] == 'help':
            print(hlp)
            exit()


    print("\n\nOLL trainer\n\n")

    mode = setMode()

    if mode == 'recap':
        cases = caseSelection(mode, 'all')
        modes.recap(cases)
        modes.training(cases)

    elif mode == 'training':
        cases = caseSelection(mode, argv[1])
        modes.training(cases)

    elif mode == 'gallery':
        cases = caseSelection(mode, 'all') if len(argv) == 2 else caseSelection(mode, argv[2])
        modes.gallery(cases)


# user input
def userInput(case):
    while True:
        try:
            userInput = input()
            if userInput == '': break
            elif userInput in ['a', 'alg', 'algorithm', 'solution', 'tell']: print(ollCases[case][0])
            elif userInput in ['c', 'case']: caseDraw.drawOllCase(ollCases[case][1])
            elif userInput in ['h', 'help']: print(hlp)
            elif userInput in ['e', 'exit', 'q', 'quit']: exit()
            else: print("\nDidn't understand input\n(a)lg, (c)ase, (e)xit")
        except KeyboardInterrupt: exit()


# case selection
def caseSelection(mode, arg):
    caseObj = []
    
    if len(argv) == 1:                                                      caseObj = ['All', scramble.randomize(mode, ollScrambles)]
    elif arg.lower() in ['sune', 'sunecases', 'edges', 'edgesoriented']:    caseObj = ['Sune', scramble.randomize(mode, caseGroups['edgesOriented'])]
    elif arg.lower() in ['t', 'tcases', 'tcase']:                           caseObj = ['T-shape', scramble.randomize(mode, caseGroups['tCases'])]
    elif arg.lower() in ['squares', 'square', 'squarecases']:               caseObj = ['Square', scramble.randomize(mode, caseGroups['squareCases'])]
    elif arg.lower() in ['corners', 'corner', 'cornersoriented']:           caseObj = ['Oriented corner', scramble.randomize(mode, caseGroups['cornersOriented'])]
    elif arg.lower() in ['lightning', 'lightningcases', 'lightningcase']:   caseObj = ['Lightning', scramble.randomize(mode, caseGroups['lightningCases'])]
    elif arg.lower() in ['p', 'pcases', 'pcase']:                           caseObj = ['P-shape', scramble.randomize(mode, caseGroups['pCases'])]
    elif arg.lower() in ['c', 'ccases', 'ccase']:                           caseObj = ['C-shape', scramble.randomize(mode, caseGroups['cCases'])]
    elif arg.lower() in ['fish', 'fishcases', 'fishcase']:                  caseObj = ['Fish-shape', scramble.randomize(mode, caseGroups['fishCases'])]
    elif arg.lower() in ['l', 'lcases', 'lcase']:                           caseObj = ['L-shape', scramble.randomize(mode, caseGroups['lCases'])]
    elif arg.lower() in ['w', 'wcases', 'wcase']:                           caseObj = ['W-shape', scramble.randomize(mode, caseGroups['wCases'])]
    elif arg.lower() in ['i', 'icases', 'icase']:                           caseObj = ['I-shape', scramble.randomize(mode, caseGroups['iCases'])]
    elif arg.lower() in ['knight', 'knights', 'knightcases', 'knightcase']: caseObj = ['Knight Move', scramble.randomize(mode, caseGroups['knightMoveCases'])]
    elif arg.lower() in ['awkward', 'awkwardcases', 'awkwardcase']:         caseObj = ['Awkward-shape', scramble.randomize(mode, caseGroups['awkwardCases'])]
    elif arg.lower() in ['dot', 'dotcases', 'dotcase']:                     caseObj = ['Dot', scramble.randomize(mode, caseGroups['dotCases'])]
    
    else:
        try:
            if isinstance(int(arg), int) and int(arg) in range(1, 58):      caseObj = ['Specific', scramble.randomize(mode, [ollScrambles[int(arg)-1]])]
            else:                                                           caseObj = ['All', scramble.randomize(mode, ollScrambles)]
        except ValueError:                                                  caseObj = ['All', scramble.randomize(mode, ollScrambles)]


    return caseObj


# set mode
def setMode():
    
    mode = ''
    
    if len(argv) == 1: mode = 'recap'                                           # recap mode
    elif argv[1].lower() in ['gallery', 'gal', 'cases']: mode = 'gallery'       # gallery mode
    elif argv[1].lower() not in ['gallery', 'gal', 'cases']: mode = 'training'  # training mode
    
    return mode



# modes
class modes:
    
    # recap mode
    def recap(cases):
        print("Recap mode")
        for i, case in enumerate(cases[1]):
            alg = scramble.inverseScramble(ollScrambles[case][choice(range(1, len(ollScrambles[case])-1))])
            rotation = choice(["", "y", "y'", "y2"])
            fullAlg = scramble.applyRotationToAlg(alg, rotation)

            print(f"{len(cases[1])-(i)} case{'s' if i < len(cases[1]) -1 else ''} left")
            print(f"{fullAlg}")
            
            userInput(case)


    # training mode
    def training(cases):
        print("Training mode")
        
        if cases[0] == 'Specific': print(f"Case {cases[1][0]+1} selected\n")
        else: print(f"{cases[0]} cases selected\n")
        
        while True:
            case = choice(cases[1])
            alg = scramble.inverseScramble(ollScrambles[case][choice(range(1, len(ollScrambles[case])-1))])
            rotation = choice(["", "y", "y'", "y2"])
            fullAlg = scramble.applyRotationToAlg(alg, rotation)

            print(f"{fullAlg}")
            
            userInput(case)


    # gallery mode
    def gallery(cases):
        print("Case gallery")
        for i, case in enumerate(cases[1]):
            caseDraw.drawOllCase(ollCases[case][1])



# oll scramble management
class scramble:

    # randomize order
    def randomize(mode, algs):
        algSet = []
        for alg in algs: algSet.append(alg[0])
        if mode != 'gallery': return sample(algSet, len(algSet))
        else: return algSet
        


    # inverse scramble
    def inverseScramble(alg):
        result = ''

        for char in alg.split()[::-1]:

            if char[-1] == "2":
                result += char + ' '

            elif char[-1] == "'":
                result += char[:-1] + ' '

            elif char[-1] != "'":
                result += char + "' "

        return result.strip()


    # apply rotation to alg
    def applyRotationToAlg(alg, rotation):
        translateObj = {}

        if rotation == 'y':
            translateObj = {'R':'F','F':'L','L':'B','B':'R'}

        elif rotation == 'y':
            translateObj = {'R':'B','B':'L','L':'F','F':'R'}

        elif rotation == 'y2':
            translateObj = {'R':'L','L':'R','B':'F','F':'B'}

        return alg.translate(str.maketrans(translateObj))



# case draw 
class caseDraw:

    # draw black
    def block(r, g, b, text):
        return f'\033[38;2;{r};{g};{b}m{text}'

    # case generator
    def drawOllCase(colorPattern):
        if machine() != 'AMD64':
            for line in colorPattern:
                print(line)
        else: print("No casedrawing support for windows. F*** Windows!")

    # case pattern translator
    def translate(tile1, tile2, tile3):
        return colors['sp'] + colors['b'] + tile1 + colors['b'] + tile2 + colors['b'] + tile3 + colors['b'] + colors['w'] + colors['sp']



# colors
colors = {
    'b' : caseDraw.block(0, 0, 0, chr(0x2588))*2,
    'g' : caseDraw.block(64, 64, 64, chr(0x2588))*2,
    'y' : caseDraw.block(255, 241, 0, chr(0x2588))*2,
    'w' : caseDraw.block(255, 255, 255, '')*2,
    'gb' : caseDraw.block(64, 64, 64, chr(0x2588))*8,
    'yb' : caseDraw.block(255, 241, 0, chr(0x2588))*8,
    'gry' : caseDraw.block(64, 64, 64, chr(0x2588))*6+caseDraw.block(255, 241, 0, chr(0x2588))*2,
    'gry' : caseDraw.block(64, 64, 64, chr(0x2588))*6+caseDraw.block(255, 241, 0, chr(0x2588))*2,
    'ygr' : caseDraw.block(255, 241, 0, chr(0x2588))*2+caseDraw.block(64, 64, 64, chr(0x2588))*6,
    'sp' : ' '*4,
    'line' : (' '*4)+(caseDraw.block(0, 0, 0, chr(0x2588))*2)*16,
}

# case draw codes
caseDrawCodes = {
    'ggg' : caseDraw.translate(colors['gb'], colors['gb'], colors['gb']),
    'yyy' : caseDraw.translate(colors['yb'], colors['yb'], colors['yb']),
    'ggy' : caseDraw.translate(colors['gb'], colors['gb'], colors['yb']),
    'ygg' : caseDraw.translate(colors['yb'], colors['gb'], colors['gb']),
    'yyg' : caseDraw.translate(colors['yb'], colors['yb'], colors['gb']),
    'gyy' : caseDraw.translate(colors['gb'], colors['yb'], colors['yb']),
    'gyg' : caseDraw.translate(colors['gb'], colors['yb'], colors['gb']),
    'ygy' : caseDraw.translate(colors['yb'], colors['gb'], colors['yb']),
    'yygy' : caseDraw.translate(colors['yb'], colors['yb'], colors['gry']),
    'ygyy' : caseDraw.translate(colors['ygr'], colors['yb'], colors['yb']),
    'yggg' : caseDraw.translate(colors['ygr'], colors['gb'], colors['gb']),
    'gggy' : caseDraw.translate(colors['gb'], colors['gb'], colors['gry']),
    'gygy' : caseDraw.translate(colors['gb'], colors['yb'], colors['gry']),
    'ygyg' : caseDraw.translate(colors['ygr'], colors['yb'], colors['gb']),
    'yggy' : caseDraw.translate(colors['ygr'], colors['gb'], colors['yb']),
    'ygygy' : caseDraw.translate(colors['ygr'], colors['yb'], colors['gry']),
    'ygggy' : caseDraw.translate(colors['ygr'], colors['gb'], colors['gry']),
    'yggry' : caseDraw.translate(colors['yb'], colors['gb'], colors['gry']),
    'gygry' : caseDraw.translate(colors['gb'], colors['yb'], colors['gry']),
    'ygrgy' : caseDraw.translate(colors['ygr'], colors['gb'], colors['yb']),
    'ygryg' : caseDraw.translate(colors['ygr'], colors['yb'], colors['gb'])
}

# oll cases
ollCases = [
    # 1
    [
        "(R U2') (R2' F R F') U2' (R' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 1",
        caseDrawCodes['ygggy'] +                                            "Blank",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "(R U2') (R2' F R F') U2' (R' F R F')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "(R U2' R') (Sledge) U2' (Sledge)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['ygggy'] +    "",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'] +                    "",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 2
    [
        "F (R U R' U') F' f (R U R' U') f'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 2",
        caseDrawCodes['yggg'] +                                             "Zamboni",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'],
        colors['line'], caseDrawCodes['ygygy'] +                            "F (R U R' U') F' f (R U R' U') f'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "F (Sexy) S (Sexy) f'",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['yggg'] +     "y (r U r') U2 R U2' R' U2 (r U' r')",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 3
    [
        "f (R U R' U') f' U' F (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 3",
        caseDrawCodes['gggy'] +                                             "Anti-Nazi",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "f (R U R' U') f' U' F (R U R' U') F'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "f (sexy) f' U' (T)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['yggy'] +     "",
        caseDrawCodes['yggy'], caseDrawCodes['yggy'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 4
    [
        "f (R U R' U') f' U F (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 4",
        caseDrawCodes['yggy'] +                                             "Nazi",
        caseDrawCodes['yggy'], caseDrawCodes['yggy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "f (R U R' U') f' U F (R U R' U') F'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "f (Sexy) f' U (T)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['gggy'] +     "",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 5
    [
        "r' U2' R U R' U r",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 5",
        caseDrawCodes['gggy'] +                                             "Lefty-Square",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "r' U2' R U R' U r",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "Mirror of Righty-Square",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ygyy'] +      "",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 6
    [
        "r U2 R' U' R U' r'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 6",
        caseDrawCodes['ygyy'] +                                             "Righty-Square",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "r U2 R' U' R U' r'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "Wide Anti-Sune",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['gggy'] +      "",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 7
    [
        "r U R' U R U2' r'",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 7",
        caseDrawCodes['gygy'] +                                             "Lightning",
        caseDrawCodes['gygy'], caseDrawCodes['gygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "r U R' U R U2' r'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Wide Sune",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygg'] +       "",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 8
    [
        "r' U' R U' R' U2 r",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 8",
        caseDrawCodes['ygg'] +                                              "Reverse Lightning",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'],
        colors['line'], caseDrawCodes['yygy'] +                             "r' U' R U' R' U2 r",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Mirror of Lightning",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['gygy'] +      "y2 l' U' L U' L' U2 l",
        caseDrawCodes['gygy'], caseDrawCodes['gygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 9
    [
        "(R U R' U') R' F (R2 U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 9",
        caseDrawCodes['ygyg'] +                                             "Kite",
        caseDrawCodes['ygyg'], caseDrawCodes['ygyg'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R U R' U') R' F (R2 U R' U') F'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Starts as a T-perm",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ggy'] +       "",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 10
    [
        "(R U R' U) (R' F R F') (R U2' R')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 10",
        caseDrawCodes['ggy'] +                                              "Anit-Kite",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R U R' U) (R' F R F') (R U2' R')",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "(Su)(sledge)(ne)",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygyg'] +      "",
        caseDrawCodes['ygyg'], caseDrawCodes['ygyg'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 11
    [
        "r' (R2 U R' U R U2 R') U M'",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 11",
        caseDrawCodes['gggy'] +                                             "Downstairs",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "r' (R2 U R' U R U2 R') U M'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "M (Sune) U M'",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['yyg'] +       "",
        caseDrawCodes['yyg'], caseDrawCodes['yyg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 12
    [
        "M' (R' U' R U' R' U2 R) U' M",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 12",
        caseDrawCodes['yyg'] +                                              "Upstairs",
        caseDrawCodes['yyg'], caseDrawCodes['yyg'],
        colors['line'], caseDrawCodes['ygyy'] +                             "M' (R' U' R U' R' U2 R) U' M",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "M' (Sune-mirror) U' M",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['gggy'] +      "",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 13
    [
        "(r U' r' U') (r U r') (F’ U F)",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 13",
        caseDrawCodes['gggy'] +                                             "Gun",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(r U' r' U') (r U r') (F’ U F)",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygg'] +        "F U R U' R2' F' R U (R U' R')",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 14
    [
        "(r' U r U) (r' U' r) y (R U' R')",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 14",
        caseDrawCodes['yggg'] +                                             "Anti-Gun",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'],
        colors['line'], caseDrawCodes['yyy'] +                              "(r' U r U) (r' U' r) y (R U' R')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ggy'] +        "(R' F R) (U R' F' R) (F U' F')",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 15
    [
        "(r' U' r) (R' U' R U) (r' U r)",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 15",
        caseDrawCodes['gggy'] +                                             "Squeegee",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(r' U' r) (R' U' R U) (r' U r)",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['yggy'] +       "y2 l' U' l (L' U' L U) l' U l",
        caseDrawCodes['yggy'], caseDrawCodes['yggy'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 16
    [
        "(r U r') (R U R' U') (r U' r')",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 16",
        caseDrawCodes['yggy'] +                                             "Anti-Squeegee",
        caseDrawCodes['yggy'], caseDrawCodes['yggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(r U r') (R U R' U') (r U' r')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "r U r' (Sexy) r U' r'",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['gggy'] +       "",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 17
    [
        "(R U R' U) (R' F R F') U2' (R' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 17",
        caseDrawCodes['ygg'] +                                              "Slash",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'],
        colors['line'], caseDrawCodes['ygygy'] +                            "(R U R' U) (R' F R F') U2' (R' F R F')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "(R U R' U) (Sledge) U2' (Sledge)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['yggy'] +     "",
        caseDrawCodes['yggy'], caseDrawCodes['yggy'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 18
    [
        "(r U R' U) R U2 r2' U' R U' R' U2 r",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 18",
        caseDrawCodes['ygy'] +                                              "Crown",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "(r U R' U) R U2 r2' U' R U' R' U2 r",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "(Lightning) (Reversed Lightning)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['ggg'] +      "y R U2' (R2' F R F') U2' M' (U R U' r')",
        caseDrawCodes['ggg'], caseDrawCodes['ggg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 19
    [
        "M U (R U R' U') M' (R' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 19",
        caseDrawCodes['ygy'] +                                              "Bunny",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "M U (R U R' U') M' (R' F R F')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "M U (Sexy) M' (Sledge)",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['ygggy'] +    "",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'] +                    "",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 20
    [
        "(r U R' U') M2' (U R U' R' U') M'",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 20",
        caseDrawCodes['ygy'] +                                              "Checkers",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "(r U R' U') M2' (U R U' R' U') M'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "(Fat Sexy) M2' (Inverse Sexy) U' M'",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['ygy'] +      "M U (R U R' U') M2' (U R U' r')",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "M U (Sexy) M2' (fat insert), reverse of #1",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 21
    [
        "(R U R' U) (R U' R' U) (R U2' R')",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 21",
        caseDrawCodes['ygygy'] +                                            "Cross",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(R U R' U) (R U' R' U) (R U2' R')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Double Sune",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygygy'] +      "y (R U2 R') (U' R U R') (U' R U' R')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "Begins and ends the same as (anti-)sune",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 22
    [
        "R U2' R2' U' R2 U' R2' U2' R",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 22",
        caseDrawCodes['ygyg'] +                                             "Bruno",
        caseDrawCodes['ygyg'], caseDrawCodes['ygyg'],
        colors['line'], caseDrawCodes['yyy'] +                              "R U2' R2' U' R2 U' R2' U2' R",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Never release the R face. Do the U-moves with left hand",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygyg'] +       "",
        caseDrawCodes['ygyg'], caseDrawCodes['ygyg'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 23
    [
        "R2 D (R' U2 R) D' (R' U2 R')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 23",
        caseDrawCodes['yyy'] +                                              "Headlights",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'],
        colors['line'], caseDrawCodes['yyy'] +                              "R2 D (R' U2 R) D' (R' U2 R')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Push the D' with ringfinger",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['gyg'] +        "y2 R2' D' (R U2 R') D (R U2 R)",
        caseDrawCodes['gyg'], caseDrawCodes['gyg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 24
    [
        "(r U R' U') (r' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 24",
        caseDrawCodes['gyy'] +                                              "Chameleon",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(r U R' U') (r' F R F')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Sexy followed by Sledge starting with r's instad of R's",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['gyy'] +        "",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 25
    [
        "F' (r U R' U') r' F R",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 25",
        caseDrawCodes['ygyy'] +                                             "Bowtie",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'],
        colors['line'], caseDrawCodes['yyy'] +                              "F' (r U R' U') r' F R",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Same as Chameleon with the last F' in front",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['yyg'] +        "",
        caseDrawCodes['yyg'], caseDrawCodes['yyg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 26
    [
        "R U2 R' U' R U' R'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 26",
        caseDrawCodes['ygyy'] +                                             "Anti-Sune",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'],
        colors['line'], caseDrawCodes['yyy'] +                              "R U2 R' U' R U' R'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Inverse Sune",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['gygy'] +       "y' R' U' R U' R' U2 R",
        caseDrawCodes['gygy'], caseDrawCodes['gygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 27
    [
        "R U R' U R U2' R'",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 27",
        caseDrawCodes['gygy'] +                                             "Sune",
        caseDrawCodes['gygy'], caseDrawCodes['gygy'],
        colors['line'], caseDrawCodes['yyy'] +                              "R U R' U R U2' R'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['yyg'] +        "y' R' U2' R U R' U R",
        caseDrawCodes['yyg'], caseDrawCodes['yyg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 28
    [
        "(r U R' U') M (U R U' R')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 28",
        caseDrawCodes['yyy'] +                                              "Arrow",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'],
        colors['line'], caseDrawCodes['yygy'] +                             "(r U R' U') M (U R U' R')",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "(Wide Sexy) M (Inverse Sexy)",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygy'] +       "",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 29
    [
        "r2 D' (r U r') D r2 (U' r' U' r)",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 29",
        caseDrawCodes['ygy'] +                                              "WTF",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "r2 D' (r U r') D r2 (U' r' U' r)",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Do the D-moves with left ringfinger",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygygy'] +     "y (R U R' U') (R U' R') (F' U' F) (R U R')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "If you suck at D moves",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 30
    [
        "F U (R U2 R' U') (R U2 R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 30",
        caseDrawCodes['ygygy'] +                                            "Anti-WTF",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "F U (R U2 R' U') (R U2 R' U') F'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Do the first U with a lefty index push",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygy'] +       "",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 31
    [
        "R' U' F (U R U' R') F' R",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 31",
        caseDrawCodes['gyy'] +                                              "Couch",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "R' U' F (U R U' R') F' R",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "Inverse of Big Lightning",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ggy'] +       "",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 32
    [
        "S (R U R' U') (R' F R f')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 32",
        caseDrawCodes['ggy'] +                                              "Anti-Couch",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "S (R U R' U') (R' F R f')",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "S (Sexy) (Wide Slegde)",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['gyy'] +       "R U B' (U' R' U) R B R'",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 33
    [
        "(R U R' U') (R' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 33",
        caseDrawCodes['ggy'] +                                              "Key",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(R U R' U') (R' F R F')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "(Sexy) (Slegde)",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ggy'] +        "",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 34
    [
        "(R U R2' U') (R' F R U) R U' F'",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 34",
        caseDrawCodes['ygggy'] +                                            "City",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(R U R2' U') (R' F R U) R U' F'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "(Sexy with R2') (Sledge) R U' F'",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygy'] +        "(R U R' U') B' (R' F R F') B",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "(Sexy) B' (Sledge) B",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 35
    [
        "(R U2') (R2' F R F') (R U2' R')",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 35",
        caseDrawCodes['yggry'] +                                            "Fish Salad",
        caseDrawCodes['yggry'], caseDrawCodes['yggry'],
        colors['line'], caseDrawCodes['ygyy'] +                             "(R U2') (R2' F R F') (R U2' R')",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "(R U2' R') (Sledge) (R U2' R')",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['gyy'] +       "",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 36
    [
        "(R U R' U') F' U2 F (U R U R')",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 36",
        caseDrawCodes['yggry'] +                                            "Wario",
        caseDrawCodes['yggry'], caseDrawCodes['yggry'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R U R' U') F' U2 F (U R U R')",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['gyy'] +       "(R' U' R U') (R' U R U) l U' R' U x",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'] +                        "Mirror of Mario",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 37
    [
        "F (R U' R' U') (R U R' F')",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 37",
        caseDrawCodes['yygy'] +                                             "Mounted Fish",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "F (R U' R' U') (R U R' F')",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ggy'] +       "",
        caseDrawCodes['ggy'], caseDrawCodes['ggy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 38
    [
        "(R U R' U) (R U' R' U') (R' F R F')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 38",
        caseDrawCodes['gyy'] +                                              "Mario",
        caseDrawCodes['gyy'], caseDrawCodes['gyy'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R U R' U) (R U' R' U') (R' F R F')",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Sune with Sledge insert",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['yggry'] +     "",
        caseDrawCodes['yggry'], caseDrawCodes['yggry'] +                    "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 39
    [
        "(R U R') (F' U' F) (U R U2 R')",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 39",
        caseDrawCodes['ygrgy'] +                                            "Lefty Big Lightning",
        caseDrawCodes['ygrgy'], caseDrawCodes['ygrgy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(R U R') (F' U' F) (U R U2 R')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygg'] +        "y2 L F' (L' U' L U) F U' L'",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'] +                        "Mirror of Big Lightning",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 40
    [
        "R' F (R U R' U') F' U R",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 40",
        caseDrawCodes['ygg'] +                                              "Big Lightning",
        caseDrawCodes['ygg'], caseDrawCodes['ygg'],
        colors['line'], caseDrawCodes['yyy'] +                              "R' F (R U R' U') F' U R",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "R' F (Sexy) F' U R",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygrgy'] +      "",
        caseDrawCodes['ygrgy'], caseDrawCodes['ygrgy'] +                    "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 41
    [
        "(R' U' R U' R' U2 R) F (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 41",
        caseDrawCodes['ygy'] +                                              "Anti-Poodle",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R' U' R U' R' U2 R) F (R U R' U') F'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "(Anti-Sune) + (T)",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['gyg'] +       "",
        caseDrawCodes['gyg'], caseDrawCodes['gyg'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 42
    [
        "(R U R' U R U2' R') F (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 42",
        caseDrawCodes['gyg'] +                                              "Poodle",
        caseDrawCodes['gyg'], caseDrawCodes['gyg'],
        colors['line'], caseDrawCodes['yygy'] +                             "(R U R' U R U2' R') F (R U R' U') F'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "(Sune) + (T)",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ygy'] +       "",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 43
    [
        "R' U' F' U F R",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 43",
        caseDrawCodes['yyy'] +                                              "Inverse P",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'],
        colors['line'], caseDrawCodes['yygy'] +                             "R' U' F' U F R",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ggg'] +       "y' f' (L' U' L U) f",
        caseDrawCodes['ggg'], caseDrawCodes['ggg'] +                        "Mirror of P",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 44
    [
        "f (R U R' U') f'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 44",
        caseDrawCodes['ygrgy'] +                                            "P",
        caseDrawCodes['ygrgy'], caseDrawCodes['ygrgy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "f (R U R' U') f'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "f (Sexy) f'",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ygyy'] +      "y2 F (U R U' R') F'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "F (Inverse Sexy) F’",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 45
    [
        "F (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 45",
        caseDrawCodes['ygrgy'] +                                            "T",
        caseDrawCodes['ygrgy'], caseDrawCodes['ygrgy'],
        colors['line'], caseDrawCodes['yyy'] +                              "F (R U R' U') F'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "F (Sexy) F'",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygrgy'] +      "",
        caseDrawCodes['ygrgy'], caseDrawCodes['ygrgy'] +                    "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 46
    [
        "R' U' (R' F R F') U R",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 46",
        caseDrawCodes['yygy'] +                                             "Seein' Headlights",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "R' U' (R' F R F') U R",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "R' U' (Sledge) U R",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['yygy'] +     "",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 47
    [
        "R' U' (R' F R F') (R' F R F') U R",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 47",
        caseDrawCodes['gygry'] +                                            "Anti-Breakneck",
        caseDrawCodes['gygry'], caseDrawCodes['gygry'],
        colors['line'], caseDrawCodes['ygyy'] +                             "R' U' (R' F R F') (R' F R F') U R",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "R' U' (double Sledge) U R",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['gggy'] +      "F' (L' U' L U) (L' U' L U) F",
        caseDrawCodes['gggy'], caseDrawCodes['gggy'] +                      "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 48
    [
        "F (R U R' U') (R U R' U') F'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 48",
        caseDrawCodes['ygryg'] +                                            "Breakneck",
        caseDrawCodes['ygryg'], caseDrawCodes['ygryg'],
        colors['line'], caseDrawCodes['yygy'] +                             "F (R U R' U') (R U R' U') F'",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "F (double Sexy) F'",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['yggg'] +      "",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'] +                      "",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 49
    [
        "F R' F2 R U2 R U2 R' F",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 49",
        caseDrawCodes['ygygy'] +                                            "Back Squeezy",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['yygy'] +                             "F R' F2 R U2 R U2 R' F",
        caseDrawCodes['yygy'], caseDrawCodes['yygy'] +                      "Mirror of Front Squeezy #1",
        caseDrawCodes['yygy'], colors['line'], caseDrawCodes['ggg'] +       "r' U r2 U' r2' U' r2 U r'",
        caseDrawCodes['ggg'], caseDrawCodes['ggg'] +                        "Mirror of Front Squeezy #2 | Never release r",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 50
    [
        "F' R U2 R' U2 R' F2 R F'",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 50",
        caseDrawCodes['ygygy'] +                                            "Front Squeezy",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "F' R U2 R' U2 R' F2 R F'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "Mirror of Back Squeezy #1",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ggg'] +       "r U' r2' U r2 U r2' U' r",
        caseDrawCodes['ggg'], caseDrawCodes['ggg'] +                        "Mirror of Back Squeezy #2 | Never release r",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ],

    # 51
    [
        "f (R U R' U') (R U R' U') f'",
        ['\n', colors['line'],
        caseDrawCodes['ygyy'] +                                             "OLL 51",
        caseDrawCodes['yggg'] +                                             "Ant",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'],
        colors['line'], caseDrawCodes['yyy'] +                              "f (R U R' U') (R U R' U') f'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "f 2(Sexy) f'",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['yggg'] +       "y2 F (U R U' R') (U R U' R') F'",
        caseDrawCodes['yggg'], caseDrawCodes['yggg'] +                      "F 2(Inverse Sexy) F'",
        caseDrawCodes['ygyy'], colors['line'], colors['w'], '\n']
    ],

    # 52
    [
        "(R U R' U R U') y (R U' R') F'",
        ['\n', colors['line'],
        caseDrawCodes['yygy'] +                                             "OLL 52",
        caseDrawCodes['gygry'] +                                            "Rice Cooker",
        caseDrawCodes['gygry'], caseDrawCodes['gygry'],
        colors['line'], caseDrawCodes['ygygy'] +                            "(R U R' U R U') y (R U' R') F'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "Starts like Sune with different insert",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['gygry'] +    "(R' U' R U' R' U) y' (R' U R) B",
        caseDrawCodes['gygry'], caseDrawCodes['gygry'] +                    "",
        caseDrawCodes['yygy'], colors['line'], colors['w'], '\n']
    ],

    # 53
    [
        "(r' U' R U') (R' U R U') R' U2 r",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 53",
        caseDrawCodes['ygggy'] +                                            "Frying Pan",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "(r' U' R U') (R' U R U') R' U2 r",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "fat double Anti-Sune",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ygygy'] +     "",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 54
    [
        "(r U R' U) (R U' R' U) R U2' r'",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 54",
        caseDrawCodes['ygygy'] +                                            "Anti-Frying Pan",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['ygyy'] +                             "(r U R' U) (R U' R' U) R U2' r'",
        caseDrawCodes['ygyy'], caseDrawCodes['ygyy'] +                      "fat double Sune",
        caseDrawCodes['ygyy'], colors['line'], caseDrawCodes['ygggy'] +     "",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'] +                    "",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 55
    [
        "R U2 R2 (U’ R U' R’) U2 F R F'",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 55",
        caseDrawCodes['ygygy'] +                                            "Highway",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'],
        colors['line'], caseDrawCodes['ygygy'] +                            "R U2 R2 (U’ R U' R’) U2 F R F'",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "Shorter but shittier",
        caseDrawCodes['ygygy'], colors['line'], caseDrawCodes['ygygy'] +    "y (R’ F R U) (R U' R2' F') R2 U' R' (U R U R')",
        caseDrawCodes['ygygy'], caseDrawCodes['ygygy'] +                    "Longer but fingertrickable",
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 56
    [
        "alg1",
        ['\n', colors['line'],
        caseDrawCodes['ygygy'] +                                            "OLL 56",
        caseDrawCodes['ygggy'] +                                            "Streetlights",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'],
        colors['line'], caseDrawCodes['yyy'] +                              "r U r' (U R U' R') (U R U' R') r U' r'",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "Long but fast",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygggy'] +      "r' U' r (U' R' U R) (U' R' U R) r' U r",
        caseDrawCodes['ygggy'], caseDrawCodes['ygggy'] +                    "Mirror",                 
        caseDrawCodes['ygygy'], colors['line'], colors['w'], '\n']
    ],

    # 57
    [
        "(R U R' U') M' (U R U' r')",
        ['\n', colors['line'],
        caseDrawCodes['yyy'] +                                              "OLL 57",
        caseDrawCodes['ygy'] +                                              "H",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'],
        colors['line'], caseDrawCodes['yyy'] +                              "(R U R' U') M' (U R U' r')",
        caseDrawCodes['yyy'], caseDrawCodes['yyy'] +                        "(Sexy) M' (Wide Inverse Sexy)",
        caseDrawCodes['yyy'], colors['line'], caseDrawCodes['ygy'] +        "",
        caseDrawCodes['ygy'], caseDrawCodes['ygy'] +                        "",
        caseDrawCodes['yyy'], colors['line'], colors['w'], '\n']
    ]
]


# oll scrambles
ollScrambles = [
    [0, "R' U' F R' F' R2 U R B' R' B", "L U F' L F L2 U' L' B L B'", "L U2 L2 B L B' U2 L' B L B'", "R' U2 R2 B' R' B U2 R B' R' B", "B U' B2 D' F R' F' D B2 U B'", "L' B2 R2 B R' B L U2 B' R' B", "F' U F2 D B' R B D' F2 U' F", "R B2 L2 B' L B' R' U2 B L B'", "L R' F R U2 F' U2 F' U2 F U2 L'", "L R' F' L' U2 F U2 F U2 F' U2 R", "L U F' L F L2 B' U' B L U' L'", "R' U' F R' F' R2 B U B' R' U R", "R' U' F R' F' R2 B U' L U L' B'", "L U F' L F L2 B' U R' U' R B", "L U F' L F L2 B2 R B R' U' B", "R' U' F R' F' R2 B2 L' B' L U B'", "R2 B2 L' B R' B2 L2 U L' U B' R'", "L2 B2 R B' L B2 R2 U' R U' B L", "L R' F R U2 B' R2 F' R2 B U2 L'", "L R' F' L' U2 B L2 F L2 B' U2 R"],
    [1, "B L' B' L U L2 F' L' F U' L'", "F' L F L' U' L2 B L B' U L", "B' R' B U2 F' U2 F U2 B' R B", "F R F' U2 B U2 B' U2 F R' F'", "L U L' B' R' U' F R' F' R2 B", "L' U' L F R U B' R B R2 F'", "L B' R2 F' R F2 R' F R2 B L'", "L' F R2 B R' B2 R B' R2 F' L", "R U2 L' B L U2 L' B' L U2 R'", "L2 F2 R' F2 L' F R2 U2 R' F' L'", "L2 B2 R B2 L B' R2 U2 R B L", "R B R' U L U' L' R U B' U' R'", "R' F' R U' L' U L R' U' F U R", "L F L' U' B U L U2 F' U L' B'", "L' B' L U F' U' L' U2 B U' L F", "B U B' R' U R B2 L' B' L U' B'", "L F U2 R' F R F2 L' U B' U B", "B' U R B' R' B2 L2 F' L' F U' L'", "F U2 B' R B2 U2 B' R' B U2 B' F'", "F2 D B' R' B D' F' R U2 R' U' F'", "B2 D' F R F' D B R' U2 R U B", "B L B2 D2 F R D F2 D B U' R2", "F' L' F2 D2 B' R' D' B2 D' F' U R2", "B2 U L' D' R2 D' B' R' D2 L2 F' L'", "F2 U' L D R2 D F R D2 L2 B L"],
    [2, "B' F R F' U2 F R B' R B2 F'", "L F2 L2 U2 L F L' U2 L2 F2 L'", "R' F2 R2 U2 R' F R U2 R2 F2 R", "B' U' R' U R B R B U B' U' R'", "L U2 L F' L' F U F U F' U L'", "F' L' U B' U B U' B' U2 B L F", "F U R U' R' F' R B U B' U' R'", "B L U L' U' B' R' U' F' U F R", "L F R U2 R' U F' L' U B' U B", "B' R B L' B R' B2 L U2 L' B L", "R B R' U2 R B2 L' B R' B L B'", "F R' F' R U F D B' R' B D' F'", "F U F' L' U L2 D R' F' R D' L'", "L F' L' F U2 L' B' R' U2 R B L", "R2 D L' B' L D' R' U' R' F' U F", "L U L' B' U' B' D' F R' F' D B2", "R' F' U F U' R2 D L' B' L D' R'", "R' U2 R B L F U2 F2 L F L2 B'", "R U2 R' F' U F2 D B' R B D' F'", "R' F2 L F L2 U2 L F R B U2 B'", "L' D' R B R' D L2 U L' B' U2 B", "B L U L' B' R2 D' L F' L' D R2", "F2 D B' R' B D' F2 L' B' U B L", "B F2 D2 B2 R' B2 D2 F L F L2 B'", "B' D2 F2 R' F2 D2 B2 F' L F L2 B'"],
    [3, "L R' F' R U2 R' F' L F' L2 R", "F R2 F2 U2 F R' F' U2 F2 R2 F'", "B' R2 B2 U2 B' R' B U2 B2 R2 B", "L U F U' F' L' F' L' U' L U F", "B' U2 B' R B R' U' R' U' R U' B", "R B U' L U' L' U L U2 L' B' R'", "R' U' F' U F R F' L' U' L U F", "L' B' U' B U L F U R U' R' F'", "B' R' F' U2 F U' R B U' L U' L'", "L F' L' B L' F L2 B' U2 B L' B'", "F' L' F U2 F' L2 B L' F L' B' L", "F D B' R B D' F' U' R' F R F'", "R' F R F' U' R' D' L F L' D R", "B' R B R' U2 B L F U2 F' L' B'", "F2 D' B L B' D F U F R U' R'", "B' U' B L U L D R' F R D' L2", "R B U' B' U' R D L' B L D' R2", "F R U' R' U F2 D' B L B' D F", "F U2 F' L' B' R' U2 R2 B' R' B2 L", "F' U2 F R U' R2 D' L F' L' D R", "F R2 B' R' B2 U2 B' R' F' L' U2 L", "R2 D' L F L' D R2 B L U' L' B'", "L' R2 D2 L2 F L2 D2 R' B' R' B2 L", "F R2 B' R' B' D2 F2 L F2 D2 B2 F'", "L D2 R2 F R2 D2 L2 R B' R' B2 L"],
    [4, "B' F R B' R2 B R B' R B2 F'", "B' R2 F R F' R U' R' U R B", "L' U B L' B' L B' U2 B U L", "R' F' L' U2 L F R' F R F' R", "L R2 D2 L D2 L' R F' L' F R", "F' L' U' L U L' U L F R U' R'", "F D' F L F L' F' D F' R' F' R", "R' F R' F2 U' F U R2 U' B U2 B'", "B' U2 B U' L2 U F' L F L' U' L2", "B2 U' B' R B R' U B2 U' L U2 L'", "L' U2 R B U B2 R B R' U' L R'", "R' U L U' R U2 L2 B L B2 U B", "L U' F U R B U' B' R' F' U2 L'", "B2 R' U F' U' F R B2 U' L U2 L'", "B2 F2 L' F L' B' U2 L' B L' B2 F", "R' U' R2 U2 B' D B U2 B2 D' B2 R'", "F2 D L D' F D L' D' F2 R' F' R", "R' D' F2 D F L' R2 U2 L R' U F", "F' L' D F2 U F2 D' L' B L2 B' F", "R' F' U B2 F' D2 F' D2 B2 F' U R", "F2 L2 R2 B2 R' B2 L' R2 F L' F R", "L' R' F2 L' B' R U2 R' B L2 F' R", "F' L2 B L2 F L2 B2 R B' R' B2 L2", "F D R' B2 R' D' R D B2 R D' F'", "F R' F R' D2 L2 B2 L2 D2 R F2 R"],
    [5, "L R' F' L F2 L' F' L F' L2 R", "L F2 R' F' R F' U F U' F' L'", "B U' L' B L B' L U2 L' U' B'", "F' L F' L' F2 R U' B U' B' R'", "R B R' U2 L U' L' U2 R B' R'", "F R B U2 B' R' F R' F' R F'", "F U F R' D R' D' R2 F' U' F'", "B' R B R' U' B L U2 L' U' B'", "F R' D' R' D2 L B2 L' D' R2 F'", "B U B' U' B' U' R U B2 U' B' R'", "B' F U' B U R U' B' U B R' F'", "R B U' B2 U' B2 U B L' B2 L R'", "L' B L F L' B' U R U' L R' F'", "R' U' R B R B2 L' B2 L R' U B'", "L2 U L F' L' F U' L2 U B' U2 B", "L2 F L U R U' L' F' L2 F R' F'", "F R2 F' R2 B R2 B' R' B R' U2 B'", "B2 U' B L U' L' B' U B2 L U2 L'", "B' F D' R' D B2 F' L U2 L' U' B'", "F' U B2 L U B' L' B U' L' B2 F", "L' F2 L2 R2 B2 F' R F' L2 R B2 L", "R' F R' B R2 F2 U2 F2 R2 B' R2 F'", "R' D' F L2 F D F' D' L2 F' D R", "R2 B F' U2 L2 B D2 B' L' F L' B'", "B' F' D2 L' B U2 B' L D2 B U2 F"],
    [6, "F' U2 F U F' U L' U' L U F", "L R' F L F L' F L F2 L2 R", "B L' B' U B L B' U2 F U F'", "B F' L2 F L2 B' L2 B L B' L", "B F' U' F2 R' F' R2 U' R' U2 B'", "B L F U' R' F R F2 U L' B'", "L' U' F R2 D B' D' R2 F' U2 L", "B U' R' U' R2 B' R' B2 U' B' U' B'", "R B' R B R' B L U L' U B' R'", "L' B' U' B U2 B L' B' L2 F U' F'", "R' F R' F' R2 U2 B' F R B R' F'", "B2 U B L' B L2 U L' U2 R B2 R'", "R' D2 L U' F U F' U L' D2 U' R", "B U2 B' R' U F2 L F L' U' F R", "B D L B2 U F U' B2 F' L' D' B'", "F U L2 R' D2 R' D2 L2 R' U R' F'", "L' D F' D' L2 B L2 D F D' B' L", "B L2 D' B R' U' R U B' D L2 B'", "L' B R2 B2 U2 B U2 L2 B R2 B' L'", "L' B L2 F2 R' D R F2 L2 B' U L", "F R2 F' D2 B' F L2 D2 B R F' R", "F D2 U' B2 U L U2 B2 D2 R U' F", "F' U2 B' D2 L' B U2 B' L D2 B F", "L' B' U2 B2 R2 F' L2 D2 F R2 B' L'", "F' D2 B2 L2 F2 U2 B D2 B R F' R"],
    [7, "F U2 F' U L' U' L U' F U' F'", "R' U R U B U2 B' U2 R' U2 R", "B' F R' B' R' B R' B' R2 B2 F'", "L' R B2 R' B2 L B2 L' B' L B'", "L' U' L' B2 D' B' D B' L U L", "F' L F' L' F L' B' U' B U' L F", "B' R B R2 F R U R' U' R' F' R2", "R' B' F R' F' R2 F R2 F' R' B R", "B L U L' U2 L' B L B2 R' U R", "F' L' U' L U2 B L U L' U' B' F", "R U R B' R D' R' D R' B U' R'", "R B U' L B' U' B U B L' B2 R'", "L U L' B2 U' R' U R2 B R' U' B", "R' F' L2 R U' L U' R' F2 L F' R", "L2 F' L' F L' B' R' U2 R2 B' R' B2", "B' R B L B2 L2 B2 R' B2 L2 B2 L'", "F L2 F' L' U2 L F2 R' F' L2 R F'", "R2 F2 L F2 R F' L2 U' L U' F R", "B2 R B R' U' B' F2 D2 B' D2 B' F2", "L R' F2 R F D' L2 U' L2 D F L'", "B U L' U' L2 D' B2 U2 B2 D L' B'", "R' U' B2 F D2 F D2 B2 F U' F R", "L' B' R B' L2 R F2 L B2 L2 R2 F2", "R' D2 U L2 U' B' U2 L2 D2 F' U R'", "R D2 L2 B2 R2 U2 L' D2 L' F' R F'"],
    [8, "L' U' B' U B U' L U' L' U2 L", "L U L' U' L' B L2 U L' U' B'", "B U2 B2 F R' B R' B' R B F'", "B L2 F' L D' L' D L' F L' B'", "L' U R B L' B' D' B' D L2 R'", "L F' L2 B L' D2 B D2 B2 L2 F", "L F' U' F2 U' F2 U F L' F' U F", "B' R B2 L' B R' B2 L U' L U' L'", "R' F' L U L' U' F L' R B L B'", "L' B L U' B D' U B U' B' D B'", "L F U2 R' F R F2 L F' L' F L'", "B L U' L' B F' L' B' L F U B'", "L' U' L B U2 F U F' L' U2 L B'", "F' L' U' L2 U2 B L B' U2 L' U' F", "R B2 U B' U B R B' R' U2 B2 R'", "L' U2 F R F' L B F U2 B' R' F'", "F' L D' L' D' B2 D B' L B' D F", "B' R' U R2 B2 L' B2 R' B L2 U' L'", "R F R' U R F' L2 D' B' D L2 R'", "B D' L B2 L F' L' B2 F L' D B'", "L B R2 B' L2 U2 B' U2 B2 R2 B' L", "L F2 R2 F2 L2 B R2 B R2 B' L R2", "L' B' D L2 F U' F' U' L2 D' B2 L", "F2 L2 B' R2 B2 F L' F L' B R2 B2", "B L D' B2 U' R' U2 R B2 D L2 B'"],
    [9, "B U L U' L' U B' U B U2 B'", "B' U' B U B L' B2 U' B U L", "L' U2 L2 R' F L' F L F' L' R", "L' B2 R B' D B D' B R' B L", "L2 R D' B D B L B' R' U' L", "B' R B2 L' B D2 R D2 R2 B2 L", "B' R U R2 U R2 U' R' B R U' R'", "L' U' L' B L B' L2 F' L' F2 U' F'", "B2 R B U B U' B' R' B2 L' B' L", "L F' L2 B L' F L2 B' U B' U B", "B2 U2 B' L B L' U' L U' B' L' B'", "R B L' B L B' R' F R B' R' F'", "B U B' L' U2 R' U' R B U2 B' L", "R' U2 L F2 U F2 U' F' R' F' L' R2", "F' L2 U' L U' L' F' L F U2 L2 F", "B2 R B R2 U2 R B L F' L F L2", "F' R' F U' F' R B2 D L D' B2 F", "B U' F2 U R' D' L2 D' L' D2 R B'", "R' U' F U' R' F' L D F2 D' L' R2", "L' B2 D' B2 U2 B D B' U2 L2 U' L'", "B' L' F2 L B2 U2 L U2 L2 F2 L B'", "B' R2 F2 R2 B2 L' F2 L' F2 L B' F2", "R2 B2 L F2 L2 R' B R' B L' F2 L2", "L' B' D L2 U F U2 F' L2 D' B2 L", "F' L' U2 F R' F D2 R' B2 D2 R2 F'"],
    [10, "B' F2 R F' R F R2 F' R B F'", "F R U R' U' R B' R B R2 F'", "L' B' U' B2 L' B' L2 U' L' U2 L", "L' U2 F' U' F2 R' F' R2 U' L R'", "L' U2 L U F R B U B' R' F'", "R' F2 L' R2 B L' B' L2 R2 F2 R", "L' B' R2 D' R' D2 B' D' B2 L R'", "F2 D B' R' B D' F' R U R' F'", "L2 B2 R B2 L B L' B R' B2 L2", "B U2 R' F2 D' L' D F2 R U' B'", "F R2 B2 D2 B D2 R F' R2 B R'", "L' R U B U' B U B2 U' B2 L R'", "B L U' L2 U2 L2 U L2 U L U' B'", "B' U2 B U' L2 U F U' F2 L' F L'", "F2 U R' F' R F' R' F' R F2 U' F2", "L2 U' L2 B L' B' L' B L' B' U L2", "R B' R' B' R2 B2 U2 B U2 B R2 B2", "F' L' B U L U' L' B' U2 L U F", "R U2 F R2 U' R2 U R2 U F' U R'", "B' R' U2 F R B' R2 F' R' B R' B", "B2 L2 B R B' L2 R' B2 U' L U' L'", "R2 F2 R F2 L' R2 B L' B R' B2 L2", "F D' R B' F2 R B R' F2 R' D F'", "F2 L2 R2 B' R' B L2 R' F2 L' U2 L", "L2 F' L2 F R' F' D2 R2 B' R2 D2 R"],
    [11, "L R2 F' R F' R' F2 R F' L' R", "R' F' U' F U F' L F' L' F2 R", "B L U L2 B L B2 U B U2 B'", "B U2 R U R2 F R F2 U B' F", "F R2 B F2 L' B L B2 F2 R2 F'", "B L F2 D F D2 L D L2 B' F", "R B U' B' R2 D' L F L' D R", "R2 D' L F L' D R F' U' F R", "L' U2 F R2 D B D' R2 F' U L", "L F2 R2 D2 R D2 F' R F2 L' F", "B F' U' L' U L' U' L2 U L2 B' F", "L' B' U B2 U2 B2 U' B2 U' B' U L", "L U2 L' U B2 U' R' U R2 B R' B", "B2 U B2 L' B L B L' B L U' B2", "R B L' U' B' U B L U2 B' U' R'", "F2 L B L' B' F L' F U2 B' U2 B", "R' F R B R' F2 L F' L' F2 R B'", "R' F2 U F U' L U F' U' L' F2 R", "B U2 L R B U B' U' L' R' U2 B'", "L F U2 R' F' L F2 R F L' F L'", "F D' R F U2 F' R' F U2 F' D F'", "R2 B2 R' U2 R' U2 R B2 R2 F R F'", "L2 B2 L' F' L B2 F L2 U B' U B", "R2 B2 F2 L F L' B2 F R2 B U2 B'", "F' U2 R' F2 D R2 U' R2 D' R U' F"],
    [12, "L U F U' F2 L' F U F U' F'", "B U' F' U B' U' L' U' L U F", "F' L' B L F L' B2 U' B U L", "B U B' L R2 F R F' L' U' R", "B2 R B R2 U2 R U' B L U L'", "R B U B2 D' B U' B' D B R'", "F' U2 F U F' U F2 U R U' R' F'", "B U R' U R U B U2 B' R B' R'", "B' R B' R' B' U B2 U' B' R B2 R'", "F R' F' R U2 R U2 B U B' U' R'", "B' U' B2 L' B' L2 F' L F L' U' L'", "L' F' L U' L' F L U F R' F' R", "R B U2 L' U2 L U L' U L B' R'", "L U2 L2 B L B' U' B' R' U' R B", "L B' U2 B U2 B L2 B2 U' B U L", "L' F D2 B' F' U' B U F D2 F' L", "B2 L' D' B' U' B D L B2 L' U L", "B2 D F' L2 F D' B' U' L U' L' B'", "L' B' U' B U' L' D' R B2 R' D L2", "R' D F' R2 U L' U' L R2 F D' R", "L F2 D R2 F' R2 F R2 F D' F L'", "L' R2 D B2 U B U' B D' R2 U2 L", "L' D' B R2 D B D' B' R2 B' D L", "R B R' F2 D' L' D F2 R U2 B' R'", "F' L' U2 F R2 D B' D' R2 F' L F"],
    [13, "B' U' R' U R2 B R' U' R' U R", "L' U R U' L U B U B' U' R'", "R' U F U F' U' R F' L F L'", "R B L' B' R' B L2 U L' U' B'", "L' U' L B' F2 R' F' R B U F'", "L2 F' L' F2 U2 F' U L' B' U' B", "L F' L F L U' L2 U L F' L2 F", "R U B U' B' U2 R' U2 R' F R F'", "R' F R F' U2 R U' R' U2 F' U F", "L U L2 B L B2 R B' R' B U B", "F' U2 F2 U F2 U F2 U' R U' R' F'", "B R B' U B R' B' U' R' F R F'", "F' L' U2 B U2 B' U' B U' B' L F", "B' U2 B2 L' B' L U L F U F' L'", "R B2 R' U2 L U' L2 B' L B' U' B2", "F' U2 F R2 U R' F' U' F R U' R2", "L F U' R U' R2 F' L F2 R F2 L2", "B R' D2 L R U L' U' R' D2 R B'", "F' R U' B2 F' L F L' B2 U R' F", "F R2 D U B R B' R' D' U' R2 F'", "L2 B D L U L' D' B' L2 B U' B'", "B' R2 D' F2 R F2 R' F2 R' D R' B", "B D L' F2 D' L' D L F2 L D' B'", "R B U2 R' F2 D' L D F2 R B' R'", "F' L' F R2 D B D' R2 F' U2 L F"],
    [14, "B U L U' L2 B L B2 R' U2 R", "L' B' R' U R B L U F U2 F'", "F U F' U L' B' R' U2 R B L", "L U2 L' B2 R B R2 U' R U B", "B U2 B2 U' B2 L U' L' B2 U B", "B' D' F R' F' D B2 L U L' B'", "R' F' U F R' D' L F' L' D R2", "F R2 D L B2 L' D2 R D R F'", "B' R' U' R U B2 U B' U B U2 B'", "B' U2 B U B' R U B U' B' R' B", "R' F' U L' U L U2 L' U2 L F R", "R B R' F R B' U' B U B' R' F'", "B' U2 B U L U' L' B' R' U R B", "L B D' L U L' D L' U' L B' L'", "F U' F2 D' U' L' U L D F2 U F'", "B D' L2 U L U' L2 D B' L' U L", "B R U' B2 U' R' U R B2 U R' B'", "R' B' D B2 L U L' U' B2 D' B R", "F' L' U B2 D' B U' B' D B2 L F", "B F2 D' L D F2 R B' U' B R' B'", "L' U' L2 F2 R' F D F' D' R F2 L'", "F' L2 B2 D' B' D2 L' D' L2 B' L F", "R B R' F2 D' L D F2 R B' U' R'", "F' L2 D2 B2 D B2 D L' F L2 U L", "F U' L D2 B2 U2 R U B2 D2 U' F"],
    [15, "L' U' B' U B2 L' B' L2 F U2 F'", "B L F U' F' L' B' U' R' U2 R", "R' U' R U' B L F U2 F' L' B'", "L' U2 L2 U F' D F' D' F2 U' L'", "F R U' R' F D B' R B D' F2", "L D R' F R D' L2 B' U' B L", "R' F2 D' B' L2 B D2 F' D' F' R", "L F U F' U' L2 U' L U' L' U2 L", "L U2 L' U' L F' U' L' U L F L'", "F R U' B U' B' U2 B U2 B' R' F'", "B2 R B R' B U B' R' U' R U' B", "B' F U' B U F' R B L' B' L R'", "F' L' F R' F' L U L' U' L F R", "L' U2 L R B U' F U' F' U2 B' R'", "B2 D B' U B D' B2 U' B' R B R'", "L' R D' B' D L B' U B2 U' B' R'", "R' U' R2 B' R F R' B R2 F' U R", "L' U' L B D' L2 U L' U' L2 D B'", "L' F' U L2 U F U' F' L2 U' F L", "L' U' L2 F R' F2 L' F2 R2 U R' F'", "R B U' L2 D L' U L D' L2 B' R'", "L' R2 D B' D' R2 F' L U L' F L", "B U B2 R2 F R' D' R D F' R2 B", "R B2 D2 L2 D' L2 D' B R' B2 U' B'", "R' U B' D2 L2 U2 F' U' L2 D2 U R'"],
    [16, "R B' R' B U2 B U' L U' L' B'", "F' L F L' U2 L' U B' U B L", "L F U2 F2 U' L' U L F U2 L'", "B' R' U2 R2 U B U' B' R' U2 B", "R U B L' U' B U L U' B2 R'", "R F' U2 B L' U2 L B' U2 F R'", "F' R U2 L' B U2 B' L U2 R' F", "B L' B' L2 R' F L F' L' F' L' R", "L' B L B2 F R' B' R B R B F'", "L' U' B U L U' L' B2 U' B U L", "B U L' U' B' U B L2 U L' U' B'", "F R' F' U B' F R2 B U R U' F'", "R' F R U' L R' F2 L' U' F' U R", "R B L B U B' L' U B U2 B2 R'", "B L' B' L U B F' D L' D' B' F", "L' B L B' U' L' R D' B D L R'", "L U' F' L F L R D' B D L R'", "B' U R B' R' B' F' D L' D' B' F", "B U B' R' U L' R2 D B' D' L R'", "L' U' L F U' B F2 D' L D B' F", "B L U' L' U B2 F D' R D B F'", "R2 B2 L' B' L B' R F R F2 U2 F", "F2 L2 B L B' L F' R' F' R2 U2 R'", "R B U R' F2 D' L' D F2 R B' R'", "F' L' U' F R2 D B D' R2 F' L F"],
    [17, "B' R' U' R U' B U2 B L' B' L", "B L U L' U B' U2 B' R B R'", "L F R U2 R' U2 R U2 R' F' L'", "R' F' L' U2 L U2 L' U2 L F R", "F R U' B U' B' R' F' L' U2 L", "R' U2 R B L F U F' U L' B'", "L U2 L' B' R' F' U' F U' R B", "F' L' U B' U B L F R U2 R'", "B U2 B' R' F' U2 F R B U2 B'", "R B U2 L' B L B2 R' F' U2 F", "F R' F' R U R U' B U B' U' R'", "L U F U' R U' R' F' L' B' U B", "R' U' F' U L' U L F R B U' B'", "F' U' F R B L U L' U B' U' R'", "R B U' B2 R B R' U' R' F' U2 F", "L' B' U B2 L' B' L U L F U2 F'", "B L' B' L2 U L' B' U2 B L U2 L'", "L2 R D' B D L R' B' U2 B U L", "L F L F2 R' F2 L' R2 U2 R' F' L'", "L R2 D F D L R' D' B' D' L2 R'", "F R B R2 D2 F L2 D F' D R F'", "F' L' B' L2 D2 F' R2 D' F D' L' F", "B2 F' L F R2 F2 D2 F L' F R2 B2", "L F' D' L D' B2 L' D2 F2 R' F' L'", "R' F D R' D B2 R D2 F2 L F R"],
    [18, "L U2 F' L' U' L U F2 U2 F' L'", "R' U2 F R U R' U' F2 U2 F R", "L U2 L' B' R' U F' U2 F R B", "R' U2 R B L U' F U2 F' L' B'", "R B2 U L' U' B' U L B' U' R'", "L' B2 U' R U B U' R' B U L", "L' R B R B R' B' L R2 F R F'", "L' R B' L' B' L B L2 R' F' L' F", "B U L U' L2 B' U' B U L U' B'", "B' U' R' U R2 B U B' U' R' U B", "L B' R' U' R U B U2 F U2 F' L'", "R' B L U L' U' B' U2 F' U2 F R", "B U L' U' F' L2 B' F U' B L B'", "B' U' R U F R2 B F' U B' R' B", "L' R D B D' L R F R F' U' R", "L' R D B D' L R' U' B' R B R'", "L' R D' B' D L R' U B L' B' L", "L' R D' B' D L' R' F' L' F U L'", "L' R2 D B' D' L R' U' R' F' U F", "R B2 U2 B' U' L B U' B' L' B' R'", "L' B2 U2 B U R' B' U B R B L", "F R F' L2 D' B D L2 F U' R' F'", "F' L' F R2 D B' D' R2 F' U L F", "R2 B2 L F' L D2 L2 B2 L F L' R2", "L2 B2 R' F R' D2 R2 B2 R' F' L2 R"],
    [19, "B F L F2 U2 F2 U2 F2 U2 L' B' F'", "L' R' F' L2 U2 L2 U2 L2 U2 F L R", "L' R' F' U2 L2 U2 L2 U2 L2 F L R", "B F L U2 F2 U2 F2 U2 F2 L' B' F'", "B L U L' B' L R2 D' F' D L' R2", "B' R' U' R B L2 R' D F D' L2 R", "B F2 D' L D B' F2 R B U' B' R'", "B' F2 D R' D' B F2 L' B' U B L", "B F L B2 U2 B2 D2 F2 D2 L' B' F'", "B2 U2 L R' F L2 R2 B D2 B2 L R'", "L2 U2 B' F R' B2 F2 L' D2 L2 B' F", "B F L D2 F2 D2 B2 U2 B2 L' B' F'", "B F' L2 D2 L B2 F2 R B F' U2 L2", "L R' F2 D2 F' L2 R2 B' L R' U2 F2", "B F L B2 D2 F2 D2 B2 U2 L' B' F'", "L' R' F' R2 D2 L2 D2 R2 U2 F L R", "B F L F2 D2 B2 U2 B2 D2 L' B' F'", "L2 B' F U2 R B2 F2 L' U2 B' F R2", "B2 L R' U2 F' L2 R2 B U2 L R' F2", "B F L U2 B2 D2 F2 D2 B2 L' B' F'", "L' R' F' U2 R2 D2 L2 D2 R2 F L R", "B F L D2 B2 U2 B2 D2 F2 L' B' F'", "L' R' F' D2 R2 U2 R2 D2 L2 F L R", "B2 L' R D2 B L2 R2 F U2 L' R B2", "L2 B F' D2 L' B2 F2 R' U2 B F' L2"],
    [20, "L U L' U L U' L' U L U2 L'", "R' U' R U' R' U R U' R' U2 R", "B' U2 B U B' U' B U B' U B", "F U2 B F' U' L2 U' L2 U L2 B'", "B L2 B2 U2 B L2 B' U2 B2 L2 B'", "B' U' B2 L2 D F2 D F2 D2 L2 B'", "B U2 B2 R2 F D2 F D2 F2 R2 B", "L2 F D2 F' L2 U2 L2 B R2 B' L2", "B L' B L B2 R B' R' B R' U2 R", "L' U2 L F' L F L' F2 R' F' R F'", "L' B' L U2 L U2 L' B U' L U' L'", "F U' B' U F2 U' B F U2 F' U' F", "R F R2 U' R2 U' R2 U2 R2 U' F' R'", "L' F' L2 U L2 U L2 U2 L2 U F L", "B L' B' R B L2 U' L' U2 B' U' R'", "F R' F' R U2 F2 L' B L' B' L2 F2", "F' L F L' U2 F2 R B' R B R2 F2", "F' U2 F2 R' D R2 U R2 D' R U' F'", "B U2 F2 L2 F U2 F U2 F2 L2 B' F2", "B F' L2 B' L2 D F2 U F2 D' L2 F", "B D2 U2 B' R2 U2 F L2 F2 U2 F R2", "L2 B' U2 B2 R2 B' U2 L2 F D2 U2 F'", "B' D' R2 B2 D L2 D2 U' F2 D2 L2 B'", "B D' U2 R2 F2 D' L2 U' F2 D2 R2 B", "B' D U2 L2 F2 D R2 U F2 D2 L2 B'"],
    [21, "R' U L U' R U' L' U' L U' L'", "F' U' L' U L F2 R U R' U' F'", "R B2 U' B2 U B2 U L R' U2 L'", "R' F2 U F2 U' F2 U' L' R U2 L", "R U2 R2 D U2 B2 U' B2 D' U' R", "R' D U B2 U B2 D' U2 R2 U2 R'", "F L' D2 L F' U' F L' D2 L F'", "R B2 D2 L2 D' L2 D' B2 R2 U R", "L2 R D2 L2 U R2 U L2 D2 L2 R", "L U2 L' U2 L' B L' F' L' F L' B'", "L F R' F R F L' F U2 F U2 F'", "L' B' R B' R' B' L B' U2 B' U2 B", "B' U' B U' L B' U2 B U2 B L' B'", "R' U2 R2 U' L U2 R2 U R2 U2 L' R'", "R B' R2 F' U F U' R2 B R2 U R", "R F' U' R2 F U' F' U R2 U F R'", "L R' F2 R' D R2 D' F2 D' F2 D L'", "F2 R2 B' R' B R' F2 U2 L F' L' F", "B L2 F2 D F2 U F' D' F U' L2 B'", "F' L2 B2 D' B2 U' B D B' U L2 F", "L2 F' D' L2 B L' B' D L2 F U' L'", "L U2 L2 B' D2 B L2 U2 F' R2 F L'", "L F' R2 F U2 L2 B' D2 B L2 U2 L'", "R' D B2 U' R2 F2 U B2 D' L2 F2 R", "R' F2 L2 D B2 U' F2 R2 U B2 D' R"],
    [22, "L' U R' U L U' R U2 L' U L", "R U' L U' R' U L' U2 R U' R'", "F L F' U' F L' F' U' L U2 L'", "F' R' F U F' R F U R' U2 R", "R' D R2 U2 R' U R U R2 D' R", "L F' L' B L F2 L' B' L F' L'", "B2 R2 D' R' U2 R D R' U2 R' B2", "R2 U2 B2 L' B2 L U2 B2 R B2 R", "B' D2 F2 D F' R2 F' D2 B' D' B2", "F U F2 U' F' L F U F2 U' F' L'", "L' R B2 R' U' R U B2 U' R' U L", "R B' R2 F R2 B R' F' U2 F' U2 F", "F U2 F' L2 B L' B' U2 B' U2 B L'", "F U R' F D' F D F2 R2 U' R' F'", "L' B' F R2 B L B' R2 B L' F' L", "L' D L2 U' F2 U F2 L' U L2 D' L2", "R U2 R2 F2 U' F2 D R2 D' R2 U R", "F U2 R U R2 D' L F2 L' D R F'", "F2 U L U' L2 D F2 D' F2 L U' F2", "R' F2 L F' R F2 L2 B' U2 B L F", "L R U2 R' F2 U2 L' U2 L F2 U2 L'", "R' D' U L2 D R2 D' L2 D R2 U' R", "F2 L2 F2 L' U2 R U2 L2 U2 R' U2 L", "F D2 L F' L' B' L F L' B D2 F'", "L R2 D2 F U F' D2 F U' F' L' R2"],
    [23, "F' U L U L' U' F U L U' L'", "F U' R' U' R U F' U' R' U R", "R U2 F U F' U R' U F U F'", "L U F U' L U L' F' L U' L2", "R B U' B' U' B L U L' B' R'", "F L F' U2 F L' F' U' L U' L'", "L' B' U B U B' R' U' R B L", "F R U R' F' L' U L F U' F'", "L R2 F' R' B' R F R' B L' R'", "B F' D' B' D F' D' B D B' F2", "L' B' U' R' F' U F U R B L", "L B' R2 B' L B R2 B' L' B2 L'", "F2 R2 F' D F D' R2 D F' D' F'", "B' D2 L D R' D' L' D R D B", "L U' B' D2 B U' B' D2 B U2 L'", "L2 D R U R' D R U' R' D2 L2", "R2 D' L' U' L D' L' U L D2 R2", "B L2 B2 F' U2 B F2 U2 F L2 F2", "F' L' U' L U L F L' U' L' U L", "L' F L F2 L' B L F2 L' B' F' L", "R B F' R' F2 R B' R' F2 R F R'", "F U2 B' U2 B U2 B' R2 B' R2 B2 F'", "F R2 U' L' U B U B' U' L R2 F'", "F' L2 U R U' B' U' B U L2 R' F", "F' U B2 R B R' U' B2 F L' B' L"],
    [24, "F U F' U R' U F U F' U' R", "R B U B' U' B2 L' B' L B' R'", "L' B' R B' R' B2 U' B' U B L", "F' L' U' L U L2 B L B' L F", "B L F' L F L2 U L U' L' B'", "B2 F2 L' F' R' F L F' R B2 F'", "L D R' F2 R D' L' U2 L' U' L", "L2 R' U L2 U' R D F2 U' F2 D'", "R F' D2 F R' U2 R F' D2 F R'", "B' R U R' B R U' R' U' B' U B", "L' B' U' B U B L B' U2 B' U2 B", "R' F R' F' R2 U R' U' R B U2 B'", "B U2 R U2 B U B' R' B' F' U F", "F D U' R D R' U R D' R' D' F'", "B' D' U L D' L' U' L D L' D B", "B L' B2 L2 B U' B' F' L F L2 B", "F U F' U2 L' B' U' B L2 F' L' F", "L' R B2 R B2 R2 U R U' L U2 R'", "B F' L2 F' L2 F2 U' F' U B' U2 F", "L' U2 B' F R' U R U' F' U' B L", "L' B' L' U2 R' U' L R B L' U2 L2", "L' B L B2 F' U R B' R' B2 U' F", "R' F' L' R B' R' F R B F' L F", "B' U' B' D' F D B D' F' D U B", "B U2 F' U B' U' B2 L2 B' L2 B' F"],
    [25, "L U L' U L' U' L2 U' L2 U2 L", "B U2 B2 U' B2 U' B' U B' U B", "R' F R U F' U' F' U L F L'", "B' R U R2 U R2 U2 R2 U R B", "L R' U' R U R' F2 R' F2 L' R2", "L R B' L B R B' L' B L' R2", "L2 R' F2 L' F2 L' U L U' L' R", "F2 L2 F' U2 F' U' F U' F L2 F2", "F R U' R' F' L' B L' B' L U L", "L' B L2 B F U F' U' B' L2 B' L", "L F2 R2 F2 L' R' U R2 U R2 U' R'", "R' B R' D' L D R D' L' D B' R", "B U B' U F D' F2 U' F2 D R2 F'", "B D F' D' L2 D F2 U' F' D' U B'", "R2 U F L2 F' R F L2 F' R' U' R2", "L B2 D' L U2 L' D L U2 L' B2 L'", "R2 B2 U' R U L U' R' U L' B2 R2", "F' L B2 U F2 U' B2 U F2 U' L' F", "R U2 R2 F2 D' F2 D' L2 D L2 D R", "R' D' F R2 B U B' U' R2 F' D R", "R' F' D' L' U' F2 U F L D R F2", "B D2 B2 F2 D2 U2 B F2 U' B U' B'", "L' D2 U R' U' R2 D B2 D' R' D2 L", "L2 R' D2 R2 D2 L2 U R2 U R2 U' R'", "R' F2 D R D' L D R' D' L' F2 R"],
    [26, "B' U' B U' B U B2 U B2 U2 B'", "L' U2 L2 U L2 U L U' L U' L'", "B U R' U2 R U R' U R U B'", "F U F2 U' F2 U' F2 U2 F2 U2 F'", "B' F U F' U' F R2 F R2 B F2", "L R' F L F' R' F L' F' L' R2", "B' F2 R' B' R F' R' B R B F'", "L R2 B' L B R' B' L' B L' R'", "L R' F2 R' F2 L' R2 U R' U R", "L' U' B U B' L2 B L' U' L B' L'", "R' F R2 F U B U' B' F' R2 F' R", "L' B' R B' R' B' L' B' L2 F U2 F'", "B2 F' L2 F' L2 B' F2 U F' U B' F", "L' R B2 U R D' R D R2 U' L R'", "R' U L' B' R2 B L B' R2 B U' R", "L2 R D' R D' F2 R' D' L D' L R'", "L' U' F' U2 F' D' B L2 B' D F2 L", "B' U2 B2 F' L2 B D' B' D L2 B' F", "F D R' F2 L' U' L U F2 R D' F'", "F R D B U R2 U' R' B' D' F' R2", "B R2 D L' B2 L D' R' U2 R' U' B'", "L' D' B L2 U F U' F' L2 B' D L", "B D2 U' F U F2 D' L2 D F D2 B'", "F R2 D' F' D B' D' F D B R2 F'", "R' F2 L D R D' L' D R' D' F2 R"],
    [27, "L R2 F R F' L' R U R' U' R", "B' F2 R' F' R B F' U' F U F'", "R F R B F' U2 B' F R F' R'", "B R B' L R' U2 L' R B' R' B'", "L' F' L B' F U2 B F' L F L", "R' F' U F U2 F' L' U' L F R", "F R U' R' U2 R B U B' R' F'", "L U' R B' R' B U L' B U' B'", "B' U F' L F L' U' B L' U L", "L2 R B L' U2 L B' L' U2 L' R'", "L' R' U L U' R F U F' L' U' L", "L' R B' R B2 L R' U2 L' B L R'", "F U F' L' B' U2 B L U' L' U2 L", "B' U2 B R U B' U' R' U2 R B R'", "B U L U F' L F L2 B' R' U2 R", "B' F' U2 R U2 R' F2 L F2 L' B F", "F' D' F' D2 B R' B' D' R F' R' F'", "B F' R' F2 D' U L2 D U' R B' F", "B2 F D' R D B F' U2 B L U' L'", "R U' F' D2 U2 B U B' D2 U2 F R'", "F L' B2 D' R' D B' L F' L' B' L", "R' B L2 D F D' L B' R B L B'", "B2 L2 B' L2 B2 F2 R B R2 F' R F'", "F D B' D' R F' D B R' U' R D'", "B R F D U' B2 D' U R2 F' R' B'"],
    [28, "B' U' R' U2 R U R' U2 R U B", "L' B L B' L U2 L' U' B' U' B", "B' U2 B2 U B' U' B' U2 R B R'", "F R B' R' B F2 U B U' B' F", "L' R D B D' R' B U' B' U L", "L2 R D' B' D L2 R' U F U F'", "L' U2 L F2 R' F2 L F R F' L'", "B' U R B' R' F D' R' D B2 F'", "B L' D' B2 U' B2 D U L U' B'", "L' R B2 R' U' B U B' U' B' U L", "F U2 F' L' B' U B L' B L B' L", "B L' U' L B' L' U B' R B L R'", "B L U' F' U' F2 U' F2 U2 F L' B'", "F' U' L' U' L2 U F U' F' L' U2 F", "L' B' R B' R' B' L F' L' B' L F", "R2 U2 R F R' F' U F' U' F U2 R2", "B' U' B U B L2 B2 R B' R' B2 L2", "B' F R' F' R B U2 F2 L F L' F", "F R' F R D R B' R B R2 D' F2", "D L2 D' B R B' D L2 D' B' R' B", "L B D R' U' F2 U R D' L2 B' L'", "B2 U2 L' B L U2 R2 F R F' R B2", "R2 F2 U' F2 D R2 B L' B2 L B D'", "R' D2 L2 F' L2 D2 R F R B' R' F'", "L2 B2 R2 D' R D F D' F' R B2 L2"],
    [29, "B U L U2 L' U' L U2 L' U' B'", "R B' R' B R' U2 R U B U B'", "B L' B L2 U' L' U' L U L' B2", "B U2 B2 U' B U B U2 L' B' L", "L' R D' B' D L B' U B U' R'", "B U' L' B L F' D L D' B2 F", "L' R B2 L U B' U' B U B U' R'", "L' U' L B L F' L' F2 U' F' U B'", "L F' L2 F U F U2 B' U B F' L", "F' U2 F R B U' B' R B' R' B R'", "F R F' L' B' F U' B U R' F' L", "L2 U2 L' F' L F U' F U F' U2 L2", "B F' L F L' B' U2 F2 R' F' R F'", "B' U' B L U L2 R D' B D L R'", "B F D2 F' U L U' L' F D2 B' F'", "R B2 U B' R D B' D' R' B' U' R'", "R U2 F R' F R D R' D' F2 U2 R'", "R2 U' B U L F U' F' L' B' U2 R2", "D' R2 D B' L' B D' R2 D B L B'", "B2 U L2 B' D' B D L B L U' B2", "R' B' D' L U F2 U' L' D R2 B R", "B2 U2 R B' R' U2 L2 F' L' F L' B2", "L2 F2 U F2 D' L2 B' R B2 R' B' D", "L D2 R2 F R2 D2 L' F' L' B L F", "R2 B2 L2 D L' D' F' D F L' B2 R2"],
    [30, "F' U' L' U' L U F U2 F' U' F", "L U F' U' F L' F' L' U L F", "B' F R' F R B F2 U' L' U' L", "B' R B R' U B U B' R' U2 R", "B2 U' B L U2 L' B' U B U B", "L2 R' F R' F D F' D' F' L2 R2", "L U2 L2 U' L2 U' L' F2 R' F' R F'", "R' U2 R U' B U B2 R B R2 U2 R", "R' U' R2 B' R' B' D B' U' B D' B2", "R U' B' U2 B U L' D' B D L R'", "B' D U' R D' B' D R' D' B U B", "F2 R' U2 B' R' B U2 F' L R F' L'", "F D U' B2 U R B2 R' B2 D' R F'", "B' U' B2 L2 R2 F' D F L R2 B' L", "B2 L2 B2 F U R U' R' B2 F' L2 B2", "F R B' F D2 B' D2 L' D2 L B2 F2", "R B L U2 L' B2 R2 F R2 B R' F'", "B U2 B' R2 D' F' L F' L' F2 D R2", "R' F R F' U2 F2 D' B L2 B' D F2", "R U2 L2 D' B' D L2 F U2 F' U R'", "R2 F2 L F' R' D R D' F L' F2 R2", "R' F2 D' L D' L' B' L B D2 F2 R", "L' U' F R2 D2 B D2 R F' R U' L", "R2 F2 L D' F L' F' L D L' F2 R2", "L F2 D2 B R B' D2 L' F2 R U2 R'"],
    [31, "F U R U R' U' F' U2 F U F'", "R' U' F U F' R F R U' R' F'", "B F' L F' L' B' F2 U R U R'", "B L' B' L U' B' U' B L U2 L'", "L U F' U' F L' R B U B' R'", "B2 U B' R' U2 R B U' B' U' B'", "B' U R B' R' B2 L F U' F' L'", "R' F R F' U2 F R' F' R F' U2 F", "R' U2 R2 U R2 U R F2 L F L' F", "B D' U L' D B D' L D B' U' B'", "L U2 L2 U' L2 F' D F' D' F2 U' L'", "L U B2 F R B R' U' B2 F' L' B'", "L' B L2 F2 L B' L' F L' F2 U2 F'", "R B R' F R U2 B' R' F' L' U2 L", "B D' B2 U2 R B' R' B U2 B2 D B'", "F2 L U2 B L B' U2 F L' R' F R", "F' D' U B2 U' L' B2 L B2 D L' F", "R' D' L F2 L' D R2 U B U2 B' R'", "L F' L' F U2 F2 D B' R2 B D' F2", "B' U2 B L2 D F R' F R F2 D' L2", "L' B' R' U2 R B2 L2 F' L2 B' L F", "L2 F2 R' F L D' L' D F' R F2 L2", "R U F' L2 D2 B' D2 L' F L' U R'", "L2 F2 R' D F' R F R' D' R F2 L2", "R' F2 D2 B' L' B D2 R F2 L' U2 L"],
    [32, "B U' B' U' R' U2 R B' R B R'", "B' U B U L U2 L' B L' B' L", "B' L' B' U B2 U' B2 U' B L B", "R' U2 R U B U' L U2 L' U' B'", "L2 U' L' U' F U' F' U L U2 L2", "B U' L F' L F L' U' L' U2 B'", "B' R B R' U' B U2 B' R' U R", "L' B' U B U2 L U' F' L F L'", "D B2 D' R2 U R2 B R B2 R' B'", "B' L' B' L2 U2 L' U B' R' U' R B'", "L U2 F R' U' R F' R' U R U2 L'", "F2 R' F' L R U L' F2 L F U' L'", "R' B' U' F U R2 U' F' U R2 B R", "R B2 L2 B' L2 U' F U' F' U2 B' R'", "L2 U F2 L' F L F U' L2 F' U F", "B2 R D B U B2 D' B2 U' R' U' B", "R B' R B2 L' B2 D B' D' L B2 R2", "B L' B2 R2 D' R' B' D L B R' B", "B L' B' D' R2 D B' L B D' R2 D", "B2 L' D' B' D' R2 D R2 D L U B'", "L' B2 R B' D B D2 R D R2 B2 L", "L2 D R' F' R' D' F' D F R2 D' L2", "R2 D' L F L D F D' F' L2 D R2", "R2 B2 L' D L B' L' B D' L B2 R2", "L2 B2 R D' R' B R B' D R' B2 L2"],
    [33, "L U L2 U' L' B L U L U' B'", "R' U' R2 U R B' R' U' R' U B", "B' U2 B2 U L U' L2 B' L2 U' L'", "R' U' L' R2 B D B D' B2 L R'", "F2 D F' U F D' R' F' R U' F'", "F2 D' F U' F' D L F L' U F", "F R2 D B2 R D2 F L D F2 R", "B U B' L' B2 U B U' B' U' B' L", "F U F' R' F R U' F' U2 F' U2 F", "F' U' F L F' L' U F U2 F U2 F'", "L' R B L U L' U' B' U L U' R'", "L' R B' R' U' R U B U' R' U L", "L' R U R B U B' U' L R' U' R'", "R' F' U F U F' U' L F' L' F2 R", "F' L' U' L F' U B U' F U B' F", "B F U2 F' L U L' U' F U2 B' F'", "B' U' B U2 L2 U F U' F2 L' F L'", "F R U B R' F R B' R' F' U' F'", "F' L' U' B' L F' L' B L F U F", "R U' B' R2 F' R' B R' U' R2 F R", "B' F' D2 B L' U' L U B' D2 B F", "F2 L2 F' R2 F L2 F' R' U R' U' F'", "R2 B2 U' R2 U B2 R2 B R B2 R' B'", "R U2 F D R D' F2 U2 F R U' R2", "B2 L2 F R' D' R D F D' F2 L2 B2"],
    [34, "L U2 L' U' F' L F U' F' L' F", "B' U2 B U R B' R' U R B R'", "L2 R2 B D2 B' L' R F2 L' F' R", "B2 F2 L' D2 L B F' R2 B R F'", "F2 U' F' R U R' U' F' U F2 U F2", "R2 U R F' U' F U R U' R2 U' R2", "F R' F' R' F2 R2 U R U' R F2 R2", "R' F R F R2 F2 U' F' U F' R2 F2", "L U F' L F L' U2 R' U L' U' R", "B' U' R B' R' B U2 F U' B U F'", "F U2 F2 L2 B F L B' L B' U2 B", "R' U2 R2 B2 L' R' B' L B' L U2 L'", "B' F2 R B' F' R2 F R F' R2 B2 F'", "L2 R' F2 L' R' F L F' R F2 L2 R", "F U2 L2 D F D' F' L' F L' U2 F'", "F R' D B2 R B2 R' U' B2 D' U F'", "R' F D' L2 F' L2 F U L2 D U' R", "L2 R' B R' D2 R B' L' F2 L' F' R", "L2 R2 D2 R D2 L2 F R F' R U2 R'", "B2 F2 D2 F' D2 B2 R' F' R F' U2 F", "F R D2 L' U F2 U' L D R2 D F'", "R' F' D2 B U' R2 U B' D' F2 D' R", "F R B R' F' R' D2 L2 F L2 D2 R", "R' F' L' F R F D2 B2 R' B2 D2 F'", "R B2 L D2 L B R2 F R B2 L2 B'"],
    [35, "L U L' U' B' U2 B U L U L'", "R' U' F' U2 L' U' L U' F U R", "R' F' L F2 R' F L' F' R F' R", "B U B' R' U F' L' U' L F R", "F' D' B L' B' D F U' L' U2 L", "F' R' D' F' D L R F' L' U F2", "B L2 D F L D2 B R2 D B2 L", "F' U' F2 R' F' R2 U R' U' R U' R'", "F' U2 F2 U R U' R' F' U' F' U2 F", "L F R U2 R' U2 F' L F' L' F L'", "B R' U R B U' L U2 L2 B L B", "R2 U' R' F R F' U R2 U2 B U' B'", "R2 F' R U' L' U R' F R2 F' L F", "F' R U' B2 L' U L U' B2 U R' F", "L B2 F R2 F R2 B F2 U2 B U2 L'", "L2 B2 L' U F U' F L B2 L' F2 L'", "F' L2 B' R' F U2 F' R B2 L' B' F", "L' U F' U2 F R2 D B' D' R2 U2 L", "B D2 F2 D2 L' B' L F L2 F2 L2 F'", "B2 D L2 F' L' F L' D' B2 R' U2 R", "B L2 D2 R F R' F' D' F D' L2 B'", "B' F2 R F L2 F L F2 R' B D2 F2", "L R2 D2 L' R2 F' L F R2 D2 L' R2", "B L' B D2 L' F R F' L D2 B2 L", "R' U2 R B2 L' D2 F' R F D2 B2 L"],
    [36, "B U L' U' L' B' L U L2 U' L'", "L' U' B U B L B' U' B2 U B", "L2 U2 L' U' F U F' U L U L2", "L' B L B' U' L U2 F U F' L'", "F U2 F' L' U L U F' L F L'", "R' U F U R' F R F' U' F' R", "R' U2 R B U' B' U' R B' R' B", "R' U' R' U' R B U2 B' R' U R2", "F U F U F' L' U2 L F U' F2", "L R' F U' F' L' B' U B U R", "L' R B2 D B' D' B' L R2 U R", "B L F2 R' F' R F' U2 L' U2 B'", "F R' F R F' R U2 R' F' L' U2 L", "L' B' U' B' D' B' D B' U L2 U2 L'", "L U' L' U2 B' R2 F R F' R U' B", "F' L D L' U' L D' F' L' F U F", "B F2 D' L' D F2 U' R U' R' U2 B'", "L2 R D' B D L2 R' U' F' L F L'", "B2 D L' F L U' L' F' L D' U B2", "L2 D' B R' B' U B R B' D U' L2", "B2 D B2 U L U B' U2 B2 L' D' B'", "L' U F D' R2 D F' U2 B U B2 L", "B L2 F' L B L' F L2 B2 R' U2 R", "L2 U2 F2 D F D' L' F U L U L2", "B2 U2 R2 D' R' D B R' U' B' U' B2"],
    [37, "F U F' U F U2 R U R' U' F'", "B' U' B U L U2 L' U' B' U' B", "B L U' L' U L F U F' L' B'", "F R B' R2 F R' B R F' R F'", "R D L' B L D' R' U B U2 B'", "R F D R D' B' F' R B U' R2", "L' B2 D' R' B' D2 L' F2 D' L2 B'", "R U R2 F R F2 U' F U F' U F", "B' R B' R' B2 L U' L' U L U2 L'", "R U2 R2 U' F' U F R U R U2 R'", "L' B' U' B L B L' U L2 U' L' B'", "F R' F R F' R U2 B U2 B' R' F'", "F2 U F R' F' R U' F2 U2 L' U L", "R' F2 R2 B' R B R2 F2 U F' U F", "B L B' U2 F L2 F2 L' F2 L' F' L'", "F U2 F' L D' L B L B' L' D L2", "B' F2 D R' D' R' D R2 D' R' B F2", "B2 L2 B U' R' U R' B' L2 B R2 B", "R B2 L F R' U2 R F' L2 B L R'", "B U' R U2 R' F2 D' L D F2 U2 B'", "L' D2 R2 D2 B L B' R' B2 R2 B2 R", "L2 D' B2 R B R' B D L2 F U2 F'", "L' B2 D2 F' R' F R D R' D B2 L", "L R2 F' R' B2 R' B' R2 F L' D2 R2", "L' B L' D2 B R' F' R B' D2 L2 B'"],
    [38, "R' F' U' F R F R' U R U' F'", "F U' F' U' L2 R B L B' L R'", "R B U' B' R' U' R2 B' R' B R'", "F R' F R F2 U F R U R' F'", "R' U2 B U2 F' U' F U2 B' U' R", "B L F U R U R' F' L' U' B'", "L2 R2 F D F D' F' R F' L2 R", "L' U' L B L' B' U L U L U' L'", "L U L' U L U' L2 B L B2 U B", "F R' F' R U R B' R B R' U' R'", "L' B' U' B U L2 U2 L' U' L U' L'", "L' U L2 U F U' F' L' U L' U2 L", "R' U2 R U2 R U B' R' B R U' R'", "B' U' B L U2 L' U' L2 F' L' F L'", "B L F U' F' L' U L U2 L' U' B'", "R' F' U' F2 U' B' U F' U' B U2 R", "L2 R' F' D' L D L2 U' F U L' R", "F2 L D' F U F' D L' F2 L U' L'", "L2 D' L' D2 R' F' R D' F L' U' F'", "B2 U B' R' U2 R2 D B' D' R' U2 B'", "R U B2 D F' L2 F D' B' U B' R'", "R2 D2 B' U B U' B L B' L' D2 R2", "R2 U B' R' B R2 U2 L' D B2 D' L", "R' U L' B L' D2 F' D2 L2 B' U R", "B D' L2 D B' U2 F2 L F' L' U F2"],
    [39, "F R U R' F' R' F U' F' U R", "R' U R U B2 F' L' B' L B' F", "F U2 L' U2 R U R' U2 L U F'", "L' B' R' U' F' U' F R B U L", "B2 F2 R' D' R' D R F' R B2 F'", "L' B D L' D R F R' D2 L2 B'", "B U B' L' B L U' B' U' B' U B", "B' U' B U' B' U B2 L' B' L2 U' L'", "R' F R F' U' F' L F' L' F U F", "B U' B2 U' R' U R B U' B U2 B'", "B' R' U' R U R' F R B R' F' R", "B L2 F' L' F U' L' U L U L' B'", "B' R' U F' U' B F L' B' R B L", "R' U' F' U2 F R B2 L' B' L U' B'", "L2 B' L F' L' B U' L2 U L' F L", "B D U B D' L' D B' D' L U' B'", "R2 U' R B F' L U L' B' U' F R", "B2 F R D B' D' B2 U R' U' B F'", "F U R F D R D' F' R U' R2 F'", "R2 B' D R' U' R D' B R2 B' U B", "B2 D B D2 F R F' D R' B U R", "L2 U' L F U2 F2 D' L D F U2 L", "F2 D2 L U' L' U L' B' L B D2 F2", "F U' B L' B D2 R D2 B2 L U' F'", "L' D B2 D' L U2 R2 B' R B U' R2"],
    [40, "L' U L U2 L' U' B' U B U L", "F' L' B' F R B' R' B2 F' L F", "R U2 R' U' F D B' R' B D' F'", "R F' L2 B2 L B' L' B' L2 F R'", "F' L' U L B' F2 D R' D' B F'", "R' U' F' U R2 D2 L2 B' L2 D2 R'", "R B' R' B U2 B' U' B2 U' B2 U2 B", "B' U2 B U B' U B2 L U L' U' B'", "B' L' U R' U' R U' L B L' U L", "B' R B' R2 U' R U B2 U2 L U' L'", "L' R2 B2 L R' U B' U' B U B R'", "L' U2 L2 R' F R F2 L' F' L F2 L'", "B' F2 R F D' F' D R' F' R' B F'", "B R B2 U B' U' L' B2 R' B L B2", "L U L' B' U2 B2 F' D L' D' B' F", "R B' R2 F2 R' B R F2 R F' U2 F", "L' D R2 D B D' B' R' B R' D' L", "B U2 F' L' U' F' L' F U L B' F", "B2 F' L2 B' F L' U2 L2 U2 L U2 B'", "L2 R D' B2 D L R' B' U B U L", "L' B' U B U L2 D R' F' R D' L'", "B2 L2 R2 F D' R F' L2 R B U B", "R2 D2 L F' R2 B R B2 R F L' R2", "F' L2 F2 R B R2 F L D2 L F2 R", "B' U2 R D2 L2 D2 R D2 F' L2 D2 R2"],
    [41, "R U' R' U2 R U B U' B' U' R'", "F R B F' L' B L B2 F R' F'", "L' U2 L U F' D' B L B' D F", "L' F R2 B2 R' B R B R2 F' L", "F R U' R' B F2 D' L D B' F", "L' B' R D L B L' D' B L R'", "L U F U' L2 D2 R2 B R2 D2 L", "L' B L B' U2 B U B2 U B2 U2 B'", "B R U' L U L' U R' B' R U' R'", "R U2 L R2 F' L' F2 R F R' F2 R", "R U R U R' F D R' D' F' U2 R'", "B U2 R D B D' R' B U' B' U' B'", "B' L' B2 U' B U R B2 L B' R' B2", "B U2 L' D' L U' L' D L2 U' L' B'", "L' B L2 F2 L B' L' F2 L' F U2 F'", "R D L2 D' B' D B L B' L D' R'", "B' U2 F R U F R F' U' R' B F'", "B2 F R2 B F' R U2 R2 U2 R' U2 B", "L' R2 D B2 D' L R' B U' B' U' R'", "B L2 U L U2 R' D F2 D' R U B'", "F U2 B' F' U2 L2 B2 L B2 L U2 B", "L2 D2 R' F L2 B' L' B2 L' F' L2 R", "B2 L2 R2 F' D L' F L' R2 B' U' B'", "F U F L2 R B' R D' B L2 R2 F2", "F R2 F2 L' B' L2 F' R' D2 R' F2 L'"],
    [42, "R U' R' U' F' U2 F U R U' R'", "B' U' B U B U L' U' B' U L", "B' F R' F' R U R U' R' U' B", "L U L' B' U' B U' L' B L B'", "L F' L' F U L' U L F U' F'", "F' L' F U2 F2 L2 B L B' L2 F2", "R' F2 L2 D' B D' B' D2 L2 F2 R", "R B F L F' U F L' B' F' U' R'", "L2 B' U B U' B' U' R B' R' B2 L2", "B L' B' L2 F2 R' F' R2 U2 R' F' L'", "F D' F2 U2 F' L F L' U2 F2 D F'", "R B L' D' L U2 L' D L B' U2 R'", "F D' R' D F D' R D F2 L' U2 L", "R' F U2 L F' L' U2 F' R2 B' R' B", "R2 B' F2 D' B' D B D F2 R' B R'", "R2 B2 L' B R' B' L B2 R2 F R F'", "B' F R' B2 L F' U2 F L' B' R2 F'", "R2 D B' L R' U L' U' R B D' R2", "L2 R2 D2 L' D2 L2 R2 U B' U B L", "R2 D2 U2 L U' B' U B L' D2 U2 R2", "R' D2 U B2 F2 D2 U2 B2 F U F R", "L2 B2 F2 R' D F D' F' R B2 F2 L2", "F R2 F2 L2 B D2 B' L' F' R2 F2 L'", "F R2 B2 R F L D2 L' F2 R2 B2 R'", "R2 D2 L2 F D2 R' D2 L2 D2 R' U2 B"],
    [43, "L' U L U F U2 F' U' L' U L", "B U B' U' B' U' R U B U' R'", "B F' L F L' U' L' U L U B'", "R' F R F' U' R U' R' F' U F", "R' U' R B U B' U R B' R' B", "F U F2 L F L B L B' U L", "L F R U2 B U B' R' U F' L'", "F R F' U2 F2 R2 B' R' B R2 F2", "L2 R U' L B' U' B U L' R' U L2", "L U F' U B U' F2 U B' U2 F' L'", "F R2 D R D' R F L F L' U F", "B2 D L' F' L B' L F L' B D' B2", "B' R2 B2 U' R' F R F' U B2 R2 B", "F D R F2 U' F U' R' U2 F2 D' F2", "L2 R2 D2 R D2 L2 R2 U' B U' B' R'", "L' B' U2 B U L2 D R' F2 R D' L'", "L' B F' L2 B D2 B' D2 F L2 B' L", "L U F U' B2 F L2 R2 B2 F2 L R2", "F2 L2 R2 B' D B L2 R F' R U' F'", "L2 D2 U2 R' U B U' B' R D2 U2 L2", "B L2 F2 D R F' R' F D' F2 L2 B'", "R2 B2 F2 L D' F' D F L' B2 F2 R2", "L U B2 F' D2 U2 B2 F2 D2 U F' L'", "F' L2 F2 R2 B' D2 B R F L2 F2 R", "F' L2 B2 L' F' R' D2 R F2 L2 B2 L"],
    [44, "R2 B U' B' U B U B2 R' B R'", "R D' B U B' U' R' U' R D R'", "L' D B' U' B U L U L' D' L", "L U L2 B L2 U L' U' B2 U2 B", "R' U' R2 B' R2 U' R U B2 U2 B'", "R' U' B F2 L F L' B' F U R", "L U B' F2 R' F' R B F' U' L'", "R' D' R' D B R2 U R B' U' R'", "L' U' L' B2 D' B' D L B' U L", "R2 B R2 U F R' F' R2 B' U' R'", "B U' L' U L U B' F2 R' F' R F'", "R2 U' L R U' F' U F R' U L' R2", "L F2 D F D' F2 U F' U' L2 U2 L", "L' R F2 L B U B' U' L' F2 L R'", "L U2 F R2 U B U' B' R2 U2 F' L'", "L2 D2 U2 R F' U' F U R' D2 U2 L2", "L2 R' B2 F2 L2 R2 B' F2 U B' U' R'", "L' B' U' B' F2 D2 U2 B2 F2 D2 U' L", "R B U B' U' L2 R D2 U2 L2 R2 D2", "D2 L' B' U' B U L' R2 D2 U2 L2 R2", "D2 L2 R2 D2 U2 L' R2 F U F' U' L'", "L R2 F' D' F R2 B2 L2 U' L2 B2 L'", "L' R2 D2 L2 F L2 D2 R2 U' B U L", "R2 B2 F2 L' B D B' D' L B2 F2 R2", "R B D2 U' B2 F2 D2 U2 B F2 U' R'"],
    [45, "B U L' U' B' U L U L U' L'", "B' U' R U B U' R' U' R' U R", "L F' L F L' U' L' U2 B' U B", "L' F' L' U L U F R U' L R'", "B L U L2 U' L B' U' L' U2 L", "B' R' U' R2 U R' B U R U2 R'", "F U R U' R B' R2 F' R B R'", "F R F' U' R B U B' R' U' R'", "F' L' F U L' B' U' B L U L", "F R B' R' F' U' R U B U' R'", "B' F U R F R' F' U' R' B F'", "R' U' R B U2 L F U F' L' B'", "R U F' U' F U F R' F' R U2 R'", "R B' R' B' U' B R B' U B2 U' R'", "R2 B2 R U' R U R2 B2 R' B' R' B", "R' B' F R' B U R D R D' U' F'", "F2 D' B L B' L U' L' U L' D F2", "R D' R2 U' R2 D B L' B2 L B R'", "F R2 B F2 L U' L' U B' F2 R2 F'", "F2 R2 F L F' R2 F L2 U' L U F", "F2 D F' R B' R' F R' B R D' F2", "B2 D F' L2 F D' B2 U2 B' R B R'", "F2 L2 B L' B' D' B L B' D L2 F2", "F2 R2 B' R B D B' R' B D' R2 F2", "F' L2 B2 D2 R D R' B' D B' L2 F"],
    [46, "B' R B U2 R' U' R U' R2 U2 R", "B' F' U2 F R2 B2 L' B R2 B2 L", "B L' B L B R B R' U R' U R", "L' U' L' B L B' L' B L B' U L", "B L U' L' B' R' U' R U R' U R", "L' U' L U' L' U2 L2 F U F' U' L'", "L' B' U R' U' R U R' U' R B L", "R U R2 F R F' L F' U F U' L'", "B U B2 R B R2 U F' U' F U R", "B' R' U' R U B F R U R' U' F'", "B U B' U R2 F R F2 U' F U R", "R' F R B' R2 F' R F R' F' R2 B", "R U2 B U2 B U2 B2 U' B2 U' B2 R'", "L' B2 R B' L B2 R' B' R B R' B", "B' U2 B L' B L U B2 U B2 U2 B'", "B' R B2 L U' L' U2 B' U' R2 U2 R", "B L2 D L D2 B D B U' B U L", "B' R2 F R' D R D' R2 B R' F' R", "B' R2 F2 R F2 R U F U' B U2 F'", "F U2 F2 L F2 R F' L' F R' U2 F'", "L2 F2 L2 F' U2 B F L' B' L2 F2 L'", "R B' L2 B' D B D' L2 B R2 U R", "L2 D R' F2 R D' L2 B2 R B R' B", "F D2 B2 R B R' D' B2 D' F' U R2", "L' B2 R2 D' R' B' D L B2 R' U B"],
    [47, "F R' F' U2 R U R' U R2 U2 R'", "B F U2 B' R2 F2 L F' R2 F2 L'", "F' L F' L' F' R' F' R U' R U' R'", "L U L F' L' F L F' L' F U' L'", "L U L' U L U2 L2 B' U' B U L", "L F U' R U R' U' R U R' F' L'", "R' U' R2 B' R' B L' B U' B' U L", "F R U R' U' B' F' R' U' R U B", "L' B' U B L F U' R U R' U' F'", "F' U' F U' R2 B' R' B2 U B' U' R'", "R B' R' F R2 B R' B' R B R2 F'", "L F2 R' F L' F2 R F R' F' R F'", "F U2 F' L F' L' U' F2 U' F2 U2 F", "F' L2 D' L' D2 F' D' F' U F' U' L'", "F R2 B' R D' R' D R2 F' R B R'", "F R2 B2 R' B2 R' U' B' U F' U2 B", "F U F2 L' F U2 L2 B L2 B' U' L", "B' U2 B2 L' B2 R' B L B' R U2 B", "L2 B2 L2 B U2 B' F' L F L2 B2 L", "L2 B2 L' F R' F L R B2 L' F2 L'", "R' F L2 F D' F' D L2 F' R2 U' R'", "L2 D' R B2 R' D L2 F2 R' F' R F'", "B' D2 F2 R' F' R D F2 D B U' R2", "L F2 R2 D R F D' L' F2 R U' F'", "L2 F2 R2 B' D2 B F L' F' R2 F2 L'"],
    [48, "R' U' R2 B' R' B U' B' R B R'", "L U F U2 F' U2 L' U' B' U2 B", "B' U2 B U L U2 F U2 F' U' L'", "F R U R' U' F2 U' L' U L F", "R' F R' D R' D' R2 F2 U' F R", "R U2 L' R' F' U2 B' U2 B F L", "F' D' L U' L U L' D F2 U2 F'", "F2 R2 F' R2 F2 L F L' R' U2 R", "L F' L2 B' F2 R2 F R2 B F2 L", "L B' U2 F R' U R F' U2 B L'", "B' L U2 R' F U F' R U2 L' B", "L B2 F R2 B R2 B2 F' L2 B' L", "F U2 F' U' L2 D' R B' R' D L2", "L U L' U L U' L' B' R' U' R B", "R' F' L' F R F' L U' L' U L F", "B U2 B2 U' B2 U' L' B' L B' U2 B", "F2 U' F L F' U F U' L2 U L F", "L' B2 L2 B' U2 B2 U2 B L' R' U2 R", "F U2 B' U F' U' R' F2 R' F2 R2 B", "L2 B2 L' F2 L B2 L' R' F' R F' L'", "B L F' L B2 U2 B F2 U2 F L2 F2", "F2 U' L D R2 D F R' F' R2 D2 L'", "L R2 D2 B2 L2 B L2 B D2 R2 F' L'", "L' F2 D2 B D2 F L2 D2 B' D2 F L'", "L' B D2 F' D2 L2 B D2 F D2 B2 L'"],
    [49, "R U R2 F R F' U F R' F' R", "L' U' B' U2 B U2 L U F U2 F'", "F U2 F' U' L' U2 B' U2 B U L", "B' R' U' R U B2 U L U' L' B'", "R B' R D' R D R2 B2 U B' R'", "R' U2 L R B U2 F U2 B' F' L'", "B D L' U L' U' L D' B2 U2 B", "B2 R2 B R2 B2 L' B' L R U2 R'", "L' F2 L2 B L2 B' F2 L R U2 R'", "L' B L2 B2 F R2 B' R2 B2 F' L'", "F L' U2 R B' U' B R' U2 L F'", "L' F U2 B' R U' R' B U2 F' L", "B L' B' R B2 D L' D' L2 B2 R'", "B' U2 B U L2 D R' F R D' L2", "F R' F R F' R U' B U2 B' R' F'", "B' U F U' B U2 R' F R F' U' F'", "R B L B' R' B L' U L U' L' B'", "B L2 U L2 B' L B L U' L B' L", "F U2 B' R B R' F' R' F2 R' F2 R2", "R' F' L F' L' F2 R2 U B U' B' R'", "L F2 L2 F U2 F2 U2 F' L R U2 R'", "L2 F2 L B2 L' F2 L R B R' B L", "F' L' B L' F2 U2 B2 F' U2 B' L2 B2", "B2 U L' D' R2 D' B' R B R2 D2 L", "L F' D2 B D2 L2 F' D2 B' D2 F2 L"],
    [50, "B U B L' B' L B' U B U2 B'", "F' U' F' L F L' F U' F' U2 F", "L F' L F L' U' L' U B' U2 B", "B' U2 B U' L U L F' L' F L'", "F U R' U' F' U R U2 R U2 R'", "B' U' R U B U' R' U2 R' U2 R", "L' F L U' R U2 R' U L' F' L", "R' U2 R U2 R B' R2 U' R U B", "B' U F' R' F U2 F' R F U' B", "F U' B R B' U2 B R' B' U F'", "F2 D B' R' B D' F2 U' L' U2 L", "B2 D' F R F' D B2 U L U2 L'", "L' B U B2 U B2 U' L U' L' B' L", "L' U' L2 U L F' L2 F U L U2 L'", "B' U2 B U R B2 R' B U B2 U' B'", "R' U' R2 B L' B L B2 R' B U' B'", "L F U' R' F R F2 L' U B' U2 B", "F U F2 L F2 U F' L2 U L2 U2 L'", "L2 U L U' F' U' L' U L2 F2 U2 F'", "F U2 B' R' U' R2 U R F R2 B F2", "B' U2 B2 L2 U L' U' L2 D L D' B'", "B' U2 B2 F' L D L2 D' L' B' L2 F", "F' U' L2 D' L U L2 D L' F2 U' F'", "B L2 F' L' D' L2 D L B' F2 U2 F'", "B D F2 D F2 D' L' D' L B2 U2 B"],
    [51, "L' U' B' U2 B U2 B' U2 B U L", "L U F U2 F' U2 F U2 F' U' L'", "R U B U' B2 R' B U2 B U2 B'", "R' U' F' U F2 R F' U2 F' U2 F", "R U2 R2 D' F U' F' U F' D R", "R' U2 R2 D B' U B U' B D' R'", "L U L' U L' B L B R B R' B", "L' U' L U' L F' L' F' R' F' R F'", "R' F' U' F2 U F' U F U2 F' U' R", "R B L U' L' U L U' L' U B' R'", "L' U' B' U B2 L' B' L2 U' F U' F'", "B L U L2 B L B2 U' B' R B R'", "L F2 U F2 U F2 U2 F' U2 F' U2 L'", "L R2 D' F' D F' R F R' F L' R2", "L' R2 D B D' B R' B' R B' L R2", "L2 R B' L B' L' B D' B D L2 R'", "L2 R' F L' F L F' D F' D' L2 R", "L2 R B' D' B D' R D R' D L2 R'", "L' R2 D L' D L D' B D' B' L R2", "F R' F D' F D F2 R2 U2 R' U' F'", "B' R B' D B' D' B2 R2 U2 R U B", "R B U B2 R2 D' R' D B R' U' R'", "R' U2 R2 B' D B D L2 D' L2 D' R'", "L U B L2 F' L2 B' F2 U2 F' U' L'", "R U B' R2 F D R' B' D' B2 R2 F'"],
    [52, "R' F' L F' L' F L F' L' F2 R", "B' R B R' U' R B' R' B2 U' B'", "B' R2 F R F' R' F R F' R B", "R B U' B2 R2 D' R' D R' B R'", "B R' U' F' U R B2 R' F R B", "B' U' B L U' L' U' L2 F' L' F L'", "L' U R U' L U' R' U2 R' F R F'", "R' F' U' F2 U R U' F' U2 F' U2 F", "L U F' U' F L' F R' F' R2 U' R'", "L U2 L' B' R' U' R B' R B R' B", "F' U2 F U2 F U R' U' F2 U F R", "F R B U2 B' U R' F R' F' R F'", "F R' F R F2 R U' L' U R' U2 L", "L R' U' R U L' U2 B2 L' B' L B'", "B U' L' B L B2 U' B2 L' B' L B'", "B' U R' U' R B U L2 F' L' F L'", "R' U F' U2 F2 R' F' R2 U2 B U B'", "F2 U2 L F L' F2 U' F2 U' F' U2 F'", "B U2 F' L' B L B2 F U' B U' B'", "L' U' L U' L2 R B L B' R' U2 L", "R' U2 R2 U R2 F' U F2 R F2 U F", "R' U' R2 B U B2 D B' D' B2 U' R'", "F' L U2 B L' B2 U2 B L2 F' L F2", "B' R2 B' F R D2 R D2 R' D2 B2 F'", "F R B2 D2 L' F2 L' F2 L2 D2 B2 F'"],
    [53, "R B L' B L B' L' B L B2 R'", "F R' F' R U R' F R F2 U F", "R' F' U F2 R2 D R D' R F' R", "F U F' L' U L U L2 B L B' L", "L U' R' U L' U R U2 R B' R' B", "R B U B2 U' R' U B U2 B U2 B'", "L' U' B L' B' L2 B L' U L U' B'", "B U2 B' U2 B' U' R U B2 U' B' R'", "B' R' F' U2 F U' R B' R B R' B", "L' R U R' U' L U2 F2 L F L' F", "B' R B' R' B2 R' U L U' R U2 L'", "F' U L F' L' F2 R' F R F2 U F", "F U' R U R' F' U' L2 B L B' L", "R U' B U2 B2 R B R2 U2 F' U' F", "B2 U2 L' B' L B2 U B2 U B U2 B", "L U L' U L2 R' F' L' F R U2 L'", "F' U2 B L F' L' B' F2 U F' U F", "R U2 R2 U' R2 B U' B2 R' B2 U' B'", "B U' L' F U' F2 L F2 U F' L B'", "B U R' U2 R B2 L' B2 L2 U' L' B'", "R B U B2 R2 B R2 F' U2 F U' R'", "R U R2 F L2 D' F D F' L2 F' R", "B L' U2 F' L F2 U2 F' L2 B L' B2", "F R2 B' F R' D2 R' D2 R D2 B F2", "B' R' F2 D2 L B2 L B2 L2 D2 B F2"],
    [54, "L U2 L2 U' L U' L' U2 B L B'", "R' U2 R2 U R' U R U2 B' R' B", "R B U' L U L2 B' R' B L B'", "L' B' U R' U' R2 B L B' R' B", "L D' L2 U B' U2 B U' L2 D L'", "L' D L2 U' F U2 F' U L2 D' L", "L U' F2 D F' U2 F D' F2 U L'", "L' U B2 D' B U2 B' D B2 U' L", "R B2 L2 D L D' B2 R' B L B'", "L' B2 R2 D' R' D B2 L B' R' B", "B L' U' B' U B2 L B2 U' B U B'", "F' L U F U' F2 L' F2 U F' U' F", "B L' B U' B L B L' B2 U B2 L", "B L' U' L2 U' L2 U2 B L B' U' B'", "F' L F' U F' L' F' L F2 U' F2 L'", "B' R U R2 U R2 U2 B' R' B U B", "R' U2 R2 U B U2 L U L' B2 R' B", "L U2 L2 U' B' U2 R' U' R B2 L B'", "B L2 F' L' B' F2 U F' U' B L' B'", "B' R2 F R B F2 U' F U B' R B", "R B2 L' D B D2 R D R2 B2 L B'", "L' B2 R D' B' D2 L' D' L2 B2 R' B"],
    [55, "L F R F' L2 F U R' U' F' L", "R' F' L' F R2 F' U' L U F R'", "R B' R' B U2 R' U R U' B U2 B'", "L' B L B' U2 L U' L' U B' U2 B", "F R U R' U' R F' L F R' F' L'", "F' L' U' L U L' F R' F' L F R", "R U2 L' U R' U' L F2 L F L' F", "R' U2 L U' R U L' B2 L' B' L B'", "L F L' U R U' L R2 F R F2 L'", "L' B' L U' R' U L' R2 B' R' B2 L", "F' U' L U2 L U' L U L' U2 L' U' F", "F U R' U2 R' U R' U' R U2 R U F'", "B U L U' F U' F' L' U' L U L' B'", "B' U' R' U F' U F R U R' U' R B", "F R U R' U2 R' U2 R U F' R' U R", "F' L' U' L U2 L U2 L' U' F L U' L'", "R B' R' B U2 B U' B L' B' L U' B'", "L' B L B' U2 B' U B' R B R' U B", "F R U R' U2 B U B' F' U2 B U B'", "B' R' U' R U2 F' U' B F U2 F' U' F", "B U' R' U L2 U' R U L' U L' U' B'"],
    [56, "L U' L' U L R' F' L F L2 R", "L' R' U L U' L' R B L' B' L2", "L U L' B' F U R' U' R B F'", "R U B' U' B R' U B L' B' L", "R' U' F U ' R U' F' L F L'", "F2 L F L' F R U R' F' U' F", "F2 R' F' R F' L' U' L F U F'", "R B L U' L' B' U2 B U B' R'", "L' U' L' B' U' B U L2 U2 L' U' L", "F R U2 R' U F' L F' L' F2 U F'", "F' L' U2 L U' F R' F R F2 U' F", "R U2 R' U' R B U2 B' R' F' U F", "B U' B' L' R B2 R' U' B U B2 L", "R B U' B' U2 L R2 D' F D L' R", "L' U B2 F D' R' D B' F' L' B' L2", "F U L F' D R' F' R' D R2 D2 L'", "F L' D2 U2 R U' R' D2 U2 L U F'", "F R U2 R2 F2 D' F' D F' R U2 F'", "L U2 F' L D' L D L2 F2 U2 F' L'", "F' R U F R' D2 L2 D L' F' L' D", "D' B R' U' B' R D2 L2 D' L B L", "F2 U F2 R B L' U2 L B' R' U' F2", "B' R B2 F2 L' D L B2 F2 R' U' B", "L2 D' B2 D L2 B F R U2 R' B' F'", "B2 D' R2 F' L' B U2 B' L F D B2"]
]

# alg subsets for training mode
caseGroups = {
    'edgesOriented' : [ollScrambles[20], ollScrambles[21], ollScrambles[22], ollScrambles[23], ollScrambles[24], ollScrambles[25], ollScrambles[26]],             # All Edges Oriented Correctly:     21, 22, 23, 24, 25, 26, 27
    'tCases' : [ollScrambles[32], ollScrambles[44]],                                                                                                              # T-Shapes:                         33, 45
    'squareCases' : [ollScrambles[4], ollScrambles[5]],                                                                                                           # Squares:                          5, 6
    'cornersOriented' : [ollScrambles[27], ollScrambles[56]],                                                                                                     # Corners Correct, Edges Flipped:   28, 57
    'lightningCases' : [ollScrambles[6], ollScrambles[7], ollScrambles[10], ollScrambles[11], ollScrambles[38], ollScrambles[39]],                                # Lightning Bolts:                  7, 8, 11, 12, 39, 40
    'pCases' : [ollScrambles[30], ollScrambles[31], ollScrambles[42], ollScrambles[43]],                                                                          # P-Shapes:                         31, 32, 43, 44
    'cCases' : [ollScrambles[33], ollScrambles[45]],                                                                                                              # C-Shapes:                         34, 46
    'fishCases' : [ollScrambles[8], ollScrambles[9], ollScrambles[34], ollScrambles[36]],                                                                         # Fish-Shapes:                      9, 10, 35, 37
    'lCases' : [ollScrambles[46], ollScrambles[47], ollScrambles[48], ollScrambles[49], ollScrambles[52], ollScrambles[53]],                                      # L-Shapes:                         47, 48, 49, 50, 53, 54
    'wCases' : [ollScrambles[35], ollScrambles[37]],                                                                                                              # W-Shapes:                         36, 38
    'iCases' : [ollScrambles[50], ollScrambles[51], ollScrambles[54], ollScrambles[55]],                                                                          # I-Shapes:                         51, 52, 55, 56
    'knightMoveCases' : [ollScrambles[12], ollScrambles[13], ollScrambles[14], ollScrambles[15]],                                                                 # Knight Move Shapes:               13, 14, 15, 16
    'awkwardCases' : [ollScrambles[28], ollScrambles[29], ollScrambles[40], ollScrambles[41]],                                                                    # Awkward Shapes:                   29, 30, 41, 42
    'dotCases' : [ollScrambles[0], ollScrambles[1], ollScrambles[2], ollScrambles[3], ollScrambles[16], ollScrambles[17], ollScrambles[18], ollScrambles[19]]     # Dot:                              1, 2, 3, 4, 17, 18, 19, 20
}


# set main
if __name__ == '__main__': main()
