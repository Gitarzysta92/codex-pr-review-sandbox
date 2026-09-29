# PR review sandbox

A public, synthetic fixture for testing automated pull-request reviews.
No production code, credentials, hardware, external services, or dependencies.
Test PRs may deliberately introduce regressions. Do not use this code in production.

The baseline branch is `develop`.

Run the permitted tests with:

```sh
python3 -m unittest discover -s tests -v
```

Reviewer output should identify the reviewed commit, explain actionable findings,
and distinguish executed test results from code inspection. Keep findings as
unpublished drafts until a human approves publication.
