# Cocktail ingredients optimizer

# Introduction
This is an old project of mine that I've since abandoned. It works, but is missing a lot of functionality.

Ever wondered: If I had $100, what ingredients should I buy to make the most cocktails?
Well, now with the help of this script and a piece of freeware called GLPK, this is actually possible!

This script depends on two files - cocktails_list.csv, and price_list.csv. In cocktails_list.csv, the ingredients for cocktails are given, and in price_list.csv, the prices for the ingredients are given.

# Usage 

You can use the cocktails_list.csv file I've provided, but bear in mind that I've only included alcoholic ingredients. The data I've used comes from reddit. Link: https://reddit.com/r/cocktails Special Credits to /u/hebug.

Just run the Python script "Cocktails.py", and what the program does is that it will write one additional file to the folder: cocktailsILP.data

The program will pause here. DON'T CLOSE IT!

Next, you have to install GLPK. GLPK is a free program that is the backbone of the optimization program. GLPK stands for the GNU Linear Programming Kit, and for those interested, it is capable of solving Integer Linear Programming problems, which I'm making use of here.

Open command prompt in your folder, and run the following line of code:
> glpsol.exe -m --model cocktailsILP.model --data cocktailsILP.data > output.txt. This writes the output of GLPK to a file called "output.txt". 

Then, you need to copy the output of the GLPK file back to python. Copy everthing from "Display statement at Line 26", and paste it into the python script.

The script will interpret the GLPK result and present a solution.

## Example output of the program

======================
FINAL PROGRAM OUTPUT
======================

7 Bottle(s) to buy:
    1. Bitters [Cardamom]
    2. Bitters [Creole]
    3. Brandy [Apple]
    4. Gin [London]
    5. Gin [Sloe]
    6. Grand Marnier
    7. Rum [Jamaican Gold]

16 Cocktails that can be made:
    1. Astor Hotel Special
    2. Blood and Sand
    3. Brooklyn (v u/bitcheslovebanjos)
    4. Champagne Flip
    5. Cloister (v Yellow)
    6. Coessential
    7. Ford Cocktail
    8. Fourth Regiment
    9. Golden Dream
    10. Harvest Moon (v PDT)
    11. Lemon Drop Martini
    12. Long Island Iced Tea (v Anvil)
    13. Lucien Gaudin
    14. Margarita
    15. Royal Smile
    16. Savoy Tango

# Formatting

Cocktails_list.csv is formatted like this:

Cocktail1 | Ingredient 1
Cocktail1 | Ingredient 2
Cocktail2 | Ingredient 1
Cocktail2 | Ingredient 2
Cocktail2 | Ingredient 3

Basically, two columns only. The program will do the compilation automatically.

Price_list.csv is formatted like this:

Ingredient 1 | Price 1
Ingredient 2 | Price 2

#Future improvements

If I've got the time, I will try to work on an interface between Python and GLPK. Building my own ILP solver will take too much time so I'd really rather not.