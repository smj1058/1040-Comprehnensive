"""Email threads — Outlook (client inboxes + Accruity shared inboxes) +
Notion Email Log + 📧 Email Intelligence subpages.

Source tags:
  `[Email <date> <sender>→<recipient> "<subject>"]` for Outlook-sourced
  `[EI:<thread>]` for already-synthesized Email Intelligence entries
  `[SharedInbox:<inbox> <date> <subject>]` for threads pulled from an
      Accruity shared/team mailbox (ops, team, ask, tax)
"""

from __future__ import annotations

from typing import Any

# Accruity shared inboxes where client-generated action items and internal
# triage threads land. These are searched in addition to the client's
# primary/secondary contact emails so threads that never directly cc the
# client (e.g. an `ask@accruitytax.com` question about SNB PTET that gets
# triaged internally before a reply goes out to the client) are still
# captured for the dossier.
SHARED_INBOXES = (
    "operations@accruitytax.com",
    "team@accruitytax.com",
    "ask@accruitytax.com",
    "tax@accruity.com",
)

# Individual-advisor mailboxes routinely forwarded from or cc'd on
# client-related threads. Used as fallback scans when a client thread may
# only appear in a personal inbox (not the team ones).
ADVISOR_INBOXES = (
    "seth@accruity.com",
    "sophia@accruity.com",
    "deontae.lafayette@accruity.com",
    "stacy@accruity.com",
    "bryan@accruity.com",
)


def _is_noise(subject: str, sender: str, body: str) -> bool:
    """Heuristic: filter marketing blasts, webinar invites, digests, etc."""
    s = (subject or "").lower()
    sender_l = (sender or "").lower()
    noise_domains = (
        "joiin.co", "mailchimp", "constantcontact", "hubspot",
        "eventbrite", "zoom.us/webinar", "linkedin.com", "calendly",
    )
    noise_subjects = (
        "webinar", "newsletter", "unsubscribe", "digest",
        "no-reply", "noreply",
    )
    return any(d in sender_l for d in noise_domains) or any(k in s for k in noise_subjects)


def read(account) -> dict[str, Any]:  # pragma: no cover - MCP
    """Pull every substantive email thread tied to this account.

    Steps:
      1. Fetch Notion Client Email Log rows via Account.Email Log relation.
      2. Fetch the existing `📧 Email Intelligence` subpage under the account's
         thin Exec Summary child page (carry forward its synthesized threads).
      3. Live-search Outlook (`outlook_email_search`) for threads involving the
         client's primary/secondary contact emails over the last 18 months.
      4. **Scan the Accruity shared inboxes** in `SHARED_INBOXES` for threads
         mentioning the client's name or any of the client's contact emails.
         For each inbox, issue two parallel searches:
           a) `mailboxOwnerEmail=<shared_inbox>` + `query="<Client Name>"`
              — catches threads where the client is named in subject/body.
           b) `mailboxOwnerEmail=<shared_inbox>` + `sender=<client_email>`
              — catches threads where the client wrote in directly.
         Requires Mail.Read.Shared delegation on each shared mailbox.
      5. If 4 returns nothing, fall back to `ADVISOR_INBOXES` for the
         relationship manager + common compliance staff. This is wider and
         noisier; only run when step 4 yields zero to avoid over-fetching.
      6. Dedupe across all sources by Conversation ID.
      7. Classify each surviving thread:
           - `active` — has an action item open against Accruity or client
           - `noise` — matches `_is_noise` heuristic
           - `informational` — no action but relevant context
      8. Tag each thread with its **origin inbox** so the dossier's §3 Email
         Intelligence can show which Accruity inbox it came from (ops/team/
         ask/tax/advisor personal) and any team-inbox thread gets a
         `[SharedInbox:<inbox> …]` source tag.

    Returns: `{"threads": [...], "by_origin": {"client": n, "ops": n,
        "team": n, "ask": n, "tax": n, "advisor": n, "notion_log": n},
        "noise": [...], "dedupe_stats": {...}}`.
    """
    raise NotImplementedError(
        "emails.read binds Outlook MCP + Notion MCP at runtime. Shared "
        "inbox search requires Mail.Read.Shared delegation on each of "
        "operations@accruitytax.com, team@accruitytax.com, "
        "ask@accruitytax.com, and tax@accruity.com."
    )
