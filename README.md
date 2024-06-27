# mudepy is maintained nudepy

## About this fork


This is fork of <https://github.com/hhatto/nude.py>. I will try to keep
it maintained with pre-compiled binary (wheel) packages.

Use it when you have this problem with original nudepy:
~~~
    skin_classifier.c:196:12: fatal error: longintrepr.h: No such file or directory
      196 |   #include "longintrepr.h"
          |            ^~~~~~~~~~~~~~~
    compilation terminated.
    error: command '/usr/bin/gcc' failed with exit code 1
~~~

If you use nudepy in your projects, just change to mudepy in
dependencies. No other changes are required.


## Installation

from pip:

    $ pip install --upgrade mudepy

from pipx:

    $ pipx install mudepy

## Usage
via command-line

```sh
$ nudepy IMAGE_FILE
```

via Python Module

```python
import nude
from nude import Nude

print(nude.is_nude('./nude.rb/spec/images/damita.jpg'))

n = Nude('./nude.rb/spec/images/damita.jpg')
n.parse()
print("damita :", n.result, n.inspect())
```

see [examples](https://github.com/hhatto/nude.py/tree/master/examples) .

## Links

-   [mudepy PyPI](http://pypi.python.org/pypi/mudepy/)
-   [mudepy GitHub](https://github.com/yaroslaff/mude.py)
-   [nudepy PyPI](http://pypi.python.org/pypi/nudepy/)
-   [nudepy GitHub](https://github.com/hhatto/nude.py)

### How to build binary wheel
Start manylinux docker container
~~~
docker run -it -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 /bin/bash
~~~
inside container:
~~~
cd io
./makeanylinux.sh
~~~