# Cultural Remix
EECS 352 Final Project
Created by: Sonia Nigam and Amar Shah

## Installing
The following dependencies need to be installed via command line to run our script.<br />
MSAF <br />
pickle <br />
librosa <br />
scipy <br />
fastdtw <br />
sklearn <br />

## Run 
jupyter notebook culturalRemix.ipynb

## File Hierarchy
This script runs under the assumption that the user has installed all the packages above. In addition the link below allows the user to download our Indian Beats Database. The user can have their own Beats Database, but for the program to run, their must be a folder called "BeatsDatabase" with all of the indian beats in it. 

link: https://www.dropbox.com/s/gw07q13j8p5qqg8/BeatsDatabase.zip?dl=0

Furthermore, the user must have a folder called "HipHop" containing any song they would like to obtain a cultural remix of. 

## Input
The song name is hardcoded in the program. You can see in the third input cell of the jupyter notebook the user can type which song from their HipHop folder that they want to input into the program. 


## Output
The program will output a final indian remix of the inputted song. The user has the option to use a wavwrite function to download the song

The program will output the percussive element of the song titled "percussive_song.mp3" in the culturalRemix Folder

Lastly, when running the program the first time, the program will output two pickled files. The program will output indianSegments.pickle and indianSpectrograms.pickle. These pickle files will allow the program to run significantly faster after the first run. 

## Website
You can find a more detailed version of our project at the link below. Our final presentation can also be located here. 

link: https://sonianigam.github.io/culturalRemix/

