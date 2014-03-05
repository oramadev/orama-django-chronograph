set HOME=%userprofile%
python.exe setup.py bdist_egg upload
python.exe setup.py bdist_wininst --target-version=2.7 register upload
python.exe setup.py sdist upload
pause