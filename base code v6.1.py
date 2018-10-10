import turtle as e

#credits
print('Created by year 10 student Rodrigo Nunes with help from Ross Woollard')
print('\n')



e.hideturtle()
e.goto(-150, 0)
yes = 0
e.speed(0)

draw = False
move = False
win = False
# ---------------------------
bl_ai = False
br_ai = False
bm_ai = False

ml_ai = False
mr_ai = False
mm_ai = False

tl_ai = False
tr_ai = False
tm_ai = False

first_try = True

bltr = False
bltl = False
bltm = False

blbr = False 
blbl = False
blbm = False

blmr = False
blml = False
blmm = False

#coords of boxes
tm = (0,-50)
tl = (-100,-50)
tr = (100, -50)

mm = (0,-150)
ml = (-100,-150)
mr = (100, -150)

bm = (0,-250)
bl = (-100,-250)
br = (100, -250)

#box active/not active

topl =False
topm =False
topr =False

midl =False
midm =False
midr =False

botl = False
botm = False
botr = False

# box filled with usr

topl_usr = False
topr_usr = False
topm_usr = False

botr_usr = False
botl_usr = False
botm_usr = False

midm_usr = False
midl_usr = False
midr_usr = False

# game functions
def sqr():
    for i in range(4):
        e.forward(100)
        e.right(90)
    e.forward(100)

def ai_win():
    global win
    
    e.up()
    e.goto(-325,50)
    e.down()
    e.write('Ha You Lost', font=('Consolas', 100))
    win = True

def cross():
    e.left(45)
    e.forward(50)
    e.back(50)
    e.right(90)
    e.forward(50)
    e.back(50)
    e.right(90)
    e.forward(50)
    e.back(50)
    e.right(90)
    e.forward(50)
    e.back(50)
    e.right(45)
    


def circle():
    e.down()
    e.circle(20, 360, 20)

for i in range(3):
    for i in range(3):
        sqr()
    yes += 100

    e.up() 
    e.goto(-150,-yes)
    e.down()

# user functions
def usr():
    global topl_usr
    global topm_usr
    global topr_usr

    global midl_usr
    global midm_usr
    global midr_usr

    global botl_usr
    global botm_usr
    global botr_usr
    
    global topl
    global topm
    global topr

    global midl
    global midm
    global midr

    global botl
    global botm
    global botr
    
    
    try:
        des = input("where would you like to place your cross?\nEG tl(top left) tm(top middle) tr(top right)")
        if topm == False:
            if des == 'tm':
                e.up()
                e.goto(tm)
                e.down()
                cross()
                topm = True
                topm_usr = True
            
        if topl == False:
            if des == 'tl':
                e.up()
                e.goto(tl)
                e.down()
                cross()
                topl = True
                topl_usr = True
                
        if topr == False:
            if des == 'tr':
                e.up()
                e.goto(tr)
                e.down()
                cross()
                topr = True
                topr_usr = True
                
        if botm == False:
            if des == 'bm':
                e.up()
                e.goto(bm)
                e.down()
                cross()
                botm = True
                botm_usr = True
                
        if botl == False:
            if des == 'bl':
                e.up()
                e.goto(bl)
                e.down()
                cross()
                botl = True
                botl_usr = True
                
        if botr == False:
            if des == 'br':
                e.up()
                e.goto(br)
                e.down()
                cross()
                botr = True
                botr_usr = True

        if midm == False:
            if des == 'mm':
                e.up()
                e.goto(mm)
                e.down()
                cross()
                midm = True
                midm_usr = True

        if midl == False:
            if des == 'ml':
                e.up()
                e.goto(ml)
                e.down()
                cross()
                midl = True
                midl_usr = True

        if midr == False:
            if des == 'mr':
                e.up()
                e.goto(mr)
                e.down()
                cross()
                midr = True
                midr_usr = True

    except:
        print('error found - user')

