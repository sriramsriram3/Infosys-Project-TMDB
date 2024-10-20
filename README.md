# TMDB Box Office Prediction

## Project Description
This project focuses on predicting the box office revenue of movies using data from The Movie Database (TMDB). By analyzing various features such as budget, genres, release date, and cast, the model attempts to predict the total revenue generated by each movie. This project was completed during an internship at Infosys, guided by mentor **S Muni Kiran**.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Features](#features)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TMDB-Box-Office-Prediction.git

2. Navigate to the project directory:
   ```bash
   cd TMDB-Box-Office-Prediction

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt

## Usage

1. Preprocessing: Run the preprocessing scripts to clean and prepare the TMDB data:
   ```bash
   python preprocessing.py
   
2. Training the Model: To train the model, run the following command:
   ```bash
   python train.py
   
3. Predicting: Once the model is trained, you can use it to make predictions on new data:
   ```bash
   python predict.py --input new_movie_data.csv

4. Evaluation: Evaluate the model’s performance using test data:
   ```bash
   python evaluate.py


## Features
Predicts box office revenue for movies using regression techniques.
Uses features like budget, genre, release date, and cast information.
Provides tools for data preprocessing, training, and evaluation.

## Technologies Used
Python: Primary programming language used for data processing and model development.
Scikit-Learn: Used for implementing machine learning models.
Pandas: For data manipulation and cleaning.
Matplotlib & Seaborn: For data visualization.
Jupyter Notebooks: For exploratory data analysis.
TMDB Dataset: The Movie Database (TMDB) as the primary data source.
Contributing
Contributions are welcome! Feel free to submit a pull request or report issues to improve the project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
Presented by:
Sriram Simhadri
Email: Simhadrisriram3@gmail.com
