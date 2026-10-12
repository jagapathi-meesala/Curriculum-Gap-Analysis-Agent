# Curriculum Gap Analysis Agent

A local, document-text-oriented prototype for mapping curriculum content to learning outcomes and producing a transparent gap report.

## Capabilities
- Normalize and compare curriculum topics against learning outcomes.
- Estimate coverage using explicit keyword/topic overlap and supplied evidence.
- Flag outcomes with weak or missing evidence.
- Suggest review actions while leaving final decisions to educators.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 adapter.py --help
python3 -m pytest -q
python3 verification/readiness_audit.py
opengap validate
```

## Input format
Pass JSON with `curriculum_topics` (list of strings) and `learning_outcomes` (list of strings). Optional `evidence` can map an outcome string to a list of supporting curriculum excerpts.

## Limitations
This prototype uses simple token overlap, not a trained semantic model. It does not read PDFs or Word documents directly, verify institutional standards, or certify accreditation. Provide extracted text and review recommendations with a subject-matter expert.
