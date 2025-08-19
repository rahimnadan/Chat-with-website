

# 💬 Chat-with-Website

Chat-with-Website is a **Generative AI project** that enables you to easily chat with any website.  
It provides a clean UI, simple setup, and can be extended or integrated into other applications with minimal effort.  



## ✨ Features
- 🎨 **Nice User Interface** – Built with Streamlit for simplicity and usability.  
- 🤖 **Auto Captcha Solution** – Automatically handles captcha challenges.  
- 🔑 **Open-Source API Keys** – Flexible for experimentation and integration.  
- 🔌 **Easily Extensible** – Can be integrated into other projects with minimal modification.  



## ⚙️ Project Setup

Follow the steps below to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/rahimnadan/Chat-with-website.git
cd Chat-with-website
````

### 2. Create a Virtual Environment

Using [uv](https://github.com/astral-sh/uv) (recommended):

```bash
uv venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy your **GROQ API key** into `.env` or export it directly:

```bash
export GROQ_API_KEY=<your_key_here>
```

### 5. Run the Application

```bash
streamlit run app.py
```



## 📂 Project Structure

```
Chat-with-website/
│── app.py              # Main Streamlit application
│── requirements.txt    # Project dependencies
│── .env                # Environment variables (add GROQ API key here)
│── README.md           # Project documentation
```



## 🚀 Roadmap / Future Improvements

* 🔍 Support for multiple LLM providers.
* 🌐 Browser extension for direct website integration.
* 🛡️ Advanced session management & security features.



## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.



## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.



### ⭐ If you like this project, consider giving it a star on GitHub!

