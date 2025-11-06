## Using PyTRiP

Code for this protocol can be found in Joan's github (https://github.com/joanmanbar/TRiP)
The code has already been downloaded to the lab mac. It can be found in /Documents/Leaf-movement/JoanPYtRiP/code

### Setting up the input folder

* I recommend setting up a folder for each set of images (each camera) within a larger folder for each experiment. Example: /Leaf-movement/Adelaide/20250124-Pennycress/C01 for camera 1 analysis. 
* Within the camera folder, I suggest creating two folders, "all_images" and "input". Load all images captured into the "all_images" folder, and then load only the images for analysis (generally 8am on the second day of constant light to the end of the experiment) into the "input" folder. Look at the pictures in folder using List, shift+click select. Copy paste into input folder. Delete any unwanted photos, minimum 3 days trial. Command Space to search on Mac. 
* The other item which must be included in each camera folder is the crop.txt (/Leaf-movement/namme/experimentID/C0x/crop.txt)

### Creating the crop.txt file

The crop.txt file tells the python script where each plant is. Take care when creating this file as the quality of the data can be restricted by the quality of this file. 

* To start, open up FIJI. 
* Once open, drag and drop the final image from the input folder into the FIJI window. 
* When the image opens, find the "Analyze" button on the top of the screen and click Plugins > Macros > Record. A blank window should open up once you've clicked "Record" 
* Crop photo from the last photo of each input trial. 
* Click the rectangle tool button on the FIJI window, if it is not already selected. Now you are ready to start drawing rectangles for each plant. 
* To draw these rectangles, drag your mouse in a way to draw a rectangle around just the plant. Ensure that the full reach of the cotyledons are selected, and that no soil is included. The only thing in this rectangle should be the plant. Once you have drawn a rectangle, "makeRectangle(0000, 0000, 0000, 0000);" should populate in the new record window. If you need to recreate a rectangle you've drawn, simply delete the line of text correlated to that rectangle and re-do it. 
* Because there is no easy way to label these lines as they populate, I suggest drawing rectangles in an order which you will remember. The best way I have found to do it is to draw them by position left to right along each row of plants. Very importantly, if there is not a plant present in a position, for any reason, do not simply skip over it, but draw a rectangle with nothing in it so that the ordering of your coordinates in the record window is not messed up. 
When you have drawn all of your rectangles, the record window should look something like this: 
```
makeRectangle(0000, 0000, 0000, 0000);
makeRectangle(0000, 0000, 0000, 0000);
makeRectangle(0000, 0000, 0000, 0000);
makeRectangle(0000, 0000, 0000, 0000);
...
```
The number of lines should be exactly the number of plants/ positions in the original image. For example, this will normally with 120 as there are 120 positions in a typical camera set-up. 

* Next, copy all lines from the record window to any text editor. Find "makeRectangle(" replace with nothing. Find "," replace with nothing. and find ");" replace with nothing. You will be left with just the coordinates for each plant. (Record all plant slots even if there is no plant growing)

This should look like this: 
```
0000 0000 0000 0000 
0000 0000 0000 0000
0000 0000 0000 0000
0000 0000 0000 0000
...
```
* Next, open an excel document or a google sheets and put plant001 in the first column. Drag this down for the appropriate number of plants (generally to plant120) the sheet should automatically increase the number for each line.  
* Paste the coordinates from the text editor in the second column. If pasted correctly, each line should have one set of coordinates which aligns with the plantxxx names in the left column.
* In the third column enter 
```
=concatenate(A1, " ", B1)
```
* Drag this equation down for all plants. Ensure that the concatenated form has the correct coordinates from each line. 
* Copy the entire third column and paste it into a blank text document into crop.txt so it's overwritten.
It should look like this:
```
plant001 0000 0000 0000 0000
plant002 0000 0000 0000 0000
plant003 0000 0000 0000 0000
plant004 0000 0000 0000 0000
...
```
* Save this file as crop.txt within the camera folder which the image came from. 

### Running the script

Before running the script, navigate to the JoanPyTRiP folder and ensure that in that folder exists a folder named "cropped" and a folder named "output" these folders must be empty. If there are things in these folders, check with the person who ran the script last to make sure these outputs have been saved somewhere before deleting them. 

* I like to keep a document called "lineofcode.txt" in each camera folder to write out my code. In this lineofcode document, this is present: 

Example: 
## Directory first: 
```
cd /Users/greenhamlab/Documents/Leaf_Movement/TRiP-Joan/code/PyTRiP

```
* Before running anything, change the parameters of this line of code for your case. In input line should include the path to the input folder within the camera. The output and code pathways can remain the same generally. The crop.txt pathway should be edited to direct to the crop.txt you've created. 
* Now, open terminal from the desktop. Paste the first line into the terminal and run it. Once finished, paste the second line and run it. 
* Outputs can be found in the "output" and "cropped" folders created earlier in this protocol. I strongly suggest copying these entire folders and pasting them into the camera folders so that the outputs never get overwritten by future runs. 
* Check # of pictures, Command A then drag and not drop
* Run code in terminal, paste code

## Mapping the genotype to the data
### The purpose of this is to add the genotype information to analyzed data. 
* First, download the merging.py file and move it into the analysis folder.
* You will need two files to run this scipt.
*   The first is the processed data file, saved as a CV, with the columns "ID", "Period", "CTP", "Rsquared", and "RAE".
*   The second is the ID and Genotype Key. This file should be set up with one column labeled "ID" containing the codes: plant001, plant002, plant003 and so on, on their own lines. The second column should be "Genotype", containing the corresponding genotype for each ID line.
* Replace the names of the csvs in the script and change directories to your local analysis folder and run the script:

```
cd /PATH/TO/FOLDER/
python3 merging.py
```
