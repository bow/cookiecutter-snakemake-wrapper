==================
:warning: archived
==================

I am no longer working on this repository and have therefore decided to archive it.


===============================
cookiecutter-snakemake-wrappers
===============================

`Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template for writing
a `snakemake wrapper <https://bitbucket.org/snakemake/snakemake-wrappers>`_.


Usage
-----

Clone the snakemake wrappers repository (if not yet done) and ``cd`` into it::

    $ git clone https://bitbucket.org/snakemake/snakemake-wrappers.git
    $ cd snakemake-wrappers

Generate the snakemake wrapper skeleton (``-f`` is required if you are creating
the wrapper in an existing discipline directory)::

    $ cookiecutter -f https://github.com/bow/cookiecutter-snakemake-wrappers.git

Then ``cd`` into your tool directory and:

    * Create a new git branch.
    * Update the ``wrapper.py`` with the actual shell command of the tool.
    * Update the README.md with an example.
    * Test the wrapper.
