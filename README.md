as of late i've received a couple of notifications that v3_005 of Monster Tile Render needed to
be updated for work in 2.6. As of 2.6.007 the script here does work for me on a Trunk build for win32 
around 12 December 2011.

If there are any more issues, contact me here or leave a bug report, but please also state which version of blender
and the revision and full error message.

Advice on how to use the program.  
: pick your output format, path, and filename, and adjust the variables available.  
: press calculate settings  
: read to yourself the result of the calculations, and think 'do they make sense? do i really want 900 tiles?'  
: press apply settings  
: open up blender console (for render update information.. at the time of writing i couldn't manage anything classier)
: press render, timetravel or go do something else.

Noteworthy  
: the filename setting doesn't impact the files written to disk,  they will be called the same as your .blend (easier to find!)  
: don't forget to pick an output directory.  
: again, look at the caculated settings and pose yourself the question; 'do they make sense' ?  
: finally, when you 'apply settings' depending on your input, the camera aspect might change relative  
: allways look through the camera, before rendering to make sure you get what you want  
: if you can't figure it out, render more than you need, stich..then crop later.

Considerations for future releases.  
: I've already written code to the effect of being able to email an image from blender to my gmail account.  
: I will try to find this .py and upload here, and consider adding things like  
: - option to either email upon tile completion  
: - email upon tile completion and email the image at the same time  
: - email upon tile completion, but don't email the images  (or thumbnail )
: - email upon tile completion, but don't email the images, email a reduced version of the composite (so you know what's going on)  
