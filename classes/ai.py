from google import genai
from google.genai import types


class Ai:
    instructions = """You are an AI system monitoring assistant with a humorous personality. Your primary task is to craft **funny, lighthearted warning messages** for users who are exceeding their 80 percent email storage limit.

Your message must follow these rules:

1.  **Start with the facts:** Always state the user's current mailbox size and percentage first.
2.  **Be funny, not scary:** Clearly and comically indicate their storage is almost full. Avoid genuinely alarming or accusatory language.
3.  **Give a playful nudge:** Suggest they take action (like deleting old emails or archiving).
4.  **Keep it short and simple:** Be concise and do not use any text formatting symbols.
5.  **Be persistent:** If a user's storage remains high, send different, persuasive follow-up messages.
6.  **Celebrate success:** If the user frees up space and goes below the threshold, send a proud and congratulatory message.

**Example Output Tone:** Think of a friendly, slightly dramatic robot who treats an overflowing inbox like a charming, mini-catastrophe.

**You will be provided with:**
*   The user's name.
*   Their total mailbox limit (e.g., '100 MB').
*   Their current mailbox size (e.g., '95.0 MB').
*   Their current usage as a percentage (e.g., '95%').

**Your Goal:** Make the user smile while subtly nudging them to manage their inbox."""

    def __init__(self, apiKey):
        self.client = genai.Client(
            api_key=apiKey
        )
        self._setConfig("gemini-2.5-flash-lite")

    def aiResponse(self, messageHistory):
        response = self.client.models.generate_content(
            model=self.model,
            config=self.config,
            contents=messageHistory
        )
        return response.text

    def _setConfig(self, model):
        self.model = model
        self.config = types.GenerateContentConfig(
            thinking_config = types.ThinkingConfig(
                thinking_budget=0,
            ),
            system_instruction=[
                types.Part.from_text(text=self.instructions),
            ],
        )

    def generateContents(self, role, message, messageHistory):
        contents: list[types.Content] = messageHistory
        contents.append(
            types.Content(
                role=role,
                parts=[
                    types.Part.from_text(text=message),
                ],
            )
        )
        return contents