# ai functions
def ai_win_check():
    global topl
    global topm
    global topr

    global midl
    global midm
    global midr

    global botl
    global botm
    global botr

    global tl_ai
    global tm_ai
    global tr_ai
    
    global ml_ai
    global mm_ai
    global mr_ai

    global bl_ai
    global bm_ai
    global br_ai
    
    if topl == False:
        if tr_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
                
        if tm_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
    if topr == False:
        if tl_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
                
        if tm_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
    if topm == False:
        if tl_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()
                
        if tr_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()

    if midl == False:
        if tr_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
                
        if tm_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
    if midr == False:
        if tl_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
                
        if mm_ai == True:
            if ml_ai == True:
                e.up()
                e.goto(mr)
                e.down()
                circle()
                ai_win()
    if botm == False:
        if bl_ai == True:
            if br_ai == True:
                e.up()
                e.goto(bm)
                e.down()
                circle()
                ai_win()
                
        if br_ai == True:
            if bl_ai == True:
                e.up()
                e.goto(bm)
                e.down()
                circle()
                ai_win()

    if botr == False:
        if bl_ai == True:
            if bm_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()
                
        if bm_ai == True:
            if bl_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()
    if botm == False:
        if bl_ai == True:
            if br_ai == True:
                e.up()
                e.goto(bm)
                e.down()
                circle()
                ai_win()
                
        if br_ai == True:
            if bl_ai == True:
                e.up()
                e.goto(bm)
                e.down()
                circle()
                ai_win()

    if topm == False:
        if tl_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()
                
        if tr_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()

    if topr == False:
        if tl_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
                
        if tm_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
    if topm == False:
        if tl_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()
                
        if tr_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()


#####################################
    if topr == False:
        if mr_ai == True:
            if br_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
                
        if br_ai == True:
            if mr_ai == True:
                e.up()
                e.goto(tr)
                e.down()
                circle()
                ai_win()
    if midr == False:
        if br_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(mr)
                e.down()
                circle()
                ai_win()
                
        if tr_ai == True:
            if br_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()

    if botr == False:
        if mr_ai == True:
            if tr_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()
                
        if tr_ai == True:
            if mr_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()


    if topm == False:
        if mm_ai == True:
            if bm_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()
                
        if bm_ai == True:
            if mm_ai == True:
                e.up()
                e.goto(tm)
                e.down()
                circle()
                ai_win()
    if midm == False:
        if bm_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()
                
        if tm_ai == True:
            if bm_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()

    if botl == False:
        if ml_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(bl)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if ml_ai == True:
                e.up()
                e.goto(bl)
                e.down()
                circle()
                ai_win()


    if topl == False:
        if ml_ai == True:
            if bl_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
                
        if bl_ai == True:
            if ml_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
    if midl == False:
        if bl_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(ml)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if bl_ai == True:
                e.up()
                e.goto(ml)
                e.down()
                circle()
                ai_win()

    if botl == False:
        if ml_ai == True:
            if tm_ai == True:
                e.up()
                e.goto(bl)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if ml_ai == True:
                e.up()
                e.goto(bl)
                e.down()
                circle()
                ai_win()


    if topl == False:
        if mm_ai == True:
            if br_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
                
        if br_ai == True:
            if mm_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
    if midm == False:
        if br_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if br_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()

    if botr == False:
        if mm_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if mm_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()


    if topl == False:
        if mm_ai == True:
            if br_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
                
        if br_ai == True:
            if mm_ai == True:
                e.up()
                e.goto(tl)
                e.down()
                circle()
                ai_win()
    if midm == False:
        if br_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if br_ai == True:
                e.up()
                e.goto(mm)
                e.down()
                circle()
                ai_win()

    if botr == False:
        if mm_ai == True:
            if tl_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()
                
        if tl_ai == True:
            if mm_ai == True:
                e.up()
                e.goto(br)
                e.down()
                circle()
                ai_win()





















def ai():
    global move
    
    global first_try
    
    global bltr
    global bltl
    global bltm

    global blbm
    global blbr
    global blbl

    global blmm
    global blml
    global blmr
    
    global topl
    global topm
    global topr

    global midl
    global midm
    global midr

    global botl
    global botm
    global botr

    global tl_ai
    global tm_ai
    global tr_ai
    
    global ml_ai
    global mm_ai
    global mr_ai

    global bl_ai
    global bm_ai
    global br_ai
    
    global topl_usr
    global topm_usr
    global topr_usr
    
    global midl_usr
    global midm_usr
    global midr_usr

    global botl_usr
    global botm_usr
    global botr_usr



    if first_try == True:
        e.up()
        e.goto(mm)
        e.down()
        circle()
        move = False
        midm = True
        first_try = False

