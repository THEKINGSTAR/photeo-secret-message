##Directory and File copy example - From Tim Golden's Python Stuff:
##http://timgolden.me.uk/python/win32_how_do_i/copy-a-file.html

import os
import shutil
import tempfile
import glob
from shutil import copyfile

#---------------------------------------------------------------

# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")

alphabet_string = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,., "
# alphabet_string = "A ,B ,C ,D ,E ,F ,G ,H ,I ,J  ,K  ,L  ,M  ,N  ,O  ,P  ,Q  ,R  ,S  ,T  ,U  ,V  ,W  ,X  ,Y  ,Z  ,.  , "
alphabet_numrec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                   14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

alphabet = alphabet_string.split(',')

#print(type(alphabet))
#print (os.getcwd())

workdir = os.getcwd()
#file_list = os.listdir(r"{}\Alphabet".format(workdir))

#print (file_list)


###################################################################################
###################################################################################
##how copy files work
#########################

""" 
cd  = os.getcwd()
old = cd+"\Alphabet"
new = cd+"\MESSAGE"
shutil.copy(old, new) 
"""

def mesage_creating(message):
    # seperating the message letters
    message = message.upper()
    message.split()
    #print(message)
    workdir = os.getcwd()

    ## EMPTYING THE MESSAGE FOLDER FRIST

    files = glob.glob("{}\MESSAGE\\**\*.jpg".format(workdir), recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    #file_list = os.listdir(r"{}\Alphabet".format(workdir))

    arrange = 0
    for litter in message:
        """ 
        creat list with the letter and space and dot of the message
        read the files in the message folder
        if not exist copy the file from the alphapet to the message folder
        if exist rename whith the last number existi
        if letter is space copy space
        if letter is dot copy dot
         """
        index = alphabet.index(litter)+1
        #print(index)
        original = "{}\Alphabet\{}".format(workdir, index)+".jpg"
        #new_name =
        target = "{}\MESSAGE\\".format(workdir) + "0{}".format(arrange)+".jpg"
        shutil.copyfile(original, target)
        arrange += 1

###################################################################################
###################################################################################


def user_input():
    message = input("Right the message you want IN PICTURES !!! , USE ONLY ALPHABET LETTERS , DOT(' . ' ) AND SPACEES \n")
    print("\n Check THE folder 'MESSAGE' FOR THE : " +message + "!" + ' '+"IN PICTURES \n")
    #creat_message(message)
    mesage_creating(message)


#---------------------------------------------------------------
###################################################################################
###################################################################################
user_input()
