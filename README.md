# Speech Synthesis Model Development Using VITS

## Overview
This project aims to develop a speech synthesis model using the VITS architecture, focusing on an underrepresented language from the AI4Bharat corpus. The goal is to create a high-quality audio synthesis model that can convert text to speech in a unique language, ensuring utility and accessibility for diverse users.

<img width="333" alt="Screenshot 2024-11-06 at 3 34 38 AM" src="https://github.com/user-attachments/assets/5e5a13bb-87ba-406c-a5b2-c8a526972dfc">


## Key Features
- **Language Selection**: Focuses on underrepresented languages to enhance diversity in speech synthesis models.
- **Data Acquisition**: Utilizes datasets from AI4Bharat Indic Voices or Svarah, ensuring compliance with data usage rights.
- **Data Preparation**: Involves thorough preprocessing of audio and transcript data for model training.
- **Model Configuration**: Configured VITS model tailored to specific language and dataset requirements.
- **Model Training**: Implements robust training protocols with performance monitoring.
- **Model Evaluation**: Rigorous evaluation against quality standards using validation and test datasets.
- **Optimization and Refinement**: Continuous improvement based on testing feedback to enhance model performance.
- **Deployment**: Enables users to convert WAV audio to FLAC via a WebSocket connection.
- **Documentation and Sharing**: Comprehensive documentation provided, including setup and usage instructions.

## Implementation Steps

### 1. Language Selection
Select a language from the AI4Bharat corpus that is underrepresented in current models. This selection is crucial for ensuring the model's uniqueness and utility.

### 2. Data Acquisition
Download the necessary datasets from [AI4Bharat Indic Voices](https://ai4bharat.org/indic-voices/) or [Svarah](https://svarah.org/), ensuring compliance with data usage rights. Focus on non-news datasets to maintain relevance.

### 3. Data Preparation
- **Pre-processing**: Clean and normalize audio inputs and ensure transcripts are properly formatted.
- **Data Splitting**: Split the dataset into training, validation, and testing sets in an 80/10/10 ratio.

### 4. Model Configuration
Clone the [VITS GitHub repository](https://github.com/juliuskrantz/VITS) and configure it to handle the chosen language and specific dataset requirements.

### 5. Model Training
Train the model using the prepared datasets. Monitor performance issues and make necessary adjustments to optimize training efficiency.

### 6. Model Evaluation
Evaluate the model using the validation and test sets to ensure it meets quality standards in audio synthesis. Use metrics such as Mean Opinion Score (MOS) for subjective quality evaluation.

### 7. Optimization and Refinement
Refine the model based on feedback and testing results to improve accuracy and overall performance.

### 8. Deployment
Prepare the model for deployment, allowing users to easily convert WAV audio to FLAC format using a WebSocket connection.

### 9. Documentation and Sharing
Document the entire process, including setup, configuration, and usage instructions. If permissible, share the model and training scripts for community use and further research.

## Requirements
Ensure you have the following dependencies installed:

- Python 3.6 or higher
- `torch`
- `torchaudio`
- `websockets`
- `soundfile`
- `numpy`

### Install Dependencies
Create a `requirements.txt` file with the following content:

```plaintext
torch
torchaudio
websockets
soundfile
numpy
```


Then run:

<img width="245" alt="Screenshot 2024-11-06 at 3 19 41 AM" src="https://github.com/user-attachments/assets/e522a818-32f4-4e98-a66c-ce816bb64088" >

Clone the Repository:
Clone this repository to your local machine:

<img width="521" alt="Screenshot 2024-11-06 at 3 20 14 AM" src="https://github.com/user-attachments/assets/c3c83458-a7e7-4820-8fa8-39b1b6e42631">

Set Up the Environment:
Install the required packages using the command provided above.

Run the Model:
Follow the specific instructions for training and running the model, which will be provided in the project’s documentation.


### Contributions are welcome! If you discover any bugs or have ideas for enhancements, feel free to fork the repository and submit a pull request.


