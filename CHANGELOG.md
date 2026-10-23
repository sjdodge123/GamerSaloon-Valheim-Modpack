# Changelog

## 1.8.0

- New: GroupBoard 1.1.1 (`Einherjer-GroupBoard`). A shared to-do list on a buildable Group board (Hammer, Misc tab, needs a workbench; 6 Wood + 1 Coal) that shows the open tasks on its face; `E` opens the list to add, tick off, edit and reorder tasks. A normal sign whose text starts with `Todo` works as a board too. Inside a ward only players with access can change it. **Needed to join**: Jotunn checks it, and any 1.1.x matches the server. Server runs the same version.

## 1.7.0

- RL Valheim Link 0.2.2 -> 0.4.0. The server now sends the contents of the base's chests (every 10 minutes) and the server's crafting recipes, build pieces and processing steps to the group's Raid Ledger, which fills the Valheim hub's Materials and Planner tabs; personal chests stay visible only to their owner and admins. With 0.4.0 on your client, an admin's game also exports the build-piece and crafting-station icons for the Planner once per game version (like the item catalogue). Nothing changes in game. Server updated to the same version.

## 1.6.3

- RL Valheim Link 0.2.1 -> 0.2.2. Brings the link up to the latest Raid Ledger format (larger item catalogues accepted; groundwork for chest contents and the crafting planner, not sent yet) and fixes a server-only diagnostic log line. Nothing changes in game, and the server's link keeps working with 0.2.1 clients too. Server updated to the same version.

## 1.6.2

- RL Valheim Link 0.2.0 -> 0.2.1. When the server runs a world it is not set to link (a test world), your client now stops sending for that session instead of sending data the server throws away. The server also logs a read-only survey of chest contents after each start (nothing is uploaded). Server updated to the same version.
- Portal Preview 1.5.0 -> 1.5.1 (client-only): capturing a portal view no longer freezes the game for 1-2 s; fixes white runestones and wrong depth right after a teleport in portal views.

## 1.6.1

- RL Valheim Link 0.1.5 -> 0.2.0. The server now accepts any client on the same link protocol, so future server-side link updates no longer need a pack update; Equipment & Quick Slots rows are labelled correctly; progress lines while the item catalogue uploads; logout captures no longer stall behind large transfers. Server updated to the same version.

## 1.6.0

- NetworkPerformanceSystem 1.17.0 -> 1.18.0. Server updated to the same version.
- Portal Preview 1.4.0 -> 1.5.0 (client-only).
- RL Valheim Link 0.1.3 -> 0.1.5 (captures made on logout/quit are no longer lost; admin list ids in the `Steam_` format are recognised; re-sends automatically after a Raid Ledger instance rebuild; operator instructions on the mod page). Server updated to the same version.

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
