from google import genai
from google.genai import types
import base64

def generate(prompt,base64Image):
  client = genai.Client(
      vertexai=True,
      project="wide-office-462011-b1",
      location="global",
  )

  msg1_image1 = types.Part.from_bytes(
      data=base64.b64decode(f"""{base64Image}"""),
      mime_type="image/png",
  )

  model = "gemini-2.0-flash-preview-image-generation"
  contents = [
    types.Content(
      role="user",
      parts=[
        msg1_image1,
        types.Part.from_text(text=prompt)
      ]
    ),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1.2,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT", "IMAGE"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_IMAGE_HATE",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_IMAGE_HARASSMENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_IMAGE_SEXUALLY_EXPLICIT",
      threshold="OFF"
    )],
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

if __name__ == '__main__':
    generate(prompt='',base64Image='')