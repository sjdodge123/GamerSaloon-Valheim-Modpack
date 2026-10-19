# Changelog

## 1.5.1

- RL Valheim Link 0.1.2 -> 0.1.3 (fixes the client sending nothing on Valheim 1.0.20). Server updated to the same version.

## 1.5.0

- New: RL Valheim Link 0.1.2 (`GamerSaloon-ValheimLink`). On each save, logout or quit your client sends your character, explored map and pins to the server, which pushes them to the group's Raid Ledger; the item catalogue is exported once per game version. Opt out with `[Client] OptOut = true` in `BepInEx/config/RaidLedger.ValheimLink.cfg`. Not join-enforced: without it you simply send nothing.
- Server runs the same version.

## 1.4.0

- Conditional Config Sync 1.0.10 -> 1.0.11 (config sync keeps going on slow connections instead of timing out).
- Quick Stack Store 1.4.15 -> 1.4.16 (Spanish and German translations).
- Server updated to the same versions.

## 1.3.0

- Ships Valheim Voice Chat settings: `MicGain = 2` (was 1). Also `ProximityMinDistance = 10` / `ProximityMaxDistance = 50`; the server now runs the mod and syncs those two to everyone on join, the shipped copy is a fallback.

## 1.2.0

- Seasonality 3.8.3 -> 3.8.4 (Deep North ice shore on ice shelves; new `Affect Armor` option). The server enforces this version on join.
- NetworkPerformanceSystem 1.16.0 -> 1.17.0 (terrain edits reach the ground owner, live map icons for nearby players, less creature ownership thrashing).
- Server updated to the same versions.

## 1.1.0

- Add Discord Screenshots 1.6.8 (F12 and death screenshots to the server's Discord channel). The webhook comes from the server; the pack ships no webhook.

## 1.0.0

- First release: the 20 mods from the server's r2modman profile, pinned to the server's versions.
- Ships XPortal `DisplayPortalColour = true`.
