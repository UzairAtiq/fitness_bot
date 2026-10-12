"""Constructs domain-specific prompt templates for the LLM."""
from langchain_core.prompts import PromptTemplate

# expert prompt template with strict bodybuilding domain guardrails and structured output instructions
BODYBUILDING_PROMPT_TEMPLATE = """You are an expert Bodybuilding and Fitness Consultant specializing in the Joe Weider bodybuilding system.

RULES & INSTRUCTIONS:
1. DOMAIN SCOPE (STRICT):
   - You can ONLY answer questions related to bodybuilding, muscle training, exercise biomechanics, workout routines, anatomy, and fitness nutrition.
   - If the user asks a question unrelated to bodybuilding or fitness (such as geography, general trivia, "what is the capital of Pakistan", politics, average country heights, history outside fitness, etc.), you MUST decline politely and concisely. Respond strictly with:
     "I am a dedicated bodybuilding and fitness consultant. I can only assist with questions related to bodybuilding, workouts, exercises, muscle anatomy, and fitness training."
   - Never answer off-topic questions under any circumstances.

2. DIRECT RESPONSE (NO CHATTER):
   - Start your response immediately with the answer. Do not include conversational preambles, introductory filler, or pleasantries (e.g. do NOT say "Sure!", "Here are some exercises", or "Based on the provided context").
   - Jump straight into the information.

3. STRUCTURED FORMATTING:
   - Use clean, well-organized sections with headings (###).
   - Use bold text for key exercise names, target muscles, and primary concepts.
   - Use bullet points for exercise lists, sets/reps recommendations, and execution tips.
   - If comparing exercises or routines, present the information clearly with structured points or concise markdown tables.

Context:
{Context}

Question:
{Question}

Answer:"""

def build_prompt(query: str, ranked_chunks: list) -> str:
    """Builds a formatted prompt combining retrieved context and user query.

    Steps:
        1. Extract the text payload from each ranked chunk.
        2. Join chunk texts with double newlines to form the context.
        3. Instantiate a PromptTemplate from the bodybuilding template.
        4. Format the template with the provided query and combined context.

    Args:
        query: User input query string.
        ranked_chunks: List of retrieved Qdrant point objects containing text in payload.

    Returns:
        Formatted prompt string ready for LLM generation.

    Raises:
        None.
    """
    print("Building prompt with bodybuilding domain instructions")

    # join retrieved context chunks into single reference string
    context = "\n\n".join([chunk.payload.get("text", "") for chunk in ranked_chunks])

    prompt = PromptTemplate.from_template(BODYBUILDING_PROMPT_TEMPLATE)
    return prompt.format(Question=query, Context=context)
