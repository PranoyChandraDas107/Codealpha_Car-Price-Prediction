Car Price Prediction Using Machine Learning

A Machine Learning regression project that predicts the selling price of used cars based on available vehicle features such as present price, driven kilometers, car age, fuel type, transmission, selling type, and previous ownership.

📌 Project Overview

The goal of this project is to build a Machine Learning model capable of estimating the selling price of a used car.

The project covers the complete Machine Learning workflow:

Data Analysis → Exploratory Data Analysis → Data Preprocessing → Feature Engineering → Model Training → Model Evaluation → Price Prediction

The project uses Python and popular Machine Learning libraries including Pandas, Scikit-learn, Matplotlib, Seaborn, and Joblib.

🎯 Objectives
Analyze a real-world used car dataset.
Perform data cleaning and preprocessing.
Handle duplicate records.
Perform exploratory data analysis.
Create a Car_Age feature from the manufacturing year.
Convert categorical variables into numerical features.
Train multiple regression models.
Compare model performance using evaluation metrics.
Select a regression model for prediction.
Save the trained model for future predictions.
Build a command-line prediction system.

📊 Dataset

The dataset contains 301 records and 9 original features.

Original Features
Feature	Description
Car_Name	Name of the car
Year	Manufacturing year
Selling_Price	Target variable — selling price
Present_Price	Current/ex-showroom price
Driven_kms	Kilometers driven
Fuel_Type	Fuel type of the car
Selling_type	Dealer or Individual
Transmission	Manual or Automatic
Owner	Number of previous owners

After removing duplicate records, 299 records were used for modeling.

Note: The provided dataset does not contain explicit Horsepower or a separate Brand_Goodwill feature. Therefore, the model uses the features actually available in the dataset. Driven_kms represents vehicle usage/mileage information.

🛠️ Technologies Used
Python
Pandas — Data analysis and preprocessing
NumPy — Numerical calculations
Scikit-learn — Machine Learning
Matplotlib — Data visualization
Seaborn — Exploratory data visualization
Joblib — Model serialization

🔄 Machine Learning Pipeline
Raw Dataset
     ↓
Data Analysis
     ↓
Remove Duplicate Records
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Save Trained Model
     ↓
User Input
     ↓
Predicted Car Price

🔍 Exploratory Data Analysis

The project performs several EDA visualizations:

Selling Price Distribution
Present Price vs Selling Price
Year vs Selling Price
Driven KMs vs Selling Price
Fuel Type vs Selling Price
Transmission vs Selling Price
Numerical Feature Correlation

These visualizations help understand relationships between vehicle characteristics and selling price.

🤖 Models Evaluated

Three regression models were tested:

Linear Regression
Decision Tree Regressor
Random Forest Regressor
Model Performance

Using an 80/20 train-test split with random_state=42:

Model	MAE	RMSE	R² Score
Linear Regression	1.4725	2.5245	0.7527
Decision Tree	1.1085	2.1056	0.8280
Random Forest	1.4707	3.5117	0.5215

For this particular train/test split, the Decision Tree Regressor produced the strongest test-set metrics among the three evaluated models.

These results are specific to this dataset and split. More robust model comparison could be performed using cross-validation and hyperparameter tuning.

📈 Final Model

The Decision Tree Regressor was trained and saved as:

car_price_model.pkl

Evaluation results:

MAE  : 1.1085
MSE  : 4.4336
RMSE : 2.1056
R²   : 0.8280
Evaluation Metrics

MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

RMSE — Root Mean Squared Error

Penalizes larger prediction errors more strongly.

R² Score

Measures how much of the variation in the target variable is explained by the model.

⭐ Feature Importance

The Decision Tree model identified the following feature importance values:

Feature	Importance
Present_Price	91.15%
Car_Age	7.92%
Driven_kms	0.66%
Fuel_Type_Petrol	0.11%
Transmission_Manual	0.09%
Fuel_Type_Diesel	0.05%
Selling_type_Individual	0.02%
Owner	~0.00%

For this trained model, Present_Price contributed the largest share of the model's feature importance.

📁 Project Structure
Car Price Prediction/
│
├── venv/
│
├── car data.csv
├── processed_car_data.csv
│
├── data_analysis.py
├── eda.py
├── preprocessing.py
├── train_model.py
├── predict.py
│
├── car_price_model.pkl
├── requirements.txt
└── README.md

⚙️ Installation & Setup

Follow the steps below to run this project locally.

1. Clone the Repository
   
git clone https://github.com/PranoyChandraDas107/Codealpha_Car-Price-Prediction.git
3. Navigate to the Project Directory

cd Codealpha_Car-Price-Prediction
4. Create a Virtual Environment

python -m venv venv
5. Activate the Virtual Environment

Windows PowerShell

.\venv\Scripts\Activate.ps1
Windows Command Prompt

venv\Scripts\activate
macOS / Linux

source venv/bin/activate
6. Install Required Dependencies

pip install -r requirements.txt
7. Verify the Installation

Run the following command to verify that the required libraries are installed correctly:

python -c "import pandas, numpy, sklearn, matplotlib, seaborn, joblib; print('All libraries installed successfully')"

Expected output:

All libraries installed successfully
7. Run the Project

Run the data analysis:

python data_analysis.py

Run Exploratory Data Analysis:

python eda.py

Run data preprocessing:

python preprocessing.py

Train the Machine Learning model:

python train_model.py

Predict a car's selling price:

python predict.py

📌 Notes
Python 3.x is required.
Make sure the dataset files are located in the project root directory.
The trained model is stored in car_price_model.pkl.
Activate the virtual environment before running the project.

👨‍💻 Author

Pranoy Chandra Das
Software Engineering 
