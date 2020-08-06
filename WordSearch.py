#  File: WordSearch.py

#  Description: This program takes a word search and a list of words and returns a text file that has the words
#               in alphabetical order along with coordinates of where the words are located within the array.


#  Student Name: Eric Ji

#  Student UT EID: ej6638

#  Partner Name: Brock Brennan

#  Partner UT EID: btb989

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/14/19

#  Date Last Modified: 9/16/19


def createGrid():
    file = open("hidden.txt", "r")
    #Takes in only the first line to create a n x n 2D list
    dimension = file.readline()
    dimension = dimension.split()
    row = int(dimension[0])
    col = int(dimension[1])
    #Sets values in the grid to be string type
    grid = [['']* row]*col
    #Sets values in grid according to line in hidden.txt
    alllines = file.readlines()
    x = 0
    for x in range(row):
        grid[x] = alllines[x+1].split()
    #Returns grid by lines without the brackets when lists are printed and row to be used by wordlist to help determine
    #Where to start reading the words in the file
    return grid

def wordList():
    file1 = open("hidden.txt", "r")
    #Reads the whole text file
    alllines1 = file1.readlines()
    #Reads the dimensions of the square
    coord = alllines1[0].split()
    row = int(coord[0])
    wordlist = []
    #Finds the size of the word list
    size = alllines1[row + 3].split()
    wordlistsize = int(size[0])
    startwordct = row + 4
    #Creates a list of the words
    for x in range(startwordct,startwordct+wordlistsize):
        line = alllines1[x].strip()
        wordlist.append(line)

    return wordlist

def horizontal(grid,wordlist):
    #Lists Used for the function
    rowlist = []
    reverserowlist = []
    horizontalwordlist1 = []
    horizontalwordlist2 = []
    horizontallocationdict = {}
    #Loads up lists with words for this specific function.
    for words in wordlist:
        horizontalwordlist1.append(words)
        horizontalwordlist2.append(words)
    #Puts each row into its own string of characters.
    for x in grid:
        rowstring = "".join(x)
        rowlist.append(rowstring)
    #Puts the reverse of each row into its own string inside of a list for the later search
    for x in grid:
        rowstringreversed = "".join(reversed(x))
        reverserowlist.append(rowstringreversed)
    #Using the list of words, it searches each string for the word and then adds them to a dictionary with the word
    # as the key and a set of coordinates as the value of the dictionary.
    for string in rowlist:
        word = horizontalwordlist1[0]
        for x in rowlist:
            found = x.find(word)
            if found > -1:
                coord = []
                row = rowlist.index(x) + 1
                col = found + 1
                coord.append(row)
                coord.append(col)
                horizontallocationdict.update({str(word): coord})
        del horizontalwordlist1[0]
    # Using the list of words, it searches each reversed string for the word and then adds them to a dictionary with the word
    # as the key and a set of coordinates as the value of the dictionary.
    for string in reverserowlist:
        word = horizontalwordlist2[0]
        for x in reverserowlist:
            found = x.find(word)
            if found > -1:
                rightside = len(grid)
                coord = []
                row = reverserowlist.index(x) + 1
                col = rightside - found
                coord.append(row)
                coord.append(col)
                horizontallocationdict.update({str(word): coord})
        del horizontalwordlist2[0]


    return horizontallocationdict

def vertical(grid, wordlist):
    listcol = []
    revlistcol = []
    list1 = []
    revlist1 = []
    vertlocation = {}
    #Creates a list of the reverse vertical letters
    for r in range(len(grid)):
        for c in range(len(grid)):
            revlistcol.append(grid[c][r])
            if c == len(grid)-1:
                strcol = ''.join(revlistcol)
                strcol = strcol[::-1]
                revlist1.append(strcol)
                revlistcol = []

    #Prints location of the word in the reverse list
    for x in range(len(revlist1)):
        # if list1[x].find(wordlist[x])!= -1:
        for y in range(len(wordlist)):
            loc = revlist1[x].find(wordlist[y])

            if loc != -1:
                rightloc = len(revlist1[x])-loc
                coord = [rightloc, x + 1]
                vertlocation[wordlist[y]] = coord

    #Creates a list of the vertical letters
    for r in range(len(grid)):
        for c in range(len(grid)):
            listcol.append(grid[c][r])
            if c == len(grid)-1:
                strcol = ''.join(listcol)
                list1.append(strcol)
                listcol = []

    #Returns location of the word
    for x in range(len(list1)):
        #if list1[x].find(wordlist[x])!= -1:
        for y in range(len(wordlist)):
            loc = list1[x].find(wordlist[y])
            #print(loc)
            if loc != -1:
                coord = [loc+1, x+1]
                vertlocation[wordlist[y]] = coord
    return vertlocation

def secondDiagonal(grid, wordlist):
    #This Function is Incomplete. We tried to get it to read across the diagonals but kept encountering issues when
    # it moves to next diagonal. It was able to go through the first half of the diagonal but encountered an INDEXERROR
    # whenever we tried to iterate through to the next diagonal.
    row = len(grid) - 1
    col = 0
    list1 = []
    diaglist = []
    length = len(grid) * 2
    x = 0
    while x < length:
        list1.append(grid[row][col])
        if row == len(grid) - 1 and x == 0:
            strdiag = ''.join(list1)
            diaglist.append(strdiag)
            row -= 1
            x += 1
            col = 0
            list1 = []
        if row == len(grid) - 1 and x != 0:
            strdiag = ''.join(list1)
            diaglist.append(strdiag)
            row = row - x - 1
            x += 1
            col = 0
            list1 = []
        if col == len(grid) - 1:
            col = 1
            row = 0
        else:
            row += 1
            col += 1
    print(diaglist)

def combineDictionaries(horizontal,vertical):
    #Combines dictionaries into one.
    merged = {**horizontal, **vertical}
    return merged

def createFile(merged):
    #This Function creates the file, and after sorting the list prints the words inside the wordlist to the text file.
    words = []
    #This loop moves the dictionary into a list for sorting.
    for x in merged:
        words.append(x)
    words.sort()
    file = open("found.txt","w")
    #Writes the file
    for item in words:
        coord = merged.get(item)
        for x in coord:
            row = coord[0]
            col = coord[1]
        file.write('%-10s %2s %3s\n' % (item, row, col))
    file.close()

def main():
    #Creates the Grid
    grid= createGrid()
    #Loads up a list of words
    wordlist = wordList()
    #Checks all of the rows forwards and backwards
    horizon = horizontal(grid, wordlist)
    #Checks all of the columns from top to bottom and from bottom to top.
    vert = vertical(grid, wordlist)
    #Incomplete Function that attempts to read the array diagonally
    #secondDiag = secondDiagonal(grid,wordlist)
    #Takes the dictionaries that were returned and combine them into one.
    merged = combineDictionaries(horizon,vert)
    #Creates the output file and prints the found words
    createFile(merged)


main()






