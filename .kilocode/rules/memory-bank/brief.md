# RimWorld AI Colony Co-Play Brief

RimWorld AI Colony Co-Play is an external AI advisor system that enables Claude to track, analyze, and advise on RimWorld colony management without modifying the game itself. Unlike existing RimWorld AI mods that add in-game terminals and UI elements, this project positions Claude Desktop as an external companion that reads game state from save files and provides strategic guidance through natural conversation.

The project exists to explore a novel human-AI collaboration pattern: co-playing a complex simulation game where the AI has persistent memory of colony history, can identify trends and risks the player might miss, and offers optimization advice grounded in actual game state rather than general knowledge. This creates a gameplay experience where Claude serves as an intelligent advisor with genuine understanding of the specific colony's situation.

The primary user is a single player (VintageDon) running heavily modded RimWorld sessions. The system must handle large save files (20-30MB XML) from 300+ mod configurations, extract meaningful state efficiently, and maintain historical context across play sessions. Future phases may expand to include a lightweight export mod for real-time state access and eventual limited game interaction capabilities.
