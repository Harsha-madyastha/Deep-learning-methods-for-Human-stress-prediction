# Thesis_Project_Files

This folder contains various aspects of the thesis project, including data preprocessing, feature extraction, and model evaluation. Below is a brief overview of each component:

## Data_Transformation_for_Classification.ipynb

This notebook focuses on preprocessing data for classification tasks. It covers the following steps:
- Importing necessary libraries for data manipulation and visualization.
- Extracting training, test, and development data indices from the partition file.
- Performing data transformation for classification tasks, such as plotting valence and arousal values, visualizing BPM variation, implementing label transformation, and preparing data for machine learning classification.
- Handling class imbalance, normalizing features, and evaluating classification models.

## ECG_Feature_Extraction

- Extracts various features from Electrocardiogram (ECG) signals.
- Features include time-domain, frequency-domain, and non-linear domain features.
- Generates Gramian Angular Summation Field (GASF) and Gramian Angular Difference Field (GADF) plots.
- Utilizes Python libraries such as pandas, numpy, matplotlib, seaborn, scipy, neurokit2, hrvanalysis, and pyts.
- Provides a script `ECG_feature_extraction.py` for running feature extraction.
- Outputs extracted features as CSV files for further analysis.

## Feature_Extraction_with_FAU_Detection_and_Spectrogram_Analysis

- Utilizes the `feat` library for Facial Action Unit (FAU) detection.
- Extracts FAUs from facial images and provides predictions including faceboxes, AU values, emotions, and face pose.
- Saves FAU detection results to a CSV file (`output3.csv`).
- Performs image preprocessing including resizing and adding borders.
- Uses the `parselmouth` library for Spectrogram extraction from audio files.
- Displays waveform and Spectrogram of audio files.
- Provides functions to draw intensity and pitch of the audio.
- Saves waveform, Spectrogram, intensity, and pitch plots as images.

## Multimodal_Feature_Processing_and_Label_Combination

- Utilizes libraries for data preprocessing, feature extraction, and model evaluation.
- Reads partition information from a CSV file to extract data indices.
- Loads pre-trained models and performs inference on validation data.
- Normalizes data using `StandardScaler`.
- Concatenates features from multiple CSV files into a single dataframe.
- Processes biosignals and facial features to create co-learning datasets.
- Saves processed data and labels into new CSV files for further analysis and model training.


