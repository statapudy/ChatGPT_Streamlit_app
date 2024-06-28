# OpenAI Powered Chatbot for Biology Students

### Initially presented at SABER 2024 Workshop B
#### Developing No-Code, AI-Enhanced, Online Study Tools for Biology Students: A Beginner's Workshop

## Overview

This repository contains a Streamlit-based web application designed to facilitate real-time, AI-powered conversations with biology students. The chatbot leverages OpenAI's API to provide an interactive learning tool that enhances the educational experience by offering immediate feedback and assistance.

## Features

- **AI-Powered Conversations**: Utilizes OpenAI's models to generate human-like responses, enabling students to engage in meaningful dialogues.
- **Customizable Configuration**: The chatbot's behavior, including the AI model, temperature, and response frequency, can be tailored via the `config.py` file.
- **User-Friendly Interface**: Built with Streamlit, the application provides an intuitive and easy-to-use chat interface.
- **Educational Integration**: Specifically tailored for use in educational settings, allowing instructors to integrate AI-driven conversational agents into their curricula without requiring extensive technical expertise.
- **Accessible Learning**: Provides an accessible platform for real-time interaction and feedback, enhancing the learning experience for biology students at no cost.

## Installation

To set up the application locally, follow these steps:

1. **Clone the Repository**:
```bash
   git clone https://github.com/The-Reuther-Lab/ChatGPT_Streamlit_app.git
   cd ChatGPT_Streamlit_app
```
   
2. **Install Dependencies**: 
```bash
   pip install -r requirements.txt
```
   
1. **Configure the Application**:
   - Edit the `config.py` file rather than the `app.py` file.
   - You will need to add your OpenAI API key to a `/streamlit/secrets.toml` file if running the app locally.
   - You can also run this app via Streamlit Community Cloud, which will rely on the API key you provide in the Streamlit UI.
   - Here is a link for Streamlit Community Cloud: [Streamlit Cloud](https://share.streamlit.io/)
   - Here is a link for setting up your own OpenAI API key: [OpenAI API](https://openai.com/index/openai-api/)

2. **Run the Application**:
bash
   streamlit run app.py
   
## Configuration

The `config.py` file contains various settings to customize the chatbot:

- **Model Name**: Choose the AI model to use (e.g., "gpt-4").
- **Temperature**: Set the randomness of responses (0 to 1).
- **Max Tokens**: Define the maximum number of tokens for responses.
- **Frequency Penalty**: Adjust the penalty for new tokens based on their existing frequency.
- **Presence Penalty**: Adjust the penalty for new tokens based on whether they appear in the text so far.
- **App Title**: The title displayed in the Streamlit app.
- **App Author**: The author information displayed in the Streamlit app.
- **Instructions**: Instructions displayed to the user on how to interact with the chatbot.
- **Warning Message**: A warning message displayed in the chat window.

## Usage

1. **Launch the Application**:
   Open your browser and navigate to the local server address provided by Streamlit.

2. **Interact with the Chatbot**:
   - Enter your message in the input box at the bottom of the chat window.
   - Press `Enter` or click the `Send` button to submit your message.
   - The chatbot will generate a response and display it in the chat window.

### Workshop Presenters:
- **Keefe Reuther**: Assistant Teaching Professor in Ecology, Behavior, and Evolution at UC San Diego. Co-developer of the course, Data Analysis and Design for Biologists. Researches tools that enhance learners' science process skills, including generative AI.
- **Liam O’Connor Mueller**: Assistant Teaching Professor in Molecular Biology at UC San Diego. Co-developer of the course, Data Analysis and Design for Biologists. Focuses on developing automated tools for improving instruction.
- **Grace Constantian**: Senior undergraduate at UC San Diego majoring in Bioinformatics.
- **Albert Nguyen**: Senior undergraduate at UC San Diego majoring in Human Biology and minoring in Computer Science.

### Workshop Abstract:
In the era of generative artificial intelligence (GenAI) tools like ChatGPT, educators face new challenges. They must integrate these transformative technologies into curricula to enhance student learning and prepare students with the skills they will need to leverage GenAI in industry after graduation (Agathokleous et al., 2023). Discipline-Based Education Research (DBER) on the use of this technology is crucial, as it provides evidence-based strategies for its appropriate use (Lodge et al., 2023; Yeralan & Ancona Lee, 2023).

This hands-on workshop will guide participants through the development of a basic, AI-driven chatbot web application using Streamlit. This chatbot will feature an open-ended chat window with minimal initial prompt structure, providing a simple yet effective tool for real-time student interaction. Targeted at individuals eager to learn about generative AI tools such as ChatGPT, this workshop requires no prior technical knowledge or experience in web design or computer programming.

By the session's conclusion, participants will have created their own web application using OpenAI's API function, offering enhanced privacy and control over the learning activities. In line with the principles of open educational resources (OER) and open-source code, a proof-of-concept web application will be presented as a foundational example.

### Workshop Learning Objectives:
By the end of the workshop, participants will be able to:
- **Generate a Tailored List of 3 Biology-Specific Terms**: Use ChatGPT to create a list of terms and definitions relevant to their course content.
- **Build an Interactive Study Activity**: Develop a Streamlit-based web application to engage students with the tailored list at multiple levels of Bloom’s Taxonomy.
- **Set Up and Customize a Streamlit Web Application**: Create a GitHub repository, connect it to ChatGPT via the OpenAI API, and launch a live web application.
- **Assess Feedback Accuracy**: Conduct simulated student interactions to evaluate and improve the chatbot’s feedback accuracy and pedagogical value.
- **Ethical Integration of AI Tools**: Discuss strategies for integrating AI-enhanced tools into biology education, focusing on impacts, ethical considerations, and future applications in DBER.

### Important Notes
1. **Pre-Workshop Preparation**: Participants should have a Google account, a GitHub account, an OpenAI account to generate an API key, and a Streamlit account.
2. **Workshop Duration**: 3 hours.
3. **Workshop Format**: A combination of live demonstrations, hands-on activities, and group discussions.
4. **DO NOT EDIT THE APP.PY FILE**: This file contains the code for the web application. Participants should only edit the term list in the `config.py` file.
5. **Feedback and Questions**: Please feel free to ask questions and provide feedback during the workshop. We are here to help you learn and grow!

### Resources
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [GitHub Repository](https://github.com/The-Reuther-Lab/ChatGPT_Streamlit_app)

#### License
This project is distributed under the GNU GPL-3 License. See the [LICENSE](https://github.com/The-Reuther-Lab/ChatGPT_Streamlit_app/blob/main/LICENSE) file for more information.