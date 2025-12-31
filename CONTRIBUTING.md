# Contributing to Open Intelligence Index

Thank you for your interest in contributing to the Open Intelligence Index! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Adding a New Entry](#adding-a-new-entry)
- [Updating Existing Entries](#updating-existing-entries)
- [Schema Guidelines](#schema-guidelines)
- [Data Quality Standards](#data-quality-standards)
- [Pull Request Process](#pull-request-process)
- [Developer Setup](#developer-setup)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Assume good intentions
- Focus on what is best for the community

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/open-intelligence-index.git
   cd open-intelligence-index
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/shaharia-lab/open-intelligence-index.git
   ```
4. **Create a new branch** for your contribution:
   ```bash
   git checkout -b feature/add-company-name
   ```

## How to Contribute

### Types of Contributions

| Type | Description |
|------|-------------|
| **New Entries** | Add new startups, companies, or entities to the index |
| **Updates** | Correct or enhance existing entries |
| **Bug Fixes** | Fix data errors or validation issues |
| **Documentation** | Improve README, schemas, or guides |
| **Schema** | Propose new schemas or schema improvements |

### What We're Looking For

- Accurate, verifiable information
- Properly formatted entries following the schema
- Descriptions that are neutral and factual
- Coverage of underrepresented regions/sectors

## Adding a New Entry

### Step 1: Verify the Company Doesn't Exist

Search the repository to avoid duplicates:
```bash
grep -r "Company Name" index/
```

### Step 2: Determine the Entry Type

Currently supported:
- **Startups/Companies** → `index/startups/`

### Step 3: Create the File

1. **Navigate to the appropriate country directory**:
   ```
   index/startups/<country-code>/
   ```

2. **Create the YAML file**:
   - Filename: `company-name.yaml` (lowercase, hyphenated)
   - Must match the `id` field in the file

### Step 4: Fill in the Entry

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/shaharia-lab/open-intelligence-index/main/schemas/startup.schema.json

id: company-name
name: "Company Name"
website: "https://example.com"
logo_url: "https://example.com/logo.png"
founded_year: 2020
description: "A short, one-sentence pitch."
long_description: |
  A longer paragraph explaining what they do, their unique selling point,
  and their core technology.

industries:
  - "Industry Category"
  - "Another Category"

technologies:
  - "AI Technology"
  - "Another Technology"

headquarters:
  city: "City Name"
  country_code: "US"  # ISO 3166-1 alpha-2
  region: "California"

funding:
  total_raised_usd: 10000000
  last_round: "Series A"
  investors:
    - "Investor Name"
    - "Another Investor"

open_source:
  active: true
  github_org: "https://github.com/company"
  huggingface_org: "https://huggingface.co/company"

socials:
  linkedin: "https://linkedin.com/company/company"
  twitter: "https://twitter.com/company"
```

### Step 5: Required Fields

| Field | Type | Required |
|-------|------|----------|
| `id` | string | Yes |
| `name` | string | Yes |
| `website` | URL | Yes |
| `founded_year` | integer | Yes |
| `description` | string | Yes |
| `industries` | array | Yes |
| `technologies` | array | Yes |
| `headquarters.city` | string | Yes |
| `headquarters.country_code` | string | Yes |

### Step 6: Validation

The CI pipeline will automatically validate your entry. You can also validate locally:

```bash
# Using Python
pip install pyyaml jsonschema

python3 << 'EOF'
import yaml
import jsonschema
import json

# Load schema
with open('schemas/startup.schema.json', 'r') as f:
    schema = json.load(f)

# Load your entry
with open('index/startups/us/company.yaml', 'r') as f:
    entry = yaml.safe_load(f)

# Validate
jsonschema.validate(instance=entry, schema=schema)
print("Validation passed!")
EOF
```

## Updating Existing Entries

1. Find the file you want to update
2. Make your changes
3. Ensure the schema still validates
4. Submit a PR with a clear description of what changed

### Example Update PR Title

```
Update funding information for OpenAI (2024 Series D)
Fix website URL for Anthropic
Add technologies field to DeepMind entry
```

## Schema Guidelines

### Field Guidelines

| Field | Best Practice |
|-------|---------------|
| `id` | Use lowercase, hyphenated format; must match filename |
| `name` | Use official legal or trading name |
| `country_code` | Use ISO 3166-1 alpha-2 (e.g., DE, GB, US, JP) |
| `total_raised_usd` | Use integer, convert from other currencies |
| `description` | Keep to one sentence; neutral and factual |
| `industries` | Use standard industry categories |
| `technologies` | Use recognized technology terms |

### Common Country Codes

| Country | Code |
|---------|------|
| United States | US |
| United Kingdom | GB |
| Germany | DE |
| France | FR |
| Japan | JP |
| China | CN |
| Canada | CA |
| India | IN |
| Brazil | BR |
| Australia | AU |

### Industry Categories

Suggested industry categories (not exhaustive):
- Artificial Intelligence
- Enterprise Software
- Healthcare
- Finance
- Manufacturing
- Robotics
- Automotive
- E-commerce
- Cybersecurity
- Education

## Data Quality Standards

### Accuracy

- Verify information from official sources
- Provide accurate funding amounts (convert to USD)
- Use official company names and URLs

### Neutrality

- Write neutral, factual descriptions
- Avoid marketing language or hype
- Don't include subjective assessments

### Completeness

- Fill all required fields
- Include optional fields when available
- Add sources for significant claims

### Timeliness

- Update outdated information
- Add recent funding rounds
- Correct changed URLs or status

## Pull Request Process

### 1. Create Your Branch

Use a descriptive branch name:
```bash
git checkout -b add/openai-us
git checkout -b update/anthropic-funding
git checkout -b fix/deepmind-url
```

### 2. Commit Your Changes

Use clear commit messages:
```bash
git commit -m "Add OpenAI (United States)"
git commit -m "Update Anthropic funding to $4B"
git commit -m "Fix broken URL in DeepMind entry"
```

### 3. Push and Create PR

```bash
git push origin add/openai-us
```

Then create a Pull Request on GitHub with:
- **Title**: Clear and descriptive
- **Description**: What you changed and why
- **References**: Sources for new information (optional but helpful)

### 4. Review Process

- The CI pipeline will run validation
- Maintainers will review your PR
- Address any feedback requested
- Once approved, your PR will be merged

### PR Checklist

Before submitting, ensure:

- [ ] Entry follows the schema
- [ ] No merge conflicts with upstream
- [ ] Commit messages are clear
- [ ] PR title and description are informative
- [ ] You've tested validation (if applicable)

## Developer Setup

### Prerequisites

- Python 3.8+
- Git
- A text editor with YAML support

### Validation Script (Optional)

Create a local validation script:

```bash
# scripts/validate.py
import sys
import yaml
import json
import jsonschema
from pathlib import Path

def validate_file(yaml_file, schema_file):
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    jsonschema.validate(instance=data, schema=schema)
    print(f"✓ {yaml_file} is valid")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate.py <yaml-file>")
        sys.exit(1)
    validate_file(sys.argv[1], "schemas/startup.schema.json")
```

## Getting Help

- **Issues**: Open a GitHub issue for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions
- **Existing PRs**: Review and comment on open PRs

## Recognition

Contributors are recognized in:
- The project's contributor list
- Release notes (for significant contributions)

Thank you for contributing to the Open Intelligence Index!
