"""Prompts for ChatGPT."""

from langchain.prompts.chat import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from llama_index.prompts.prompts import RefinePrompt, RefineTableContextPrompt

# Refine Prompt
CHAT_REFINE_PROMPT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "У нас есть возможность уточнить вышеуказанный ответ "
        "(только если это необходимо) с помощью дополнительного контекста ниже.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Исходя из нового контекста, уточни исходный ответ для лучшего "
        "ответа на вопрос. "
        "Если контекст не является полезным, выведи исходный ответ снова."

    ),
]


CHAT_REFINE_PROMPT_LC = ChatPromptTemplate.from_messages(CHAT_REFINE_PROMPT_TMPL_MSGS)
CHAT_REFINE_PROMPT = RefinePrompt.from_langchain_prompt(CHAT_REFINE_PROMPT_LC)


# Table Context Refine Prompt
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "Мы предоставили схему таблицы ниже. "
        "---------------------\n"
        "{schema}\n"
        "---------------------\n"
        "Мы также предоставили некоторую контекстную информацию ниже. "
        "{context_msg}\n"
        "---------------------\n"
        "Исходя из контекстной информации и схемы таблицы, "
        "уточни исходный ответ для лучшего "
        "ответа на вопрос. "
        "Если контекст не является полезным, верни исходный ответ."

    ),
]
CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC = ChatPromptTemplate.from_messages(
    CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS
)
CHAT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt.from_langchain_prompt(
    CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC
)
