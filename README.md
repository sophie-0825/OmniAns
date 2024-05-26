<div align="center">
<h1>
PDF Chatbot Template
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

This example demonstrates how to use asyncflows PDF Chatbot to extract text from PDF files and use it to answer questions.

It extracts text from PDFs (`asyncflows[pdf]`), 
and runs retrieval and reranking models locally on your computer (`asyncflows[transformers]`).

<div align="center">
<img width="1180" alt="chatbot" src="https://github.com/asynchronous-flows/pdf-chatbot-example/assets/24586651/8f5c8335-59e0-491b-9428-6ffe4379ebfd">
</div>

## Running the Example

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/pdf-chatbot-example
```

3. Change into the directory

```bash
cd pdf-chatbot-template
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

6. Run the example

```bash
python chatbot.py
```

## Using your own Data

To use your own data, replace the PDFs in the `documents/` directory with your own PDFs. The chatbot will then use the text from these PDFs to answer questions.
