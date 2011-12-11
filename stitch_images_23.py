# GPL2 LICENCE - code by Dealga McArdle (zeffii) 2011 july 12
'''
usage, 
1) stick the output of Monster Tile Renderer in a folder.
2) set the path variable to that folder  ('..fullpath/stitching/files/')
3) run the script.

'''


# stitching your images, get py 2.6/2.7 and get PIL
import os
import re
import PIL
from PIL import Image

output_format = 'PNG'
path = '/home/zeffii/stitching/files2/'
os.chdir(path) # set this folder active

mycurdir = os.getcwdu()
filelist = os.listdir(mycurdir) # lists content (supposed to be images only!)
filelist = sorted(filelist)

stitchlist = []
for i in filelist:
    strname = str(i[:])
    filepath = path+strname
    
    # disect filename, get dimensions
    db = Image.open(filepath)
    # match = re.search('\d+\_\d+', filepath) # not inclusive enough
    match = re.search('\_(\d+\_\d+)\.', filepath)
    
    match_str = ""
    if match.group() != None:
        match_str = match.group(1)
    else:
        print("use filenames like yourfilname_col_row.ext")
        print("then, if still issues, check the directory for uncommon characters")
        break

    col_row = tuple(match_str.split("_"))
    col_row = [int(dimension) for dimension in col_row]
    
    # store as tuple, tuple, string
    stitch_up = (tuple(col_row), db.size, filepath)
    stitchlist.append(stitch_up)

# stitchlist items are ((column,row),(x, y), '/path/full_including_extension')
rows = stitchlist[-1][0][0]
columns = stitchlist[-1][0][1]

# there has to be neater way to generate a multidimensional list with elements 
# that don't all point to the same place in memory
main_matrix = []
for i in range(rows):
    minor_matrix = []
    for m in range(columns):
        minor_matrix.append([])
    main_matrix.append(minor_matrix)

# temporary
for entry in stitchlist: 
    main_matrix[entry[0][0]-1][entry[0][1]-1] = entry[1]
    
# get composite dimensions
px_wide = sum([i[0][0] for i in main_matrix])
px_high = sum([i[1] for i in main_matrix[0]])
print("px_wide", px_wide, " px_high", px_high)

# permanent
for entry in stitchlist: 
    main_matrix[entry[0][0]-1][entry[0][1]-1] = entry

comp_image = Image.new('RGB', (px_wide, px_high))

ypos = 0
xpos = 0
current_height = 0
current_width = 0
for col in main_matrix:
    ypos = 0
    #do top to bottom
    for row in col:
        ymp = Image.open(row[2])
        current_width = row[1][0]
        current_height = row[1][1]
        ymp = ymp.crop((0,0,current_width, current_height))
        comp_image.paste(ymp, (xpos,ypos))
        ypos += current_height
    xpos += current_width

comp_image.show()
comp_image.save(path+"composited.png", format=output_format)