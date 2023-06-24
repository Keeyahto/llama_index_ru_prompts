"""Default choice select prompt."""

from llama_index.prompts.base import Prompt
from llama_index.prompts.prompt_type import PromptType

# deprecated, kept for backward compatibility
ChoiceSelectPrompt = Prompt

DEFAULT_CHOICE_SELECT_PROMPT_TMPL = (
    "Ниже показан список документов. Каждому документу присвоен номер, а также представлено "
    "краткое описание документа. Также предоставлен вопрос.\n"
    "Укажите номера документов, которые вы должны просмотреть для ответа на вопрос, "
    "в порядке убывания релевантности, а также оценку релевантности. Оценка релевантности - это число от 1 до 10, "
    "основанное на том, насколько вы считаете документ релевантным для вопроса.\n"
    "Не включайте документы, которые не относятся к вопросу.\n"
    "Пример формата:\n"
    "Документ 1:\n<краткое описание документа 1>\n\n"
    "Документ 2:\n<краткое описание документа 2>\n\n"
    "...\n\n"
    "Документ 10:\n<краткое описание документа 10>\n\n"
    "Вопрос: <вопрос>\n"
    "Ответ:\n"
    "Документ: 9, Релевантность: 7\n"
    "Документ: 3, Релевантность: 4\n"
    "Документ: 7, Релевантность: 3\n\n"
    "Давайте попробуем сейчас:\n\n"
    "{context_str}\n"
    "Вопрос: {query_str}\n"
    "Ответ:\n"

)
DEFAULT_CHOICE_SELECT_PROMPT = Prompt(
    DEFAULT_CHOICE_SELECT_PROMPT_TMPL, prompt_type=PromptType.CHOICE_SELECT
)
