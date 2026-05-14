import json
import os
from typing import Dict

from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# if not client:
#     raise RuntimeError("GOOGLE_API_KEY not found in environment. Set it in .env.")

# genai.configure(api_key=API_KEY)

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

    # response = genai.model.generate_text(
    #     model="gemini-2.5-flash",
    #     prompt=prompt,
    #     temperature=0.7,
    #     max_output_tokens=200,
    # )

    print(f"++++++++++++++++++++++++++++++++++++{os.getenv("GEMINI_MODEL")}")

    response = client.models.generate_content(
        # model="gemini-2.5-flash",
        model= os.getenv("GEMINI_MODEL"),
        contents= prompt,
        # max_output_tokens= os.getenv("GEMINI_MAX_OUTPUT_TOKENS") 
    )

    text = response.text.strip()

    # print(f"----------------------{text.strip()}")
    # print(f"----------------------{json.loads(text)}")
    return json.loads(text)
    # return text

    try:
        captions = json.loads(text)
    except json.JSONDecodeError:
        cleaned = text.strip("` \n")
        captions = json.loads(cleaned)

    return {
        "cute": captions.get("cute", "").strip(),
        "minimal": captions.get("minimal", "").strip(),
        "gen_z": captions.get("gen_z", "").strip(),
    }


if __name__ == "__main__":
    # import argparse

    # parser = argparse.ArgumentParser(
    #     description="Generate CCoffee Instagram captions using Gemini 2.5 Flash."
    # )
    # parser.add_argument("menu_name", help="Menu item name")
    # parser.add_argument("price", help="Menu item price")
    # args = parser.parse_args()

    # captions = generate_captions(args.menu_name, args.price)
    # print(json.dumps(captions, ensure_ascii=False, indent=2))

    captions = generate_captions("ลาเต้เย็น", "50 บาท")

    # captions = {
    #     "cute": "ลาเต้เย็น 50 บาท อร่อยสุดๆ หวานน้อย ดื่มแล้วสดชื่นมากๆ ค่ะ ☕️💖",
    #     "minimal": "ลาเต้เย็น 50 บาท",
    #     "gen_z": "ลาเต้เย็น 50 บาท ดื่มแล้วตื่นเต้นมาก ค่ะ ☕️💥"
    # }

    print(f"cute: {captions['cute']}")
    print(f"minimal: {captions['minimal']}")
    print(f"gen_z: {captions['gen_z']}")
