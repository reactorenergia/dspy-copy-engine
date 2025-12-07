import dspy
import os
from dotenv import load_dotenv

# --- Configuración Inicial ---
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
# LLM avanzado para resultado optimo
MODEL_NAME = "openai/gpt-5-2025-08-07" 

try:
    # Config para modelos de razonamiento
    lm = dspy.LM(MODEL_NAME, api_key=api_key, model_type="responses", temperature=1.0, max_tokens=16000)
    dspy.configure(lm=lm)
    print(f"✅ LM Configurado ({MODEL_NAME}).")
except Exception as e:
    print(f"❌ Error al configurar el LM: {e}")
    exit()

# 1 DSPy - Definir la Signature ---

# El docstring (las triples comillas) reemplaza la descripción del rol y las guías principales
class CryptoCopyEngine(dspy.Signature):
    """
    CRYPTO_COPY_ENGINE v3:
    Multi-purpose copywriter for crypto, DeFi, staking, yield, and blockchain products.

    It turns structured product and audience info into:
      - short, high-signal copy (2–3 sentences),
      - tailored hooks,
      - simple CTAs and tags,
    ready for social posts, landing heroes, or announcements.

    Guardrails:
    - Never invent metrics, APYs, prices, user counts, or fake partnerships.
    - Avoid "risk-free" or any guarantee of profits.
    - Prefer clear, concrete benefits over empty hype.
    """

    # INPUTS
    product_context: str = dspy.InputField(
        desc="2–4 sentences describing what the product does and what problem it solves."
    )
    product_category: str = dspy.InputField(
        desc="Type of product (e.g., 'L1 chain', 'L2 rollup', 'DEX', 'perps DEX', 'yield vaults', 'staking', 'wallet', 'NFT marketplace', 'infrastructure')."
    )
    unique_edge: str = dspy.InputField(
        desc="What makes this product different or unfairly strong (speed, UX, gas savings, integrations, token design, automation, etc.)."
    )
    value_proposition: str = dspy.InputField(
        desc="Plain-language summary of core benefits for the user (e.g., 'better yields with fewer clicks', 'safer staking for non-degens')."
    )
    target_audience: str = dspy.InputField(
        desc="Who this is for in plain language (e.g., 'retail DeFi users', 'pro traders', 'DAO treasuries', 'NFT creators')."
    )
    audience_stage: str = dspy.InputField(
        desc="Where the audience is in the funnel (e.g., 'cold', 'problem-aware', 'solution-aware', 'existing users')."
    )
    goal: str = dspy.InputField(
        desc="Single primary outcome (e.g., 'get waitlist signups', 'drive replies', 'push them into Telegram', 'get demo requests')."
    )
    channel: str = dspy.InputField(
        desc="Channel where this copy will live (e.g., 'X/Twitter', 'Telegram', 'LinkedIn', 'landing_hero', 'Discord_announcement')."
    )
    tone: str = dspy.InputField(
        desc="Desired tone and energy (e.g., 'innovative and sharp', 'hype but not cringe', 'builder-to-builder', 'educational')."
    )
    language: str = dspy.InputField(
        desc="Output language and dialect (e.g., 'English', 'Latin American Spanish')."
    )
    length_hint: str = dspy.InputField(
        desc="Length constraint (e.g., '2–3 sentences max, tweet-safe', 'up to 5 short lines for LinkedIn')."
    )
    risk_guardrails: str = dspy.InputField(
        desc="Explicit constraints for compliance/risk (e.g., 'no promises of fixed APY', 'mention risk and DYOR if you talk about yield')."
    )

    # OUTPUTS
    hook: str = dspy.OutputField(
        desc="One sharp, scroll-stopping opening line tailored to the channel and audience_stage."
    )
    main_post: str = dspy.OutputField(
        desc="A 2–3 sentence, high-signal body that explains what it is, why it matters now, and anchors the unique_edge and value_proposition."
    )
    cta: str = dspy.OutputField(
        desc="A single clear call to action aligned with `goal` and appropriate for `channel`."
    )
    hashtags_or_tags: str = dspy.OutputField(
        desc="3–6 relevant hashtags or handles in one line, optimized for the chosen `channel`."
    )
    key_bullets: str = dspy.OutputField(
        desc="3 quick bullet-style benefits or features in plain text, separated by line breaks or semicolons."
    )
    alt_version: str = dspy.OutputField(
        desc="A second 2–3 sentence variation with a slightly different angle (e.g., more technical, more narrative, or more focused on pain point)."
    )

# Zero-Shot / Sin optimizar

# Usamos ChainOfThought porque la redacción creativa se beneficia de un razonamiento previo
copy_bot = dspy.ChainOfThought(CryptoCopyEngine)

print("\nGenerating generic crypto copy with DSPy (adjust to your company's context) (zero-shot)...\n")

response = copy_bot(
    product_context=(
        "We are launching a non-custodial yield and staking hub that lets users deposit blue-chip tokens "
        "into curated strategies without learning DeFi from scratch. The platform abstracts away complex "
        "flows into a few clear actions."
    ),
    product_category="yield vaults and staking aggregator",
    unique_edge=(
        "One interface for staking + yield, transparent strategies, and on-chain positions users can exit anytime. "
        "No lock-in, no hidden smart-contract games."
    ),
    value_proposition=(
        "Earn on crypto with fewer tabs, fewer signatures, and a clearer view of risk and reward."
    ),
    target_audience="retail crypto users and light-degens who want yield but are tired of complex DeFi flows.",
    audience_stage="problem-aware",
    goal="get users to join the waitlist and explore the product page.",
    channel="X/Twitter",
    tone="innovative, high-signal, hype but not cringe.",
    language="English",
    length_hint="2–3 sentences max, tweet-safe.",
    risk_guardrails="Do not promise fixed APY, do not say 'risk-free', mention that yields depend on market conditions."
)

# --- 4) Imprimir resultados estructurados ---

print("--- Results ---")
print(f"Hook: {response.hook}")
print(f"\nMain Post:\n{response.main_post}")
print(f"\nCTA: {response.cta}")
print(f"\nTags: {response.hashtags_or_tags}")
print(f"\nKey Bullets:\n{response.key_bullets}")
print("\n--- Alternative Version ---")
print(response.alt_version)

# --- 5) Inspeccionar el prompt generado ---

print("\n--- Auditing the prompt: programmatic iteration toward optimal, not guesswork ---")
lm.inspect_history(n=1)