# `extracts/` — local mirror of `G:\Shared drives\_SMJ\___Product Development\ExecSumm-Emails\extracts\`

Sidecar JSON extractions produced by the source readers. One file per
(client, source, refresh-date):

```
<Client>_<source>_<YYYY-MM-DD>.extract.json
```

Source values: `pbc`, `insights`, `tax_analysis`, `tax_memo`,
`tax_meeting_prep`, `transcript`, `email_thread`, `claude_chat`, `notion`.

The assembler consumes these extractions (not the raw files) so the dossier
can cite specific cells/rows/timestamps via the source-tag format defined in
`execsumm_emails/provenance.py`.
