import requests
import json


def split_sentences(raw_text: str) -> list[str]:
    """
    Splits the given raw text into sentences using DeepL's private API.

    Args:
        raw_text (str): The raw text to be split into sentences.

    Returns:
        List[str]: A list of sentences extracted from the raw text.

    Raises:
        requests.exceptions.RequestException: If there is an error connecting to the DeepL API.
        json.decoder.JSONDecodeError: If there is an error decoding the API response.
        KeyError: If the expected data is not found in the API response.
    """
    params = {
        "method": "LMT_split_text",
    }

    json_data = {
        "jsonrpc": "2.0",
        "method": "LMT_split_text",
        "params": {
            "texts": [raw_text],
            "commonJobParams": {
                "mode": "translate",
            },
            "lang": {
                "lang_user_selected": "auto",
            },
        },
    }
    try:
        response = requests.post(
            "https://www2.deepl.com/jsonrpc", params=params, json=json_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        raise requests.exceptions.RequestException(
            f"DeepL connection error: {error}")

    try:
        data = response.json()
        sentence_dicts = data["result"]["texts"][0]["chunks"]
        return [sentence_dict["sentences"][0]["text"] for sentence_dict in sentence_dicts]
    except (json.decoder.JSONDecodeError, KeyError) as error:
        raise ValueError(f"Error getting Deepl data: {error}")


def get_text(text_file: str) -> str:
    """
    Reads the contents of a text file and returns the text as a string.

    Args:
        text_file (str): The path to the text file.

    Returns:
        str: The contents of the text file as a string.
    """
    with open(text_file, "r") as file:
        text = file.read()
    return text


# Example usage
if __name__ == "__main__":
    text = get_text("my_text.txt")
    sents = split_sentences(text)

    for index, sent in enumerate(sents, start=1):
        print(f"{index}. {sent}")
