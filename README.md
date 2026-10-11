# Gamer Saloon

The client mod set for the **Gamer Saloon** Valheim server. Install this one pack and you have every mod the server expects, at the exact versions it runs.

## Install

1. Install [r2modman](https://thunderstore.io/package/ebkr/r2modman/) or the Thunderstore Mod Manager and pick **Valheim**.
2. Create a profile, search for **GamerSaloon**, and install it. Every mod below comes with it.
3. Launch the game with **Start modded**.

## Updating — please read

- When the pack updates, update **the pack** (GamerSaloon) and nothing else.
- **Do not click "Update all"** on the individual mods. XPortal and Advanced Portals check versions on join: a mod newer than the server's means you cannot connect. The pack is bumped when the server is.

## What's in it

| Mod | What it does | Needed to join? |
|---|---|---|
| XPortal | Pick a portal's destination from a list | Yes (exact version) |
| Advanced Portals | Ancient / Obsidian / Black Marble portals that carry ore | Yes |
| Seasonality | Seasons, seasonal weather and textures | Yes |
| Quick Stack Store | Quick stack (P) / restock (L) to nearby chests, sort, trash | Recommended |
| Equipment and Quick Slots | Equipment panel + quick slots (Z, V, B) | Recommended |
| MultiUserChest | Several players can use one chest at once | Recommended |
| NetworkPerformanceSystem | Smoother multiplayer sync | Optional |
| Portal Preview | See the destination inside a portal | Optional |
| Quiet Portals | Quieter portals | Optional |
| Craft From Chests | Craft using materials in nearby chests | Optional |
| MassFarming | Plant and harvest in a grid | Optional |
| HoverCompare | Compare items on hover | Optional |
| ComfyAutoRepair | Repairs everything when you use a crafting station | Optional |
| InstantMonsterLootDrop | Loot drops instantly, short auto-pickup | Optional |
| Valheim Voice Chat | Proximity voice chat over Steam | Optional |
| Discord Screenshots | F12 or dying posts a screenshot to our Discord | Optional |

Libraries pulled in automatically: BepInExPack, Jotunn, JsonDotNET, YamlDotNet, Conditional Config Sync.

## Settings this pack sets

- **XPortal** — `DisplayPortalColour = true`: shows each portal's colour in the destination list.

Everything else is left at the mod's defaults. Server rules (Seasonality, quick-stack range, Advanced Portals costs) come from the server when you join.

## Tips

- **Voice chat push-to-talk** defaults to **Left Alt**, which Quick Stack Store also uses for favouriting. Rebind it in the voice chat menu (**F9**) — avoid V and B too (quick slots).
- **Discord Screenshots** needs no setup: the server tells your game where to post. Leave its webhook settings empty. F12 is also Steam's screenshot key, so rebind one of them if you don't want both.
- A pack update rewrites the XPortal file above, which resets your personal default portal.
