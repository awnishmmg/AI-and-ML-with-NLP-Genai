import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";

dotenv.config();

const ai = new GoogleGenAI({
  apiKey: process.env.API_KEY,
  project: process.env.PROJECT_ID,
  location: process.env.LOCATION,
  vertexai: true,
});

const generationConfig = {
  maxOutputTokens: 2048,
  temperature: 1,
  topP: 1,
  seed: 0,
  safetySettings: [
    { category: "HARM_CATEGORY_HATE_SPEECH", threshold: "BLOCK_LOW_AND_ABOVE" },
    {
      category: "HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold: "BLOCK_LOW_AND_ABOVE",
    },
    {
      category: "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold: "BLOCK_LOW_AND_ABOVE",
    },
    { category: "HARM_CATEGORY_HARASSMENT", threshold: "BLOCK_LOW_AND_ABOVE" },
  ],
};

export async function askGemini(req, res) {
  if (req.method !== "POST") {
    res.status(405).send("Method Not Allowed");
    return;
  }

  const prompt = req.body?.prompt;
  if (!prompt) {
    res.status(400).json({ error: "Prompt is required" });
    return;
  }

  try {
    const reqPayload = {
      model: process.env.MODEL,
      contents: [{ role: "user", parts: [{ text: prompt }] }],
      config: generationConfig,
    };

    const stream = await ai.models.generateContentStream(reqPayload);
    let responseText = "";

    for await (const chunk of stream) {
      if (chunk.text) responseText += chunk.text;
    }

    res.status(200).json({ reply: responseText });
  } catch (error) {
    console.error("Gemini Error:", error.message);
    res.status(500).json({ error: "Failed to fetch Gemini response." });
  }
}
