import os
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model


if __name__ == "__main__":
    if not os.environ.get("MISTRAL_API_KEY"):
        os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter API key for Mistral AI: ")
    model = init_chat_model("mistral-large-latest", model_provider="mistralai")

    system_template = "Translate the following from English into {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    prompt = prompt_template.invoke({"language": "Urdu", "text": "hi!"})

    print(prompt_template)
    print(prompt_template.messages)
    print(prompt)
    print(prompt.to_messages())