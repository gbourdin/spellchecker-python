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


DEFAULT_MAIN_DICT_NAME = 'dict.txt'
DEFAULT_OUTPUT_DOC_NAME = 'out.txt'


def consult_user(word, known_words, ignored_words):
    ans = input("Palabra no reconocida: {0}\n".format(word) +
                "Aceptar (a) - Ignorar (i) - Reemplazar (r): ")

    if ans.startswith('a'):
        known_words.add(word)
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


def process_document(in_filename, out_filename, known_words, ignored_words):
    doc_in = Document(in_filename, mode=READ_MODE)
    doc_out = Document(out_filename, mode=WRITE_MODE)

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

    parser = ArgumentParser(prog='spellchecker')

    parser.add_argument("documento", help="Documento de entrada")
    parser.add_argument("diccionario", nargs='?',
                        help="Diccionario de entrada/salida")

    args = parser.parse_args()
    doc_in_filename = args.documento
    known_words_filename = args.diccionario

    known_words = Dictionary()
    ignored_words = Dictionary()

    if known_words_filename:
        known_words.load(known_words_filename)
    else:
        known_words_filename = DEFAULT_MAIN_DICT_NAME

    process_document(
        doc_in_filename, DEFAULT_OUTPUT_DOC_NAME, known_words, ignored_words
    )

    known_words.save(known_words_filename)

    print('El documento {0} ha sido procesado. '.format(doc_in_filename) +
          'Resultados en out.txt')

if __name__ == "__main__":
    sys.exit(main())
