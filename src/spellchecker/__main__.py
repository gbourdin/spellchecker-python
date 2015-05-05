# coding=utf-8
from __future__ import unicode_literals, absolute_import
from argparse import ArgumentParser
import sys

from .dictionary import Dictionary
from .document import Document, READ_MODE, WRITE_MODE

try:  # Awful hack for python 2/3 compatibility
    input = raw_input
except NameError:
    pass


def consult_user(word, known_words, ignored_words):
    ans = input("Palabra no reconocida: {0}\n".format(word) +
                "Aceptar (a) - Ignorar (i) - Reemplazar (r): ")

    if ans.startswith('a'):
        known_words.add('a')
        return word
    elif ans.startswith('i'):
        ignored_words.add(word)
        return word
    elif ans.startswith('r'):
        new_word = input(
            'Ingrese la palabra que reemplazara a {0}: '.format(word)
        )
        return new_word
    else:
        return consult_user(word, known_words, ignored_words)


def process_document(filename, known_words, ignored_words):
    doc_in = Document(filename, mode=READ_MODE)
    doc_out = Document('out.txt', mode=WRITE_MODE)

    word = doc_in.get_word(doc_out)

    while word:
        if (word in known_words) or (word in ignored_words):
            doc_out.put_word(word)
        else:
            word = consult_user(word, known_words, ignored_words)
            doc_out.put_word(word)

        word = doc_in.get_word(doc_out)

    doc_in.close()
    doc_out.close()

    return known_words


def main():
    doc_in_filename = ''
    print("Oh noes, I'm not implemented yet!")
    print("El documento %s ha sido procesado. Resultados en out.txt".format(
        doc_in_filename))

if __name__ == "__main__":
    sys.exit(main())
