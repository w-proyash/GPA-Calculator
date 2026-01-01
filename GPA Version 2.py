#Group Identification

Group = input('Which group do you read in? : ')

print("\nNote: With digit method, you have to input your practical marks\nbut with percentage method, you can't enter practical marks.\nBut without practical marks, the grade may be a bit inaccurate.")

way = input('\nDo you want to determine result in digit method or percentage method? (digit/percent): ')

#Marks Input
print('Enter your obtained marks')

Bng_1 = int(input('Bangla 1st paper: '))
Bng_2 = int(input('Bangla 2nd paper: '))
Eng_1 = int(input('English 1st paper: '))
Eng_2 = int(input('English 2nd paper: '))
GM = int(input('General Maths: '))
Reli = int(input('Religion: '))
BGS = int(input('BGS: '))
ICT = int(input('ICT: '))
Eng = Eng_1 + Eng_2
Bng = Bng_1 + Bng_2

if Group == 'Science' or 'science' or 'SCIENCE' or 's':
    Phy = int(input('Physics: '))
    Chem = int(input('Chemistry: '))
    HM = int(input('Higher Math: '))
    Bio = int(input('Biology: '))

elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' :
    Acc = int(input('Accounting: '))
    BE = int(input('Business Entrepreneurship: '))
    FB = int(input('Finance & Banking: '))
    
elif Group == 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
    Hss = int(input('History & Culture: '))
    Eco = int(input('Economics: '))
    Geo = int(input('Geography: '))
else:
    print('invalid input')

#Main Code

    #Percent

def perc(o, t):
    perc = (o/t)*100

    return perc
    
    #Practical

def prac(sub1, sub2, sub3, sub4, sub5):

    prc1 = int(input(f"Enter your practical marks in {sub1} :"))
    prc2 = int(input(f"Enter your practical marks in {sub2} :"))
    prc3 = int(input(f"Enter your practical marks in {sub3} :"))
    prc4 = int(input(f"Enter your practical marks in {sub4} :"))
    prc5 = int(input(f"Enter your practical marks in {sub5} :"))

    return prc1, prc2, prc3, prc4, prc5

def nice(sub):                #For single paper subs
   
    if 80 <= sub <= 100:
        LG = 'A+'
        PG = 5.00
    elif 70 <= sub <= 79:
        LG = 'A'
        PG = 4.00
    elif 60 <= sub <= 69:
        LG = 'A-'
        PG = 3.50
    elif 50 <= sub <= 59:
        LG = 'B'
        PG = 3.00
    elif 40 <= sub <= 49:
        LG = 'C'
        PG = 2.00
    elif 33 <= sub <= 39:
        LG = 'D'
        PG = 1.00
    elif 00 <= sub <= 32:
        LG = 'F'
        PG = 0.00
    
    return LG, PG

def sonic(sub):               #For double paper subs
    if 160 <= sub <= 200:
        LG = 'A+'
        PG = 5.00
    elif 140 <= sub <= 159:
        LG = 'A'
        PG = 4.00
    elif 120 <= sub <= 139:
        LG = 'A-'
        PG = 3.50
    elif 100 <= sub <= 119:
        LG = 'B'
        PG = 3.00
    elif 80 <= sub <= 99:
        LG = 'C'
        PG = 2.00
    elif 65 <= sub <= 79:
        LG = 'D'
        PG = 1.00
    elif 0 <= sub <= 64:
        LG = 'F'
        PG = 0.00
    return LG, PG

def calc(s1, s2, s3):
    if optional > 2.00:
        PG = (BNG_PG + ENG_PG + GM_PG + R_PG + B_PG + I_PG + s1 + s2 + s3 + (optional-2))/9
        return PG
    elif optional <= 2.00:
        PG = (BNG_PG + ENG_PG + GM_PG + R_PG + B_PG + I_PG + s1 + s2 + s3)/no_s
        return PG

#Execution

