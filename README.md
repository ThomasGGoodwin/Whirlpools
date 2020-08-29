# Whirlpools
This was made using Spiral by Tomoko Fuse (pgs 153-155) as a reference
## Requirements for Use
1. Some way to run a Python Script. You can use the command line, PyCharm, Jupyter, or some other method of running the code.
2. Make sure that all the files (Runner.py, Whirl_Funcs.py, and save.txt) are in the same folder on your device.
3. For choosing/identifying colors, I recommend just using this [link](https://www.google.com/search?q=color+picker)
## How to use the tool
1. Input the required variables. These are n, pho, phi, base, and iters.
2. If you want your spiral to be colored, check the color box and input the color variables.
3. If you enable the Lampshade checkbox, the crease pattern will generate a set of triangles at the top that will make a point once the whole thing is folded.
4. It is recommended to view a top-down preview of the spiral by clicking the Preview checkbox and clicking the Go! button.
5. If you like the preview, uncheck the Preview checkbox and press Go again.
6. If the crease pattern is too small or too large, adjust the base variable until the size is appropriate.
7. Take a screenshot of the crease pattern and print it using some other program like Word or Powerpoint.
## How to fold a given crease pattern, once the whole thing is cut out.
1. If your spiral is colorless, fold the lines as follows. The black ones are valley folds and the orange diagonal lines are mountain folds.
2. If your spiral is colored, do the opposite. The lines that are diagonals of a quadrilateral are valley folds and everything else is a mountain fold.
3. Once each fold in pre-creased, do the following.
4. If your spiral is colorless, cut off about half of the leftmost side (when looking at the base as the bottom). This half of a column will go beneath the other side (it should become apparent as you fold).
5. If your spiral is colored, cut off about half of the rightmost side (when looking at the base as the bottom). This half of a column will go beneath the other side (it should become apparent as you fold).
6. Fold all the folds at once, as you do so the model should collapse in on itself and become a spiral!
##Important Notes
1. If you close the drawing window, you will have to restart the program before you click go again.
2. Don't click Go until the previous drawing has been completed.
## Variable Descriptions/Explanations
### Variables for the spiral itself
1. n: the number of corners of the primal polygon. In practical terms, this describes how many sides each layer will have
2. rho: the angle of rotation. This is how much each triangle in a layer rotates by. The larger this value is, the more the crease pattern will tighten up. If this were 0, all the triangles in a row would have parallel bases. The greater this is, the greater the crease pattern will spiral in on itself.
    * This is a special case(rho=0). It will make a tube instead of spiraling inward. If you do this, the lampshade feature won't work, so be warned.
3. phi: the angle of spirality. This determines the lengths of each triangle. The larger this value is, the taller the triangles will be and the smaller the hole in the center will be.
    * If the value is 0, the folding pattern will only be a couple of lines.
### Variables for making it look good
4. base: How long the base of the starting triangle will be. This will probably have to be adjusted every time you use a new one. The goal is to try to fit the whole crease pattern on the drawing window.
5. iters: How many layers of triangles there are. Don't make them too small.
6. background color: Only applies when colors are enabled. The color of the background of the crease pattern. 
7. color list: Only applies when colors are enabled. The colors that the spiral wil be. The colors should be in hexadecimal and should be seperated by commas. Here is an example: #aabbcc,#22ab4f,#3d2a5c,#45c2f0
### You probably won't have to touch these
8. startx: Sets the starting x coordinate for the Turtle module.
9. starty: Sets the starting y coordinate for the Turtle module.
10.rad: Only applies when previewing a spiral. Changes the size of the preview. Think of the preview as being encompassed by a circle and rad is the length of the radius.
