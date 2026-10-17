# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Thunderstore **modpack** for the Gamer Saloon Valheim server — no game code. The pack is a manifest (`thunderstore.toml`) listing exact mod versions plus a few shipped config files. Merging to `main` publishes it to Thunderstore as `GamerSaloon-GamerSaloon`.

## Commands

```bash
python3 scripts/check_pack.py deps        # every pinned dependency exists on Thunderstore at that exact version (+ description ≤ 250 chars)
python3 scripts/check_pack.py updates     # list dependencies with a newer/deprecated release on Thunderstore
python3 scripts/check_pack.py changelog   # CHANGELOG.md has a "## <versionNumber>" section
python3 scripts/check_pack.py bumped <base.toml>   # versionNumber is higher than base's
python3 scripts/check_pack.py version     # print versionNumber
tcli build                                # build the zip into ./build (needs `dotnet tool install --global tcli --version 0.2.4`)
```

`check_pack.py` is stdlib-only (Python ≥ 3.11 for `tomllib`). There is no test suite; the checks above are what CI runs.

## How a change ships

- `thunderstore.toml` `[package.dependencies]` = the mods, pinned `Namespace-Name = "x.y.z"`. Libraries (BepInEx, Jotunn, etc.) are listed explicitly too.
- Everything under `config/` is copied into each player's `BepInEx/config` on install/update (`[[build.copy]]`), **overwriting** their personal settings for those files. Only ship a config when the pack needs a non-default value; README "Settings this pack sets" documents each one.
- `README.md` is the Thunderstore page; `CHANGELOG.md` ships in the zip.
- **PR** → `.github/workflows/validate.yml` (required check `validate`): deps exist, changelog has the version, version bumped *if* shipped files (`thunderstore.toml`, `config/`, `README.md`, `CHANGELOG.md`, `icon.png`) changed, `tcli build`, zip uploaded as artifact.
- **Push to main** → `.github/workflows/publish.yml`: if `versionNumber` isn't on Thunderstore yet, `tcli publish` with the `TCLI_AUTH_TOKEN` secret and tag `v<version>`. Repo-only merges are a no-op publish.

## Rules specific to this pack

- **Versions must match the server.** XPortal rejects any version mismatch on join; Advanced Portals and Seasonality are also enforced. Never bump a join-enforced mod in the pack without the server being bumped to the same version (the CHANGELOG notes "Server updated to the same versions"). Players are told not to "Update all", so the pack is the only update channel.
- Thunderstore refuses to re-upload a version: any shipped change needs a `versionNumber` bump (semver; new mod or mod bump = minor, config tweak = minor/patch per history) and a matching `## x.y.z` CHANGELOG entry.
- When adding/removing a mod, update the README mod table (with its "Needed to join?" column) and the `description` if it names the mod.
- `namespace` must stay `GamerSaloon` (the team owning the publish token).
- Never ship secrets in `config/` — e.g. Discord Screenshots' webhook comes from the server, so its config stays unshipped/empty.
- Work on a branch and open a PR; `main` is protected and publishing happens only from CI. Don't run `tcli publish` locally.
