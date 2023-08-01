python -m pip install .
python -m pip install .[deploy]
python setup.py sdist
python setup.py bdist
python setup.py bdist_egg
python setup.py bdist_wheel
