"""
Runs a conversation turn. Gemma only reads the message; Python decides what to
save and writes the reply.

Gemma is called before the transaction (it takes seconds). If it fails, nothing
is saved and the user can send the same text again.
"""

# --- Example -------------------------------------------------------------------
# def copy_example(original: ModelExample, text: str) -> ModelExample:
#     parent, created = OtherModel.objects.get_or_create(name="copies")  # find it or create it
#     same_day = list(ModelExample.objects.filter(parent=parent, day=original.day))
#     if len(same_day) > 1:
#         raise ValueError("There is already a copy for that day.")    # the view picks the status code
#     with transaction.atomic():                                         # all or nothing
#         new = ModelExample.objects.create(name=f"{original.name} copy", notes=text, parent=parent)
#         original.amount += 1
#         original.save()
#     return new
# -------------------------------------------------------------------------------

TITLE_LENGTH = 120

REPLY_LOGGED = "Anotado."
REPLY_NOTHING_FOUND = "No encontré datos para registrar en ese mensaje."
REPLY_QUERY = "Todavía no respondo consultas sobre tus datos; puedes verlos en Resumen."
REPLY_OTHER = "Aquí registro hábitos, síntomas, estados, factores del entorno y mediciones; no doy consejos médicos."
REPLY_ADVICE = "No puedo darte un diagnóstico ni recomendaciones: para eso consulta con un médico."
