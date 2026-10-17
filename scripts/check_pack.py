#!/usr/bin/env python3
"""Sanity checks for the modpack before it is built or published.

  check_pack.py deps              every dependency exists on Thunderstore at that exact version
  check_pack.py bumped <base.toml> versionNumber is higher than the one in <base.toml>
  check_pack.py published         exit 0 if this version is already on Thunderstore, 1 if not
  check_pack.py version           print versionNumber
  check_pack.py changelog         CHANGELOG.md has a "## <versionNumber>" section
  check_pack.py updates           list dependencies with a newer (or deprecated) release on Thunderstore
"""
import json
import sys
import tomllib
import urllib.error
import urllib.request

API = "https://thunderstore.io/api/experimental/package"
# Thunderstore's CDN rejects urllib's default user agent.
HEADERS = {"User-Agent": "gamersaloon-modpack-ci"}


def load(path="thunderstore.toml"):
    with open(path, "rb") as f:
        return tomllib.load(f)


def exists(namespace, name, version):
    req = urllib.request.Request(f"{API}/{namespace}/{name}/{version}/", headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp).get("version_number") == version
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        raise


def latest(namespace, name):
    req = urllib.request.Request(f"{API}/{namespace}/{name}/", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return data["latest"]["version_number"], data["latest"]["date_created"][:10], data["is_deprecated"]


def parse_version(v):
    return tuple(int(p) for p in v.split("."))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "deps"
    pkg = load()["package"]

    if cmd == "version":
        print(pkg["versionNumber"])
        return 0

    if cmd == "deps":
        bad = []
        for full, version in pkg["dependencies"].items():
            namespace, name = full.split("-", 1)
            ok = exists(namespace, name, version)
            print(f"{'ok ' if ok else 'BAD'} {full}-{version}")
            if not ok:
                bad.append(f"{full}-{version}")
        desc = pkg["description"]
        if len(desc) > 250:
            bad.append(f"description is {len(desc)} chars (max 250)")
        if bad:
            print("\nProblems:\n  " + "\n  ".join(bad))
            return 1
        return 0

    if cmd == "bumped":
        base = load(sys.argv[2])["package"]["versionNumber"]
        head = pkg["versionNumber"]
        if parse_version(head) <= parse_version(base):
            print(f"versionNumber {head} must be higher than main's {base} — Thunderstore will not accept the same version twice.")
            return 1
        print(f"version {base} -> {head}")
        return 0

    if cmd == "changelog":
        with open("CHANGELOG.md") as f:
            headings = [line.strip() for line in f if line.startswith("## ")]
        if f"## {pkg['versionNumber']}" not in headings:
            print(f"CHANGELOG.md has no '## {pkg['versionNumber']}' section.")
            return 1
        print(f"changelog has {pkg['versionNumber']}")
        return 0

    if cmd == "updates":
        newer = 0
        for full, version in pkg["dependencies"].items():
            namespace, name = full.split("-", 1)
            newest, date, deprecated = latest(namespace, name)
            if parse_version(newest) > parse_version(version):
                newer += 1
                print(f"NEW {full}: {version} -> {newest} ({date})")
            else:
                print(f"ok  {full}-{version}")
            if deprecated:
                print(f"    {full} is DEPRECATED on Thunderstore")
        print(f"\n{newer} dependenc{'y has' if newer == 1 else 'ies have'} a newer release.")
        return 0

    if cmd == "published":
        return 0 if exists(pkg["namespace"], pkg["name"], pkg["versionNumber"]) else 1

    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
