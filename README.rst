A program to run ``FlexibleSUSY`` over sets of model parameters.

Usage
-----

In order to use, run::

   ./scan  -D <number of dots> \
           -P <number of threads> \
           -S <model scenario> \
           -X <path to executable> \

It will store the output to a database file.

Commands
--------

-D <number of dots>:
   Amount of points to be evaluated.
   It is overwritten by static ``ndots`` attribute (if exists) of
   model scenario.

-P <number of threads>:
   A number of parallel versions to launch.

-S <model scenario>:
   A path for model scenario script (a ``python`` program).
   The file will owerride the one in a cwd.

-X <path to executable>:
   A path to ``FlexibleSUSY/models/MODEL/run_MODEL.x``

How to write scenario?
----------------------

+----------------------+----------------------------+-------------------------+
| LesHouches.in.MODEL  | scenario.py                | Commentaries            |
+----------------------+----------------------------+-------------------------+
|.. code-block::       |.. code-block:: python      |``ndots``: *optional*    |
|                      |                            |   Override the value,   |
|   Block A            |   class Scenario:          |   defined by ``-D``.    |
|    1 1e+2            |                            |                         |
|                      |     ndots = 100            |``input``:               |
|   Block B            |                            |   Specify, which        |
|    1 2 2e+2          |     def __init__(self, i): |   values should be      |
|                      |                            |   changed in the input  |
|                      |       self.input = dict(   |   Les Houches file      |
|                      |         A_1 = 1,           |   before the run of     |
+----------------------+         B_1_2 = 1e-3,      |   FlexibleSUSY.         |
| LesHouches.out.MODEL |       )                    |                         |
+----------------------+                            |``output``:              |
|.. code-block::       |       self.output = [      |   Specify, which values |
|                      |         'C_3',             |   should be stored from |
|   Block C            |         'D_4_5'            |   the output Les Houches|
|    3 3e+2            |       ]                    |   file, created after   |
|                      |                            |   the run of            |
|   Block D            |                            |   FlexibleSUSY.         |
|    4 5 4e+2          |                            |                         |
+----------------------+----------------------------+-------------------------+
