# Open Intelligence Index

<div align="center">

**A comprehensive, open-source index of AI products, services, startups, businesses, and more.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge-GitHub-Open%20Source-blue.svg)](https://github.com/shaharia-lab/open-intelligence-index)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#-features) &bull; [Directory Structure](#-directory-structure) &bull; [Contributing](#-contributing) &bull; [License](#-license)

</div>

---

## About

The **Open Intelligence Index** is a crowdsourced, centralized repository documenting the global AI landscape. Our mission is to create the most comprehensive, accessible, and well-structured index of AI companies, products, services, and startups worldwide.

Unlike proprietary databases, this index is:
- **Free** - Completely open source under the MIT License
- **Collaborative** - Anyone can contribute and improve the data
- **Structured** - All entries follow defined schemas for consistency
- **Accessible** - Human-readable YAML format, machine-parsable JSON Schema

## Features

- Structured data with JSON Schema validation
- GitHub Actions CI for automatic validation
- IDE auto-completion via YAML Language Server
- Geographic and categorical organization
- Open source and developer-friendly

## Directory Structure

```
open-intelligence-index/
├── schemas/                  # JSON Schema definitions
│   └── startup.schema.json   # Schema for startup entries
├── index/                    # Main data directory
│   └── startups/             # Startup/company index
│       └── germany/          # Country-based organization
│           └── aleph-alpha.yaml
├── .github/
│   └── workflows/
│       └── validate-schema.yml  # CI validation pipeline
├── schema.yaml               # Human-readable schema reference
├── CONTRIBUTING.md           # Contribution guidelines
├── DISCLAIMER.md             # Data usage disclaimer
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## Quick Start

### For Contributors

1. **Fork and clone** the repository
2. **Create a new branch** for your addition
3. **Add your entry** following the schema (see [Adding a New Entry](#adding-a-new-entry))
4. **Submit a Pull Request**

### For Users

You can use this index in your projects by:
- Parsing the YAML files directly
- Converting to JSON for API usage
- Building custom queries and filters

## Adding a New Entry

### Adding a Startup Entry

1. **Navigate to the appropriate directory** based on the company's location:
   ```bash
   cd index/startups/<country-code>/
   ```

2. **Create a new YAML file** named after the company (use lowercase, hyphenated):
   ```bash
   # Example: For "DeepMind" in the UK
   touch index/startups/gb/deepmind.yaml
   ```

3. **Add the schema reference** at the top (enables IDE validation):
   ```yaml
   # yaml-language-server: $schema=https://raw.githubusercontent.com/shaharia-lab/open-intelligence-index/main/schemas/startup.schema.json
   ```

4. **Fill in the required fields**:
   ```yaml
   id: deepmind
   name: "DeepMind"
   website: "https://deepmind.com"
   founded_year: 2010
   description: "A leading AI research company focused on solving intelligence."
   industries:
     - "Artificial Intelligence"
     - "Research"
   technologies:
     - "Deep Learning"
     - "Reinforcement Learning"
   headquarters:
     city: "London"
     country_code: "GB"
   ```

5. **Optional fields** include `logo_url`, `long_description`, `funding`, `open_source`, and `socials`.

6. **Validate locally** (optional):
   ```bash
   # Install Python dependencies
   pip install pyyaml jsonschema

   # Validate your file
   python scripts/validate.py index/startups/gb/deepmind.yaml
   ```

7. **Commit and create a PR**:
   ```bash
   git add index/startups/gb/deepmind.yaml
   git commit -m "Add DeepMind (UK)"
   git push origin add-deepmind
   ```

### Schema Validation

All entries are automatically validated against the schema when you submit a PR. The CI pipeline will:
- Convert YAML to JSON
- Validate against `schemas/startup.schema.json`
- Report any validation errors

## Schemas

Each index type has its own schema definition in the `schemas/` directory:

| Schema | Description | Status |
|--------|-------------|--------|
| `startup.schema.json` | Startup/Company entries | Active |
| `product.schema.json` | AI Product entries | Planned |
| `service.schema.json` | AI Service entries | Planned |

## Contributing

We welcome contributions from everyone! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Types of Contributions

- Add new startup/company entries
- Update existing entries with new information
- Fix errors or outdated data
- Improve documentation
- Propose new schemas for additional index types
- Report bugs or suggest improvements

### Code of Conduct

Be respectful, constructive, and inclusive. We aim to maintain a welcoming community for all contributors.

## Disclaimer

**IMPORTANT**: This is a crowd-sourced database. All data is provided "AS IS" without warranty of any kind.

**Please read our full [DISCLAIMER.md](DISCLAIMER.md) before using this data.** Key points:

- Data is submitted by community volunteers and not independently verified
- You must independently verify all information before use
- Not responsible for inaccuracies, errors, or outdated information
- Inclusion does not constitute endorsement or recommendation

## Data Sources

Data is crowdsourced from:
- Community contributions
- Publicly available information
- Company websites and press releases
- Public databases and news sources

## Roadmap

- [ ] Add product index schema
- [ ] Add service index schema
- [ ] Add investor/VC index schema
- [ ] Add search API/web interface
- [ ] Add data freshness indicators
- [ ] Add automated data enrichment

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- All contributors who help build and maintain this index
- The open-source community for tools and inspiration
- Companies making the AI landscape more transparent

---

<div align="center">

**Got questions?** Open an issue or start a discussion.

**Ready to contribute?** Check out [CONTRIBUTING.md](CONTRIBUTING.md)

Made with by the Open Intelligence Index community

</div>
