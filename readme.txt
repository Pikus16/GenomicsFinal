README:
Derek Modzelewski
Ben Pikus


Sample execution:
       sh run.sh
       run.sh contains the sample execution from the final project description
       

Data Files:
     for each of the 33 tissues:
     	 A .bed file with a one line header, first 4 columns are description, each row is a SNP, each column is a patient, the intersection is that patient's standardized expression of that SNP in this tissue.
     SINCE OUR DATA IS LARGE AND HARD TO OBTAIN:
     	   you may simply use our preprocessed versions, putting them in $results/pickled, where $results is the output directory specified in run.sh


Expected Output Files:
	 In $results/pickled, there should be:
	    dat.y.pickle
	    dat.yt.pickle
	    tdat:
		random1.y.pickle
	   	random1.yt.pickle
	    models:
	    	(pickle files for the trained models)
	 In $results/plots
	    for each organ, i:
	    	$results/plots/i:
			contains a plot for each tissue, where patients are colored by their quadrant in i
	 BIC_Scores.png
		plot of BIC vs h settings
	 SSD_Scores.png
		plot of SSD vs h settings for trivial model and our model, for random data and our data (any of the 4 combinations)
	 results.txt
		final output: best h value, SSD with that h, %variance explained