# Top row block
    if move == True:
        if topm == False:
            if topr_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(tm)
                    e.down()
                    circle()
                    topm = True
                    bltr = True
                    tm_ai = True
                    move = False
            if topl_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(tm)
                    e.down()
                    circle()
                    topm = True
                    bltl = True
                    tm_ai = True
                    move = False
    if move == True:
        if topl == False:
            if topr_usr == True:
                if topm_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltr = True
                    tl_ai = True
                    move = False
            if topm_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltm = True
                    tl_ai = True
                    move = False
    if move == True:
        if topr == False:
            if topl_usr == True:
                if topm_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltm = True
                    tr_ai = True
                    move = False
            if topm_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    tr_ai = True
                    move = False
    # Middle row block
    if move == True:
        if midm == False:
            if midr_usr == True:
                if midl_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmr = True
                    mm_ai = True
                    move = False
            if midl_usr == True:
                if midr_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blml = True
                    mm_ai = True
                    move = False
    if move == True:
        if midl == False:
            if midr_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(ml)
                    e.down()
                    circle()
                    midl = True
                    blmr = True
                    ml_ai = True
                    move = False
            if midm_usr == True:
                if midr_usr == True:
                    e.up()
                    e.goto(ml)
                    e.down()
                    circle()
                    midl = True
                    blmm = True
                    ml_ai = True
                    move = False
    if move == True:
        if midr == False:
            if midl_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(mr)
                    e.down()
                    circle()
                    midr = True
                    blmm = True
                    mr_ai = True
                    move = False
            if midm_usr == True:
                if midl_usr == True:
                    e.up()
                    e.goto(mr)
                    e.down()
                    circle()
                    midr = True
                    blmr = True
                    mr_ai = True
                    move = False
    # Bottom row block
    if move == True:
        if botm == False:
            if botr_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(bm)
                    e.down()
                    circle()
                    botm = True
                    blbr = True
                    bm_ai = True
                    move = False
            if botl_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(bm)
                    e.down()
                    circle()
                    botm = True
                    blbl = True
                    bm_ai = True
                    move = False
    if move == True:
        if botl == False:
            if botr_usr == True:
                if botm_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbr = True
                    bl_ai = True
                    move = False
            if botm_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbm = True
                    bl_ai = True
                    move = False
    if move == True:   
        if botr == False:
            if botl_usr == True:
                if botm_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbm = True
                    br_ai = True
                    move = False
            if botm_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbr = True
                    br_ai = True
                    move = False
    # left side vertical block
    if move == True:
        if topl == False:
            if midl_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltl = True
                    tl_ai = True
                    move = False
            if botl_usr == True:
                if midl_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltl = True
                    tl_ai = True
                    move = False
    if move == True:            
        if midl == False:
            if topl_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(ml)
                    e.down()
                    circle()
                    midl = True
                    blml = True
                    ml_ai = True
                    move = False
            if botl_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(ml)
                    e.down()
                    circle()
                    topl = True
                    bltl = True
                    ml_ai = True
                    move = False
    if move == True:
        if botl == False:
            if topl_usr == True:
                if midl_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbl = True
                    bl_ai = True
                    move = False
            if midl_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbl = True
                    move = False

    # right side vertical block
    if move == True:
        if topr == False:
            if midr_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    tr_ai = True
                    move = False
            if botr_usr == True:
                if midr_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    tr_ai = True
                    move = False
    if move == True:             
        if midr == False:
            if topr_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(mr)
                    e.down()
                    circle()
                    midr = True
                    blmr = True
                    mr_ai = True
                    move = False
            if botr_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(mr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    mr_ai = True
                    move = False
    if move == True:
        if botr == False:
            if topr_usr == True:
                if midr_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbr = True
                    bl_ai = True
                    move = False
            if midr_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbr = True
                    bl_ai = True
                    move = False
                
    # middle vertical block
    if move == True:
        if topm == False:
            if midm_usr == True:
                if botm_usr == True:
                    e.up()
                    e.goto(tm)
                    e.down()
                    circle()
                    topm = True
                    tmtm = True
                    bl_ai = True
                    move = False
            if botm_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(tm)
                    e.down()
                    circle()
                    topm = True
                    bltm = True
                    tmtm = True
                    move = False
    if move == True:                    
        if midm == False:
            if topm_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmm = True
                    mm_ai = True
                    move = False
            if botm_usr == True:
                if topm_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    topm = True
                    bltm = True
                    mm_ai = True 
                    move = False
    if move == True:
        if botm == False:
            if topm_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(bm)
                    e.down()
                    circle()
                    botm = True
                    blbm = True
                    bm_ai = True
                    move = False
            if midm_usr == True:
                if topm_usr == True:
                    e.up()
                    e.goto(bm)
                    e.down()
                    circle()
                    botm = True
                    blbm = True
                    bm_ai = True
                    move = False
    # across block left to right
    if move == True:
        if topl == False:
            if midm_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltl = True
                    tl_ai = True
                    move = False
            if botr_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(tl)
                    e.down()
                    circle()
                    topl = True
                    bltl = True
                    tl_ai = True
                    move = False
    if move == True:
        if botr == False:
            if midm_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbr = True
                    br_ai = True
                    move = False
            if topl_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(br)
                    e.down()
                    circle()
                    botr = True
                    blbr = True
                    br_ai = True
                    move = False
    if move == True:
        if midm == False:
            if botr_usr == True:
                if topl_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmm = True
                    mm_ai = True
                    move = False
            if topl_usr == True:
                if botr_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmm = True
                    mm_ai = True
                    move = False

    # across right to left
    if move == True:
        if topr == False:
            if midm_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    tr_ai = True
                    move = False
            if botl_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(tr)
                    e.down()
                    circle()
                    topr = True
                    bltr = True
                    tr_ai = True
                    move = False
    if move == True:
        if botl == False:
            if midm_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbl = True
                    bl_ai = True
                    move = False
            if topr_usr == True:
                if midm_usr == True:
                    e.up()
                    e.goto(bl)
                    e.down()
                    circle()
                    botl = True
                    blbl = True
                    bl_ai = True
                    move = False
    if move == True:
        if midm == False:
            if botl_usr == True:
                if topr_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmm = True
                    mm_ai = True
                    move = False
            if topr_usr == True:
                if botl_usr == True:
                    e.up()
                    e.goto(mm)
                    e.down()
                    circle()
                    midm = True
                    blmm = True
                    mm_ai = True
                    move = False


# ai move
    if move == True:
        if midl == False:
            e.up()
            e.goto(ml)
            e.down()
            circle()
            midl = True
            ml_ai = True
            move = False
    
    if move == True:
        if topr == False:
            e.up()
            e.goto(tr)
            e.down()
            circle()
            topr = True
            tr_ai = True
            move = False
    if move == True:
        if topl == False:
            e.up()
            e.goto(tl)
            e.down()
            circle()
            topl = True
            tl_ai = True
            move = False
    if move == True:
        if topm == False:
            e.up()
            e.goto(tm)
            e.down()
            circle()
            topm = True
            tm_ai = True
            move = False
            
    if move == True:
        if botr == False:
            e.up()
            e.goto(br)
            e.down()
            circle()
            botr = True
            br_ai = True
            move = False
    if move == True:
        if botl == False:
            e.up()
            e.goto(bl)
            e.down()
            circle()
            botl = True
            bl_ai = True
            move = False
    if move == True:
        if botm == False:
            e.up()
            e.goto(bm)
            e.down()
            circle()
            botm = True
            bm_ai = True
            move = False
            
    if move == True:
        if midr == False:
            e.up()
            e.goto(mr)
            e.down()
            circle()
            midr = True
            mr_ai = True
            move = False
    if move == True:
        if midl == False:
            e.up()
            e.goto(ml)
            e.down()
            circle()
            midl = True
            ml_ai = True
            move = False
    if move == True:
        if midm == False:
            e.up()
            e.goto(mm)
            e.down()
            circle()
            midm = True
            mm_ai = True
            move = False
    move = True

def draw():
    global draw
    
    global topl
    global topm
    global topr

    global midl
    global midm
    global midr

    global botl
    global botm
    global botr
    
    if botl == True:
        if botr == True:
            if botm == True:
                if midl == True:
                    if midr == True:
                        if midm == True:
                            if topl == True:
                                if topr == True:
                                    if topm == True:
                                        e.up()
                                        e.goto(-625,50)
                                        e.down()
                                        e.write('Is that really the best you can do', font=('Consolas', 50))
                                        draw = True
                                        
                            
                
        





# ------------
while True:
    ai_win_check()
    if win == True:
        break
    if draw == True:
        break
    ai()
    draw()
    usr()

    





