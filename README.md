#Title			: CDFDropletDetection
######Description		: Utilizing OpenCV libraries in python to track droplets in video in python script, directories provided with literature and testing materials
##Author			: M.B. Adams
##Date			: 09-01-2015
######Version		: 1.0
######Notes			: (For python script) Associated input file (.inp), output in ASCII.
######Python Version		: 2.6.6

Welcome to the README.md file for the Chaotic Dripping Faucet (CDF) Droplet Detection repo from GH. This file will hopefully answer any necessary questions you need about using this code for the CDF Experiment for the Advanced Laboratory at the University of Rochester, Department of Physics and Astronomy. This code was made so that students can detect droplets in the experiment in question from video taken with a GoPro camera, that can film at 300 frames per second. If this README.md does not satisfy your needs, please contact the author at madams@pas.rochester.edu


## REPO FLOW
1. README.md: (read this first, of course)
2. DropletDetector.py: The script that does the detecting.
3. **ManualsnPapers**
   1. CameraInstructions.pdf: Instructions written by Ryan Vogt on how to use the GoPro camera (filming in slow motion, and taking 300 fps video).
   2. CIDFLabManual.pdf: Lab manual, written in general, for the experiment. May be kind of old, and in need of an update.
   3. coullet-mahadevan-riera-2004: Physics article written on the experiment, as a reference.
   4. laws-2003.pdf: Teaching physics article on student experiments that deal with chaotic dynamics.
4.** TestVideonData**
     1. DropletData.dat: An example of the output from DropletDetector.py.
     2. Untitled1.mov: A movie (not filmed at 300 fps, with shitty quality) that the script was used on. So now you know what things will be like in the worst case scenario.
5. VideoAnalysis.inp: The input file that the script DropletDetector.py reads.

## BEFORE USING DropletDetector.py

Visit (http://shop.gopro.com/softwareandapp/gopro-studio/GoPro-Studio.html) the GoPro Studio webpage to download the GoPro Studio Software. It is free; open source. Once you have downloaded this. Take the video you want to extract data from, and ensure that you have turned off the ***fish eye***, which the camera innately uses.

## HOW TO RUN DropletDetector.py
1. Open VideoAnalysis.inp
   * First line: path to your movie.
   * Second line: path to your output file, and you can choose its name. Would suggest marking it as an ascii, .dat file.
   * x_left: Cropping of the video from the left.
   * x_right: Cropping of the video from the right
   * thres1: First level of thresholding
   * thres2: Second level of thresholding
   * R_min: Minimum radius of circle
   * R_max: Maximum radius of circle
2. Ultimately you will want to go through 1. and debug the processing based on these parameters.
3. Once you have your video, name of your output file, and everything of choice ready, you can then run: **python DropletDetector.py** in the directory where your code is located. Note that this script does not use python3.
4. You may want to go through a process of debugging for each video so that you can hone the detection as best as possible.
5. Once the script has gone through the whole video, it should spit out an output file. In the case we have here, with the VideoAnalysis.inp, it is called **DropletData.dat**. You can choose this name to be whatever you want. There are no headers written for the file I/O, however each column in the .dat file represents the following:
   * Column 1: The frame for which a circle was detected
   * Column 2: The x-position of the center of that circle
   * Column 3: The y-position of the center of that circle
   * Column 4: The radius of that circle
6. For more on the OpenCV documentation on the HoughCircle detector used, check out: http://docs.opencv.org/modules/imgproc/doc/feature_detection.html?highlight=houghcircles#houghcircles

