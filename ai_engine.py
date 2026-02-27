from openai import OpenAI
import os
from dotenv import load_dotenv
print("API KEY:", os.getenv("OPENAI_API_KEY"))

load_dotenv()

client = OpenAI(api_key="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")

def generate_gcd_explanation(a, b, g, x, y, steps):
    prompt = f"""
You are a number theory professor.

Explain step-by-step how the Euclidean Algorithm was applied to compute gcd({a}, {b}).

Euclidean Steps:
{steps}

The gcd obtained is {g}.
The linear combination found is:
{a}({x}) + {b}({y}) = {g}.

Explain:
1. Why the Euclidean Algorithm works.
2. How Bézout’s Identity is demonstrated.
3. Why a solution exists to ax + by = gcd(a,b).
4. Keep explanation academic but clear.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in number theory."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content