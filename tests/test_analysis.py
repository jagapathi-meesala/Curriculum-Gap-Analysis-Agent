from core.analysis import compare_curriculum_outcomes, assess_coverage_gaps, generate_improvement_plan

def test_matching_topic_is_potentially_covered():
    r = compare_curriculum_outcomes(["Python programming and data analysis"], ["Apply Python programming"])
    assert r["results"][0]["status"] == "potentially-covered"

def test_no_overlap_is_flagged_not_claimed_absent():
    r = compare_curriculum_outcomes(["Art history"], ["Explain database indexing"])
    assert r["results"][0]["status"] == "insufficient-textual-evidence"
    assert "not proof of absence" in r["limitations"][1]

def test_evidence_can_support_outcome():
    outcome = "Explain database indexing"
    r = compare_curriculum_outcomes(["Art history"], [outcome], {outcome: ["Lesson covers database indexing techniques"]})
    assert r["results"][0]["status"] == "potentially-covered"

def test_partial_overlap_review():
    r = compare_curriculum_outcomes(["Python basics"], ["Explain distributed database architecture"])
    assert r["results"][0]["status"] in {"review-coverage", "insufficient-textual-evidence"}

def test_gap_report_counts():
    a = compare_curriculum_outcomes(["Art history"], ["Explain database indexing"])
    g = assess_coverage_gaps(a)
    assert g["review_count"] == 1

def test_plan_requires_human_approval():
    p = generate_improvement_plan({"flagged_outcomes": [{"learning_outcome": "Outcome X"}]})
    assert p["approval_required"] is True

def test_invalid_input_rejected():
    try:
        compare_curriculum_outcomes("not a list", ["Outcome"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
