# Explainability

This document explains the inputs, decision process, outputs, and limitations of the Curriculum Gap Analysis Agent and each of its tools.

## Inputs

The agent accepts curriculum descriptions, course learning outcomes, topic lists, and available evidence supplied by the user. Inputs may be incomplete, inconsistent, or expressed using different terminology.

The agent uses only the information provided to it and the processing implemented in its tools. Missing evidence is not treated as proof that a curriculum topic is absent.

## Decision

The agent compares curriculum topics and learning outcomes using the implemented text-analysis and matching logic. It identifies possible coverage gaps, records the evidence supporting its findings, and generates recommendations for human review.

A potential gap is a review signal, not a definitive conclusion that a learning outcome is unmet. Users should be able to trace findings to the supplied curriculum evidence.

## Limits

The agent performs preliminary curriculum analysis. It does not independently verify institutional accreditation, teaching quality, student mastery, or compliance with an external educational standard.

Results depend on the completeness, clarity, and accuracy of the supplied inputs and on the matching logic implemented by the agent. Similar wording may conceal different meanings, while equivalent concepts may use different terminology.

Educators must review the evidence, validate the findings, and approve any proposed curriculum changes.

## Tool: assess-coverage-gaps

### Inputs and Data Sources
This tool receives the curriculum information and coverage evidence provided in its input. Its findings depend on the supplied material.

### Decision and Reasoning
It identifies potential gaps by applying the implemented coverage-assessment logic. Each reported gap should be interpreted in the context of the available evidence.

### Outputs and Evidence
The tool returns a coverage assessment and potential gaps according to its implemented output schema. Findings should be checked against the source curriculum.

### Limits and Constraints
It cannot establish that a topic is genuinely absent when the input is incomplete. It does not certify accreditation or educational compliance.

### Failure Handling
Missing, malformed, or insufficient input may prevent a reliable assessment. Correct the input and rerun the analysis rather than treating an incomplete result as a confirmed gap.

### Human Review
An educator must verify each significant finding before making curriculum decisions.

## Tool: compare-curriculum-outcomes

### Inputs and Data Sources
This tool receives curriculum topics and learning outcomes supplied by the user.

### Decision and Reasoning
It compares the supplied topics and outcomes using the matching logic implemented by the tool. A match indicates possible textual or conceptual alignment, not proof of mastery.

### Outputs and Evidence
The tool reports comparison results according to its implemented output schema. Review the original topics and outcomes when interpreting each match or mismatch.

### Limits and Constraints
Terminology differences, ambiguous statements, and incomplete descriptions can affect the results. The tool cannot independently confirm that an outcome is taught or assessed.

### Failure Handling
If the provided outcomes or curriculum data are missing or invalid, correct the input and rerun the comparison.

### Human Review
Educators should confirm the relevance and meaning of each suggested alignment.

## Tool: generate-improvement-plan

### Inputs and Data Sources
This tool uses the curriculum analysis and potential gaps supplied to it.

### Decision and Reasoning
It generates proposed improvement actions based on the available findings and the recommendation logic implemented by the tool.

### Outputs and Evidence
The tool produces a proposed improvement plan according to its implemented output schema. Recommendations should be connected to the identified curriculum evidence.

### Limits and Constraints
The plan is advisory. It cannot determine institutional priorities, staffing, teaching resources, accreditation requirements, or the feasibility of a change without appropriate context.

### Failure Handling
Incomplete or unsupported findings may result in an incomplete plan. Validate the underlying analysis before generating or acting on recommendations.

### Human Review
Course coordinators and educators must assess feasibility, educational value, and alignment with approved curriculum requirements before adopting a recommendation.

## Data Quality and Uncertainty

The reliability of the results depends on the quality and completeness of the source information. The agent should not invent missing curriculum content, claim that an unverified match is certain, or present a potential gap as an independently verified fact.

## Security and Responsible Use

Only provide curriculum information that is appropriate to process. Avoid including personal student information unless it is necessary and authorized. Review generated reports before sharing them.

## Audit and Reproducibility

For a reproducible review, retain the curriculum inputs, generated results, relevant tool version, and the human decisions made after reviewing the findings. Re-run the analysis when the source curriculum changes.
