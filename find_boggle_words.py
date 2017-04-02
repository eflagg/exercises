#Create list of all English words for constant time look up to see if word is valid
with open("wordsEn.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):

    return word in english_words

#Board class with attribute of list of letters
class Board(object):

    def __init__(self):

        self.letters = set([])

    def add_letters(self, letters):

        for letter in letters:
            self.letters.add(letter)

    #Find all the possible words within the boggle board using recursion
    def find_words(self):

        #Recursive helper function, keeping track of letters already seen/used,
        #all words found, the current word, and the current letter
        def _find_words(seen, words, word, letter):

            #If word is in English word set, append it to global words list
            if is_english_word(word):
                words.add(word)
            #Iterate through neighbor letters and recurse on each. The seen and the
            #current word are updated in signature to deal with scope
            for neighbor_letter in letter.neighbors:
                if neighbor_letter not in seen:
                    _find_words(seen.union(set([letter])), words, (word + neighbor_letter.value), neighbor_letter)

            return words

        seen = set([])
        words = set([])

        #Iterate through words on board and create start of word with each letter to start recursion
        for letter in self.letters:
            words = words.union(_find_words(seen, words, letter.value, letter))

        return words

#Letter class with attributes of value and neighbors to indicate which other 
#letters it's next to on the board
class Letter(object):

    def __init__(self, value):
        
        self.value = value
        self.neighbors = set([])

    def __repr__(self):
        return "<Letter: %s>" % self.value

    def add_neighbors(self, neighbors):

        for neigh in neighbors:
            self.neighbors.add(neigh)
            neigh.neighbors.add(self)

#[[p,o,p],
#[d,e,c],
#[n,r,o]]

letter1 = Letter("p")
letter2 = Letter("o")
letter3 = Letter("p")
letter4 = Letter("d")
letter5 = Letter("e")
letter6 = Letter("c")
letter7 = Letter("n")
letter8 = Letter("r")
letter9 = Letter("o")

letter1.add_neighbors([letter2, letter4, letter5])
letter2.add_neighbors([letter3, letter4, letter5, letter6])
letter3.add_neighbors([letter5, letter6])
letter4.add_neighbors([letter5, letter7, letter8])
letter5.add_neighbors([letter6, letter7, letter8, letter9])
letter6.add_neighbors([letter8, letter9])
letter7.add_neighbors([letter8])
letter8.add_neighbors([letter9])

board = Board()
board.add_letters([letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, letter9])

board.find_words()


