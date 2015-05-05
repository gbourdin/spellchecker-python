===================
spellchecker-python
===================
No es realmente un spellchecker, es la implementación en python, por nerdear un poco únicamente,
de un trabajo del laboratorio de la materia Paradigmas de la Programación, de FaMAF.

Es una pequeña prueba de concepto para ver cuanto mas lento es hacer I/O en
python que en C.

Compatible con (al menos) python 2, python 3 y pypy.

Hay un branch `performance` con algunos cambios para reducir la cantidad de
I/O que muestran una mejora significativa cuando se usa con python 3.


Como Usar
=========
Para master:

::

    git clone https://github.com/gbourdin/spellchecker-python.git
    cd spellchecker-python/src
    python -m spellchecker <documento-de-entrada> <diccionario-de-entrada>

Para el branch de `performance`
::

    git clone https://github.com/gbourdin/spellchecker-python.git
    cd spellchecker-python/src
    git checkout -b performance origin/performance
    python -m spellchecker <documento-de-entrada> <diccionario-de-entrada>