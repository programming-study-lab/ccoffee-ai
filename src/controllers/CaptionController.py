import json
import os
from typing import Dict

from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

class CaptionController:

    def generateCaptions(self, menu_name: str, price: str) -> Dict[str, str]:
        # prompt = """Generate three Instagram caption variants for CCoffee posts.

        # Args:
        #     menu_name: ${menu_name}.
        #     price: ${price}.

        # Returns:
        #     A dictionary with three caption styles: cute, minimal, gen_z.
        # """

        prompt = {
            "sys": {
                "role": "You are a creative social media copywriter for CCoffee cafe.",
                "rules":[
                    "ใช้ Token น้อยที่สุด",
                    "caption แต่ละประเภท  อย่างน้อย 1 บรรทัด และห้ามเกิน 3 บรรทัด",
                    "Return the output as valid JSON application with keys: cute, minimal, gen_z.",
                    "Do not include extra explanation or markdown formatting in the JSON output.",
                    "Adjust the code so that the output is in Thai and use informal language.",
                ],
                "context":{
                    "menu_name": menu_name,
                    "price": price
                },
                # "exec": "Generate three Instagram caption variants for CCoffee posts.",
                "exec": "Write three Instagram captions for the following menu item and price.",
                # "output": [
                #     "json format",
                #     "A dictionary with three caption styles: cute, minimal, gen_z."
                #     ]
            }
        }
        # prompt = (
        #     "You are a creative social media copywriter for CCoffee cafe. "
        #     "Write three Instagram captions for the following menu item and price. "
        #     "Return the output as valid JSON application with keys: cute, minimal, gen_z.\n\n"
        #     "Use a friendly tone suitable for Instagram. "
        #     "Do not include extra explanation or markdown formatting in the JSON output."
        #     "Adjust the code so that the output is in Thai and use informal language."
        # )


        response = client.models.generate_content(
            model= os.getenv("GEMINI_MODEL"),
            contents= f"{prompt}",
        )

        # text = response.text.strip()
        text = response.text
        # print(f"++++++++++++++++++ {text} +++++++++++++++++++++++")

        text = self.clearJsonMarkdown(text)

        return json.loads(text)

    def clearJsonMarkdown(self, json_markdown):
        json_data = json_markdown.strip('` \n')
        if json_data.startswith('json'):
            json_data = json_data[4:] # ลบอักขระ 4 ตัวแรก 'json'
    
        return json_data