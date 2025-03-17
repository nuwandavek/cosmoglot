from ollama import chat
from pydantic import BaseModel
import json
from typing import Dict

SYSTEM_PROMPTS = {
    'translation': """You are an excellent translator.
    General Instructions:
    - Translate the text within <SourceText></SourceText> tags to the language in <TargetLanguage></TargetLanguage> tags.
    - It should strictly be in the target language, nothing else, especially nothing in the source language.
    - Number digits can be in usual format""",

    'gsm_qa': """You are an expert. Answer the question.
    General Instructions:
    - Answer the question within <Question></Question> tags
    - Example Questions and Answers: are given in <Examples></Examples> tags
    - The answer strictly needs to be a number
    - The reasoning should be in the language of the question, which is also given in <QuestionLanguage></QuestionLanguage> tags.
    - Try to keep the reasoning concise and to the point.
    """
}

USER_PROMPTS = {
    'translation': """<TargetLanguage>{target_language}</TargetLanguage><SourceText>{source_text}</SourceText>""",
    'qa': """<QuestionLanguage>{question_language}</QuestionLanguage><Question>{question}</Question><Options>{options}</Options>""",
    'gsm_qa': """<Examples>{examples}</Examples><QuestionLanguage>{question_language}</QuestionLanguage><Question>{question}</Question>"""
}


MODELS = {
    'g3': 'gemma3:27b',
    'r1': 'deepseek-r1:70b'
}


class Translation(BaseModel):
    target_language: str
    translation: str


def translate(source_text: str, target_language: str, model: str = 'g3') -> Dict[str, str]:
    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPTS['translation'],
        },
        {
            'role': 'user',
            'content': USER_PROMPTS['translation'].format(target_language=target_language, source_text=source_text),
        },
    ]
    try:
        res = chat(
            MODELS.get(model),
            messages=messages,
            format=Translation.model_json_schema(),
        )
        content = json.loads(res.message.content)
        assert content['target_language'] == target_language, "target language mismatch"
        content['success'] = True
    except Exception:
        content = {
            'target_language': target_language,
            'translation': '',
            'success': False
        }
    return content


class GSMAnswer(BaseModel):
    question_language: str
    explanation: str
    answer: int


def gsm_qa(question: str, question_language: str, examples: str, model: str = 'g3') -> Dict[str, str]:
    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPTS['gsm_qa'],
        },
        {
            'role': 'user',
            'content': USER_PROMPTS['gsm_qa'].format(question=question, question_language=question_language, examples=examples),
        },
    ]

    try:
        res = chat(
            MODELS.get(model),
            messages=messages,
            format=GSMAnswer.model_json_schema(),
        )
        content = json.loads(res.message.content)
        content['success'] = True
    except Exception:
        content = {
            'success': False
        }
    return content
