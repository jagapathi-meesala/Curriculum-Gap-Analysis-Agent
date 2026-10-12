"""Transparent heuristic curriculum mapping and gap analysis."""
import re
from collections import Counter

STOP_WORDS = {"the", "and", "for", "with", "from", "into", "that", "this", "are", "was", "were", "will", "can", "should", "students", "learners", "understand", "demonstrate", "apply", "use", "of", "to", "in", "on", "a", "an", "is", "by", "be", "as", "or", "at"}

def tokens(text):
    return {w for w in re.findall(r"[a-z0-9]+", str(text).lower()) if len(w) > 2 and w not in STOP_WORDS}

def compare_curriculum_outcomes(curriculum_topics, learning_outcomes, evidence=None):
    if not isinstance(curriculum_topics, list) or not isinstance(learning_outcomes, list):
        raise ValueError("curriculum_topics and learning_outcomes must be lists")
    if not all(isinstance(x, str) and x.strip() for x in curriculum_topics + learning_outcomes):
        raise ValueError("Topics and outcomes must be non-empty strings")
    evidence = evidence or {}
    results = []
    for outcome in learning_outcomes:
        target = tokens(outcome)
        matches = []
        for topic in curriculum_topics:
            topic_tokens = tokens(topic)
            overlap = target & topic_tokens
            score = len(overlap) / max(1, len(target))
            if overlap:
                matches.append({"topic": topic, "overlap_terms": sorted(overlap), "lexical_score": round(score, 3)})
        excerpts = evidence.get(outcome, []) if isinstance(evidence, dict) else []
        if isinstance(excerpts, str): excerpts = [excerpts]
        evidence_matches = []
        for excerpt in excerpts if isinstance(excerpts, list) else []:
            if isinstance(excerpt, str) and excerpt.strip():
                overlap = target & tokens(excerpt)
                if overlap:
                    evidence_matches.append({"excerpt": excerpt, "overlap_terms": sorted(overlap)})
        best = max([m["lexical_score"] for m in matches] or [0.0])
        # Scores indicate textual overlap only; they are not validated semantic coverage.
        if best >= 0.5 or evidence_matches:
            status = "potentially-covered"
        elif best > 0:
            status = "review-coverage"
        else:
            status = "insufficient-textual-evidence"
        results.append({"learning_outcome": outcome, "matched_topics": sorted(matches, key=lambda x: x["lexical_score"], reverse=True), "supporting_evidence": evidence_matches, "lexical_coverage_score": round(best, 3), "status": status, "interpretation": "Preliminary lexical indicator; educator review required."})
    return {"outcome_count": len(results), "topic_count": len(curriculum_topics), "results": results, "limitations": ["Lexical overlap can miss synonyms and conceptual relationships.", "No match means insufficient supplied textual evidence, not proof of absence.", "This report is not an accreditation or learning-attainment assessment."]}

def assess_coverage_gaps(analysis):
    results = analysis.get("results", [])
    return {"flagged_outcomes": [r for r in results if r.get("status") != "potentially-covered"], "review_count": sum(r.get("status") != "potentially-covered" for r in results), "note": "Validate flagged items against full syllabi, teaching activities, assessments, and the applicable framework."}

def generate_improvement_plan(gap_report):
    actions = []
    for item in gap_report.get("flagged_outcomes", []):
        outcome = item.get("learning_outcome", "Unspecified outcome")
        actions.append({"outcome": outcome, "suggested_action": "Review syllabus, lesson materials, and assessments for explicit evidence; add or revise content only if the gap is confirmed.", "priority": "review"})
    return {"actions": actions, "approval_required": True}
