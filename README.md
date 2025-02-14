# 🎬 Movie Recommendation System 🍿  

## 🚀 Overview  
This is a **Movie Recommendation System** that suggests movies based on user preferences using **Natural Language Processing (NLP) & Machine Learning**.  
It uses **Cosine Similarity** and **Bag of Words (BoW)** encoding for recommendations.

## ⚡ Features  
✅ **NLP Preprocessing**: Lowercasing, Tokenization, Stemming, Stopword Removal  
✅ **Feature Engineering**: Bag of Words (BoW) for text encoding  
✅ **Similarity Calculation**: Cosine Similarity to recommend the most relevant movies  
✅ **Interactive Web App**: Built using **Streamlit**  
✅ **Movie Posters**: Integrated with **TMDb API**  
✅ **Genre-Based Filtering**: Users can filter recommendations by movie genre  

---

## 📂 Project Structure  
📂 Movie-Recommendation-System
│── app.py # Streamlit Web App
│── Movie Recommendation System.ipynb # Jupyter Notebook (Data Preprocessing & Model)
│── movie_dict.pkl # Processed movie data
│── similarity.pkl # Precomputed similarity matrix
│── tmdb_5000_movies.xls # Movie dataset
│── tmdb_5000_credits.csv # Movie cast & crew dataset
│── requirements.txt # List of dependencies
│── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Installation  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/2-0-0-5-emil/-Movie-Recommendation-System.git
cd Movie-Recommendation-System
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run app.py
✅ The web app should now open in your browser!

🌐 Live Demo
You can try the live demo here:
🔗 Try the App Here

🚀 Deploy on Streamlit Cloud
Want to deploy your project for free on Streamlit Cloud? Follow these steps:

1️⃣ Push Your Project to GitHub
Make sure all your latest changes are pushed:

sh
Copy
Edit
git add .
git commit -m "Final update for Streamlit deployment"
git push origin main

2️⃣ Go to Streamlit Cloud
🔗 https://share.streamlit.io/

3️⃣ Deploy Your App
Click "New App"
Select your GitHub repository
Choose app.py as the main script
Click "Deploy" 🚀
✅ Your app will be live, and you can share the link!

🔗 Links
📌 GitHub Repository: https://github.com/2-0-0-5-emil/-Movie-Recommendation-System
📌 Live Demo: https://4mjpsxjnraxnhjpchfp9bm.streamlit.app/

💡 Future Improvements
🔹 Improve recommendation accuracy with Deep Learning models
🔹 Add Collaborative Filtering for better personalization
🔹 Integrate user ratings & feedback

Would love to hear your feedback! 🎥🔥

#MachineLearning #NLP #Python #AI #MovieRecommendation #Streamlit #DataScience
