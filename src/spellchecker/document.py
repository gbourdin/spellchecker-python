# coding=utf-8
from __future__ import unicode_literals, absolute_import
from collections import deque

# Constants for the read/write modes, just for the hell of it
READ_MODE = 'r'
WRITE_MODE = 'w+'


class Document(object):
    def __init__(self):
        self.document = None
        self.mode = None

    def open(self, filename, mode):
        """
        Opens the document that will be contained by this object.
        Use READ_MODE if you only want to read, WRITE_MODE if you want
        to create a new file and write to it.
        """
        self.document = open(filename, mode)
        self.mode = mode

    def get_word(self, doc_out):  # Would be awesome if this was an iterator
        """
        Gets the next available word from the document writing all
        the preceding non-alphabetic characters to doc_out.

        :param doc_out: A document for all non-alphabetic characters to be
         copied to, should be already opened and writeable.
        :return: The next word in the stream or None if there's no more
        words in the document.
        """
        # These buffers should reduce the amount of re-allocs
        trash_buffer = deque()
        word_buffer = deque()

        next_char = self.document.read(1)
        while next_char and (not next_char.isalpha()):
            trash_buffer.append(next_char)
            next_char.read(1)

        # I'm out of the previous loop, word might be over
        while next_char and (next_char.isalpha()):
            word_buffer.append(next_char)
            next_char.read(1)

        if next_char:  # If document is not over "put it back in the buffer"
            self.document.seek(self.document.tell() - 1)  # Go back 1 character

        # Write trash to doc_out before returning!
        doc_out.put_word(''.join(trash_buffer))

        if len(word_buffer):
            return ''.join(word_buffer)
        else:
            return None

    def put_word(self, word=''):
        """
        Writes a word to the document. Document must be open in WRITE_MODE
        :param word: A string of characters that should be written to the file
        :return: Number of characters writen
        """
        if not self.document:
            raise IOError('Document was not open')

        return self.document.write(word)

    def close(self):
        if self.document:
            self.document.close()
