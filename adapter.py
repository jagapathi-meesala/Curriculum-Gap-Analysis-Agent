"""CLI adapter for the Curriculum Gap Analysis Agent."""
import argparse, json, sys
from core.analysis import compare_curriculum_outcomes, assess_coverage_gaps, generate_improvement_plan

def main():
    parser = argparse.ArgumentParser(description="Analyze curriculum coverage from a JSON input file.")
    parser.add_argument("input", nargs="?", help="JSON file containing curriculum_topics and learning_outcomes")
    args = parser.parse_args()
    if not args.input:
        parser.print_help(); return 0
    try:
        with open(args.input, encoding="utf-8") as f: data = json.load(f)
        analysis = compare_curriculum_outcomes(data.get("curriculum_topics", []), data.get("learning_outcomes", []), data.get("evidence", {}))
        analysis["gap_report"] = assess_coverage_gaps(analysis)
        analysis["improvement_plan"] = generate_improvement_plan(analysis["gap_report"])
        print(json.dumps(analysis, indent=2, ensure_ascii=False))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr); return 2
    return 0
if __name__ == "__main__": raise SystemExit(main())
