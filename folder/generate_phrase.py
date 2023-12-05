from wonderwords import RandomSentence


def generate_random_paragraph(num_sentences):
    random_sentences = [RandomSentence().sentence() for _ in range(num_sentences)]
    return ' '.join(random_sentences)


class PhraseGenerator:
    def __init__(self):
        pass
