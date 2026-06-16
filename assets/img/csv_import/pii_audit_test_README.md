# PII audit CI test fixture

`pii_audit_test_upload_completed.png` is an **intentional test image** for PR #14146.

It contains production-style customer data (external IDs, customer-specific attribute names, production CSV filename) and **should fail** the **Check screenshot PII** CI job.

Remove this file and the PNG before merging the PII audit feature to `develop`.
