# Explainability

## Inputs
The agent accepts curriculum topic strings, learning outcome strings, and optional evidence excerpts mapped to outcomes. Results are limited to those inputs.

## Decision
For each outcome, the agent tokenizes meaningful words and checks overlap with curriculum topic text and supplied evidence. It reports matched topics, supporting excerpts, a heuristic coverage score, and a status. This is a lexical heuristic and may miss synonyms or infer false matches.

## Limits
The agent cannot establish teaching quality, learner achievement, legal compliance, or accreditation. A low score means insufficient textual evidence in the supplied input, not proof that the topic is not taught. Educators should review the mappings and add domain-specific standards before decisions.

## Tool: compare-curriculum-outcomes
Inputs: curriculum topics and learning outcomes. Decision: calculates lexical overlap and proposes topic mappings. Limits: cannot establish conceptual equivalence.

## Tool: assess-coverage-gaps
Inputs: outcomes and optional supporting evidence. Decision: flags outcomes with low lexical coverage or no evidence. Limits: missing input evidence may create false gaps.

## Tool: generate-improvement-plan
Inputs: analysis results. Decision: converts flagged outcomes into review actions. Limits: recommendations are suggestions and require educator approval.
