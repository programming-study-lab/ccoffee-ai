import json
import os
from typing import Dict

from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

def generate_captions(menu_name: str, price: str) -> Dict[str, str]:
    """Generate three Instagram caption variants for CCoffee posts.

    Args:
        menu_name: The menu item name.
        price: The menu item price.

    Returns:
        A dictionary with three caption styles: cute, minimal, gen_z.
    """
    prompt = (
        "You are a creative social media copywriter for CCoffee cafe. "
        "Write three Instagram captions for the following menu item and price. "
        "Return the output as valid JSON application with keys: cute, minimal, gen_z.\n\n"
        "Use a friendly tone suitable for Instagram. "
        "Do not include extra explanation or markdown formatting in the JSON output."
        "Adjust the code so that the output is in Thai and use informal language."
    )

    response = client.models.generate_content(
        model= os.getenv("GEMINI_MODEL"),
        contents= prompt,
    )

    text = response.text.strip()

    return json.loads(text)


if __name__ == "__main__":
    captions = generate_captions("ลาเต้เย็น", "50 บาท")

    print(f"cute: {captions['cute']}")
    print(f"minimal: {captions['minimal']}")
    print(f"gen_z: {captions['gen_z']}")
