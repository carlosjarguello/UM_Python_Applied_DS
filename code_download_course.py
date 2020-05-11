#resplace by your file name
file ="data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv"
import os
!cp "$file" .
# create an archive file with all assignments and
# data files could have zip,tar, .tar.gz, .tgz, extensions
# check http://linuxcommand.org/man_pages/tar1.html for more info
filename = "course2data.zip"
if os.path.exists(filename):
    ! rm "$filename"
filesToCompress = '*.* readonly/*'

!tar -czf "$filename" $filesToCompress > /dev/null
from IPython.display import HTML
link = '<a href="{0}" target = _blank>Click here to download {0}</a>'
HTML(link.format(filename))
