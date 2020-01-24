
from streaming_tokenizer import StreamingTokenizer

# NOTE: this should be turned into pytests

def test_edge_cases():
    text = "Shay's dog talked in Chinese, which is un-American"
    for token in StreamingTokenizer(force_lower=True, emit_punctuation=True)\
        .tokenize_str(text):
        print(token)

def test_text_string():
    text = '''
        It was the best of times,
        it was the worst of times,
        it was the age of wisdom,
        it was the age of foolishness,
        it was the epoch of belief,
        it was the epoch of incredulity,
        it was the season of Light,
        it was the season of Darkness,
        it was the spring of hope,
        it was the winter of despair,
        we had everything before us,
        we had nothing before us,
        we were all going direct to Heaven,
        we were all going direct the other way--
        in short, the period was so far like the present period, that some of
        its noisiest authorities insisted on its being received, for good or for
        evil, in the superlative degree of comparison only.
    '''.strip()
    for token in StreamingTokenizer(force_lower=True, emit_punctuation=True)\
        .tokenize_str(text):
        print(token)

def test_dickens():
    for token in StreamingTokenizer(force_lower=True, emit_punctuation=True)\
        .tokenize_file('test_data/tale-of-two-cities.txt'):
        print(token)

def test_jkrowling():
    for token in StreamingTokenizer(force_lower=True, emit_punctuation=True)\
        .tokenize_file('test_data/the-philosophers-stone.txt'):
        print(token)

if __name__ == '__main__':
    test_text_string()
