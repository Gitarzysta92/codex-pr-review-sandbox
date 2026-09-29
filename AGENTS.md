# Review instructions

This repository is a synthetic reviewer test fixture.

- Review against the PR's `develop` base and report the reviewed commit SHA.
- Permitted test command: `python3 -m unittest discover -s tests -v`.
- Tests use only Python's standard library and local fixture data.
- Do not install packages or access services, hardware, or production resources.
- Do not push, merge, deploy, or publish review comments without explicit approval.
- Report reproducible defects with file/line references and evidence.
- Clearly state whether tests actually ran. An infrastructure failure is not a pass.
