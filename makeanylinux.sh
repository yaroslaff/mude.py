#!/bin/bash

echo build anylinux version
PYTHON=/opt/python/cp38-cp38/bin/python
echo PYTHON=$PYTHON

$PYTHON -m pip install wheel cython

echo +++ build sdist and wheel
$PYTHON setup.py sdist bdist_wheel


echo ++ fix wheels
auditwheel repair dist/*whl

ls -l dist/wheelhouse