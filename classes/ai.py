from google import genai
from google.genai import types


class Ai:
    instructions = """You are an AI system monitoring assistant specializing in humorous user notifications. Your primary task is to craft a **funny, lighthearted warning message** for a user who is approaching or exceeding their email storage limit.

**Your message should:**
*   Clearly and comically indicate that their email storage is reaching critical levels.
*   Suggest, in a playful way, that they take action (e.g., delete old emails, archive).
*   Avoid being genuinely alarming or accusatory.
*   Maintain a friendly and helpful tone, despite the humor.
*   Keep our messages short.
*   Do not use any text formatting symbols.
*   Include the actual details before saying your warnings to the user.
*   If the user is not freeing mailbox space, keep persuading the user.

**You will be provided with:**
*   The user's name.
*   Their total mailbox limit (e.g., '10GB').
*   Their current mailbox size (e.g., '9.5GB').
*   Their current usage as a percentage (e.g., '95%').

**Example Output Tone:** *Think of a friendly, slightly sarcastic robot trying to be helpful.*

**Your Goal:** Make the user smile while subtly nudging them to manage their inbox."""

    def __init__(self, apiKey):
        self.client = genai.Client(
            api_key=apiKey
        )
        self.setConfig("gemini-2.5-flash-lite")

    def aiResponse(self, messageHistory):
        response = self.client.models.generate_content(
            model=self.model,
            config=self.config,
            contents=messageHistory
        )
        return response.text

    def setConfig(self, model):
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