if way == 'digit':

    did_you = input('Did you include practical marks? [y/n]: ')

    if did_you == 'y': 
        if Group == 'Science' or 'science' or 'SCIENCE' or 's':
            phyprac, chemprac, bioprac, hmprac, ictprac = prac('Physics', 'Chemistry', 'Biology', 'Higher Math', 'ICT')
            Phy = Phy + phyprac
            Chem = Chem + chemprac
            Bio = Bio + bioprac
            HM = HM + hmprac
            ICT = ICT + ictprac

    ENG_LG, ENG_PG = sonic(Eng)
    BNG_LG, BNG_PG = sonic(Bng)
    GM_LG, GM_PG = nice(GM)
    R_LG, R_PG = nice(Reli)
    B_LG, B_PG = nice(BGS)

#ICT GPA-
    if 40 <= ICT <= 50:
        I_LG = 'A+'
        I_PG = 5.00
    elif 35 <= ICT <= 39:
        I_LG = 'A'
        I_PG = 4.00
    elif 30 <= ICT <= 34:
        I_LG = 'A-'
        I_PG = 3.50
    elif 25 <= ICT <= 29:
        I_LG = 'B'
        I_PG = 3.00
    elif 20 <= ICT <= 24:
        I_LG = 'C'
        I_PG = 2.00
    elif 17 <= ICT <= 19:
        I_LG = 'D'
        I_PG = 1.00
    elif ICT < 17:
        I_LG = 'F'
        I_PG = 0.00

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        P_LG, P_PG = nice(Phy)
        C_LG, C_PG = nice(Chem)
        BIO_LG, BIO_PG = nice(Bio)
        HM_LG, HM_PG = nice(HM)

    elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' :
        A_LG, A_PG = nice(Acc)
        BE_LG, BE_PG = nice(BE)
        FB_LG, FB_PG = nice(FB)

    elif Group == 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
        H_LG, H_PG = nice(Hss)
        E_LG, E_PG = nice(Eco)
        G_LG, G_PG = nice(Geo)


    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        optional = input('Which is you Optional Subject?(bio/hm) : ')
        if optional == 'bio':
            optional = BIO_PG
        elif optional == 'hm':
            optional = HM_PG
        
    elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' or 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
        Optional = int(input('Put in your optional subject marks: '))
        OPT_LG, optional = nice(Optional)

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        if optional == BIO_PG:
            GPA = calc(P_PG, C_PG, HM_PG)
        elif optional == HM_PG:
            GPA = calc(P_PG, C_PG, BIO_PG)
    elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' :
        GPA = calc(A_PG, BE_PG, FB_PG)
    elif Group == 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
        GPA = calc(H_PG, E_PG, G_PG)

elif way == 'percent':
    Eng = perc(Eng, 200)
    Bng = perc(Bng, 200)
    ICT = perc(ICT, 25)

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        Phy = perc(Phy, 75)
        Chem = perc(Chem, 75)
        HM = perc(HM, 75)
        Bio = perc(Bio, 75)

    ENG_LG, ENG_PG = nice(Eng)
    BNG_LG, BNG_PG = nice(Bng)
    GM_LG, GM_PG = nice(GM)
    R_LG, R_PG = nice(Reli)
    B_LG, B_PG = nice(BGS)
    I_LG, I_PG = nice(ICT)

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        P_LG, P_PG = nice(Phy)
        C_LG, C_PG = nice(Chem)
        BIO_LG, BIO_PG = nice(Bio)
        HM_LG, HM_PG = nice(HM)

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        optional = input('Which is you Optional Subject?(bio/hm) : ')
        if optional == 'bio':
            optional = BIO_PG
        elif optional == 'hm':
            optional = HM_PG
        
    elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' or 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
        Optional = int(input('Put in your optional subject marks: '))
        OPT_LG, optional = nice(Optional)

    if Group == 'Science' or 'science' or 'SCIENCE' or 's':
        if optional == BIO_PG:
            GPA = calc(P_PG, C_PG, HM_PG)
        elif optional == HM_PG:
            GPA = calc(P_PG, C_PG, BIO_PG)
    elif Group == 'Commerce' or 'commerce' or 'COMMERCE' or 'c' or 'Business Studies' or 'BS' or 'bs' :
        GPA = calc(A_PG, BE_PG, FB_PG)
    elif Group == 'Arts' or 'a' or 'ARTS' or 'Humanities' or 'HUMANITIES' or 'h':
        GPA = calc(H_PG, E_PG, G_PG)


print('        ')
print('        ')
if GPA > 5.00:
    print('Your GPA is 5.00!')
elif GPA <= 5.00:
    print(f'Your GPA is {GPA}!')