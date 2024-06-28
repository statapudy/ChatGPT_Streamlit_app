# config.py

# THIS IS THE FILE YOU SHOULD EDIT TO CUSTOMIZE THE APP. DO NOT EDIT app.py UNLESS YOU KNOW WHAT YOU ARE DOING.

############################################################################################################

# Below is the configuration for the chatbot

# The model_name refers to the name of the model you want to use. You can choose from the following models: https://platform.openai.com/docs/models/gpt-4o
ai_model = "gpt-4o"

# Temperature refers to the randomness/creativity of the responses. A higher temperature will result in more random/creative responses. It varies between 0 and 1.
temperature = 0

# Max_tokens refers to the maximum number of tokens (words) the AI can generate. The higher the number, the longer the response. It varies between 1 and 2048.
max_tokens = 1000

# Frequency penalty parameter for the response. Higher penalty will result in more diverse responses. It varies between 0 and 1.
frequency_penalty = 0.5

# Presence penalty parameter for the response. Higher penalty will result in less repetitive responses. It varies between 0 and 1.
presence_penalty = 0.5

# Below is all the text you can customize for the app. Don't remove the quotations around the text. Don't change the variable names.

# The title of the app
app_title = "OpenAI Powered Chatbot for Biology Students"

# The subtitle of the app
app_author = "courtesy of UCSD School of Biological Sciences"

# This is an intro paragraph you can add under the title. it is not currently being used in the app.
intro_para = " "

# The user's instructions for the app
instructions = '''
Welcome to the Open-Ended GPT-4 Chatbot! This guide will help you understand how to use the chatbot effectively and provide tips for creating effective prompts.

## Getting Started

1. **Open the Application**: Launch the chatbot application from your browser.
2. **Enter Your Message**: Type your message in the input box at the bottom of the chat window.
3. **Send Your Message**: Press `Enter` or click the `Send` button to submit your message.
4. **Read the Response**: The chatbot will generate a response and display it in the chat window.

## Effective Prompting Guide

To get the most out of the chatbot, it's essential to craft your prompts effectively. Here are some tips:

### Be Clear and Specific

- **Specificity**: Clearly state what you want to know or discuss. For example, instead of asking, "Tell me about biology," ask, "Can you explain the process of photosynthesis?"
- **Context**: Provide context if necessary. For example, "In the context of human biology, what is the function of the mitochondria?"

### Use Proper Grammar and Punctuation

- **Clarity**: Use correct grammar and punctuation to ensure your prompt is easy to understand.
- **Complete Sentences**: Write in complete sentences to avoid ambiguity.

### Ask Open-Ended Questions

- **Engagement**: Open-ended questions encourage detailed responses. For example, "What are the benefits of using AI in education?" is better than "Is AI useful?"

### Break Down Complex Questions

- **Simplify**: If you have a complex question, break it into smaller, more manageable parts. For example, instead of asking, "How does the nervous system work?" you could ask, "What are the main components of the nervous system?" followed by "How do neurons transmit signals?"

### Experiment and Iterate

- **Trial and Error**: Don't be afraid to experiment with different phrasing. If you don't get the desired response, try rephrasing your question.
- **Feedback**: Use the chatbot's responses to refine your prompts for better results.

## Example Prompts

1. **General Inquiry**: "Can you explain the theory of evolution?"
2. **Detailed Explanation**: "What are the main stages of cellular respiration?"
3. **Contextual Query**: "In computer science, what is the significance of algorithms?"
4. **Comparative Question**: "How does renewable energy compare to fossil fuels in terms of environmental impact?"
5. **Exploratory Question**: "What are some of the latest advancements in biotechnology?"

## Troubleshooting

- **No Response**: If the chatbot does not respond, check your internet connection and try refreshing the page.
- **Inaccurate Responses**: If the response seems inaccurate, try rephrasing your prompt for clarity.
- **Technical Issues**: For technical issues, contact the support team or refer to the application's help section.

By following these guidelines, you can effectively interact with the GPT-4 chatbot and obtain meaningful and informative responses. Enjoy exploring the capabilities of this advanced AI tool!
'''

# The title of the sidebar
sidebar_title = "Resources for effectively using an AI chatbot"

app_creation_message = "The template for this app was created by Keefe Reuther and the members of the Reuther Lab - [https://reutherlab.biosci.ucsd.edu/](https://reutherlab.biosci.ucsd.edu/)"

app_repo_license_message = "It can be found at [https://github.com/The-Reuther-Lab/ChatGPT_Streamlit_app](https://github.com/The-Reuther-Lab/ChatGPT_Streamlit_app) and is distributed under the GNU GPL-3 License."

warning_message = "**ChatGPT can make errors and does not replace verified and reputable online and classroom resources.**"

############################################################################################################

# System role message to set limits on user questions
system_role_message = """
This chatbot is assuming the role are an assistant knowledgeable in university-level biology. I will only answer questions likely related to biology, teaching, learning, and related topics that may be of relevance in a biology classroom. If a user asks a question outside of biology, this chatbot will inform you that your question is outside of its purview and prompt you to ask another question
"""

############################################################################################################

### RESOURCES

# Resources: In this section, you can add links for the student to access and potentially learn more about the topic or verify information.
# You can add the title of the resource, the URL, and a brief description. To delete or add more resources, follow the same format.
resources = [
    {
        "title": "OpenAI Prompt engineering guide",
        "url": "https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results",
        "description": "A guide to help you craft effective prompts for the OpenAI chatbot. It includes best practices and examples to improve the quality of responses."
    },
    {
        "title": "UC Berkeley Library Guide to Detecting Fake News",
        "url": "https://guides.lib.berkeley.edu/fake-news",
        "description": "This UC Berkeley Library guide offers comprehensive strategies and resources for identifying fake news, understanding its impact, and evaluating the credibility of various news sources, including lists of known fake news sites and tips for detecting misinformation."
    },
        {
        "title": "Is it cheating to use ChatGPT?",
        "url": "https://guides.lib.berkeley.edu/fake-news",
        "description": "The UC San Diego Academic Integrity Office provides guidance on the appropriate use of generative AI tools in educational settings, emphasizing the importance of adhering to instructor guidelines and the potential consequences of misuse, including integrity violations and academic penalties."
    },
]
