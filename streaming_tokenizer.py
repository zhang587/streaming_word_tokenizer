import io
import re
import os
from string import punctuation


class Token(object):
    def __init__(self, str, is_punctuation=True):
        self.str = str
        self.is_punctuation = is_punctuation
        self.is_delimiter = not str.strip()

    def __str__(self):
        if self.is_delimiter:
            return '<DELIMITER>'
        else:
            token_list = re.findall(r"[\w]+|[^\s\w]", self.str)
            for i in token_list:
                print(i)
        return '<{}>'.format(self.str)


class StreamingTokenizer(object):

    def __init__(self, force_lower, omit_punctuation, split_pattern='\s+'):
        self.force_lower = force_lower
        self.omit_punctuation = omit_punctuation
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
                yield Token(word)
