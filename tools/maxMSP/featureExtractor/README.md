# Feature Extractor

This patch detects signals on it's inputs and extracts 33 features from the audio signal, to then be sent to Wekinator to train a predictive model.

It's entirely dependent on the CNMAT analyze~ external to perform the analysis, and but additionally does some light conditioning to the data. The data is then prepared to send to Wekiantor's inputs over OSC, using the CNMAT OpenSoundControl external.

This is based on the Bark Extractor by Rebecca Fiebrink, for her class[Machine Learning for Musicians and Artists](https://www.kadenze.com/courses/machine-learning-for-musicians-and-artists/info).