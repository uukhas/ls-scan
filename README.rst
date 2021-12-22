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

-S <model scenario>:
   A path for model scenario script (a ``python`` program).
   The file will owerride the one in a cwd.

-X <path to executable>:
   A path to ``FlexibleSUSY/models/MODEL/run_MODEL.x``
