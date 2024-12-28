## This code is created to create zipped files
from pathlib import Path
from zipfile import zipfile

zip = zipfile("staff.zip" , "w")  #In this section, it creates a new file and I activated the writing mode for it

for path in path("staff").rglob("*.*"):
    zip.write(path)

zip.close()
