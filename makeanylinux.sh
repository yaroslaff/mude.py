#!/bin/bash

echo build anylinux version
PYTHON=/opt/python/cp38-cp38/bin/python
echo PYTHON=$PYTHON

$PYTHON -m pip install wheel cython build

echo +++ build sdist and wheel
# $PYTHON setup.py sdist bdist_wheel
$PYTHON -m build

echo ++ fix wheels
cd dist/
auditwheel repair *whl
ls -l wheelhouse