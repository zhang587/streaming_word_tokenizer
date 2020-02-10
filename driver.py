
from streaming_tokenizer import StreamingTokenizer
import time
# NOTE: this should be turned into pytests

def test_edge_cases():
    text = "Shay's dog talked in Chinese, which is un-American. She went to see Dr.Linda yesterday"
    for token in StreamingTokenizer(force_lower=True, omit_punctuation=False)\
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
    for token in StreamingTokenizer(force_lower=True, omit_punctuation=False)\
        .tokenize_str(text):
        print(token)

def test_punctuation():
    text = '''
    In fact, it turns out that the best way to punctuate a text message may be by not punctuating it at all: 
    Researchers at Binghamton University have found that ending your text with a period — full stop — may make 
    you seem more insincere. !!
    '''.strip()
    for token in StreamingTokenizer(force_lower=True, omit_punctuation=False)\
        .tokenize_str(text):
        print(token)

def test_dickens():
    for token in StreamingTokenizer(force_lower=True, omit_punctuation=False)\
        .tokenize_file('test_data/tale-of-two-cities.txt'):
        print(token)

def test_jkrowling():
    for token in StreamingTokenizer(force_lower=True, omit_punctuation=False)\
        .tokenize_file('test_data/the-philosophers-stone.txt'):
        print(token)

if __name__ == '__main__':
    start_time = time.time()
    test_jkrowling()
    end_time = time.time()
    execution_time = end_time-start_time
    print("execution time", execution_time)