# coding=utf-8
from __future__ import unicode_literals, absolute_import


class Dictionary(object):
    """
    A glorified set
    """
    def __init__(self):
        self.words = set()

    def load(self, filename):
        """
        Opens filename and loads each word from the file into the dictionary
        :param filename: file that will be opened, should be readable
        """
        with open(filename, mode='r') as dict_in:
            for line in dict_in:
                for word in line.strip().split(' '):
                    # strip removes EOL, split helps deal with multiple words
                    # in one line
                    self.add(word)

    def save(self, filename):
        """
        Opens filename and writes all the words in the dictionary to it
        each word goes to a new line
        :param filename: file to be used as output. If it exits, it should
        be writeable
        """
        with open(filename, mode='w+') as dict_out:
            for word in self.words:
                dict_out.write(word + '\n')

    def add(self, word):
        """
        Adds a word to the dictionary. Words will only be added if they
        are not present already.
        """
        return self.words.add(word)

    def contains(self, word):
        """
        Checks if a word is present in the dictionary
        :return: True if it is, False otherwise
        """
        return word in self.words

    def __contains__(self, item):
        return self.contains(item)
