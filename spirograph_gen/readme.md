###Spirographs!
This is a project that uses a set of trigonometric parametric occasions in order to mimmic the output of spirograph toys.



![alt text](https://github.com/georgevine/Python_Playground/raw/master/img/spirograph2.png "Spirograph")



The important parameters for spirograph generation are the radii of the two "gears" (see image), as well as the distance from the "hole where the pen is inserted" to the center of the small gear. In the code, we set 'r' equal to the radius of the small gear, 'R' equal to the radius of the large gear, and 'l' equal to the distance from the hole where the pen is inserted to the center of the small gear.


##Use guide
# Dependencies:
Pillow, for image manipulation

#Running
use the command `python spiro.py` to randomly generate 6 spirographs. If you append this command with `--sparams R r l`
substituting R, r, and l with your desired values, the single desired spirograph will be generated. At any time during the generation, you can press the  's' key to save the generated image as a png file


#Example
![alt text](https://github.com/georgevine/Python_Playground/raw/master/spirograph_gen/spiro-01Aug2016-142435.eps "Example")
