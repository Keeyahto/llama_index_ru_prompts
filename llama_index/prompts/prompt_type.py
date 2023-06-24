"""Prompt types enum."""

from enum import Enum


class PromptType(str, Enum):
    """Prompt type."""

    # суммаризация
    SUMMARY = "суммаризация"
    # вставка узла в дерево
    TREE_INSERT = "вставка_узла"
    # выбор запроса из дерева
    TREE_SELECT = "выбор_из_дерева"
    # выбор нескольких запросов из дерева
    TREE_SELECT_MULTIPLE = "выбор_из_дерева_несколько"
    # вопрос-ответ
    QUESTION_ANSWER = "вопрос_ответ"
    # уточнение
    REFINE = "уточнение"
    # извлечение ключевых слов
    KEYWORD_EXTRACT = "извлечение_ключевых_слов"
    # извлечение ключевых слов из запроса
    QUERY_KEYWORD_EXTRACT = "извлечение_ключевых_слов_из_запроса"

    # извлечение схемы
    SCHEMA_EXTRACT = "извлечение_схемы"

    # текст в SQL
    TEXT_TO_SQL = "текст_в_SQL"

    # контекст таблицы
    TABLE_CONTEXT = "контекст_таблицы"

    # извлечение знаний в виде троек
    KNOWLEDGE_TRIPLET_EXTRACT = "извлечение_троек_знаний"

    # простой ввод
    SIMPLE_INPUT = "простой_ввод"

    # Pandas
    PANDAS = "Pandas"

    # JSON path
    JSON_PATH = "JSON_path"

    # выбор одного варианта
    SINGLE_SELECT = "одиночный_выбор"

    # выбор нескольких вариантов
    MULTI_SELECT = "множественный_выбор"

    VECTOR_STORE_QUERY = "запрос_в_векторное_хранилище"

    # подзапрос
    SUB_QUESTION = "подзапрос"

    # синтез SQL-ответа
    SQL_RESPONSE_SYNTHESIS = "синтез_SQL-ответа"

    # разговор
    CONVERSATION = "разговор"

    # разбиение запроса
    DECOMPOSE = "разбиение"

    # выбор варианта
    CHOICE_SELECT = "выбор_варианта"

    # пользовательский (по умолчанию)
    CUSTOM = "пользовательский"



