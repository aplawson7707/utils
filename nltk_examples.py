import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_string = "I've known adventures, seen places you people will never see, I've been Offworld and back… frontiers! I've stood on the back deck of a blinker bound for the Plutition Camps with sweat in my eyes watching stars fight on the shoulder of Orion... I've felt wind in my hair, riding test boats off the black galaxies and seen an attack fleet burn like a match and disappear. I've seen it, felt it..."
worf_quote = "Sir, I protest. I am not a merry man!"
string_for_stemming = "The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."
sagan_quote = "If you wish to wish to make an apple pie from scratch you must first invent the universe."
jabberwocky = "'Twas brillig, and the slithy toves did gyre and gimble in the wabe: all mimsy were the borogoves, and the mome raths outgrabe."
string_for_lemmatizing = "The friends of DeSoto love scarves."

stopwords = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def tokenizeMethods(string):
    sentences = sent_tokenize(string)
    words = word_tokenize(string)
    s = 1
    w = 1
    for sentence in sentences:
        print(f"{s}: {sentence}")
        s = s + 1

    for word in words:
        print(f"{w}: {word}")
        w = w + 1

def filterOutStopwords(string):
    words_in_quote = word_tokenize(string)
    filtered_list = []

    # append to empty array
    for word in words_in_quote:
        if word.casefold() not in stopwords:
            filtered_list.append(word)

    # or.... use list comprehension
    filtered_list_2 = [
        word for word in words_in_quote if word.casefold() not in stopwords
    ]

    print(words_in_quote)
    print(filtered_list)
    print(filtered_list_2)

def stemmingMethod(string):
    words = word_tokenize(string)
    stemmed_words = [stemmer.stem(word) for word in words]
    print(words)
    print(stemmed_words)

def partsOfSpeech(string):
    words = word_tokenize(string)
    pos = nltk.pos_tag(words)
    print(pos)

def showPartsOfSpeechTags():
    pos_tags = nltk.help.upenn_tagset()
    print(pos_tags)

# A lemma is a word that represents a whole group of words, and that group of words is called a lexeme.
# For example, if you were to look up the word “blending” in a dictionary, 
# then you’d need to look at the entry for “blend,” but you would find “blending” listed in that entry.

def lemmatizingMethod(string):
    words = word_tokenize(string)
    lemmas = [lemmatizer.lemmatize(word) for word in words]
    print(lemmas)

lemmatizingMethod(string_for_lemmatizing)
