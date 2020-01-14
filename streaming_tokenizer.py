import io
from string import punctuation
class StreamingTokenizer(object):

    def __init__(self, force_lower, emit_punctuation):
        self.force_lower = force_lower
        self.emit_punctuation = emit_punctuation

    def tokenizer(self):
        file = u"""
        It was the best of times, it was the worst of times, it was the age of wisdom, it was the age 
        of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season 
        of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, 
        we had everything before us, we had nothing before us, we were all going direct to Heaven, we were
        all going direct the other way – in short, the period was so far like the present period, that 
        some of its noisiest authorities insisted on its being received, for good or for evil, in the 
        superlative degree of comparison only."""
        for row in io.StringIO(file):
            if self.emit_punctuation:
                new_row = ''.join(c for c in row if c not in punctuation)
            if self.force_lower:
                new_row = row.lower()
            yield new_row
           

        
    
dummy_tokenizer = StreamingTokenizer(force_lower=True, emit_punctuation=False)
res = dummy_tokenizer.tokenizer()
print(res)