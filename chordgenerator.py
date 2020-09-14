
    # Prints 1 common RANDOM chord progression in major keys: C, D, F, G, A
    # Possible extensions: 1) let user choose which key to randomly print 2) Print multiple progressions based on desire 3) print new random progression 
    # Show common note for each progression 
    # major scale = 1 - 1 - 1/2 - 1 - 1 - 1 - 1/2 
    # minor scale = 1 - 1/2 - 1 - 1 - 1/2 - 1  1 


import random

C_145 = ("C,F,G")
D_145 = ("D,G,A")
F_145 = ("F,Bb,C")
G_145 = ("G,C,D")
A_145 = ("A,D,E")

C_1645 = ("C,Am,F,G")
D_1645 = ("D,Bm,G,A")
F_1645 = ("F_Dm_Bb_C")
G_1645 = ("G,Em,C,D")
A_1645 = ("A,F#m,D,E")

C_1625 = ("C,Am,Dm,G")
D_1625 = ("D,Bm,Em,A")
F_1625 = ("F,Dm,Gm,C")
G_1625 = ("G,Em,Am,D")
A_1625 = ("A,F#m,Bm,E")

#classical pop pattern

C_1564 = ("C,G,Am,F")
D_1564 = ("D,A,Bm,G")
F_1564 = ("F,C,Dm,Bb")
G_1564 = ("G,D,Em,C")
A_1564 = ("A,Em,F#m,D")

C_1465 = ("C,F,Am,G")
D_1465 = ("D,G,Bm,A")
F_1465 = ("F,Bb,Dm,C")
G_1465 = ("G,C,Em,D")
A_1465 = ("A,D,F#m,E")

C_1345 = ("C,Em,F,G")
D_1345 = ("D,F#m,G,A")
F_1345 = ("F,Am,Bb,C")
G_1345 = ("G,Bm,C,D")
A_1345 = ("G,Bm,C,D")

C_1415 = ("C,F,C,G")
D_1415 = ("D,G,D,A")
F_1415 = ("F,Bb,F,C")
G_1415 = ("G,C,G,D")
A_1415 = ("A,D,A,E")

C_1425 = ("C,F,Dm,G")
D_1425 = ("D,G,Em,A")
F_1425 = ("F,Bb,Gm,C")
G_1425 = ("G,C,Am,D")
A_1425 = ("A,D,Bm,E")

c_major_tones = "C, D, E, F, G, A , B"
c_major_chords = "C, Dm, Em, F, G, Am, Bdim"
g_major_tones = "G, A, B, C, D, E, F♯"
g_major_chords = "G, Am, Bm, C, D, Em, F♯dim"
d_major_tones =  "D, E, F♯, G, A, B, C♯" 
d_major_chords = "D, Em, F♯m, G, A, Bm, C♯dim"
a_major_tones = "A, B, C#, D, E, F#, G#dim" 
a_major_chords = "A, Bm, C#m, D, E, F#m, G#dim"
e_major_tones = "E, F♯, G♯, A, B, C♯, D♯"
e_major_chords = "E, F♯m, G♯m, A, Bm, C♯m, D♯dim"
b_major_tones = "B, C♯, D♯, E, F♯, G♯, A♯"
b_major_chords = "Bm, C♯m, D♯m, E, F♯, G♯m, A♯dim"
f_major_tones = "F, G, A, B♭, C, D, E"
f_major_chords = "F, Gm, Am, B♭, C, Dm, Edim"

vars = (C_145,D_145,F_145,G_145,A_145,C_1645,D_1645,F_1645,G_1645,A_1645,C_1625,D_1625,F_1625,G_1625,A_1625,C_1564,D_1564,F_1564,G_1564,A_1564,C_1465,D_1465,F_1465,G_1465,A_1465,C_1345,D_1345,F_1345,G_1345,A_1345,C_1415,D_1415,F_1415,G_1415,A_1415,C_1425,D_1425,F_1425,G_1425,A_1425)

random_progression = random.choice(vars)

print ("Welcome to the CHORD GENERATOR!") 
print()
print ("I am at your disposal, offering 45 different progressions in the key of C, D, F, G, A. ") 
print ()
print ("Here is your first random chord progression:")
print (random_progression)
chords_first = random_progression[0]
print ()


question = input ("On your keyboard, type the word: yes, if you want new chords, or type the words: remaining chords, if you want to see the remaining chords for you chord progression in the key of " + chords_first +":")
print()

while question == ("yes"):
    random_progression = random.choice(vars)
    print (random_progression)
    chords_first = random_progression[0]
    print ()
    question = input ("Keep typing yes for new chords, or remaing chords if you want to build on your current progression in the key of " + chords_first +":")
    
    
if question == ("remaining chords"):
                if chords_first == "C": print (c_major_chords)
                if chords_first == "D": print (d_major_chords)
                if chords_first == "E": print (e_major_chords)
                if chords_first == "F": print (f_major_chords)
                if chords_first == "G": print (g_major_chords)
                if chords_first == "A": print (a_major_chords)
                if chords_first == "B": print (b_major_chords)

print()
print("Good luck on your chosen chord progression. If you want help adding lyrics to your chords, follow this link: www.lyrics.com")