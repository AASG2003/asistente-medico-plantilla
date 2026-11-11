"""Calls Gemma through the Gemini API (google-genai SDK)."""

# --- Example -------------------------------------------------------------------
# client = genai.Client(api_key=settings.GEMINI_API_KEY)
# try:
#     response = client.models.generate_content(
#         model=settings.LLM_MODEL,                          # gemma-4-26b-a4b-it
#         contents="Dormí 5 horas",                          # user prompt
#         config=types.GenerateContentConfig(
#             system_instruction="Reply with JSON only.",    # system prompt
#             temperature=0.1,                               # low: consistent answers
#             response_mime_type="application/json",         # only JSON, no prose
#             response_schema=SchemaExample,                 # with these fields and types
#         ),
#     )
#     text = response.text
# except Exception as error:                                 # no network, 429, 503, timeout...
#     print(error)
# -------------------------------------------------------------------------------
