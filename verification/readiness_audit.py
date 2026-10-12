from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["agent.yaml", "SOUL.md", "README.md", "RULES.md", "DUTIES.md", "AGENTS.md", "EXPLAINABILITY.md", "requirements.txt", "adapter.py", "core/analysis.py", "tools/compare-curriculum-outcomes.yaml", "tools/assess-coverage-gaps.yaml", "tools/generate-improvement-plan.yaml", "skills/curriculum-mapping/SKILL.md", "skills/learning-outcome-analysis/SKILL.md", "skills/gap-reporting/SKILL.md", "tests/test_analysis.py"]
missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
print(f"Required files: {len(REQUIRED)-len(missing)}/{len(REQUIRED)} present")
if missing:
    print("Missing:", *missing, sep="\n- "); sys.exit(1)
print("Readiness audit: PASS")
