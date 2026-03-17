<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="logo/light.svg"/>
        <img alt="Browserbase logo" src="logo/light.svg" width="300" />
    </picture>
</p>

<p align="center">
    <a href="https://docs.browserbase.com">Documentation</a>
    <span>&nbsp;·&nbsp;</span>
    <a href="https://www.browserbase.com/playground">Playground</a>
</p>
<br/>

# Selenium with Browserbase

Browserbase is the developer platform for reliable browser automation. Get complete control over headless browsers and leverage Browserbase's powerful features:

- 🚀 [Cloud Infrastructure](https://docs.browserbase.com/) - Scalable, reliable browser infrastructure
- 🕵️ [Stealth Mode](https://docs.browserbase.com/features/stealth-mode) - Undetectable browser automation
- 🔍 [Session Debugger](https://docs.browserbase.com/features/sessions) - Debug and replay browser sessions

Perfect for web automation, testing, and data collection.

**Get started in under one minute** with Selenium.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, we suggest using [uv](https://docs.astral.sh/uv/) to manage your dependencies.

```bash
uv sync
```

### 2. Create `.env` file:

```bash
cp .env.example .env
```

### 3. Get your Browserbase API Key:

- [Create an account](https://www.browserbase.com/sign-up) or [log in to Browserbase](https://www.browserbase.com/sign-in)
- Copy your API Key [from your Settings page](https://www.browserbase.com/settings) into the `.env` file

### 4. Run the script:

```bash
python main.py # or uv run python main.py
```

## Further reading

- [Explore the Browserbase Python SDK](https://docs.browserbase.com/reference/sdk/python)
- [Explore the Selenium Python API](https://selenium-python.readthedocs.io/api.html)
