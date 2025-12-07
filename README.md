## From System Prompts to DSPy Programs

This repo is an important step in moving from **handcrafted system prompts** to **programmable, optimizable prompt pipelines** with DSPy.

### What changes with DSPy?

The key mindset shift in DSPy is this:

> You don’t hand the model a huge “system prompt” as a raw string.  
> Instead, you translate the structure and intent of that prompt into a `dspy.Signature` in Python.  
> DSPy then **builds the actual prompt for you**.

So instead of:

- One giant system prompt written by hand  
- Tweaking words and tone in the UI  

you now have:

- A **Python class** that defines
  - Inputs (what context you give the model)
  - Outputs (what you expect back)
  - High-level behavior (inside the docstring)
- DSPy compiles this into a **structured prompt** automatically.

---

### `copywriter.py`: crypto cpy engine

This demo implements a first version of **CRYPTO COPY_ENGINE**
A specialized copywriter for crypto, DeFi, and blockchain products.

In `copywriter.py` example you can see how a classic “system prompt” becomes a structured class:

- The **docstring** describes the role and global rules.
- Each **InputField** describes one piece of context:
  - `product_context`, `unique_edge`, `target_audience`, etc.
- Each **OutputField** describes what we want back:
  - `hook`, `main_post`, `cta`, `hashtags_or_tags`, `alt_version`.


### Installation and config:

- apt update
- apt install software-properties-common -y
it runs on python 3.11
- apt install python3.11 python3.11-venv python3.11-dev -y
### Py version & vnenv
- python3.11 --version
- python3.11 -m venv .venv
- source .venv/bin/activate
- python --version
- python -m pip install --upgrade pip setuptools wheel
- pip install dspy-ai

how to run:

```bash
chmod +x copywriter.py
python copywriter.py