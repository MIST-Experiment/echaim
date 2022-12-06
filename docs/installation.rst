Installation
============

..

The ``echaim`` package build is tested only on Linux and OS X systems. The build is confirmed to work on Windows
if your default C compiler is `MinGW <https://www.mingw-w64.org/>`_. If you are having troubles with installing it
on Windows - consider using `WSL <https://docs.microsoft.com/en-us/windows/wsl/install>`_.

Impotant! Before installing the ``echaim`` pakage you need to install `CMAKE <https://cmake.org/>`_.

Now you can simply install ``echaim`` using ``pip`` or any other package manager::

    python3 -m pip install echaim


Currently, the package does not update the index database automatically. You can (and should) do it manually
by calling the ``update()`` function::

    from echaim import update; update()