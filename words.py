def print_upper_words(words):
    """Print captolized words on seperate lines
    print_upper_words([Hello, everyone, I, am, AN, ExAmPlE])
    HELLO
    EVERYONE
    I
    AM
    AN
    EXAMPLE
    """

    for word in words:
        print(word.upper())

def print_upper_words_pro(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words_pro_max(words, letters):
    """
    Checks each work to see if it starts with the correct letter,
    then prints those words uppercase
    
    print_upper_words_pro_max(["apple", "banana", "carrot", "dolphin", "eagle", "forest", "giraffe", "horiz
    ...: on", "island", "jellyfish", "kangaroo", "lemon", "mountain", "night", "orange", "pencil", "quartz", "ri
    ...: ver", "sun", "tiger", "umbrella", "violet", "whale", "xylophone", "yellow", "zebra", "avocado", "breeze
    ...: ", "crystal", "dragon", "energy", "flame", "grape", "honey", "iceberg", "journey", "koala", "lantern",
    ...: "mermaid", "nebula", "ocean", "pyramid", "quill", "rainbow", "sapphire", "treasure", "universe", "volca
    ...: no", "window", "xenon", "yarn", "zenith"],["s","d","a","z"])
APPLE
DOLPHIN
SUN
ZEBRA
AVOCADO
DRAGON
SAPPHIRE
ZENITH
    """
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break