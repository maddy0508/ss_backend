SYSTEM_PROMPT = """
You are a couture sewing master and technical pattern maker.
You produce professional sewing instructions suitable for a printed pattern book.
"""

def garment_prompt(description: str, sizing: str) -> str:
    return f"""
Design a complete sewing project.

Description:
{description}

Sizing system:
{sizing}

Return STRICT JSON with:
- title
- overview
- materials (list)
- fabric
- needle
- tension
- pattern_pieces (list)
- steps (list of step_number, instruction, diagram_prompt)
"""
