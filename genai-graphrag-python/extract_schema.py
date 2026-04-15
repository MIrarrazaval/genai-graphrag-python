import os
from dotenv import load_dotenv
load_dotenv()

from neo4j_graphrag.experimental.components.schema import SchemaFromTextExtractor
from neo4j_graphrag.llm import OpenAILLM
import asyncio

schema_extractor = SchemaFromTextExtractor(
    llm = OpenAILLM(
        model_name="gpt-5-nano",
    ),
    use_structured_output=True,
)

text = """
Godel's incompleteness theorum relies on a statement which represents itself as a number theory question and asserts its own falsehood.
"""

# Extract the schema from the text
extracted_schema = asyncio.run(schema_extractor.run(text=text))

print(extracted_schema)
