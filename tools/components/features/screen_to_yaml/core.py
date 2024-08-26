from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
from typing import Iterator
import itertools

from tools.components.features.screen_to_yaml.constants import BASE_PROMPT, CONTEXT_PROMPT

load_dotenv(find_dotenv())

class TeeIterator:
    def __init__(self, iterator: Iterator):
        self.iterator, self.tee = itertools.tee(iterator)

    def __iter__(self):
        return self.iterator

    def get_tee(self):
        return self.tee


def generate_summary(yaml_text: str) -> str:
    prompt = PromptTemplate(
        template=CONTEXT_PROMPT,
        input_variables=["yaml"],
    )
    
    chain = (
        prompt
        | ChatOpenAI(model="gpt-4o-mini", temperature=0)
        | StrOutputParser()
    )
    return chain.stream({"yaml": yaml_text})


def generate_yaml(text: str) -> Iterator[str]:
    prompt = PromptTemplate(
        template=BASE_PROMPT,
        input_variables=["text"],
    )
    
    chain = (
        prompt
        | ChatOpenAI(model="gpt-4o-mini", temperature=0)
        | StrOutputParser()
    ).with_config({"run_name": "Screen to YAML"})
    
    return chain.stream({"text": text})