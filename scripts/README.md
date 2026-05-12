# Scripts

One-click utilities for tasks that the cloud sandbox can't do (anything that requires writing to your local Windows filesystem).

## `sync-to-onedrive.ps1`

Copies every `dossiers/<Client>/dossier.html` from this repo into your OneDrive folder at:

```
C:\Users\SethJohnson\OneDrive - Subledge\_Client Review\Dossier Files\
```

OneDrive then syncs to the cloud automatically; share the folder from OneDrive web to give your team access.

### How to run

1. Open a PowerShell terminal on your Windows laptop
2. `cd` into the root of the cloned repo (the folder containing `dossiers/`, `docs/`, `scripts/`, etc.)
3. Run:

```powershell
.\scripts\sync-to-onedrive.ps1
```

   If PowerShell refuses to run the script because of execution policy, run this once to allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

4. The script reports `✓ <Client>` for each copy and `- <Client>` for any skipped (no `dossier.html` present)

### What it copies

For each client folder under `dossiers/`:
- `dossier.html` — the rendered, team-readable dossier (primary deliverable)
- `dossier.md` — markdown source (for archival/reference)
- `state.json` — refresh progress + sidecar URLs

Plus project-level docs into the OneDrive root:
- `PROJECT_OVERVIEW.md`
- `HANDOFF_2026-04-22.md`
- `BATCH_REFRESH_PROMPT.md`

### When to run

- After every refresh batch finishes on GitHub. `git pull` first, then run the script.
- Whenever you want OneDrive in sync with the repo.

### Config

If you ever move the OneDrive folder, edit `$ONEDRIVE_TARGET` at the top of `sync-to-onedrive.ps1`.

---

*The repo also has the `.html` files plus a copy of every `.md` in `dossiers/` — those exist as backup in case OneDrive sync ever gets weird.*
