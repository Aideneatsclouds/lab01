# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 1
- Student name: Yaaswiny Abbiramavally Thinaharan
- Matric no: A24CS0213
- Group ID: n/a
- AI level: Level 1
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [X] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-10-25
- Tool: Google (2026). Gemini. Retrieved October 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: Help me resolve pip command-not-found issues in PowerShell using uv and set up the project environment dependencies.
- Output: Suggested calling uv directly and installing packages from requirements.txt into the virtual environment.
- Verified by: checked terminal outputs and ran package freeze
- My change: Adopted the uv workflow to bypass PATH issues and generated requirements-frozen.txt.
- Used in: requirements-frozen.txt and README.md

## Entry 2

- Date: 2026-10-25
- Tool: Google (2026). Gemini. Retrieved October 2026 from https://gemini.google.com
- Purpose: generate-code
- Prompt: How do I implement check_environment() and package_version() using platform and importlib.metadata without crashing on missing packages?
- Output: Provided code using try-except blocks for PackageNotFoundError to map installed package versions safely.
- Verified by: ran python src/env_check.py and generated results/environment_report.txt
- My change: Implemented the exception-safe version checks and output formatting.
- Used in: src/env_check.py and results/environment_report.txt

## Entry 3

- Date: 2026-10-25
- Tool: Google (2026). Gemini. Retrieved October 2026 from https://gemini.google.com
- Purpose: generate-code
- Prompt: How do I write gc_percent, format_report, and parse_counts in basics.py with proper validation, error handling, and string parsing?
- Output: Provided functions handling zero totals, negative base count exceptions, string replacement for spaces/commas, and f-string formatting.
- Verified by: ran python -m pytest to confirm all visible tests passed
- My change: Integrated and verified the calculation logic for sequence statistics.
- Used in: src/basics.py

## Entry 4

- Date: 2026-10-25
- Tool: Google (2026). Gemini. Retrieved October 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: How do I write custom tests covering boundary cases, zero totals, and invalid inputs in tests/test_lab01_own.py?
- Output: Provided a pytest structure with tests for 100% GC boundaries, zero totals, and invalid token parsing.
- Verified by: ran python -m pytest and ruff check src
- My change: Created the custom test file and adjusted the boundary expected value to match 100% GC content.
- Used in: tests/test_lab01_own.py

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
