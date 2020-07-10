# sousvidetracker
Anova Sous Vide Metric Logger

This code is used to log a sous vide cook on a first generation Anova sous vide wand. I run my code on a Raspberry Pi 3 Model B, using the internal bluetooth controller to talk to the sous vided.


# Acknowledgements

Thanks to dfrankland for figuring out how to talk to the Anova Sous Vide.

https://github.com/dfrankland/sous-vide/

Thanks to c3v6a2vy for taking drandkland's work and converting it to a Python library.

https://c3v6a2vy.github.io/pyanova/

# Installation

pip3 install pyanova

# Running the program

Edit the Set Time and Set Temp variables and run the code. 

Import the the CSV into Excel or ElasticSearch / Kibana to visualize the cook. 

