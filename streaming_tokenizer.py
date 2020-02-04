import io
import re
import os
from string import punctuation


class Token(object):
    def __init__(self, str):
        self.str = str
        self.is_punctuation = punctuation
        self.is_delimiter = not str.strip()

    def __str__(self):
        if self.is_delimiter:
            return '<DELIMITER>'
        ## TODO: finish this part
        if self.is_punctuation:
            return '<PUNCTUATION>'
        else:
            return '<{}>'.format(self.str)

class StreamingTokenizer(object):

    def __init__(self, force_lower, omit_punctuation, emit_punctuation, split_pattern='\s+'):
        self.force_lower = force_lower
        self.omit_punctuation = omit_punctuation 
        self.emit_punctuation = emit_punctuation
        # compile the split pattern for speed
        self.pattern = re.compile(split_pattern)

    def tokenize_str(self, str):
        """
            Takes a string as input rather than a file
        """
        return self._tokenize(io.StringIO(str))

    def tokenize_file(self, filepath):
        """
            Take a file as input and return (yield) Token objects
        """

        if not os.path.isfile(filepath):
            raise "File path {} does not exist. Exiting...".format(filepath)
        else:
            with open(filepath, "r", encoding = "utf-8") as fd:
                yield from self._tokenize(fd)

    def translate_str(self, word):
        
        return word.translate(str.maketrans('', '', punctuation))

    def _tokenize(self, fd):
        #
        # Note: using the readline method assumes the text file has newlines
        # if this assumption doesn't hold the file must be read char by char
        #
        # Note: one way to detect punctuation is to use two patterns, one
        # of the user provided strip pattern and one of string.punctuation
        # then let regex tell you which pattern matched, that's the most robust
        # way to detect punct chars (and runs of chars like "!!" as a single token)
        for line in fd:
            for word in self.pattern.split(line):
                if self.force_lower:
                    word = word.lower()
                if self.omit_punctuation:
                    word = self.translate_str(word)
                ## TODO: finish this part
                if self.emit_punctuation:
                    char_list = [char for char in word]
                yield Token(word)
