# Ambulatory Blood Pressure Nocturnal Dipping & Surge Sentinel Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Ambulatory blood pressure dipping ratio (nocturnal dip %), non-dipper / reverse-dipper cardiovascular risk, and morning surge index. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_nocturnal_dipping_ratio`: Calculate nocturnal systolic dipping percentage and classify dipper pattern (Normal, Non-dipper, Extreme dipper, Reverse dipper).
- `generate_chrono_hypertensive_lifestyle_advisory`: Synthesize chronotherapy and lifestyle timing adjustments based on nocturnal dipping status.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_ambulatory_blood_pressure_dipper_sentinel_skill.server --test
```
