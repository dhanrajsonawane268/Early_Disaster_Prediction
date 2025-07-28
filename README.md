# 🌪️ Early Disaster Prediction using Machine Learning

This is an intelligent desktop-based application that predicts natural disasters such as floods, earthquakes, and cyclones using machine learning models. It alerts users in real-time with an interactive GUI, sound alerts, and report generation.

---

## 🚀 Features

- ✅ Predict disasters (Flood, Earthquake, Cyclone, or None) using ML
- 📊 Visual prediction charts using `matplotlib`
- 🖥️ Interactive GUI built with `customtkinter`
- 🧾 PDF Report generation with disaster result
- 🔊 Sound alert system for high-risk predictions
- 📂 Dynamic input handling from `latest_input.csv`
- 🧠 Model retrainable via `train_model.py`
- 📁 Structured logging of predictions

---

## 🛠️ Tech Stack

| Module            | Tech / Tool Used                  |
|-------------------|-----------------------------------|
| Language          | Python                            |
| GUI               | `customtkinter`, `Tkinter`        |
| ML                | `scikit-learn` (Random Forest)    |
| Data Processing   | `pandas`, `numpy`                 |
| Visualization     | `matplotlib`                      |
| Report Export     | `fpdf`                            |
| Sound Notification| `playsound`                       |

---

## 📂 Project Folder Structure

Early_Disaster_Prediction/
│
├── app/
│ ├── gui.py # GUI logic
│ ├── predict.py # ML prediction logic
│ ├── csv_reader.py # Input CSV reader
│ ├── logs/ # Prediction log files
│ ├── *.pdf # Exported reports
│ └── model.pkl # Latest model for prediction
│
├── data/
│ └── flood_dataset.csv # Training dataset
│
├── model/
│ ├── disaster_model.pkl # Trained model file
│ └── main.py # Model retraining script (optional)
│
├── main.py # Combined GUI + Logic launcher
├── main_predictor.py # Standalone prediction module
├── train_model.py # Training script (generates .pkl)
├── requirements.txt # Required Python libraries
└── README.md # Project documentation



---

## 🧠 How the Model Works

- **Algorithm**: Random Forest Classifier
- **Input Features**:
  - Temperature
  - Rainfall
  - Humidity
  - Wind Speed
- **Training**: `train_model.py` trains the model using `flood_dataset.csv`
- **Prediction**: `predict.py` reads from CSV or GUI input and uses model to predict

---

## 🖼️ GUI Functionalities

- 🧾 Accept user input (4 parameters)
- 📈 Display prediction result with confidence
- 📊 Real-time plot of disaster probability
- 🔊 Trigger sound if disaster is likely
- 🖨️ Export results into PDF report
- 🧠 Auto-load trained model for faster inference

---

## 🧪 Installation & Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dhanrajsonawane268/Early_Disaster_Prediction.git
cd Early_Disaster_Prediction


2️⃣ (Optional) Create a Virtual Environment


python -m venv venv
venv\Scripts\activate   # Windows only

3️⃣ Install Required Libraries
You can use requirements.txt:


pip install -r requirements.txt
Or manually install:

pip install pandas numpy matplotlib scikit-learn fpdf customtkinter playsound


▶️ Run the Application
To launch GUI:


python main.py
Or directly run:


cd app
python gui.py
To retrain ML model:



python train_model.py
📸 Sample Output



Prediction: FLOOD
Probability: 89.2%
Alert Triggered: YES
PDF Report Saved: Disaster_Report_20250725_073605.pdf

📜 Dependencies
Here are the Python libraries used:

nginx

pandas
numpy
matplotlib
scikit-learn
fpdf
customtkinter
playsound
All are included in requirements.txt

📌 Future Enhancements
Integrate live weather API (OpenWeatherMap)

Add SMS/Email Alert system using Twilio

Web Interface (Streamlit/Django)

Store user inputs in DB for analytics

Improve model with real-time weather feeds

✨ Author
Dhanraj Rajendra Sonawane
📧 dhanrajsonawane268@gmail.com
🧑‍🎓 MCA | Python & AI/ML Enthusiast
🔗 GitHub Profile

📢 Contribution
Feel free to fork this repo, create a branch, make changes and open a pull request.
For major feature changes, open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.
You can use, distribute, and modify freely with attribution.


---

## ✅ What Next?

- Want this `README.md` file generated & uploaded automatically? Just say: **"generate file and upload to GitHub"**
- Want `.gitignore` file too? I’ll generate it.
- Want visual screenshots added? Upload them here or tell me file names in `assets/`.

Ready to upload this perfect README? 😎 Just say the word.

