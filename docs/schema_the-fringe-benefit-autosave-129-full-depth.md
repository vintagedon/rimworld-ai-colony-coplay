# RimWorld Save Schema Discovery

**Source:** `the-fringe-benefit#§#Autosave-129.rws`
**Generated:** 2026-01-18 10:22:53
**File Size:** 17.1 MB

## Summary

| Metric | Value |
|--------|-------|
| Total XML Elements | 418,374 |
| Unique Tag Paths | 4,854 |
| Maximum Depth | 17 |

## Schema Tree

Format: `tag_name (count)` — attributes: [attr1, attr2] — has text content

└── savegame (1)
    ├── game (1)
    │   ├── analysisManager (1)
    │   │   └── analysisDetails (1)
    │   │       ├── keys (1)
    │   │       └── values (1)
    │   ├── areaHelper (1)
    │   │   ├── maps (1)
    │   │   │   ├── keys (1)
    │   │   │   │   └── li (1) — [text]
    │   │   │   └── values (1)
    │   │   │       └── li (1)
    │   │   │           ├── areaExtended (1)
    │   │   │           │   ├── keys (1)
    │   │   │           │   │   └── li (4) — [text]
    │   │   │           │   └── values (1)
    │   │   │           │       └── li (4)
    │   │   │           └── areas (1)
    │   │   │               └── li (8)
    │   │   │                   ├── ID (8) — [text]
    │   │   │                   ├── areaStates (8)
    │   │   │                   │   ├── states (8)
    │   │   │                   │   │   ├── keys (8)
    │   │   │                   │   │   │   └── li (11) — [text]
    │   │   │                   │   │   └── values (8)
    │   │   │                   │   │       └── li (11)
    │   │   │                   │   │           └── layers (11)
    │   │   │                   │   │               ├── keys (11)
    │   │   │                   │   │               │   └── li (13) — [text]
    │   │   │                   │   │               └── values (11)
    │   │   │                   │   │                   └── li (13) — [text]
    │   │   │                   │   └── key (7) — [text]
    │   │   │                   └── innerGrid (8)
    │   │   │                       ├── arrDeflate (8) — [text]
    │   │   │                       ├── mapSizeX (8) — [text]
    │   │   │                       ├── mapSizeZ (8) — [text]
    │   │   │                       └── trueCount (7) — [text]
    │   │   └── pawns (1)
    │   │       ├── keys (1)
    │   │       │   └── li (10) — [text]
    │   │       └── values (1)
    │   │           └── li (10)
    │   │               └── areaStatesByMap (10)
    │   │                   ├── keys (10)
    │   │                   │   └── li (10) — [text]
    │   │                   └── values (10)
    │   │                       └── li (10)
    │   │                           ├── key (10) — [text]
    │   │                           └── states (10)
    │   │                               ├── keys (10)
    │   │                               │   └── li (14) — [text]
    │   │                               └── values (10)
    │   │                                   └── li (14)
    │   │                                       └── layers (14)
    │   │                                           ├── keys (14)
    │   │                                           │   └── li (17) — [text]
    │   │                                           └── values (14)
    │   │                                               └── li (17) — [text]
    │   ├── battleLog (1)
    │   │   └── battles (1)
    │   │       └── li (114)
    │   │           ├── absorbedBy (114) — [text]
    │   │           ├── creationTimestamp (114) — [text]
    │   │           ├── entries (114)
    │   │           │   └── li (322) — attrs: [Class]
    │   │           │       ├── logID (322) — [text]
    │   │           │       ├── ticksAbs (322) — [text]
    │   │           │       ├── recipientPawn (278) — [text]
    │   │           │       ├── initiatorPawn (239) — [text]
    │   │           │       ├── projectileDef (232) — [text]
    │   │           │       ├── weaponDef (232) — [text]
    │   │           │       ├── damagedParts (171) — attrs: [IsNull]
    │   │           │       │   └── li (79)
    │   │           │       │       ├── body (79) — [text]
    │   │           │       │       └── index (79) — [text]
    │   │           │       ├── damagedPartsDestroyed (171) — attrs: [IsNull]
    │   │           │       │   └── li (79) — [text]
    │   │           │       ├── originalTargetMobile (125) — [text]
    │   │           │       ├── originalTargetPawn (125) — [text]
    │   │           │       ├── initiator (83) — [text]
    │   │           │       ├── def (46) — [text]
    │   │           │       ├── implementType (46) — [text]
    │   │           │       ├── ruleDef (46) — [text]
    │   │           │       ├── ownerDef (44) — [text]
    │   │           │       ├── subjectPawn (44) — [text]
    │   │           │       ├── coverDef (42) — [text]
    │   │           │       ├── transitionDef (37) — [text]
    │   │           │       ├── culpritHediffDef (32) — [text]
    │   │           │       ├── recipientThing (32) — [text]
    │   │           │       ├── alwaysShowInCompact (29) — [text]
    │   │           │       ├── toolLabel (28) — [text]
    │   │           │       ├── culpritTargetPart (20)
    │   │           │       │   ├── body (20) — [text]
    │   │           │       │   └── index (20) — [text]
    │   │           │       ├── culpritHediffTargetPart (17)
    │   │           │       │   ├── body (17) — [text]
    │   │           │       │   └── index (17) — [text]
    │   │           │       ├── burst (10) — [text]
    │   │           │       └── eventDef (7) — [text]
    │   │           └── loadID (114) — [text]
    │   ├── cameraMap (1)
    │   │   ├── camRootPos (1) — [text]
    │   │   ├── desiredSize (1) — [text]
    │   │   ├── extendedShakeRequests (1)
    │   │   └── unpausedExtendedShakeRequests (1)
    │   ├── components (1)
    │   │   └── li (41) — attrs: [Class]
    │   │       ├── raidGroups (2)
    │   │       │   └── li (9)
    │   │       │       ├── faction (9) — [text]
    │   │       │       ├── lords (9)
    │   │       │       │   └── li (1) — [text]
    │   │       │       ├── pawns (5)
    │   │       │       │   └── li (6) — [text]
    │   │       │       ├── defenders (4)
    │   │       │       │   └── li (20) — [text]
    │   │       │       ├── initTime (4) — [text]
    │   │       │       └── raiders (4)
    │   │       │           └── li (2) — [text]
    │   │       ├── taggedItems (2)
    │   │       │   ├── keys (2)
    │   │       │   └── values (2)
    │   │       ├── FavouriteAssignments (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── Favourites (1)
    │   │       ├── Hub (1) — [text]
    │   │       ├── NextId (1) — [text]
    │   │       ├── Priorities (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (12) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (12)
    │   │       │           ├── Pawn (12) — [text]
    │   │       │           ├── Priorities (12)
    │   │       │           │   └── li (2,700)
    │   │       │           │       ├── Priorities (2,700) — [text]
    │   │       │           │       └── Workgiver (2,700) — [text]
    │   │       │           └── loadId (12) — [text]
    │   │       ├── QuestLog (1)
    │   │       ├── absentMindedWithLastDiscardedTick (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── achievementList (1)
    │   │       │   └── li (212)
    │   │       │       ├── def (212) — [text]
    │   │       │       ├── tracker (212) — attrs: [Class]
    │   │       │       │   ├── cardAssigned (212) — [text]
    │   │       │       │   ├── uniqueId (212) — [text]
    │   │       │       │   ├── def (78) — [text]
    │   │       │       │   ├── count (67) — [text]
    │   │       │       │   ├── kindDefs (35)
    │   │       │       │   │   ├── keys (35)
    │   │       │       │   │   │   └── li (215) — [text]
    │   │       │       │   │   └── values (35)
    │   │       │       │   │       └── li (215) — [text]
    │   │       │       │   ├── factionDefs (18) — attrs: [IsNull]
    │   │       │       │   │   └── li (5) — [text]
    │   │       │       │   ├── instigatorFactionDefs (18) — attrs: [IsNull]
    │   │       │       │   │   └── li (4) — [text]
    │   │       │       │   ├── killedThings (18)
    │   │       │       │   │   └── li (3,197) — [text]
    │   │       │       │   ├── thingList (15)
    │   │       │       │   │   ├── keys (15)
    │   │       │       │   │   │   └── li (3) — [text]
    │   │       │       │   │   └── values (15)
    │   │       │       │   │       └── li (3) — [text]
    │   │       │       │   ├── triggeredCount (15) — [text]
    │   │       │       │   ├── abilityDefs (12) — attrs: [IsNull]
    │   │       │       │   ├── abilityDef (10) — [text]
    │   │       │       │   ├── targetThingDefs (10) — attrs: [IsNull]
    │   │       │       │   ├── kindDef (9) — [text]
    │   │       │       │   ├── madeFrom (9) — [text]
    │   │       │       │   ├── requireAll (9) — [text]
    │   │       │       │   ├── raceDef (7) — [text]
    │   │       │       │   ├── registeredBuildings (7)
    │   │       │       │   │   └── li (3,773) — [text]
    │   │       │       │   ├── ingestorsThingDefs (6) — attrs: [IsNull]
    │   │       │       │   │   └── li (2) — [text]
    │   │       │       │   ├── raceDefs (6)
    │   │       │       │   │   ├── keys (6)
    │   │       │       │   │   │   └── li (6) — [text]
    │   │       │       │   │   └── values (6)
    │   │       │       │   │       └── li (6) — [text]
    │   │       │       │   ├── total (6) — [text]
    │   │       │       │   ├── defs (5)
    │   │       │       │   │   ├── keys (5)
    │   │       │       │   │   │   └── li (11) — [text]
    │   │       │       │   │   └── values (5)
    │   │       │       │   │       └── li (11) — [text]
    │   │       │       │   ├── entitiesList (5)
    │   │       │       │   │   ├── keys (5)
    │   │       │       │   │   │   └── li (5) — [text]
    │   │       │       │   │   └── values (5)
    │   │       │       │   │       └── li (5) — [text]
    │   │       │       │   ├── ingestorThingDef (5) — [text]
    │   │       │       │   ├── title (5) — [text]
    │   │       │       │   ├── totalEntities (5) — [text]
    │   │       │       │   ├── coreModsOnly (4) — [text]
    │   │       │       │   ├── countTemporary (4) — [text]
    │   │       │       │   ├── tech (4) — [text]
    │   │       │       │   ├── ticksPassed (4) — [text]
    │   │       │       │   ├── amountOfMods (3) — [text]
    │   │       │       │   ├── level (3) — [text]
    │   │       │       │   ├── outcome (3) — [text]
    │   │       │       │   ├── registeredPlants (3)
    │   │       │       │   │   └── li (50) — [text]
    │   │       │       │   ├── singleTransaction (3) — [text]
    │   │       │       │   ├── targetThingDef (3) — [text]
    │   │       │       │   ├── xenotypeDefs (3)
    │   │       │       │   │   ├── keys (3)
    │   │       │       │   │   │   └── li (11) — [text]
    │   │       │       │   │   └── values (3)
    │   │       │       │   │       └── li (11) — [text]
    │   │       │       │   ├── allowedSeasons (2)
    │   │       │       │   │   └── li (4) — [text]
    │   │       │       │   ├── average (2) — [text]
    │   │       │       │   ├── checkIfCorpse (2) — [text]
    │   │       │       │   ├── checkTargetOnlyOfPlayerFaction (2) — [text]
    │   │       │       │   ├── foodDef (2) — [text]
    │   │       │       │   ├── gameTime (2) — [text]
    │   │       │       │   ├── includeingredient (2) — [text]
    │   │       │       │   ├── instigatorThingDef (2) — [text]
    │   │       │       │   ├── nociosphereActivations (2) — [text]
    │   │       │       │   ├── numberOfPrisoners (2) — [text]
    │   │       │       │   ├── numberOfSlaves (2) — [text]
    │   │       │       │   ├── onlyCountPlayerPawns (2) — [text]
    │   │       │       │   ├── quality (2) — [text]
    │   │       │       │   ├── targetBelowHealthPercentage (2) — [text]
    │   │       │       │   ├── weaponDef (2) — [text]
    │   │       │       │   ├── checkIfTree (1) — [text]
    │   │       │       │   ├── consecutive (1) — [text]
    │   │       │       │   ├── countClones (1) — [text]
    │   │       │       │   ├── genesList (1)
    │   │       │       │   │   ├── keys (1)
    │   │       │       │   │   │   └── li (1) — [text]
    │   │       │       │   │   └── values (1)
    │   │       │       │   │       └── li (1) — [text]
    │   │       │       │   ├── includeIngredientDef (1) — [text]
    │   │       │       │   ├── kindDefList (1)
    │   │       │       │   │   ├── keys (1)
    │   │       │       │   │   │   └── li (3) — [text]
    │   │       │       │   │   └── values (1)
    │   │       │       │   │       └── li (3) — [text]
    │   │       │       │   ├── mood (1) — [text]
    │   │       │       │   ├── mustHaveAll (1) — [text]
    │   │       │       │   ├── onlyPsycast (1) — [text]
    │   │       │       │   ├── targetFactionTechLevel (1) — [text]
    │   │       │       │   ├── targetManhunter (1) — [text]
    │   │       │       │   ├── targetOnFire (1) — [text]
    │   │       │       │   ├── triggeredWorth (1) — [text]
    │   │       │       │   ├── worth (1) — [text]
    │   │       │       │   └── xenotypeDef (1) — [text]
    │   │       │       ├── uniqueHash (212) — [text]
    │   │       │       ├── dateUnlocked (14) — [text]
    │   │       │       └── unlocked (14) — [text]
    │   │       ├── activeAspirations (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── angryWorkers (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── artCreator (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (5) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (5) — [text]
    │   │       ├── axialTilt (1) — [text]
    │   │       ├── backwardsCompatibilityVersion (1) — [text]
    │   │       ├── bigBoned (1)
    │   │       │   └── li (3) — [text]
    │   │       ├── birthdays (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── corpses (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── cowards (1)
    │   │       │   └── li (4) — [text]
    │   │       ├── currentPriority (1) — [text]
    │   │       ├── currentStoryteller (1) — [text]
    │   │       ├── defaultFoodRestriction (1)
    │   │       │   ├── filter (1)
    │   │       │   │   ├── allowedDefs (1)
    │   │       │   │   │   └── li (361) — [text]
    │   │       │   │   ├── allowedHitPointsPercents (1) — [text]
    │   │       │   │   ├── allowedMentalBreakChance (1) — [text]
    │   │       │   │   ├── allowedQualityLevels (1) — [text]
    │   │       │   │   └── disallowedSpecialFilters (1)
    │   │       │   │       └── li (11) — [text]
    │   │       │   ├── id (1) — [text]
    │   │       │   └── label (1) — [text]
    │   │       ├── draftedActions (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (7) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (7)
    │   │       │           ├── autocastAbilities (7)
    │   │       │           └── pawnID (7) — [text]
    │   │       ├── duplicates (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── emergedBiosignatures (1)
    │   │       ├── finishedQuests (1)
    │   │       ├── fireGrayPallTick (1) — [text]
    │   │       ├── forcedJobs (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── forcedSongs (1)
    │   │       ├── futureQuests (1)
    │   │       ├── hediffEntries (1)
    │   │       ├── honoredDeadPawns (1)
    │   │       ├── honors (1)
    │   │       ├── hypnotisedPawns (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── joinedColonists (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (7) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (7) — [text]
    │   │       ├── killedBosses (1)
    │   │       ├── lastFoodType (1)
    │   │       │   └── LastFoodType_Map (1)
    │   │       │       ├── keys (1)
    │   │       │       │   └── li (8) — [text]
    │   │       │       └── values (1)
    │   │       │           └── li (8) — [text]
    │   │       ├── lastHonorAward (1) — [text]
    │   │       ├── lastQuest (1) — attrs: [IsNull]
    │   │       ├── lastRoyalGossipTick (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (1) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (1) — [text]
    │   │       ├── lastWealth (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (2) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (2) — [text]
    │   │       ├── levelDef (1) — [text]
    │   │       ├── listeners (1)
    │   │       ├── llastFoodType (1)
    │   │       │   └── LastFoodType_Map (1)
    │   │       │       ├── keys (1)
    │   │       │       │   └── li (8) — [text]
    │   │       │       └── values (1)
    │   │       │           └── li (8) — [text]
    │   │       ├── looseCorpseTrackers (1)
    │   │       ├── madSurgeonsWithLastHarvestedTick (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (3) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (3) — [text]
    │   │       ├── manffalo_and_experience_backup (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── metalHellPawns (1)
    │   │       ├── metalHellReturnTick (1) — [text]
    │   │       ├── monolith (1) — [text]
    │   │       ├── monolithLetters (1)
    │   │       ├── newestMetalhorrorBiosignatureTick (1) — [text]
    │   │       ├── nextHarbingerTreeCheckTick (1) — [text]
    │   │       ├── pawnsWithAdditionalTrait (1)
    │   │       ├── pawnsWithWorkers (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (5) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (5)
    │   │       │           └── workersWithWorkingTicks (5)
    │   │       │               ├── keys (5)
    │   │       │               │   └── li (30) — [text]
    │   │       │               └── values (5)
    │   │       │                   └── li (30)
    │   │       │                       ├── lastTick (30) — [text]
    │   │       │                       └── workTick (29) — [text]
    │   │       ├── perfectionistsWithJobsToStop (1)
    │   │       ├── points (1) — [text]
    │   │       ├── postRaidPeriodTicks (1) — [text]
    │   │       ├── prioritySongs (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── questChainStates (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── questGiverManagers (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── raidQueues (1)
    │   │       ├── reinforcementGroups (1)
    │   │       ├── ritualCooldowns (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── sendAICoreRequestReminder (1) — [text]
    │   │       ├── sentOncePerGame (1) — [text]
    │   │       ├── sentOncePerGameGenes (1) — [text]
    │   │       ├── snobs (1)
    │   │       │   └── li (3) — [text]
    │   │       ├── squeamishWithLastVomitedTick (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── subcount (1) — [text]
    │   │       ├── teachersWithPupils (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (12) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (12)
    │   │       │           ├── pupil (12) — [text]
    │   │       │           └── skillDef (12) — [text]
    │   │       ├── tickCounterManffaloXP (1) — [text]
    │   │       ├── ticksTillIncident (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── tileFoldersEnabled (1) — [text]
    │   │       ├── timesCalledBossgroups (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── totalEarnedPoints (1) — [text]
    │   │       ├── triggeredSignals (1)
    │   │       ├── voidNodeActivator (1) — [text]
    │   │       ├── wanderLustersWithLastMapExitedTick (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (5) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (5) — [text]
    │   │       ├── worldPreset (1) — [text]
    │   │       └── worldType (1) — [text]
    │   ├── currentMapIndex (1) — [text]
    │   ├── customXenogermDatabase (1)
    │   │   └── customXenogerms (1)
    │   ├── customXenotypeDatabase (1)
    │   │   └── customXenotypes (1)
    │   ├── dateNotifier (1)
    │   │   └── lastSeason (1) — [text]
    │   ├── drugPolicyDatabase (1)
    │   │   └── policies (1)
    │   │       └── li (4)
    │   │           ├── drugs (4)
    │   │           │   └── li (152)
    │   │           │       ├── drug (152) — [text]
    │   │           │       ├── allowedForAddiction (148) — [text]
    │   │           │       ├── allowedForJoy (22) — [text]
    │   │           │       ├── allowScheduled (1) — [text]
    │   │           │       └── takeToInventory (1) — [text]
    │   │           ├── id (4) — [text]
    │   │           ├── label (4) — [text]
    │   │           └── sourceDef (4) — [text]
    │   ├── entityCodex (1)
    │   │   ├── discoveredEntities (1)
    │   │   │   └── li (1) — [text]
    │   │   ├── hiddenCategories (1)
    │   │   │   ├── keys (1)
    │   │   │   │   └── li (3) — [text]
    │   │   │   └── values (1)
    │   │   │       └── li (3) — [text]
    │   │   └── hiddenEntries (1)
    │   │       ├── keys (1)
    │   │       │   └── li (27) — [text]
    │   │       └── values (1)
    │   │           └── li (27) — [text]
    │   ├── foodRestrictionDatabase (1)
    │   │   └── foodRestrictions (1)
    │   │       └── li (11)
    │   │           ├── filter (11)
    │   │           │   ├── allowedDefs (11)
    │   │           │   │   └── li (6,307) — [text]
    │   │           │   ├── allowedHitPointsPercents (11) — [text]
    │   │           │   ├── allowedMentalBreakChance (11) — [text]
    │   │           │   ├── allowedQualityLevels (11) — [text]
    │   │           │   └── disallowedSpecialFilters (11)
    │   │           │       └── li (13) — [text]
    │   │           ├── id (11) — [text]
    │   │           └── label (11) — [text]
    │   ├── gameEnder (1)
    │   ├── hiddenItemsManager (1)
    │   │   └── hiddenItemDefs (1)
    │   │       ├── keys (1)
    │   │       │   └── li (33) — [text]
    │   │       └── values (1)
    │   │           └── li (33) — [text]
    │   ├── history (1)
    │   │   ├── archive (1)
    │   │   │   ├── archivables (1)
    │   │   │   │   └── li (200) — attrs: [Class]
    │   │   │   │       ├── ID (200) — [text]
    │   │   │   │       ├── def (200) — [text]
    │   │   │   │       ├── lookTargets (200) — attrs: [IsNull]
    │   │   │   │       │   └── targets (129)
    │   │   │   │       │       └── li (147) — [text]
    │   │   │   │       ├── quest (200) — [text]
    │   │   │   │       ├── text (200) — [text]
    │   │   │   │       ├── startingFrame (147) — [text]
    │   │   │   │       ├── startingTick (147) — [text]
    │   │   │   │       ├── startingTime (147) — [text]
    │   │   │   │       ├── ThreatPointsBreakdown (53) — attrs: [IsNull]
    │   │   │   │       ├── arrivalTick (53) — [text]
    │   │   │   │       ├── hyperlinkHediffDefs (53) — attrs: [IsNull]
    │   │   │   │       ├── hyperlinkThingDefs (53) — attrs: [IsNull]
    │   │   │   │       ├── label (53) — [text]
    │   │   │   │       ├── relatedFaction (53) — [text]
    │   │   │   │       └── title (4) — [text]
    │   │   │   └── pinnedArchivables (1)
    │   │   ├── autoRecorderGroups (1)
    │   │   │   └── li (4)
    │   │   │       ├── def (4) — [text]
    │   │   │       └── recorders (4)
    │   │   │           └── li (11)
    │   │   │               ├── def (11) — [text]
    │   │   │               └── recordsDeflate (11) — [text]
    │   │   ├── historyEventsManager (1)
    │   │   │   ├── colonistEvents (1)
    │   │   │   │   └── vals (1)
    │   │   │   │       └── li (193)
    │   │   │   │           ├── customGoodwill (193) — attrs: [IsNull]
    │   │   │   │           │   └── li (9,238) — [text]
    │   │   │   │           └── ticksGame (193) — attrs: [IsNull]
    │   │   │   │               └── li (268) — [text]
    │   │   │   └── eventsAffectingFaction (1)
    │   │   │       ├── keys (1)
    │   │   │       │   └── li (5) — [text]
    │   │   │       └── values (1)
    │   │   │           └── li (5)
    │   │   │               └── vals (5)
    │   │   │                   └── li (965)
    │   │   │                       ├── customGoodwill (965) — attrs: [IsNull]
    │   │   │                       │   └── li (6) — [text]
    │   │   │                       └── ticksGame (965) — attrs: [IsNull]
    │   │   │                           └── li (6) — [text]
    │   │   ├── lastPsylinkAvailable (1) — [text]
    │   │   └── mechanoidDatacoreOpportunityAvailable (1) — [text]
    │   ├── info (1)
    │   │   ├── realPlayTimeInteracting (1) — [text]
    │   │   ├── startingAndOptionalPawns (1)
    │   │   │   └── li (6) — [text]
    │   │   └── startingTile (1) — [text]
    │   ├── letterStack (1)
    │   │   ├── letterQueue (1)
    │   │   └── letters (1)
    │   ├── loadoutDatabase (1)
    │   │   └── loadouts (1)
    │   │       └── li (2)
    │   │           ├── filter (2)
    │   │           │   ├── allowedDefs (2)
    │   │           │   │   └── li (300) — [text]
    │   │           │   ├── allowedHitPointsPercents (2) — [text]
    │   │           │   ├── allowedMentalBreakChance (2) — [text]
    │   │           │   ├── allowedQualityLevels (2) — [text]
    │   │           │   └── disallowedSpecialFilters (2)
    │   │           ├── label (2) — [text]
    │   │           └── uniqueID (2) — [text]
    │   ├── maps (1)
    │   │   └── li (1)
    │   │       ├── areaManager (1)
    │   │       │   └── areas (1)
    │   │       │       └── li (8) — attrs: [Class]
    │   │       │           ├── ID (8) — [text]
    │   │       │           ├── innerGrid (8)
    │   │       │           │   ├── arrDeflate (8) — [text]
    │   │       │           │   ├── mapSizeX (8) — [text]
    │   │       │           │   ├── mapSizeZ (8) — [text]
    │   │       │           │   └── trueCount (6) — [text]
    │   │       │           ├── color (2) — [text]
    │   │       │           └── label (2) — [text]
    │   │       ├── attackTargetReservationManager (1)
    │   │       │   └── reservations (1)
    │   │       ├── autoSlaughterManager (1)
    │   │       │   └── configs (1)
    │   │       │       └── li (455)
    │   │       │           └── animal (455) — [text]
    │   │       ├── components (1)
    │   │       │   └── li (77) — attrs: [Class]
    │   │       │       ├── LWMDS_settingsForBPandFrames (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── PatientFoodPolicy (1) — [text]
    │   │       │       ├── QuestLog (1)
    │   │       │       ├── TA_Expose_Numbers (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── TA_Expose_People (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   │   └── li (1) — [text]
    │   │       │       │   └── values (1)
    │   │       │       │       └── li (1) — [text]
    │   │       │       ├── TA_Expose_People_isSaved (1) — [text]
    │   │       │       ├── acceptSurgery (1) — [text]
    │   │       │       ├── allMapTeleports (1)
    │   │       │       ├── animalsToCarry (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── awaitingIngredients (1)
    │   │       │       ├── awaitingPickup (1)
    │   │       │       ├── biomeGrid (1) — attrs: [IsNull]
    │   │       │       ├── cannons (1)
    │   │       │       ├── colonist_junk_tracker_backup (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── colonist_obelisk_tracker_backup (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── controller (1) — [text]
    │   │       │       ├── defaultAreaRestriction (1) — [text]
    │   │       │       ├── defaultAreaShopping (1) — [text]
    │   │       │       ├── destroyedBuildings (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── drugPolicy (1)
    │   │       │       │   ├── drugs (1)
    │   │       │       │   │   └── li (38)
    │   │       │       │   │       ├── allowedForAddiction (38) — [text]
    │   │       │       │   │       ├── drug (38) — [text]
    │   │       │       │   │       └── allowedForJoy (12) — [text]
    │   │       │       │   └── label (1) — [text]
    │   │       │       ├── durabilities (1)
    │   │       │       │   └── li (27)
    │   │       │       │       ├── durability (27) — [text]
    │   │       │       │       └── thing (27) — [text]
    │   │       │       ├── fleshmassDestroyTicks (1)
    │   │       │       ├── fleshmassToDestroy (1)
    │   │       │       ├── growZoneRegistry (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   │   └── li (6) — [text]
    │   │       │       │   └── values (1)
    │   │       │       │       └── li (6)
    │   │       │       │           ├── minHarvestDay (6) — [text]
    │   │       │       │           ├── minHarvestDayForNewlySown (6) — [text]
    │   │       │       │           ├── averageGrowth (5) — [text]
    │   │       │       │           ├── nutritionYield (4) — [text]
    │   │       │       │           ├── averageFertility (3) — [text]
    │   │       │       │           └── fertilityLow (3) — [text]
    │   │       │       ├── hediffOverlays (1)
    │   │       │       ├── incidentQueue (1)
    │   │       │       │   └── queuedIncidents (1)
    │   │       │       │       └── li (3)
    │   │       │       │           ├── fireTick (3) — [text]
    │   │       │       │           └── firingInc (3)
    │   │       │       │               ├── def (3) — [text]
    │   │       │       │               └── parms (3)
    │   │       │       │                   ├── ThreatPointsBreakdown (3) — attrs: [IsNull]
    │   │       │       │                   ├── attackTargets (3) — attrs: [IsNull]
    │   │       │       │                   ├── controllerPawn (3) — [text]
    │   │       │       │                   ├── faction (3) — [text]
    │   │       │       │                   ├── gifts (3) — attrs: [IsNull]
    │   │       │       │                   ├── letterHyperlinkHediffDefs (3) — attrs: [IsNull]
    │   │       │       │                   ├── letterHyperlinkThingDefs (3) — attrs: [IsNull]
    │   │       │       │                   ├── lord (3) — [text]
    │   │       │       │                   ├── mechClusterSketch (3) — attrs: [IsNull]
    │   │       │       │                   ├── pawnGroups (3) — attrs: [IsNull]
    │   │       │       │                   ├── pawnIdeo (3) — [text]
    │   │       │       │                   ├── quest (3) — [text]
    │   │       │       │                   ├── sendLetter (3) — [text]
    │   │       │       │                   ├── spawnRotation (3) — [text]
    │   │       │       │                   ├── target (3) — [text]
    │   │       │       │                   └── threatPoints (3) — [text]
    │   │       │       ├── lastQuest (1) — attrs: [IsNull]
    │   │       │       ├── lastRenderedCounter (1) — [text]
    │   │       │       ├── lastRenderedHour (1) — [text]
    │   │       │       ├── launcherTargets (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── listeners (1)
    │   │       │       ├── lootables_InMap (1)
    │   │       │       ├── nextQueueInspection (1) — [text]
    │   │       │       ├── obelisks_InMap (1)
    │   │       │       ├── objectives (1)
    │   │       │       ├── openingHours (1)
    │   │       │       │   └── li (24) — [text]
    │   │       │       ├── paragonsToCarry (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── patients (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── pawnsDesiringSuicide (1)
    │   │       │       ├── questTags (1) — attrs: [IsNull]
    │   │       │       ├── refuseGuestsUntilWeHaveBeds (1) — [text]
    │   │       │       ├── refusedOperations (1)
    │   │       │       ├── restaurants (1)
    │   │       │       │   └── li (1)
    │   │       │       │       ├── day (1) — [text]
    │   │       │       │       ├── debts (1)
    │   │       │       │       │   └── debts (1)
    │   │       │       │       ├── menu (1)
    │   │       │       │       │   └── menuFilter (1) — attrs: [IsNull]
    │   │       │       │       ├── name (1) — [text]
    │   │       │       │       ├── orders (1)
    │   │       │       │       │   └── orders (1)
    │   │       │       │       ├── registers (1)
    │   │       │       │       └── stock (1)
    │   │       │       ├── roadEdgeTiles (1)
    │   │       │       ├── roofMaintenanceGrid (1)
    │   │       │       │   └── grid (1)
    │   │       │       │       ├── keys (1)
    │   │       │       │       └── values (1)
    │   │       │       ├── rsTargetEndX (1) — [text]
    │   │       │       ├── rsTargetEndZ (1) — [text]
    │   │       │       ├── rsTargetStartX (1) — [text]
    │   │       │       ├── rsTargetStartZ (1) — [text]
    │   │       │       ├── signaledCaravanArriving (1) — [text]
    │   │       │       ├── stores (1)
    │   │       │       ├── studiables_InMap (1)
    │   │       │       ├── surfaceResourceGrid (1)
    │   │       │       │   └── oreGridDeflate (1) — [text]
    │   │       │       ├── terrains (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── terrorism (1)
    │   │       │       │   ├── keys (1)
    │   │       │       │   └── values (1)
    │   │       │       ├── tickCounterCaravan (1) — [text]
    │   │       │       ├── tickCounterJunk (1) — [text]
    │   │       │       ├── tickCounterMechs (1) — [text]
    │   │       │       ├── tickCounterObelisks (1) — [text]
    │   │       │       ├── tickCounterRooms (1) — [text]
    │   │       │       ├── tickCounterRoyalty (1) — [text]
    │   │       │       ├── tickerDirection (1) — [text]
    │   │       │       ├── transitiveDirection (1) — [text]
    │   │       │       ├── triggeredSignals (1)
    │   │       │       ├── uniqueIDsManager (1)
    │   │       │       └── windDirection (1) — [text]
    │   │       ├── compressedThingMapDeflate (1) — [text]
    │   │       ├── damageWatcher (1)
    │   │       │   └── everDamage (1) — [text]
    │   │       ├── deepResourceGrid (1)
    │   │       │   ├── countGridDeflate (1) — [text]
    │   │       │   └── defGridDeflate (1) — [text]
    │   │       ├── deferredSpawner (1)
    │   │       │   └── requests (1)
    │   │       ├── designationManager (1)
    │   │       │   └── allDesignations (1)
    │   │       │       └── li (216)
    │   │       │           ├── def (216) — [text]
    │   │       │           └── target (216) — [text]
    │   │       ├── enrouteManager (1)
    │   │       │   └── enroute (1)
    │   │       ├── flecks (1)
    │   │       ├── fogGrid (1)
    │   │       │   └── fogGridDeflate (1) — [text]
    │   │       ├── gameConditionManager (1)
    │   │       │   ├── activeConditions (1)
    │   │       │   └── mapBrightnessTracker (1)
    │   │       │       └── lerpSeconds (1) — [text]
    │   │       ├── gasGrid (1)
    │   │       │   ├── cycleIndexDiffusion (1) — [text]
    │   │       │   ├── cycleIndexDissipation (1) — [text]
    │   │       │   └── gasDensityDeflate (1) — [text]
    │   │       ├── generatedId (1) — [text]
    │   │       ├── generatorDef (1) — [text]
    │   │       ├── landingBlockers (1)
    │   │       ├── layoutStructureSketches (1)
    │   │       ├── lordManager (1)
    │   │       │   ├── lords (1)
    │   │       │   └── stencilDrawers (1)
    │   │       ├── lordsStarter (1)
    │   │       │   └── lastLordStartTick (1) — [text]
    │   │       ├── mapInfo (1)
    │   │       │   ├── parent (1) — [text]
    │   │       │   └── size (1) — [text]
    │   │       ├── mineStrikeManager (1)
    │   │       │   └── strikeRecords (1)
    │   │       ├── pawnDestinationReservationManager (1)
    │   │       │   └── reservedDestinations (1)
    │   │       │       ├── keys (1)
    │   │       │       │   └── li (15) — [text]
    │   │       │       └── values (1)
    │   │       │           └── li (15)
    │   │       │               └── list (15)
    │   │       │                   └── li (3)
    │   │       │                       ├── claimant (3) — [text]
    │   │       │                       ├── job (3) — [text]
    │   │       │                       └── target (3) — [text]
    │   │       ├── physicalInteractionReservationManager (1)
    │   │       │   └── reservations (1)
    │   │       ├── planManager (1)
    │   │       │   └── allPlans (1)
    │   │       ├── pocketTileInfo (1) — attrs: [IsNull]
    │   │       ├── pollutionGrid (1)
    │   │       │   └── grid (1)
    │   │       │       ├── arrDeflate (1) — [text]
    │   │       │       ├── mapSizeX (1) — [text]
    │   │       │       └── mapSizeZ (1) — [text]
    │   │       ├── rememberedCameraPos (1)
    │   │       │   ├── rootPos (1) — [text]
    │   │       │   └── rootSize (1) — [text]
    │   │       ├── reservationManager (1)
    │   │       │   └── reservations (1)
    │   │       │       └── li (56)
    │   │       │           ├── claimant (56) — [text]
    │   │       │           ├── job (56) — [text]
    │   │       │           ├── maxPawns (56) — [text]
    │   │       │           ├── target (56) — [text]
    │   │       │           └── stackCount (49) — [text]
    │   │       ├── retainedCaravanData (1)
    │   │       │   ├── arrivalAction (1) — attrs: [IsNull]
    │   │       │   ├── destinationTile (1) — [text]
    │   │       │   └── nextTileCostLeftPct (1) — [text]
    │   │       ├── roofGrid (1)
    │   │       │   └── roofsDeflate (1) — [text]
    │   │       ├── sandGrid (1)
    │   │       │   └── depthGridDeflate (1) — [text]
    │   │       ├── snowGrid (1)
    │   │       │   └── depthGridDeflate (1) — [text]
    │   │       ├── storageGroups (1)
    │   │       │   ├── groups (1)
    │   │       │   │   └── li (3)
    │   │       │   │       ├── label (3) — [text]
    │   │       │   │       ├── map (3) — [text]
    │   │       │   │       ├── members (3)
    │   │       │   │       │   └── li (10) — [text]
    │   │       │   │       ├── settings (3)
    │   │       │   │       │   ├── filter (3)
    │   │       │   │       │   │   ├── allowedDefs (3)
    │   │       │   │       │   │   │   └── li (813) — [text]
    │   │       │   │       │   │   ├── allowedHitPointsPercents (3) — [text]
    │   │       │   │       │   │   ├── allowedMentalBreakChance (3) — [text]
    │   │       │   │       │   │   ├── allowedQualityLevels (3) — [text]
    │   │       │   │       │   │   └── disallowedSpecialFilters (3)
    │   │       │   │       │   │       └── li (9) — [text]
    │   │       │   │       │   ├── priority (3) — [text]
    │   │       │   │       │   └── stackGap (3)
    │   │       │   │       │       └── allowedPerItem (3)
    │   │       │   │       │           ├── keys (3)
    │   │       │   │       │           └── values (3)
    │   │       │   │       └── loadID (2) — [text]
    │   │       │   └── map (1) — [text]
    │   │       ├── storyState (1)
    │   │       │   ├── colonistCountTicks (1)
    │   │       │   │   ├── keys (1)
    │   │       │   │   │   └── li (1) — [text]
    │   │       │   │   └── values (1)
    │   │       │   │       └── li (1) — [text]
    │   │       │   ├── lastFireTicks (1)
    │   │       │   │   ├── keys (1)
    │   │       │   │   │   └── li (23) — [text]
    │   │       │   │   └── values (1)
    │   │       │   │       └── li (23) — [text]
    │   │       │   ├── lastRaidFaction (1) — [text]
    │   │       │   ├── lastRoyalFavorQuestTick (1) — [text]
    │   │       │   ├── lastThreatBigTick (1) — [text]
    │   │       │   ├── recentRandomDecrees (1)
    │   │       │   ├── recentRandomIncidents (1)
    │   │       │   │   └── li (5) — [text]
    │   │       │   └── recentRandomQuests (1)
    │   │       ├── tempTerrain (1)
    │   │       │   ├── cycleIndex (1) — [text]
    │   │       │   ├── freezeManager (1)
    │   │       │   │   └── map (1) — [text]
    │   │       │   ├── terrainToRemoveCells (1)
    │   │       │   └── terrainToRemoveTicks (1)
    │   │       ├── temperatureCache (1)
    │   │       │   └── temperaturesDeflate (1) — [text]
    │   │       ├── temporaryThingDrawer (1)
    │   │       │   └── drawables (1)
    │   │       ├── terrainGrid (1)
    │   │       │   ├── colorGridDeflate (1) — [text]
    │   │       │   ├── foundationGridDeflate (1) — [text]
    │   │       │   ├── tempGridDeflate (1) — [text]
    │   │       │   ├── topGridDeflate (1) — [text]
    │   │       │   └── underGridDeflate (1) — [text]
    │   │       ├── things (1)
    │   │       │   └── thing (9,628) — attrs: [Class]
    │   │       │       ├── def (9,628) — [text]
    │   │       │       ├── despawnedTick (9,628) — [text]
    │   │       │       ├── id (9,628) — [text]
    │   │       │       ├── map (9,628) — [text]
    │   │       │       ├── pos (9,628) — [text]
    │   │       │       ├── questTags (9,628) — attrs: [IsNull]
    │   │       │       ├── spawnedTick (9,623) — [text]
    │   │       │       ├── health (9,299) — [text]
    │   │       │       ├── growth (7,328) — [text]
    │   │       │       ├── age (7,325) — [text]
    │   │       │       ├── unlitTicks (7,295) — [text]
    │   │       │       ├── beenRevealed (1,480) — [text]
    │   │       │       ├── faction (1,033) — [text]
    │   │       │       ├── stuff (797) — [text]
    │   │       │       ├── stackCount (789) — [text]
    │   │       │       ├── everSeenByPlayer (760) — [text]
    │   │       │       ├── sourcePrecept (760) — [text]
    │   │       │       ├── lastUser (645) — [text]
    │   │       │       ├── rot (630) — [text]
    │   │       │       ├── sown (425) — [text]
    │   │       │       ├── parentThing (357) — [text]
    │   │       │       ├── disappearAfterTicks (156) — [text]
    │   │       │       ├── growTick (156) — [text]
    │   │       │       ├── tickDelta (110) — [text]
    │   │       │       ├── verbTracker (98)
    │   │       │       │   └── verbs (98) — attrs: [IsNull]
    │   │       │       │       └── li (251) — attrs: [Class]
    │   │       │       │           ├── MVCF_ManagedVerb (251)
    │   │       │       │           │   ├── enabled (251) — [text]
    │   │       │       │           │   └── loadId (251) — [text]
    │   │       │       │           ├── canHitNonTargetPawnsNow (251) — [text]
    │   │       │       │           ├── lastShotTick (251) — [text]
    │   │       │       │           ├── loadID (251) — [text]
    │   │       │       │           ├── currentTarget (238) — [text]
    │   │       │       │           ├── currentDestination (226) — [text]
    │   │       │       │           └── surpriseAttack (4) — [text]
    │   │       │       ├── huntingPackMaster (81) — [text]
    │   │       │       ├── huntingPackMembers (81)
    │   │       │       ├── newGraphicPath (80) — [text]
    │   │       │       ├── newGraphicSinglePath (80) — [text]
    │   │       │       ├── quality (73) — [text]
    │   │       │       ├── abilities (61) — attrs: [IsNull]
    │   │       │       │   └── abilities (13)
    │   │       │       │       └── li (5)
    │   │       │       │           ├── Id (5) — [text]
    │   │       │       │           ├── charges (5) — [text]
    │   │       │       │           ├── def (5) — [text]
    │   │       │       │           ├── maxCharges (5) — [text]
    │   │       │       │           ├── sourcePrecept (5) — [text]
    │   │       │       │           └── verbTracker (5)
    │   │       │       │               └── verbs (5)
    │   │       │       │                   └── li (5) — attrs: [Class]
    │   │       │       │                       ├── MVCF_ManagedVerb (5) — attrs: [IsNull]
    │   │       │       │                       ├── ability (5) — [text]
    │   │       │       │                       ├── canHitNonTargetPawnsNow (5) — [text]
    │   │       │       │                       ├── currentDestination (5) — [text]
    │   │       │       │                       ├── currentTarget (5) — [text]
    │   │       │       │                       ├── lastShotTick (5) — [text]
    │   │       │       │                       └── loadID (5) — [text]
    │   │       │       ├── MVCF_VerbManager (60) — attrs: [IsNull]
    │   │       │       │   └── currentVerb (57) — [text]
    │   │       │       ├── ThingsHauledToInventory (60)
    │   │       │       ├── ageTracker (60)
    │   │       │       │   ├── ageBiologicalTicks (60) — [text]
    │   │       │       │   ├── ageReversalDemandedAtAgeTicks (60) — [text]
    │   │       │       │   ├── birthAbsTicks (60) — [text]
    │   │       │       │   ├── growth (60) — [text]
    │   │       │       │   ├── nextGrowthCheckTick (60) — [text]
    │   │       │       │   └── initializedAgeReversalDemand (10) — [text]
    │   │       │       ├── apparel (60) — attrs: [IsNull]
    │   │       │       │   ├── lastApparelWearoutTick (11) — [text]
    │   │       │       │   ├── lockedApparel (11)
    │   │       │       │   └── wornApparel (11)
    │   │       │       │       └── innerList (11)
    │   │       │       │           └── li (21)
    │   │       │       │               ├── abilities (21)
    │   │       │       │               ├── def (21) — [text]
    │   │       │       │               ├── despawnedTick (21) — [text]
    │   │       │       │               ├── health (21) — [text]
    │   │       │       │               ├── id (21) — [text]
    │   │       │       │               ├── quality (21) — [text]
    │   │       │       │               ├── questTags (21) — attrs: [IsNull]
    │   │       │       │               ├── sourcePrecept (21) — [text]
    │   │       │       │               ├── stackCount (21) — [text]
    │   │       │       │               ├── everSeenByPlayer (17) — [text]
    │   │       │       │               ├── pos (17) — [text]
    │   │       │       │               ├── stuff (17) — [text]
    │   │       │       │               ├── color (6) — [text]
    │   │       │       │               ├── colorActive (6) — [text]
    │   │       │       │               ├── styleDef (4) — [text]
    │   │       │       │               └── wornByCorpse (2) — [text]
    │   │       │       ├── carryTracker (60)
    │   │       │       │   └── innerContainer (60)
    │   │       │       │       ├── innerList (60)
    │   │       │       │       └── maxStacks (60) — [text]
    │   │       │       ├── connections (60)
    │   │       │       │   └── connectedThings (60)
    │   │       │       ├── creepjoiner (60) — attrs: [IsNull]
    │   │       │       ├── deadlifeDustFaction (60) — [text]
    │   │       │       ├── drafter (60) — attrs: [IsNull]
    │   │       │       │   └── autoUndrafter (7)
    │   │       │       │       └── lastNonWaitingTick (6) — [text]
    │   │       │       ├── drugs (60) — attrs: [IsNull]
    │   │       │       │   ├── curAssignedDrugs (7) — [text]
    │   │       │       │   └── drugTakeRecords (7)
    │   │       │       ├── duplicate (60)
    │   │       │       ├── equipment (60) — attrs: [IsNull]
    │   │       │       │   ├── bondedWeapon (11) — [text]
    │   │       │       │   └── equipment (11)
    │   │       │       │       └── innerList (11)
    │   │       │       │           └── li (7)
    │   │       │       │               ├── def (7) — [text]
    │   │       │       │               ├── despawnedTick (7) — [text]
    │   │       │       │               ├── health (7) — [text]
    │   │       │       │               ├── id (7) — [text]
    │   │       │       │               ├── quality (7) — [text]
    │   │       │       │               ├── questTags (7) — attrs: [IsNull]
    │   │       │       │               ├── sourcePrecept (7) — [text]
    │   │       │       │               ├── stackCount (7) — [text]
    │   │       │       │               ├── taleRef (7) — attrs: [IsNull]
    │   │       │       │               ├── verbTracker (7)
    │   │       │       │               │   └── verbs (7)
    │   │       │       │               │       └── li (26) — attrs: [Class]
    │   │       │       │               │           ├── MVCF_ManagedVerb (26)
    │   │       │       │               │           │   ├── enabled (26) — [text]
    │   │       │       │               │           │   └── loadId (26) — [text]
    │   │       │       │               │           ├── canHitNonTargetPawnsNow (26) — [text]
    │   │       │       │               │           ├── lastShotTick (26) — [text]
    │   │       │       │               │           └── loadID (26) — [text]
    │   │       │       │               ├── everSeenByPlayer (6) — [text]
    │   │       │       │               ├── pos (6) — [text]
    │   │       │       │               ├── codedPawn (3) — [text]
    │   │       │       │               └── stuff (2) — [text]
    │   │       │       ├── filth (60)
    │   │       │       │   ├── carriedFilth (60)
    │   │       │       │   │   └── li (53)
    │   │       │       │   │       ├── def (53) — [text]
    │   │       │       │   │       ├── despawnedTick (53) — [text]
    │   │       │       │   │       ├── id (53) — [text]
    │   │       │       │   │       ├── questTags (53) — attrs: [IsNull]
    │   │       │       │   │       ├── growTick (6) — [text]
    │   │       │       │   │       ├── sources (4)
    │   │       │       │   │       │   └── li (4) — [text]
    │   │       │       │   │       └── thickness (4) — [text]
    │   │       │       │   └── lastTerrainFilthDef (56) — [text]
    │   │       │       ├── flight (60)
    │   │       │       ├── foodRestriction (60) — attrs: [IsNull]
    │   │       │       │   ├── allowedBabyFoodTypes (7) — attrs: [IsNull]
    │   │       │       │   └── curRestriction (7) — [text]
    │   │       │       ├── genes (60) — attrs: [IsNull]
    │   │       │       │   ├── endogenes (7)
    │   │       │       │   │   └── li (14)
    │   │       │       │   │       ├── def (14) — [text]
    │   │       │       │   │       ├── loadID (14) — [text]
    │   │       │       │   │       ├── overriddenByGene (14) — [text]
    │   │       │       │   │       └── pawn (14) — [text]
    │   │       │       │   ├── xenogenes (7)
    │   │       │       │   └── xenotype (7) — [text]
    │   │       │       ├── guest (60) — attrs: [IsNull]
    │   │       │       │   ├── enabledNonExclusiveInteractions (7)
    │   │       │       │   ├── finalResistanceInteractionData (7) — attrs: [IsNull]
    │   │       │       │   ├── hostFaction (7) — [text]
    │   │       │       │   ├── ideoForConversion (7) — [text]
    │   │       │       │   ├── interactionMode (7) — [text]
    │   │       │       │   ├── joinStatus (7) — [text]
    │   │       │       │   ├── lastPrisonBreakTicks (7) — [text]
    │   │       │       │   ├── lastResistanceInteractionData (7) — attrs: [IsNull]
    │   │       │       │   ├── slaveFaction (7) — [text]
    │   │       │       │   ├── slaveInteractionMode (7) — [text]
    │   │       │       │   ├── spotToWaitInsteadOfEscaping (7) — [text]
    │   │       │       │   └── recruitable (2) — [text]
    │   │       │       ├── guilt (60) — attrs: [IsNull]
    │   │       │       ├── healthTracker (60)
    │   │       │       │   ├── hediffSet (60)
    │   │       │       │   │   └── hediffs (60)
    │   │       │       │   │       └── li (15) — attrs: [Class]
    │   │       │       │   │           ├── abilities (15) — attrs: [IsNull]
    │   │       │       │   │           ├── ageTicks (15) — [text]
    │   │       │       │   │           ├── canBeThreateningToPart (15) — [text]
    │   │       │       │   │           ├── combatLogEntry (15) — [text]
    │   │       │       │   │           ├── def (15) — [text]
    │   │       │       │   │           ├── loadID (15) — [text]
    │   │       │       │   │           ├── severity (15) — [text]
    │   │       │       │   │           ├── visible (14) — [text]
    │   │       │       │   │           ├── part (12)
    │   │       │       │   │           │   ├── body (12) — [text]
    │   │       │       │   │           │   └── index (12) — [text]
    │   │       │       │   │           ├── tickAdded (12) — [text]
    │   │       │       │   │           ├── infectionChanceFactor (6) — [text]
    │   │       │       │   │           ├── isPermanent (6) — [text]
    │   │       │       │   │           ├── painCategory (6) — [text]
    │   │       │       │   │           ├── tendTicksLeft (4) — [text]
    │   │       │       │   │           ├── tendQuality (3) — [text]
    │   │       │       │   │           ├── totalTendQuality (3) — [text]
    │   │       │       │   │           ├── combatLogText (2) — [text]
    │   │       │       │   │           ├── destroysBodyParts (1) — [text]
    │   │       │       │   │           ├── lastInjury (1) — [text]
    │   │       │       │   │           ├── nextForcedWorkTickEnd (1) — [text]
    │   │       │       │   │           ├── source (1) — [text]
    │   │       │       │   │           ├── sourceBodyPartGroup (1) — [text]
    │   │       │       │   │           ├── sourceLabel (1) — [text]
    │   │       │       │   │           └── sourceToolLabel (1) — [text]
    │   │       │       │   ├── immunity (60)
    │   │       │       │   │   └── imList (60)
    │   │       │       │   │       └── li (1)
    │   │       │       │   │           ├── hediffDef (1) — [text]
    │   │       │       │   │           ├── immunity (1) — [text]
    │   │       │       │   │           └── source (1) — [text]
    │   │       │       │   ├── surgeryBills (60)
    │   │       │       │   │   └── bills (60)
    │   │       │       │   └── beCarriedByCaravanIfSick (53) — [text]
    │   │       │       ├── ideo (60) — attrs: [IsNull]
    │   │       │       │   ├── babyIdeoExposure (7) — attrs: [IsNull]
    │   │       │       │   ├── certainty (7) — [text]
    │   │       │       │   ├── ideo (7) — [text]
    │   │       │       │   ├── previousIdeos (7)
    │   │       │       │   └── joinTick (1) — [text]
    │   │       │       ├── infectionVectors (60) — attrs: [IsNull]
    │   │       │       │   ├── givenPrearrival (7) — [text]
    │   │       │       │   └── pathways (7)
    │   │       │       │       ├── keys (7)
    │   │       │       │       └── values (7)
    │   │       │       ├── interactions (60) — attrs: [IsNull]
    │   │       │       │   ├── lastInteraction (11) — [text]
    │   │       │       │   ├── lastInteractionDef (11) — [text]
    │   │       │       │   ├── lastInteractionTime (11) — [text]
    │   │       │       │   └── wantsRandomInteract (1) — [text]
    │   │       │       ├── inventory (60)
    │   │       │       │   ├── innerContainer (60)
    │   │       │       │   │   └── innerList (60)
    │   │       │       │   │       └── li (12) — attrs: [Class]
    │   │       │       │   │           ├── def (12) — [text]
    │   │       │       │   │           ├── despawnedTick (12) — [text]
    │   │       │       │   │           ├── health (12) — [text]
    │   │       │       │   │           ├── id (12) — [text]
    │   │       │       │   │           ├── questTags (12) — attrs: [IsNull]
    │   │       │       │   │           ├── stackCount (12) — [text]
    │   │       │       │   │           ├── rotProg (8) — [text]
    │   │       │       │   │           ├── infectedPawns (6)
    │   │       │       │   │           └── ingredients (6)
    │   │       │       │   │               └── li (12) — [text]
    │   │       │       │   ├── itemsNotForSale (60)
    │   │       │       │   └── unpackedCaravanItems (60)
    │   │       │       ├── inventoryStock (60) — attrs: [IsNull]
    │   │       │       │   └── stockEntries (7)
    │   │       │       │       ├── keys (7)
    │   │       │       │       │   └── li (21) — [text]
    │   │       │       │       └── values (7)
    │   │       │       │           └── li (21)
    │   │       │       │               ├── thingDef (21) — [text]
    │   │       │       │               └── count (7) — [text]
    │   │       │       ├── isEnabled (60) — [text]
    │   │       │       ├── jobs (60)
    │   │       │       │   ├── curDriver (60) — attrs: [Class, IsNull]
    │   │       │       │   │   ├── curToilIndex (57) — [text]
    │   │       │       │   │   ├── locomotionUrgencySameAs (57) — [text]
    │   │       │       │   │   ├── startTick (57) — [text]
    │   │       │       │   │   ├── ticksLeftThisToil (57) — [text]
    │   │       │       │   │   ├── canMoveOrCrawl (52) — [text]
    │   │       │       │   │   ├── hasSavedValues (52) — [text]
    │   │       │       │   │   └── asleep (51) — [text]
    │   │       │       │   ├── curJob (60) — attrs: [IsNull]
    │   │       │       │   │   ├── ability (57) — [text]
    │   │       │       │   │   ├── bill (57) — [text]
    │   │       │       │   │   ├── commTarget (57) — [text]
    │   │       │       │   │   ├── countQueue (57) — attrs: [IsNull]
    │   │       │       │   │   │   └── li (2) — [text]
    │   │       │       │   │   ├── def (57) — [text]
    │   │       │       │   │   ├── interactableIndex (57) — [text]
    │   │       │       │   │   ├── jobGiverThinkTree (57) — [text]
    │   │       │       │   │   ├── lastJobGiverKey (57) — [text]
    │   │       │       │   │   ├── loadID (57) — [text]
    │   │       │       │   │   ├── lord (57) — [text]
    │   │       │       │   │   ├── placedThings (57) — attrs: [IsNull]
    │   │       │       │   │   ├── psyfocusTargetLast (57) — [text]
    │   │       │       │   │   ├── quest (57) — [text]
    │   │       │       │   │   ├── source (57) — [text]
    │   │       │       │   │   ├── startTick (57) — [text]
    │   │       │       │   │   ├── targetQueueA (57) — attrs: [IsNull]
    │   │       │       │   │   │   └── li (2) — [text]
    │   │       │       │   │   ├── targetQueueB (57) — attrs: [IsNull]
    │   │       │       │   │   ├── verbToUse (57) — [text]
    │   │       │       │   │   ├── targetA (54) — [text]
    │   │       │       │   │   ├── expiryInterval (3) — [text]
    │   │       │       │   │   ├── checkOverrideOnExpire (1) — [text]
    │   │       │       │   │   ├── count (1) — [text]
    │   │       │       │   │   ├── locomotionUrgency (1) — [text]
    │   │       │       │   │   ├── targetB (1) — [text]
    │   │       │       │   │   └── workGiverDef (1) — [text]
    │   │       │       │   ├── formingCaravanTick (60) — [text]
    │   │       │       │   ├── jobQueue (60)
    │   │       │       │   │   └── jobs (60)
    │   │       │       │   └── posture (52) — [text]
    │   │       │       ├── kindDef (60) — [text]
    │   │       │       ├── learning (60) — attrs: [IsNull]
    │   │       │       ├── loadouts (60)
    │   │       │       │   └── curLoadout (60) — [text]
    │   │       │       ├── mechanitor (60) — attrs: [IsNull]
    │   │       │       ├── meleeVerbs (60)
    │   │       │       │   ├── curMeleeVerb (60) — [text]
    │   │       │       │   ├── terrainVerbs (60) — attrs: [IsNull]
    │   │       │       │   │   ├── def (10) — [text]
    │   │       │       │   │   └── tracker (10)
    │   │       │       │   │       └── verbs (10)
    │   │       │       │   │           └── li (8) — attrs: [Class]
    │   │       │       │   │               ├── MVCF_ManagedVerb (8) — attrs: [IsNull]
    │   │       │       │   │               ├── canHitNonTargetPawnsNow (8) — [text]
    │   │       │       │   │               ├── lastShotTick (8) — [text]
    │   │       │       │   │               ├── loadID (8) — [text]
    │   │       │       │   │               ├── currentDestination (6) — [text]
    │   │       │       │   │               ├── currentTarget (6) — [text]
    │   │       │       │   │               └── surpriseAttack (1) — [text]
    │   │       │       │   ├── curMeleeVerbUpdateTick (57) — [text]
    │   │       │       │   └── lastTerrainBasedVerbUseTick (3) — [text]
    │   │       │       ├── mindState (60)
    │   │       │       │   ├── babyAutoBreastfeedMoms (60)
    │   │       │       │   │   ├── keys (60)
    │   │       │       │   │   └── values (60)
    │   │       │       │   ├── babyCaravanBreastfeed (60)
    │   │       │       │   │   ├── keys (60)
    │   │       │       │   │   └── values (60)
    │   │       │       │   ├── breachingTarget (60) — attrs: [IsNull]
    │   │       │       │   ├── canFleeIndividual (60) — [text]
    │   │       │       │   ├── droppedWeapon (60) — [text]
    │   │       │       │   ├── duty (60) — attrs: [IsNull]
    │   │       │       │   ├── enemyTarget (60) — [text]
    │   │       │       │   ├── inspirationHandler (60)
    │   │       │       │   │   └── curState (60) — attrs: [IsNull]
    │   │       │       │   ├── knownExploder (60) — [text]
    │   │       │       │   ├── lastAttackTargetTick (60) — [text]
    │   │       │       │   ├── lastDayInteractionTick (60) — [text]
    │   │       │       │   ├── lastEngageTargetTick (60) — [text]
    │   │       │       │   ├── lastMannedThing (60) — [text]
    │   │       │       │   ├── lastMeleeThreatHarmTick (60) — [text]
    │   │       │       │   ├── lastSelfTendTick (60) — [text]
    │   │       │       │   ├── meleeThreat (60) — [text]
    │   │       │       │   ├── mentalBreaker (60)
    │   │       │       │   │   ├── ticksBelowMinor (3) — [text]
    │   │       │       │   │   ├── ticksUntilCanDoMentalBreak (3) — [text]
    │   │       │       │   │   └── ticksBelowMajor (2) — [text]
    │   │       │       │   ├── mentalFitGenerator (60)
    │   │       │       │   │   └── ticksUntilCanDoMentalFit (1) — [text]
    │   │       │       │   ├── mentalStateHandler (60)
    │   │       │       │   │   └── curState (60) — attrs: [IsNull]
    │   │       │       │   ├── priorityWork (60)
    │   │       │       │   │   ├── prioritizedCell (60) — [text]
    │   │       │       │   │   └── prioritizeTick (46) — [text]
    │   │       │       │   ├── resurrectTarget (60) — attrs: [IsNull]
    │   │       │       │   ├── thinkData (60)
    │   │       │       │   │   ├── keys (60)
    │   │       │       │   │   │   └── li (219) — [text]
    │   │       │       │   │   └── values (60)
    │   │       │       │   │       └── li (219) — [text]
    │   │       │       │   ├── lastJobTag (57) — [text]
    │   │       │       │   ├── applyBedThoughtsOnLeave (56) — [text]
    │   │       │       │   ├── lastRangedHarmTick (56) — [text]
    │   │       │       │   ├── lastIngestTick (55) — [text]
    │   │       │       │   ├── lastAttackedTarget (53) — [text]
    │   │       │       │   ├── applyBedThoughtsTick (52) — [text]
    │   │       │       │   ├── nextMoveOrderIsWait (39) — [text]
    │   │       │       │   ├── canSleepTick (21) — [text]
    │   │       │       │   ├── lastCombatantTick (10) — [text]
    │   │       │       │   ├── lastBedDefSleptIn (8) — [text]
    │   │       │       │   ├── lastHarmTick (8) — [text]
    │   │       │       │   ├── lastSwamTick (7) — [text]
    │   │       │       │   ├── nextApparelOptimizeTick (7) — [text]
    │   │       │       │   ├── lastRotStinkTick (5) — [text]
    │   │       │       │   ├── active (3) — [text]
    │   │       │       │   ├── lastAssignedInteractTime (2) — [text]
    │   │       │       │   ├── lastInventoryRawFoodUseTick (2) — [text]
    │   │       │       │   ├── nextInventoryStockTick (2) — [text]
    │   │       │       │   └── lastDisturbanceTick (1) — [text]
    │   │       │       ├── name (60) — attrs: [Class, IsNull]
    │   │       │       │   ├── first (7) — [text]
    │   │       │       │   ├── last (7) — [text]
    │   │       │       │   ├── nick (6) — [text]
    │   │       │       │   ├── name (3) — [text]
    │   │       │       │   └── numerical (2) — [text]
    │   │       │       ├── natives (60)
    │   │       │       │   └── verbTracker (60)
    │   │       │       │       └── verbs (60) — attrs: [IsNull]
    │   │       │       ├── needs (60)
    │   │       │       │   └── needs (60)
    │   │       │       │       └── li (182) — attrs: [Class]
    │   │       │       │           ├── def (182) — [text]
    │   │       │       │           ├── curLevel (174) — [text]
    │   │       │       │           ├── lastNonStarvingTick (56) — [text]
    │   │       │       │           ├── bored (7)
    │   │       │       │           │   └── vals (7)
    │   │       │       │           │       └── li (91) — [text]
    │   │       │       │           ├── recentMemory (7)
    │   │       │       │           │   ├── lastLightTick (7) — [text]
    │   │       │       │           │   └── lastOutdoorTick (7) — [text]
    │   │       │       │           ├── thoughts (7)
    │   │       │       │           │   └── memories (7)
    │   │       │       │           │       └── memories (7)
    │   │       │       │           │           └── li (187) — attrs: [Class]
    │   │       │       │           │               ├── age (187) — [text]
    │   │       │       │           │               ├── def (187) — [text]
    │   │       │       │           │               ├── durationTicksOverride (187) — [text]
    │   │       │       │           │               ├── otherPawn (187) — [text]
    │   │       │       │           │               ├── sourcePrecept (187) — [text]
    │   │       │       │           │               ├── opinionOffset (135) — [text]
    │   │       │       │           │               ├── moodPowerFactor (96) — [text]
    │   │       │       │           │               └── stageIndex (17) — [text]
    │   │       │       │           └── tolerances (7)
    │   │       │       │               └── vals (7)
    │   │       │       │                   └── li (91) — [text]
    │   │       │       ├── outfits (60) — attrs: [IsNull]
    │   │       │       │   ├── curOutfit (7) — [text]
    │   │       │       │   └── overrideHandler (7)
    │   │       │       │       └── forcedAps (7)
    │   │       │       ├── ownership (60)
    │   │       │       │   ├── assignedDeathrestCasket (60) — [text]
    │   │       │       │   ├── assignedGrave (60) — [text]
    │   │       │       │   ├── assignedMeditationSpot (60) — [text]
    │   │       │       │   ├── assignedThrone (60) — [text]
    │   │       │       │   └── ownedBed (60) — [text]
    │   │       │       ├── pather (60)
    │   │       │       │   ├── lastEnteredCellTick (60) — [text]
    │   │       │       │   ├── nextCell (60) — [text]
    │   │       │       │   ├── nextCellCostInitial (60) — [text]
    │   │       │       │   ├── moving (58) — [text]
    │   │       │       │   ├── lastMovedTick (57) — [text]
    │   │       │       │   ├── peMode (57) — [text]
    │   │       │       │   ├── cellsUntilClamor (7) — [text]
    │   │       │       │   ├── destination (2) — [text]
    │   │       │       │   └── nextCellCostLeft (2) — [text]
    │   │       │       ├── playerSettings (60) — attrs: [IsNull]
    │   │       │       │   ├── allowedAreas (10)
    │   │       │       │   │   ├── keys (10)
    │   │       │       │   │   │   └── li (3) — [text]
    │   │       │       │   │   └── values (10)
    │   │       │       │   │       └── li (3) — [text]
    │   │       │       │   ├── displayOrder (10) — [text]
    │   │       │       │   ├── master (10) — [text]
    │   │       │       │   ├── medCare (10) — [text]
    │   │       │       │   ├── selfTend (5) — [text]
    │   │       │       │   └── joinTick (3) — [text]
    │   │       │       ├── psychicEntropy (60) — attrs: [IsNull]
    │   │       │       │   ├── limitEntropyAmount (59) — [text]
    │   │       │       │   └── currentPsyfocus (32) — [text]
    │   │       │       ├── reading (60) — attrs: [IsNull]
    │   │       │       │   └── curAssignment (7) — [text]
    │   │       │       ├── records (60)
    │   │       │       │   ├── battleActive (60) — [text]
    │   │       │       │   ├── records (60)
    │   │       │       │   │   └── vals (60)
    │   │       │       │   │       └── li (4,320) — [text]
    │   │       │       │   └── battleExitTick (10) — [text]
    │   │       │       ├── roping (60)
    │   │       │       │   ├── hitchingPostInt (60) — [text]
    │   │       │       │   └── ropees (60)
    │   │       │       ├── rotationTracker (60)
    │   │       │       ├── royalty (60) — attrs: [IsNull]
    │   │       │       │   ├── abilities (7)
    │   │       │       │   ├── favor (7)
    │   │       │       │   │   ├── keys (7)
    │   │       │       │   │   └── values (7)
    │   │       │       │   ├── heirs (7)
    │   │       │       │   │   ├── keys (7)
    │   │       │       │   │   └── values (7)
    │   │       │       │   ├── highestTitles (7)
    │   │       │       │   │   ├── keys (7)
    │   │       │       │   │   └── values (7)
    │   │       │       │   ├── permits (7)
    │   │       │       │   └── titles (7)
    │   │       │       ├── shambler (60) — attrs: [IsNull]
    │   │       │       ├── skills (60) — attrs: [IsNull]
    │   │       │       │   ├── lastXpSinceMidnightResetTimestamp (8) — [text]
    │   │       │       │   └── skills (8)
    │   │       │       │       └── li (96)
    │   │       │       │           ├── def (96) — [text]
    │   │       │       │           ├── level (90) — [text]
    │   │       │       │           ├── xpSinceLastLevel (71) — [text]
    │   │       │       │           ├── passion (29) — [text]
    │   │       │       │           └── xpSinceMidnight (19) — [text]
    │   │       │       ├── social (60) — attrs: [IsNull]
    │   │       │       │   ├── additionalPregnancyApproachData (59)
    │   │       │       │   │   └── partners (59)
    │   │       │       │   │       ├── keys (59)
    │   │       │       │   │       └── values (59)
    │   │       │       │   ├── directRelations (59)
    │   │       │       │   │   └── li (7)
    │   │       │       │   │       ├── def (7) — [text]
    │   │       │       │   │       └── otherPawn (7) — [text]
    │   │       │       │   ├── pregnancyApproaches (59)
    │   │       │       │   │   ├── keys (59)
    │   │       │       │   │   └── values (59)
    │   │       │       │   ├── relativeInvolvedInRescueQuest (59) — [text]
    │   │       │       │   ├── romanceEnableTick (59) — [text]
    │   │       │       │   ├── virtualRelations (59)
    │   │       │       │   │   └── li (2)
    │   │       │       │   │       ├── def (2) — [text]
    │   │       │       │   │       └── record (2) — [text]
    │   │       │       │   └── canGetRescuedThought (1) — [text]
    │   │       │       ├── stances (60)
    │   │       │       │   ├── curStance (60) — attrs: [Class]
    │   │       │       │   ├── stagger (60)
    │   │       │       │   │   └── staggerMoveSpeedFactor (9) — [text]
    │   │       │       │   ├── stunner (60)
    │   │       │       │   │   ├── adaptationTicksLeft (60)
    │   │       │       │   │   │   ├── keys (60)
    │   │       │       │   │   │   └── values (60)
    │   │       │       │   │   └── showStunMote (60) — [text]
    │   │       │       │   └── lastTickFullBodyBusy (15) — [text]
    │   │       │       ├── story (60) — attrs: [IsNull]
    │   │       │       │   ├── bodyType (8) — [text]
    │   │       │       │   ├── hairColor (8) — [text]
    │   │       │       │   ├── hairDef (8) — [text]
    │   │       │       │   ├── headType (8) — [text]
    │   │       │       │   ├── traits (8)
    │   │       │       │   │   └── allTraits (8)
    │   │       │       │   │       └── li (20)
    │   │       │       │   │           ├── def (20) — [text]
    │   │       │       │   │           ├── sourceGene (20) — [text]
    │   │       │       │   │           ├── suppressedBy (20) — [text]
    │   │       │       │   │           └── degree (3) — [text]
    │   │       │       │   ├── adulthood (7) — [text]
    │   │       │       │   ├── birthLastName (7) — [text]
    │   │       │       │   ├── childhood (7) — [text]
    │   │       │       │   └── favoriteColorDef (7) — [text]
    │   │       │       ├── style (60) — attrs: [IsNull]
    │   │       │       │   ├── beardDef (7) — [text]
    │   │       │       │   ├── bodyTattoo (7) — [text]
    │   │       │       │   └── faceTattoo (7) — [text]
    │   │       │       ├── styleObserver (60) — attrs: [IsNull]
    │   │       │       ├── thinker (60) — attrs: [Class]
    │   │       │       ├── timetable (60) — attrs: [IsNull]
    │   │       │       │   └── times (7)
    │   │       │       │       └── li (168) — [text]
    │   │       │       ├── trader (60) — attrs: [IsNull]
    │   │       │       ├── training (60) — attrs: [IsNull]
    │   │       │       │   ├── attackTarget (6) — [text]
    │   │       │       │   ├── countDecayFrom (6) — [text]
    │   │       │       │   ├── learned (6)
    │   │       │       │   │   └── vals (6)
    │   │       │       │   │       └── li (138) — [text]
    │   │       │       │   ├── steps (6)
    │   │       │       │   │   └── vals (6)
    │   │       │       │   │       └── li (138) — [text]
    │   │       │       │   └── wantedTrainables (6)
    │   │       │       │       └── vals (6)
    │   │       │       │           └── li (138) — [text]
    │   │       │       ├── treeSightings (60) — attrs: [IsNull]
    │   │       │       │   ├── fullTreeSightings (7)
    │   │       │       │   ├── miniTreeSightings (7)
    │   │       │       │   └── superTreeSightings (7)
    │   │       │       ├── vfee_honors (60)
    │   │       │       │   ├── honors (60)
    │   │       │       │   └── pendingHonors (60)
    │   │       │       ├── workSettings (60) — attrs: [IsNull]
    │   │       │       │   └── priorities (8)
    │   │       │       │       └── vals (8)
    │   │       │       │           └── li (416) — [text]
    │   │       │       ├── lastStudiedTick (59) — [text]
    │   │       │       ├── targetHolder (59) — [text]
    │   │       │       ├── innerContainer (50) — attrs: [Class]
    │   │       │       │   ├── innerList (50)
    │   │       │       │   │   └── li (45) — attrs: [Class]
    │   │       │       │   │       ├── def (9) — [text]
    │   │       │       │   │       ├── despawnedTick (9) — [text]
    │   │       │       │   │       ├── id (9) — [text]
    │   │       │       │   │       ├── questTags (9) — attrs: [IsNull]
    │   │       │       │   │       ├── verbTracker (7)
    │   │       │       │   │       │   └── verbs (7) — attrs: [IsNull]
    │   │       │       │   │       │       └── li (24) — attrs: [Class]
    │   │       │       │   │       │           ├── MVCF_ManagedVerb (24)
    │   │       │       │   │       │           │   ├── enabled (24) — [text]
    │   │       │       │   │       │           │   └── loadId (24) — [text]
    │   │       │       │   │       │           ├── canHitNonTargetPawnsNow (24) — [text]
    │   │       │       │   │       │           ├── currentDestination (24) — [text]
    │   │       │       │   │       │           ├── currentTarget (24) — [text]
    │   │       │       │   │       │           ├── lastShotTick (24) — [text]
    │   │       │       │   │       │           └── loadID (24) — [text]
    │   │       │       │   │       ├── MVCF_VerbManager (6) — attrs: [IsNull]
    │   │       │       │   │       ├── ThingsHauledToInventory (6)
    │   │       │       │   │       ├── abilities (6)
    │   │       │       │   │       │   └── abilities (6)
    │   │       │       │   │       ├── ageTracker (6)
    │   │       │       │   │       │   ├── ageBiologicalTicks (6) — [text]
    │   │       │       │   │       │   ├── ageReversalDemandedAtAgeTicks (6) — [text]
    │   │       │       │   │       │   ├── birthAbsTicks (6) — [text]
    │   │       │       │   │       │   ├── growth (6) — [text]
    │   │       │       │   │       │   ├── lifeStageChange (6) — [text]
    │   │       │       │   │       │   └── nextGrowthCheckTick (6) — [text]
    │   │       │       │   │       ├── apparel (6)
    │   │       │       │   │       │   ├── lastApparelWearoutTick (6) — [text]
    │   │       │       │   │       │   ├── lockedApparel (6)
    │   │       │       │   │       │   └── wornApparel (6)
    │   │       │       │   │       │       └── innerList (6)
    │   │       │       │   │       │           └── li (22) — attrs: [Class]
    │   │       │       │   │       │               ├── abilities (22)
    │   │       │       │   │       │               ├── def (22) — [text]
    │   │       │       │   │       │               ├── despawnedTick (22) — [text]
    │   │       │       │   │       │               ├── health (22) — [text]
    │   │       │       │   │       │               ├── id (22) — [text]
    │   │       │       │   │       │               ├── questTags (22) — attrs: [IsNull]
    │   │       │       │   │       │               ├── stackCount (22) — [text]
    │   │       │       │   │       │               ├── quality (21) — [text]
    │   │       │       │   │       │               ├── sourcePrecept (21) — [text]
    │   │       │       │   │       │               ├── color (12) — [text]
    │   │       │       │   │       │               ├── colorActive (12) — [text]
    │   │       │       │   │       │               ├── stuff (9) — [text]
    │   │       │       │   │       │               ├── codedPawn (3) — [text]
    │   │       │       │   │       │               ├── remainingCharges (1) — [text]
    │   │       │       │   │       │               ├── tickDelta (1) — [text]
    │   │       │       │   │       │               └── verbTracker (1)
    │   │       │       │   │       │                   └── verbs (1)
    │   │       │       │   │       │                       └── li (1) — attrs: [Class]
    │   │       │       │   │       │                           ├── MVCF_ManagedVerb (1) — attrs: [IsNull]
    │   │       │       │   │       │                           ├── canHitNonTargetPawnsNow (1) — [text]
    │   │       │       │   │       │                           ├── lastShotTick (1) — [text]
    │   │       │       │   │       │                           └── loadID (1) — [text]
    │   │       │       │   │       ├── bed (6) — [text]
    │   │       │       │   │       ├── boughtItems (6)
    │   │       │       │   │       ├── carryTracker (6)
    │   │       │       │   │       │   └── innerContainer (6)
    │   │       │       │   │       │       ├── innerList (6)
    │   │       │       │   │       │       └── maxStacks (6) — [text]
    │   │       │       │   │       ├── connections (6)
    │   │       │       │   │       │   └── connectedThings (6)
    │   │       │       │   │       ├── creepjoiner (6) — attrs: [IsNull]
    │   │       │       │   │       ├── currentlyCasting (6) — [text]
    │   │       │       │   │       ├── currentlyCastingTargets (6)
    │   │       │       │   │       ├── deadlifeDustFaction (6) — [text]
    │   │       │       │   │       ├── drafter (6) — attrs: [IsNull]
    │   │       │       │   │       ├── drugs (6) — attrs: [IsNull]
    │   │       │       │   │       ├── duplicate (6)
    │   │       │       │   │       ├── equipment (6)
    │   │       │       │   │       │   ├── bondedWeapon (6) — [text]
    │   │       │       │   │       │   └── equipment (6)
    │   │       │       │   │       │       └── innerList (6)
    │   │       │       │   │       │           └── li (6)
    │   │       │       │   │       │               ├── def (6) — [text]
    │   │       │       │   │       │               ├── despawnedTick (6) — [text]
    │   │       │       │   │       │               ├── health (6) — [text]
    │   │       │       │   │       │               ├── id (6) — [text]
    │   │       │       │   │       │               ├── quality (6) — [text]
    │   │       │       │   │       │               ├── questTags (6) — attrs: [IsNull]
    │   │       │       │   │       │               ├── sourcePrecept (6) — [text]
    │   │       │       │   │       │               ├── stackCount (6) — [text]
    │   │       │       │   │       │               ├── taleRef (6) — attrs: [IsNull]
    │   │       │       │   │       │               ├── verbTracker (6)
    │   │       │       │   │       │               │   └── verbs (6)
    │   │       │       │   │       │               │       └── li (22) — attrs: [Class]
    │   │       │       │   │       │               │           ├── MVCF_ManagedVerb (22)
    │   │       │       │   │       │               │           │   ├── enabled (22) — [text]
    │   │       │       │   │       │               │           │   └── loadId (22) — [text]
    │   │       │       │   │       │               │           ├── canHitNonTargetPawnsNow (22) — [text]
    │   │       │       │   │       │               │           ├── lastShotTick (22) — [text]
    │   │       │       │   │       │               │           └── loadID (22) — [text]
    │   │       │       │   │       │               ├── codedPawn (3) — [text]
    │   │       │       │   │       │               ├── innerContainer (2) — attrs: [Class]
    │   │       │       │   │       │               │   └── innerList (2)
    │   │       │       │   │       │               ├── biocoded (1) — [text]
    │   │       │       │   │       │               └── biocodedPawnLabel (1) — [text]
    │   │       │       │   │       ├── faction (6) — [text]
    │   │       │       │   │       ├── filth (6) — attrs: [IsNull]
    │   │       │       │   │       ├── flight (6) — attrs: [IsNull]
    │   │       │       │   │       ├── foodRestriction (6) — attrs: [IsNull]
    │   │       │       │   │       ├── genes (6)
    │   │       │       │   │       │   ├── endogenes (6)
    │   │       │       │   │       │   │   └── li (12)
    │   │       │       │   │       │   │       ├── def (12) — [text]
    │   │       │       │   │       │   │       ├── loadID (12) — [text]
    │   │       │       │   │       │   │       ├── overriddenByGene (12) — [text]
    │   │       │       │   │       │   │       └── pawn (12) — [text]
    │   │       │       │   │       │   ├── xenogenes (6)
    │   │       │       │   │       │   └── xenotype (6) — [text]
    │   │       │       │   │       ├── guest (6)
    │   │       │       │   │       │   ├── enabledNonExclusiveInteractions (6)
    │   │       │       │   │       │   ├── finalResistanceInteractionData (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── hostFaction (6) — [text]
    │   │       │       │   │       │   ├── ideoForConversion (6) — [text]
    │   │       │       │   │       │   ├── interactionMode (6) — [text]
    │   │       │       │   │       │   ├── joinStatus (6) — [text]
    │   │       │       │   │       │   ├── lastPrisonBreakTicks (6) — [text]
    │   │       │       │   │       │   ├── lastResistanceInteractionData (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── slaveFaction (6) — [text]
    │   │       │       │   │       │   ├── slaveInteractionMode (6) — [text]
    │   │       │       │   │       │   └── spotToWaitInsteadOfEscaping (6) — [text]
    │   │       │       │   │       ├── guestArea (6) — [text]
    │   │       │       │   │       ├── guilt (6)
    │   │       │       │   │       ├── healthTracker (6)
    │   │       │       │   │       │   ├── hediffSet (6)
    │   │       │       │   │       │   │   └── hediffs (6)
    │   │       │       │   │       │   │       └── li (10) — attrs: [Class]
    │   │       │       │   │       │   │           ├── abilities (10) — attrs: [IsNull]
    │   │       │       │   │       │   │           ├── canBeThreateningToPart (10) — [text]
    │   │       │       │   │       │   │           ├── combatLogEntry (10) — [text]
    │   │       │       │   │       │   │           ├── def (10) — [text]
    │   │       │       │   │       │   │           ├── loadID (10) — [text]
    │   │       │       │   │       │   │           ├── severity (10) — [text]
    │   │       │       │   │       │   │           ├── part (9)
    │   │       │       │   │       │   │           │   ├── body (9) — [text]
    │   │       │       │   │       │   │           │   └── index (9) — [text]
    │   │       │       │   │       │   │           ├── lastInjury (5) — [text]
    │   │       │       │   │       │   │           ├── infectionChanceFactor (2) — [text]
    │   │       │       │   │       │   │           ├── isPermanent (2) — [text]
    │   │       │       │   │       │   │           └── painCategory (1) — [text]
    │   │       │       │   │       │   ├── immunity (6)
    │   │       │       │   │       │   │   └── imList (6)
    │   │       │       │   │       │   └── surgeryBills (6)
    │   │       │       │   │       │       └── bills (6)
    │   │       │       │   │       ├── ideo (6)
    │   │       │       │   │       │   ├── babyIdeoExposure (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── certainty (6) — [text]
    │   │       │       │   │       │   ├── ideo (6) — [text]
    │   │       │       │   │       │   └── previousIdeos (6)
    │   │       │       │   │       ├── infectionVectors (6)
    │   │       │       │   │       │   └── pathways (6)
    │   │       │       │   │       │       ├── keys (6)
    │   │       │       │   │       │       └── values (6)
    │   │       │       │   │       ├── interactions (6) — attrs: [IsNull]
    │   │       │       │   │       ├── inventory (6)
    │   │       │       │   │       │   ├── innerContainer (6)
    │   │       │       │   │       │   │   └── innerList (6)
    │   │       │       │   │       │   │       └── li (12) — attrs: [Class]
    │   │       │       │   │       │   │           ├── def (12) — [text]
    │   │       │       │   │       │   │           ├── despawnedTick (12) — [text]
    │   │       │       │   │       │   │           ├── id (12) — [text]
    │   │       │       │   │       │   │           ├── questTags (12) — attrs: [IsNull]
    │   │       │       │   │       │   │           ├── stackCount (12) — [text]
    │   │       │       │   │       │   │           ├── health (6) — [text]
    │   │       │       │   │       │   │           └── sourcePrecept (4) — [text]
    │   │       │       │   │       │   ├── itemsNotForSale (6)
    │   │       │       │   │       │   └── unpackedCaravanItems (6)
    │   │       │       │   │       ├── inventoryStock (6) — attrs: [IsNull]
    │   │       │       │   │       ├── isEnabled (6) — [text]
    │   │       │       │   │       ├── jobs (6)
    │   │       │       │   │       │   ├── curDriver (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── curJob (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── formingCaravanTick (6) — [text]
    │   │       │       │   │       │   └── jobQueue (6)
    │   │       │       │   │       │       └── jobs (6)
    │   │       │       │   │       ├── kindDef (6) — [text]
    │   │       │       │   │       ├── lastKeepDisplayTick (6) — [text]
    │   │       │       │   │       ├── lastStudiedTick (6) — [text]
    │   │       │       │   │       ├── learnedAbilities (6)
    │   │       │       │   │       ├── learning (6) — attrs: [IsNull]
    │   │       │       │   │       ├── loadouts (6)
    │   │       │       │   │       │   └── curLoadout (6) — [text]
    │   │       │       │   │       ├── lord (6) — [text]
    │   │       │       │   │       ├── mechanitor (6) — attrs: [IsNull]
    │   │       │       │   │       ├── meleeVerbs (6)
    │   │       │       │   │       │   ├── curMeleeVerb (6) — [text]
    │   │       │       │   │       │   └── terrainVerbs (6) — attrs: [IsNull]
    │   │       │       │   │       ├── mindState (6)
    │   │       │       │   │       │   ├── babyAutoBreastfeedMoms (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── babyCaravanBreastfeed (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── breachingTarget (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── canFleeIndividual (6) — [text]
    │   │       │       │   │       │   ├── droppedWeapon (6) — [text]
    │   │       │       │   │       │   ├── duty (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── enemyTarget (6) — [text]
    │   │       │       │   │       │   ├── inspirationHandler (6)
    │   │       │       │   │       │   │   └── curState (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── knownExploder (6) — [text]
    │   │       │       │   │       │   ├── lastAttackTargetTick (6) — [text]
    │   │       │       │   │       │   ├── lastAttackedTarget (6) — [text]
    │   │       │       │   │       │   ├── lastEngageTargetTick (6) — [text]
    │   │       │       │   │       │   ├── lastMannedThing (6) — [text]
    │   │       │       │   │       │   ├── lastMeleeThreatHarmTick (6) — [text]
    │   │       │       │   │       │   ├── lastRangedHarmTick (6) — [text]
    │   │       │       │   │       │   ├── lastSelfTendTick (6) — [text]
    │   │       │       │   │       │   ├── meleeThreat (6) — [text]
    │   │       │       │   │       │   ├── mentalBreaker (6)
    │   │       │       │   │       │   ├── mentalFitGenerator (6)
    │   │       │       │   │       │   ├── mentalStateHandler (6)
    │   │       │       │   │       │   │   └── curState (6) — attrs: [IsNull]
    │   │       │       │   │       │   ├── nextMoveOrderIsWait (6) — [text]
    │   │       │       │   │       │   ├── priorityWork (6)
    │   │       │       │   │       │   │   └── prioritizedCell (6) — [text]
    │   │       │       │   │       │   ├── resurrectTarget (6) — attrs: [IsNull]
    │   │       │       │   │       │   └── thinkData (6)
    │   │       │       │   │       │       ├── keys (6)
    │   │       │       │   │       │       └── values (6)
    │   │       │       │   │       ├── name (6) — attrs: [Class]
    │   │       │       │   │       │   ├── first (6) — [text]
    │   │       │       │   │       │   ├── last (6) — [text]
    │   │       │       │   │       │   └── nick (6) — [text]
    │   │       │       │   │       ├── natives (6) — attrs: [IsNull]
    │   │       │       │   │       ├── needs (6)
    │   │       │       │   │       │   └── needs (6)
    │   │       │       │   │       │       └── li (18) — attrs: [Class]
    │   │       │       │   │       │           ├── curLevel (18) — [text]
    │   │       │       │   │       │           ├── def (18) — [text]
    │   │       │       │   │       │           ├── lastNonStarvingTick (6) — [text]
    │   │       │       │   │       │           ├── recentMemory (6)
    │   │       │       │   │       │           └── thoughts (6)
    │   │       │       │   │       │               └── memories (6)
    │   │       │       │   │       │                   └── memories (6)
    │   │       │       │   │       ├── outfits (6) — attrs: [IsNull]
    │   │       │       │   │       ├── ownership (6)
    │   │       │       │   │       │   ├── assignedDeathrestCasket (6) — [text]
    │   │       │       │   │       │   ├── assignedGrave (6) — [text]
    │   │       │       │   │       │   ├── assignedMeditationSpot (6) — [text]
    │   │       │       │   │       │   ├── assignedThrone (6) — [text]
    │   │       │       │   │       │   └── ownedBed (6) — [text]
    │   │       │       │   │       ├── pather (6) — attrs: [IsNull]
    │   │       │       │   │       ├── playerSettings (6) — attrs: [IsNull]
    │   │       │       │   │       ├── psychicEntropy (6)
    │   │       │       │   │       │   ├── currentPsyfocus (6) — [text]
    │   │       │       │   │       │   └── limitEntropyAmount (6) — [text]
    │   │       │       │   │       ├── reading (6) — attrs: [IsNull]
    │   │       │       │   │       ├── records (6)
    │   │       │       │   │       │   ├── battleActive (6) — [text]
    │   │       │       │   │       │   └── records (6)
    │   │       │       │   │       │       └── vals (6)
    │   │       │       │   │       │           └── li (432) — [text]
    │   │       │       │   │       ├── roping (6) — attrs: [IsNull]
    │   │       │       │   │       ├── rotationTracker (6) — attrs: [IsNull]
    │   │       │       │   │       ├── royalty (6)
    │   │       │       │   │       │   ├── abilities (6)
    │   │       │       │   │       │   ├── favor (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── heirs (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── highestTitles (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── permits (6)
    │   │       │       │   │       │   └── titles (6)
    │   │       │       │   │       ├── shambler (6) — attrs: [IsNull]
    │   │       │       │   │       ├── shoppingArea (6) — [text]
    │   │       │       │   │       ├── skills (6)
    │   │       │       │   │       │   ├── lastXpSinceMidnightResetTimestamp (6) — [text]
    │   │       │       │   │       │   └── skills (6)
    │   │       │       │   │       │       └── li (72)
    │   │       │       │   │       │           ├── def (72) — [text]
    │   │       │       │   │       │           ├── level (59) — [text]
    │   │       │       │   │       │           └── passion (23) — [text]
    │   │       │       │   │       ├── social (6)
    │   │       │       │   │       │   ├── additionalPregnancyApproachData (6)
    │   │       │       │   │       │   │   └── partners (6)
    │   │       │       │   │       │   │       ├── keys (6)
    │   │       │       │   │       │   │       └── values (6)
    │   │       │       │   │       │   ├── directRelations (6)
    │   │       │       │   │       │   │   └── li (2)
    │   │       │       │   │       │   │       ├── def (2) — [text]
    │   │       │       │   │       │   │       ├── otherPawn (2) — [text]
    │   │       │       │   │       │   │       └── startTicks (1) — [text]
    │   │       │       │   │       │   ├── everSeenByPlayer (6) — [text]
    │   │       │       │   │       │   ├── pregnancyApproaches (6)
    │   │       │       │   │       │   │   ├── keys (6)
    │   │       │       │   │       │   │   └── values (6)
    │   │       │       │   │       │   ├── relativeInvolvedInRescueQuest (6) — [text]
    │   │       │       │   │       │   ├── romanceEnableTick (6) — [text]
    │   │       │       │   │       │   └── virtualRelations (6)
    │   │       │       │   │       ├── stances (6)
    │   │       │       │   │       │   ├── curStance (6) — attrs: [Class]
    │   │       │       │   │       │   ├── stagger (6)
    │   │       │       │   │       │   └── stunner (6)
    │   │       │       │   │       │       ├── adaptationTicksLeft (6)
    │   │       │       │   │       │       │   ├── keys (6)
    │   │       │       │   │       │       │   └── values (6)
    │   │       │       │   │       │       └── showStunMote (6) — [text]
    │   │       │       │   │       ├── story (6)
    │   │       │       │   │       │   ├── birthLastName (6) — [text]
    │   │       │       │   │       │   ├── bodyType (6) — [text]
    │   │       │       │   │       │   ├── childhood (6) — [text]
    │   │       │       │   │       │   ├── favoriteColorDef (6) — [text]
    │   │       │       │   │       │   ├── hairColor (6) — [text]
    │   │       │       │   │       │   ├── hairDef (6) — [text]
    │   │       │       │   │       │   ├── headType (6) — [text]
    │   │       │       │   │       │   ├── traits (6)
    │   │       │       │   │       │   │   └── allTraits (6)
    │   │       │       │   │       │   │       └── li (14)
    │   │       │       │   │       │   │           ├── def (14) — [text]
    │   │       │       │   │       │   │           ├── sourceGene (14) — [text]
    │   │       │       │   │       │   │           ├── suppressedBy (14) — [text]
    │   │       │       │   │       │   │           └── degree (2) — [text]
    │   │       │       │   │       │   └── adulthood (5) — [text]
    │   │       │       │   │       ├── style (6)
    │   │       │       │   │       │   ├── beardDef (6) — [text]
    │   │       │       │   │       │   ├── bodyTattoo (6) — [text]
    │   │       │       │   │       │   └── faceTattoo (6) — [text]
    │   │       │       │   │       ├── styleObserver (6)
    │   │       │       │   │       ├── targetHolder (6) — [text]
    │   │       │       │   │       ├── thinker (6)
    │   │       │       │   │       ├── tickDelta (6) — [text]
    │   │       │       │   │       ├── ticksToReset (6) — [text]
    │   │       │       │   │       ├── timetable (6) — attrs: [IsNull]
    │   │       │       │   │       ├── trader (6) — attrs: [IsNull]
    │   │       │       │   │       ├── training (6) — attrs: [IsNull]
    │   │       │       │   │       ├── treeSightings (6)
    │   │       │       │   │       │   ├── fullTreeSightings (6)
    │   │       │       │   │       │   ├── miniTreeSightings (6)
    │   │       │       │   │       │   └── superTreeSightings (6)
    │   │       │       │   │       ├── vfee_honors (6)
    │   │       │       │   │       │   ├── honors (6)
    │   │       │       │   │       │   └── pendingHonors (6)
    │   │       │       │   │       ├── workSettings (6)
    │   │       │       │   │       │   └── priorities (6) — attrs: [IsNull]
    │   │       │       │   │       ├── gender (4) — [text]
    │   │       │       │   │       ├── health (2) — [text]
    │   │       │       │   │       ├── stackCount (2) — [text]
    │   │       │       │   │       └── sourcePrecept (1) — [text]
    │   │       │       │   ├── contentsLookMode (36) — [text]
    │   │       │       │   ├── maxStacks (36) — [text]
    │   │       │       │   └── removeContentsIfDestroyed (36) — [text]
    │   │       │       ├── rotProg (50) — [text]
    │   │       │       ├── overrideGraphicIndex (40) — [text]
    │   │       │       ├── thickness (38) — [text]
    │   │       │       ├── operationsBillStack (36)
    │   │       │       │   └── bills (36)
    │   │       │       ├── timeOfDeath (36) — [text]
    │   │       │       ├── vanishAfterTimestamp (36) — [text]
    │   │       │       ├── approachingPawn (31) — [text]
    │   │       │       ├── glowOn (31) — [text]
    │   │       │       ├── lastFriendlyTouchTick (31) — [text]
    │   │       │       ├── nextSpawnTimestamp (31) — [text]
    │   │       │       ├── styleDef (31) — [text]
    │   │       │       ├── forbidden (29) — [text]
    │   │       │       ├── taleRef (28) — attrs: [Class, IsNull]
    │   │       │       │   ├── tale (7) — [text]
    │   │       │       │   ├── seed (6) — [text]
    │   │       │       │   └── bakedTale (1) — [text]
    │   │       │       ├── gender (27) — [text]
    │   │       │       ├── assignedPawns (25)
    │   │       │       │   └── li (8) — [text]
    │   │       │       ├── uninstalledAssignedPawns (25)
    │   │       │       ├── alreadySetDefaultMed (21) — [text]
    │   │       │       ├── settings (21)
    │   │       │       │   ├── filter (21)
    │   │       │       │   │   ├── allowedDefs (21)
    │   │       │       │   │   │   └── li (17,162) — [text]
    │   │       │       │   │   ├── allowedHitPointsPercents (21) — [text]
    │   │       │       │   │   ├── allowedMentalBreakChance (21) — [text]
    │   │       │       │   │   ├── allowedQualityLevels (21) — [text]
    │   │       │       │   │   └── disallowedSpecialFilters (21)
    │   │       │       │   │       └── li (75) — [text]
    │   │       │       │   ├── stackGap (21)
    │   │       │       │   │   └── allowedPerItem (21)
    │   │       │       │   │       ├── keys (21)
    │   │       │       │   │       └── values (21)
    │   │       │       │   └── priority (20) — [text]
    │   │       │       ├── storageGroup (21) — [text]
    │   │       │       ├── diningSpots (16)
    │   │       │       ├── billStack (14)
    │   │       │       │   └── bills (14)
    │   │       │       │       └── li (21) — attrs: [Class]
    │   │       │       │           ├── allowedSkillRange (21) — [text]
    │   │       │       │           ├── includeGroup (21) — [text]
    │   │       │       │           ├── ingredientFilter (21)
    │   │       │       │           │   ├── allowedDefs (21)
    │   │       │       │           │   │   └── li (1,919) — [text]
    │   │       │       │           │   ├── allowedHitPointsPercents (21) — [text]
    │   │       │       │           │   ├── allowedMentalBreakChance (21) — [text]
    │   │       │       │           │   ├── allowedQualityLevels (21) — [text]
    │   │       │       │           │   └── disallowedSpecialFilters (21)
    │   │       │       │           │       └── li (113) — [text]
    │   │       │       │           ├── pawnRestriction (21) — [text]
    │   │       │       │           ├── precept (21) — [text]
    │   │       │       │           ├── productFilter (21) — attrs: [IsNull]
    │   │       │       │           │   ├── allowedDefs (12)
    │   │       │       │           │   ├── allowedHitPointsPercents (12) — [text]
    │   │       │       │           │   ├── allowedMentalBreakChance (12) — [text]
    │   │       │       │           │   ├── allowedQualityLevels (12) — [text]
    │   │       │       │           │   └── disallowedSpecialFilters (12)
    │   │       │       │           ├── recipe (21) — [text]
    │   │       │       │           ├── repeatCount (21) — [text]
    │   │       │       │           ├── repeatMode (21) — [text]
    │   │       │       │           ├── storeGroup (21) — [text]
    │   │       │       │           ├── storeMode (21) — [text]
    │   │       │       │           ├── targetCount (21) — [text]
    │   │       │       │           ├── unpauseWhenYouHave (21) — [text]
    │   │       │       │           ├── xenogerm (21) — [text]
    │   │       │       │           └── loadID (20) — [text]
    │   │       │       ├── countdownTicksLeft (14) — [text]
    │   │       │       ├── instigator (14) — [text]
    │   │       │       ├── thingsIgnoredByExplosion (14)
    │   │       │       ├── ProxyHeat_active (13) — [text]
    │   │       │       ├── allowAutoRefuel (11) — [text]
    │   │       │       ├── bed (11) — [text]
    │   │       │       ├── boughtItems (11)
    │   │       │       ├── currentlyCasting (11) — [text]
    │   │       │       ├── currentlyCastingTargets (11)
    │   │       │       ├── guestArea (11) — [text]
    │   │       │       ├── lastKeepDisplayTick (11) — [text]
    │   │       │       ├── learnedAbilities (11)
    │   │       │       ├── lord (11) — [text]
    │   │       │       ├── shoppingArea (11) — [text]
    │   │       │       ├── ticksToReset (11) — [text]
    │   │       │       ├── OriginMap (10) — [text]
    │   │       │       ├── forOwnerType (9) — [text]
    │   │       │       ├── fuel (9) — [text]
    │   │       │       ├── sources (9)
    │   │       │       │   └── li (9) — [text]
    │   │       │       ├── stunHandler (8)
    │   │       │       │   ├── adaptationTicksLeft (8)
    │   │       │       │   │   ├── keys (8)
    │   │       │       │   │   └── values (8)
    │   │       │       │   └── showStunMote (8) — [text]
    │   │       │       ├── RRPawnBadge_Badge1 (7) — [text]
    │   │       │       ├── gun (7) — attrs: [Class]
    │   │       │       │   ├── def (7) — [text]
    │   │       │       │   ├── despawnedTick (7) — [text]
    │   │       │       │   ├── id (7) — [text]
    │   │       │       │   ├── questTags (7) — attrs: [IsNull]
    │   │       │       │   ├── sourcePrecept (7) — [text]
    │   │       │       │   └── verbTracker (7)
    │   │       │       │       └── verbs (7)
    │   │       │       │           └── li (7) — attrs: [Class]
    │   │       │       │               ├── MVCF_ManagedVerb (7)
    │   │       │       │               │   ├── enabled (7) — [text]
    │   │       │       │               │   └── loadId (7) — [text]
    │   │       │       │               ├── canHitNonTargetPawnsNow (7) — [text]
    │   │       │       │               ├── lastShotTick (7) — [text]
    │   │       │       │               ├── loadID (7) — [text]
    │   │       │       │               ├── currentDestination (3) — [text]
    │   │       │       │               └── currentTarget (3) — [text]
    │   │       │       ├── lastSleepDisturbedTick (7) — [text]
    │   │       │       ├── title (7) — [text]
    │   │       │       ├── active (6) — [text]
    │   │       │       ├── authorName (6) — [text]
    │   │       │       ├── infectedPawns (6)
    │   │       │       ├── ingredients (6)
    │   │       │       │   └── li (15) — [text]
    │   │       │       ├── fertilizedBy (5) — [text]
    │   │       │       ├── lastAttackTargetTick (4) — [text]
    │   │       │       ├── storageSettings (4)
    │   │       │       │   ├── filter (4)
    │   │       │       │   │   ├── allowedDefs (4)
    │   │       │       │   │   │   └── li (16) — [text]
    │   │       │       │   │   ├── allowedHitPointsPercents (4) — [text]
    │   │       │       │   │   ├── allowedMentalBreakChance (4) — [text]
    │   │       │       │   │   ├── allowedQualityLevels (4) — [text]
    │   │       │       │   │   └── disallowedSpecialFilters (4)
    │   │       │       │   │       └── li (12) — [text]
    │   │       │       │   ├── priority (4) — [text]
    │   │       │       │   └── stackGap (4)
    │   │       │       │       └── allowedPerItem (4)
    │   │       │       │           ├── keys (4)
    │   │       │       │           └── values (4)
    │   │       │       ├── targetTemperature (4) — [text]
    │   │       │       ├── lastAttackedTarget (3) — [text]
    │   │       │       ├── powerOn (3) — [text]
    │   │       │       ├── sourcePawn (3) — [text]
    │   │       │       ├── RRPawnBadge_Badge0 (2) — [text]
    │   │       │       ├── addHediffOnce (2) — [text]
    │   │       │       ├── configuredTargetFuelLevel (2) — [text]
    │   │       │       ├── currentTemp (2) — [text]
    │   │       │       ├── disabled (2) — [text]
    │   │       │       ├── groupID (2) — [text]
    │   │       │       ├── lastLaunchTick (2) — [text]
    │   │       │       ├── leftToLoad (2) — attrs: [IsNull]
    │   │       │       ├── lightType (2) — [text]
    │   │       │       ├── massCapacityOverride (2) — [text]
    │   │       │       ├── maxItemsPerCell (2) — [text]
    │   │       │       ├── metamorphosisTick (2) — [text]
    │   │       │       ├── phase (2) — [text]
    │   │       │       ├── signalTag (2) — [text]
    │   │       │       ├── ticksSinceLastEmitted (2) — [text]
    │   │       │       ├── tmpSavedPawns (2)
    │   │       │       ├── wasDowned (2) — [text]
    │   │       │       ├── canCut (1) — [text]
    │   │       │       ├── chargerBeforeTakeoff (1) — [text]
    │   │       │       ├── currentPlayer (1) — [text]
    │   │       │       ├── delayUntilFeralCheck (1) — [text]
    │   │       │       ├── destroyIfUnfogged (1) — [text]
    │   │       │       ├── eggProgress (1) — [text]
    │   │       │       ├── enabled (1) — [text]
    │   │       │       ├── fixedPawnReference (1) — [text]
    │   │       │       ├── lastRoomTemperatureChange (1) — [text]
    │   │       │       ├── lastRoomTemperatureChangeTicks (1) — [text]
    │   │       │       ├── letter (1) — attrs: [IsNull]
    │   │       │       ├── letterDef (1) — [text]
    │   │       │       ├── letterLabelKey (1) — [text]
    │   │       │       ├── letterMessageKey (1) — [text]
    │   │       │       ├── lookTargets (1) — attrs: [IsNull]
    │   │       │       ├── medical (1) — [text]
    │   │       │       ├── pawnsThatCanPsylinkLastGrassGrow (1)
    │   │       │       ├── rect (1) — [text]
    │   │       │       ├── repeatWakeUpSignalOnTick (1) — [text]
    │   │       │       ├── ropedPawns (1)
    │   │       │       ├── storedPower (1) — [text]
    │   │       │       ├── subplants (1)
    │   │       │       ├── switchOn (1) — [text]
    │   │       │       ├── wakeUpSignalTag (1) — [text]
    │   │       │       ├── wakeUpSignalTags (1) — attrs: [IsNull]
    │   │       │       ├── wantSwitchOn (1) — [text]
    │   │       │       ├── wokeUpTick (1) — [text]
    │   │       │       └── woolGrowth (1) — [text]
    │   │       ├── treeDestructionTracker (1)
    │   │       │   └── playerTreeDestructionTicks (1)
    │   │       │       └── li (486) — [text]
    │   │       ├── uniqueID (1) — [text]
    │   │       ├── visitorManager (1)
    │   │       │   └── passingShips (1)
    │   │       ├── waterBodyTracker (1)
    │   │       │   └── waterBodies (1)
    │   │       │       └── li (12)
    │   │       │           ├── cellCount (12) — [text]
    │   │       │           ├── commonFish (12)
    │   │       │           │   └── li (3) — [text]
    │   │       │           ├── fishType (12) — [text]
    │   │       │           ├── population (12) — [text]
    │   │       │           ├── uncommonFish (12)
    │   │       │           │   └── li (1) — [text]
    │   │       │           ├── rootCell (11) — [text]
    │   │       │           └── shouldHaveFish (3) — [text]
    │   │       ├── weatherDecider (1)
    │   │       │   └── curWeatherDuration (1) — [text]
    │   │       ├── weatherManager (1)
    │   │       │   ├── curWeather (1) — [text]
    │   │       │   ├── curWeatherAge (1) — [text]
    │   │       │   └── lastWeather (1) — [text]
    │   │       ├── wildPlantSpawner (1)
    │   │       │   ├── calculatedWholeMapNumDesiredPlants (1) — [text]
    │   │       │   ├── calculatedWholeMapNumDesiredPlantsTmp (1) — [text]
    │   │       │   ├── calculatedWholeMapNumNonZeroFertilityCells (1) — [text]
    │   │       │   ├── calculatedWholeMapNumNonZeroFertilityCellsTmp (1) — [text]
    │   │       │   └── cycleIndex (1) — [text]
    │   │       └── zoneManager (1)
    │   │           └── allZones (1)
    │   │               └── li (8) — attrs: [Class]
    │   │                   ├── ID (8) — [text]
    │   │                   ├── baseLabel (8) — [text]
    │   │                   ├── cells (8)
    │   │                   │   └── li (570) — [text]
    │   │                   ├── color (8) — [text]
    │   │                   ├── label (8) — [text]
    │   │                   ├── plantDefToGrow (6) — [text]
    │   │                   └── settings (2)
    │   │                       ├── filter (2)
    │   │                       │   ├── allowedDefs (2)
    │   │                       │   │   └── li (3,031) — [text]
    │   │                       │   ├── allowedHitPointsPercents (2) — [text]
    │   │                       │   ├── allowedMentalBreakChance (2) — [text]
    │   │                       │   ├── allowedQualityLevels (2) — [text]
    │   │                       │   └── disallowedSpecialFilters (2)
    │   │                       ├── priority (2) — [text]
    │   │                       └── stackGap (2)
    │   │                           └── allowedPerItem (2)
    │   │                               ├── keys (2)
    │   │                               └── values (2)
    │   ├── outfitDatabase (1)
    │   │   └── outfits (1)
    │   │       └── li (7)
    │   │           ├── filter (7)
    │   │           │   ├── allowedDefs (7)
    │   │           │   │   └── li (529) — [text]
    │   │           │   ├── allowedHitPointsPercents (7) — [text]
    │   │           │   ├── allowedMentalBreakChance (7) — [text]
    │   │           │   ├── allowedQualityLevels (7) — [text]
    │   │           │   └── disallowedSpecialFilters (7)
    │   │           │       └── li (6) — [text]
    │   │           ├── id (7) — [text]
    │   │           └── label (7) — [text]
    │   ├── playLog (1)
    │   │   └── entries (1)
    │   │       └── li (150) — attrs: [Class]
    │   │           ├── extras (150)
    │   │           │   └── li (19) — [text]
    │   │           ├── initiator (150) — [text]
    │   │           ├── initiatorFaction (150) — [text]
    │   │           ├── initiatorIdeo (150) — [text]
    │   │           ├── intDef (150) — [text]
    │   │           ├── logID (150) — [text]
    │   │           ├── recipient (150) — [text]
    │   │           └── ticksAbs (150) — [text]
    │   ├── playSettings (1)
    │   │   ├── lockNorthUp (1) — [text]
    │   │   ├── showColonistBar (1) — [text]
    │   │   ├── showLearningHelper (1) — [text]
    │   │   ├── showWorldFeatures (1) — [text]
    │   │   ├── showZones (1) — [text]
    │   │   ├── usePlanetDayNightSystem (1) — [text]
    │   │   └── useWorkPriorities (1) — [text]
    │   ├── questManager (1)
    │   │   └── quests (1)
    │   │       └── li (23)
    │   │           ├── acceptedBy (23) — [text]
    │   │           ├── appearanceTick (23) — [text]
    │   │           ├── challengeRating (23) — [text]
    │   │           ├── name (23) — [text]
    │   │           ├── parent (23) — [text]
    │   │           ├── parts (23)
    │   │           │   └── li (201) — attrs: [Class]
    │   │           │       ├── inSignal (134) — [text]
    │   │           │       ├── outcome (54) — [text]
    │   │           │       ├── state (38) — [text]
    │   │           │       ├── inSignalEnable (32) — [text]
    │   │           │       ├── worldObject (30) — [text]
    │   │           │       ├── alertCulprits (27)
    │   │           │       ├── delayTicks (27) — [text]
    │   │           │       ├── inspectStringTargets (27) — attrs: [IsNull]
    │   │           │       ├── outSignal (27) — [text]
    │   │           │       ├── enableTick (25) — [text]
    │   │           │       ├── outSignalsCompleted (24)
    │   │           │       │   └── li (24) — [text]
    │   │           │       ├── mapParent (16) — [text]
    │   │           │       ├── getLookTargetsFromSignal (14) — [text]
    │   │           │       ├── lookTargets (14)
    │   │           │       │   └── targets (14)
    │   │           │       │       └── li (14) — [text]
    │   │           │       ├── message (14) — [text]
    │   │           │       ├── messageType (14) — [text]
    │   │           │       ├── defsToExcludeFromHyperlinks (13) — attrs: [IsNull]
    │   │           │       ├── pawns (13)
    │   │           │       │   └── li (4)
    │   │           │       │       ├── MVCF_VerbManager (2) — attrs: [IsNull]
    │   │           │       │       ├── ThingsHauledToInventory (2)
    │   │           │       │       ├── abilities (2)
    │   │           │       │       │   └── abilities (2)
    │   │           │       │       ├── ageTracker (2)
    │   │           │       │       │   ├── ageBiologicalTicks (2) — [text]
    │   │           │       │       │   ├── ageReversalDemandedAtAgeTicks (2) — [text]
    │   │           │       │       │   ├── birthAbsTicks (2) — [text]
    │   │           │       │       │   ├── growth (2) — [text]
    │   │           │       │       │   ├── lifeStageChange (2) — [text]
    │   │           │       │       │   └── nextGrowthCheckTick (2) — [text]
    │   │           │       │       ├── apparel (2)
    │   │           │       │       │   ├── lastApparelWearoutTick (2) — [text]
    │   │           │       │       │   ├── lockedApparel (2) — attrs: [IsNull]
    │   │           │       │       │   └── wornApparel (2)
    │   │           │       │       │       └── innerList (2)
    │   │           │       │       │           └── li (5)
    │   │           │       │       │               ├── abilities (5)
    │   │           │       │       │               ├── def (5) — [text]
    │   │           │       │       │               ├── despawnedTick (5) — [text]
    │   │           │       │       │               ├── health (5) — [text]
    │   │           │       │       │               ├── id (5) — [text]
    │   │           │       │       │               ├── quality (5) — [text]
    │   │           │       │       │               ├── questTags (5) — attrs: [IsNull]
    │   │           │       │       │               ├── sourcePrecept (5) — [text]
    │   │           │       │       │               ├── stackCount (5) — [text]
    │   │           │       │       │               ├── color (3) — [text]
    │   │           │       │       │               ├── colorActive (3) — [text]
    │   │           │       │       │               ├── stuff (2) — [text]
    │   │           │       │       │               └── codedPawn (1) — [text]
    │   │           │       │       ├── bed (2) — [text]
    │   │           │       │       ├── boughtItems (2)
    │   │           │       │       ├── carryTracker (2)
    │   │           │       │       │   └── innerContainer (2)
    │   │           │       │       │       ├── innerList (2)
    │   │           │       │       │       └── maxStacks (2) — [text]
    │   │           │       │       ├── connections (2)
    │   │           │       │       │   └── connectedThings (2)
    │   │           │       │       ├── creepjoiner (2) — attrs: [IsNull]
    │   │           │       │       ├── currentlyCasting (2) — [text]
    │   │           │       │       ├── currentlyCastingTargets (2)
    │   │           │       │       ├── deadlifeDustFaction (2) — [text]
    │   │           │       │       ├── def (2) — [text]
    │   │           │       │       ├── despawnedTick (2) — [text]
    │   │           │       │       ├── drafter (2) — attrs: [IsNull]
    │   │           │       │       ├── drugs (2) — attrs: [IsNull]
    │   │           │       │       ├── duplicate (2)
    │   │           │       │       ├── equipment (2)
    │   │           │       │       │   ├── bondedWeapon (2) — [text]
    │   │           │       │       │   └── equipment (2)
    │   │           │       │       │       └── innerList (2)
    │   │           │       │       │           └── li (2)
    │   │           │       │       │               ├── ability (2) — attrs: [IsNull]
    │   │           │       │       │               │   ├── Id (1) — [text]
    │   │           │       │       │               │   ├── charges (1) — [text]
    │   │           │       │       │               │   ├── def (1) — [text]
    │   │           │       │       │               │   ├── maxCharges (1) — [text]
    │   │           │       │       │               │   ├── sourcePrecept (1) — [text]
    │   │           │       │       │               │   └── verbTracker (1)
    │   │           │       │       │               │       └── verbs (1)
    │   │           │       │       │               │           └── li (1) — attrs: [Class]
    │   │           │       │       │               │               ├── MVCF_ManagedVerb (1) — attrs: [IsNull]
    │   │           │       │       │               │               ├── ability (1) — [text]
    │   │           │       │       │               │               ├── canHitNonTargetPawnsNow (1) — [text]
    │   │           │       │       │               │               ├── currentDestination (1) — [text]
    │   │           │       │       │               │               ├── currentTarget (1) — [text]
    │   │           │       │       │               │               ├── lastShotTick (1) — [text]
    │   │           │       │       │               │               └── loadID (1) — [text]
    │   │           │       │       │               ├── codedPawn (2) — [text]
    │   │           │       │       │               ├── def (2) — [text]
    │   │           │       │       │               ├── despawnedTick (2) — [text]
    │   │           │       │       │               ├── health (2) — [text]
    │   │           │       │       │               ├── id (2) — [text]
    │   │           │       │       │               ├── quality (2) — [text]
    │   │           │       │       │               ├── questTags (2) — attrs: [IsNull]
    │   │           │       │       │               ├── sourcePrecept (2) — [text]
    │   │           │       │       │               ├── stackCount (2) — [text]
    │   │           │       │       │               ├── taleRef (2) — attrs: [IsNull]
    │   │           │       │       │               │   ├── seed (1) — [text]
    │   │           │       │       │               │   └── tale (1) — [text]
    │   │           │       │       │               ├── verbTracker (2)
    │   │           │       │       │               │   └── verbs (2)
    │   │           │       │       │               │       └── li (8) — attrs: [Class]
    │   │           │       │       │               │           ├── MVCF_ManagedVerb (8)
    │   │           │       │       │               │           │   ├── enabled (8) — [text]
    │   │           │       │       │               │           │   └── loadId (8) — [text]
    │   │           │       │       │               │           ├── canHitNonTargetPawnsNow (8) — [text]
    │   │           │       │       │               │           ├── lastShotTick (8) — [text]
    │   │           │       │       │               │           └── loadID (8) — [text]
    │   │           │       │       │               ├── color (1) — [text]
    │   │           │       │       │               ├── name (1) — [text]
    │   │           │       │       │               ├── title (1) — [text]
    │   │           │       │       │               └── traits (1)
    │   │           │       │       │                   └── li (2) — [text]
    │   │           │       │       ├── faction (2) — [text]
    │   │           │       │       ├── filth (2) — attrs: [IsNull]
    │   │           │       │       ├── flight (2) — attrs: [IsNull]
    │   │           │       │       ├── foodRestriction (2) — attrs: [IsNull]
    │   │           │       │       ├── genes (2)
    │   │           │       │       │   ├── endogenes (2)
    │   │           │       │       │   │   └── li (4)
    │   │           │       │       │   │       ├── def (4) — [text]
    │   │           │       │       │   │       ├── loadID (4) — [text]
    │   │           │       │       │   │       ├── overriddenByGene (4) — [text]
    │   │           │       │       │   │       └── pawn (4) — [text]
    │   │           │       │       │   ├── xenogenes (2)
    │   │           │       │       │   └── xenotype (2) — [text]
    │   │           │       │       ├── guest (2)
    │   │           │       │       │   ├── enabledNonExclusiveInteractions (2)
    │   │           │       │       │   ├── finalResistanceInteractionData (2) — attrs: [IsNull]
    │   │           │       │       │   ├── hostFaction (2) — [text]
    │   │           │       │       │   ├── ideoForConversion (2) — [text]
    │   │           │       │       │   ├── interactionMode (2) — [text]
    │   │           │       │       │   ├── joinStatus (2) — [text]
    │   │           │       │       │   ├── lastPrisonBreakTicks (2) — [text]
    │   │           │       │       │   ├── lastResistanceInteractionData (2) — attrs: [IsNull]
    │   │           │       │       │   ├── recruitable (2) — [text]
    │   │           │       │       │   ├── slaveFaction (2) — [text]
    │   │           │       │       │   ├── slaveInteractionMode (2) — [text]
    │   │           │       │       │   └── spotToWaitInsteadOfEscaping (2) — [text]
    │   │           │       │       ├── guestArea (2) — [text]
    │   │           │       │       ├── guilt (2)
    │   │           │       │       ├── healthTracker (2)
    │   │           │       │       │   ├── hediffSet (2)
    │   │           │       │       │   │   └── hediffs (2)
    │   │           │       │       │   │       └── li (6) — attrs: [Class]
    │   │           │       │       │   │           ├── abilities (6) — attrs: [IsNull]
    │   │           │       │       │   │           ├── canBeThreateningToPart (6) — [text]
    │   │           │       │       │   │           ├── combatLogEntry (6) — [text]
    │   │           │       │       │   │           ├── def (6) — [text]
    │   │           │       │       │   │           ├── loadID (6) — [text]
    │   │           │       │       │   │           ├── part (6)
    │   │           │       │       │   │           │   ├── body (6) — [text]
    │   │           │       │       │   │           │   └── index (6) — [text]
    │   │           │       │       │   │           ├── severity (6) — [text]
    │   │           │       │       │   │           ├── tickAdded (6) — [text]
    │   │           │       │       │   │           ├── infectionChanceFactor (4) — [text]
    │   │           │       │       │   │           ├── isPermanent (4) — [text]
    │   │           │       │       │   │           ├── painCategory (2) — [text]
    │   │           │       │       │   │           ├── tendQuality (2) — [text]
    │   │           │       │       │   │           ├── tendTicksLeft (2) — [text]
    │   │           │       │       │   │           └── totalTendQuality (2) — [text]
    │   │           │       │       │   ├── immunity (2)
    │   │           │       │       │   │   └── imList (2)
    │   │           │       │       │   └── surgeryBills (2)
    │   │           │       │       │       └── bills (2)
    │   │           │       │       ├── id (2) — [text]
    │   │           │       │       ├── ideo (2)
    │   │           │       │       │   ├── babyIdeoExposure (2) — attrs: [IsNull]
    │   │           │       │       │   ├── certainty (2) — [text]
    │   │           │       │       │   ├── ideo (2) — [text]
    │   │           │       │       │   ├── joinTick (2) — [text]
    │   │           │       │       │   └── previousIdeos (2)
    │   │           │       │       ├── infectionVectors (2)
    │   │           │       │       │   └── pathways (2)
    │   │           │       │       │       ├── keys (2)
    │   │           │       │       │       └── values (2)
    │   │           │       │       ├── interactions (2) — attrs: [IsNull]
    │   │           │       │       ├── inventory (2)
    │   │           │       │       │   ├── innerContainer (2)
    │   │           │       │       │   │   └── innerList (2)
    │   │           │       │       │   │       └── li (4) — attrs: [Class]
    │   │           │       │       │   │           ├── def (4) — [text]
    │   │           │       │       │   │           ├── despawnedTick (4) — [text]
    │   │           │       │       │   │           ├── health (4) — [text]
    │   │           │       │       │   │           ├── id (4) — [text]
    │   │           │       │       │   │           ├── questTags (4) — attrs: [IsNull]
    │   │           │       │       │   │           ├── stackCount (4) — [text]
    │   │           │       │       │   │           ├── infectedPawns (1)
    │   │           │       │       │   │           └── ingredients (1)
    │   │           │       │       │   ├── itemsNotForSale (2)
    │   │           │       │       │   │   └── li (1) — [text]
    │   │           │       │       │   └── unpackedCaravanItems (2)
    │   │           │       │       ├── inventoryStock (2) — attrs: [IsNull]
    │   │           │       │       ├── isEnabled (2) — [text]
    │   │           │       │       ├── jobs (2)
    │   │           │       │       │   ├── curDriver (2) — attrs: [IsNull]
    │   │           │       │       │   ├── curJob (2) — attrs: [IsNull]
    │   │           │       │       │   ├── formingCaravanTick (2) — [text]
    │   │           │       │       │   └── jobQueue (2)
    │   │           │       │       │       └── jobs (2)
    │   │           │       │       ├── kindDef (2) — [text]
    │   │           │       │       ├── lastKeepDisplayTick (2) — [text]
    │   │           │       │       ├── lastStudiedTick (2) — [text]
    │   │           │       │       ├── learnedAbilities (2)
    │   │           │       │       ├── learning (2) — attrs: [IsNull]
    │   │           │       │       ├── loadouts (2)
    │   │           │       │       │   └── curLoadout (2) — [text]
    │   │           │       │       ├── lord (2) — [text]
    │   │           │       │       ├── mechanitor (2) — attrs: [IsNull]
    │   │           │       │       ├── meleeVerbs (2)
    │   │           │       │       │   ├── curMeleeVerb (2) — [text]
    │   │           │       │       │   └── terrainVerbs (2) — attrs: [IsNull]
    │   │           │       │       ├── mindState (2)
    │   │           │       │       │   ├── babyAutoBreastfeedMoms (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── babyCaravanBreastfeed (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── breachingTarget (2) — attrs: [IsNull]
    │   │           │       │       │   ├── canFleeIndividual (2) — [text]
    │   │           │       │       │   ├── droppedWeapon (2) — [text]
    │   │           │       │       │   ├── duty (2) — attrs: [IsNull]
    │   │           │       │       │   ├── enemyTarget (2) — [text]
    │   │           │       │       │   ├── inspirationHandler (2)
    │   │           │       │       │   │   └── curState (2) — attrs: [IsNull]
    │   │           │       │       │   ├── knownExploder (2) — [text]
    │   │           │       │       │   ├── lastAttackTargetTick (2) — [text]
    │   │           │       │       │   ├── lastAttackedTarget (2) — [text]
    │   │           │       │       │   ├── lastEngageTargetTick (2) — [text]
    │   │           │       │       │   ├── lastMannedThing (2) — [text]
    │   │           │       │       │   ├── lastMeleeThreatHarmTick (2) — [text]
    │   │           │       │       │   ├── lastRangedHarmTick (2) — [text]
    │   │           │       │       │   ├── lastSelfTendTick (2) — [text]
    │   │           │       │       │   ├── meleeThreat (2) — [text]
    │   │           │       │       │   ├── mentalBreaker (2)
    │   │           │       │       │   ├── mentalFitGenerator (2)
    │   │           │       │       │   ├── mentalStateHandler (2)
    │   │           │       │       │   │   └── curState (2) — attrs: [IsNull]
    │   │           │       │       │   ├── nextMoveOrderIsWait (2) — [text]
    │   │           │       │       │   ├── priorityWork (2)
    │   │           │       │       │   │   ├── prioritizeTick (2) — [text]
    │   │           │       │       │   │   └── prioritizedCell (2) — [text]
    │   │           │       │       │   ├── resurrectTarget (2) — attrs: [IsNull]
    │   │           │       │       │   └── thinkData (2)
    │   │           │       │       │       ├── keys (2)
    │   │           │       │       │       └── values (2)
    │   │           │       │       ├── name (2) — attrs: [Class]
    │   │           │       │       │   ├── first (2) — [text]
    │   │           │       │       │   ├── last (2) — [text]
    │   │           │       │       │   └── nick (2) — [text]
    │   │           │       │       ├── natives (2) — attrs: [IsNull]
    │   │           │       │       ├── needs (2)
    │   │           │       │       │   └── needs (2)
    │   │           │       │       │       └── li (6) — attrs: [Class]
    │   │           │       │       │           ├── curLevel (6) — [text]
    │   │           │       │       │           ├── def (6) — [text]
    │   │           │       │       │           ├── lastNonStarvingTick (2) — [text]
    │   │           │       │       │           ├── recentMemory (2)
    │   │           │       │       │           └── thoughts (2)
    │   │           │       │       │               └── memories (2)
    │   │           │       │       │                   └── memories (2)
    │   │           │       │       ├── outfits (2) — attrs: [IsNull]
    │   │           │       │       ├── ownership (2)
    │   │           │       │       │   ├── assignedDeathrestCasket (2) — [text]
    │   │           │       │       │   ├── assignedGrave (2) — [text]
    │   │           │       │       │   ├── assignedMeditationSpot (2) — [text]
    │   │           │       │       │   ├── assignedThrone (2) — [text]
    │   │           │       │       │   └── ownedBed (2) — [text]
    │   │           │       │       ├── pather (2) — attrs: [IsNull]
    │   │           │       │       ├── playerSettings (2) — attrs: [IsNull]
    │   │           │       │       ├── psychicEntropy (2)
    │   │           │       │       │   └── limitEntropyAmount (2) — [text]
    │   │           │       │       ├── questTags (2) — attrs: [IsNull]
    │   │           │       │       ├── reading (2) — attrs: [IsNull]
    │   │           │       │       ├── records (2)
    │   │           │       │       │   ├── battleActive (2) — [text]
    │   │           │       │       │   └── records (2)
    │   │           │       │       │       └── vals (2)
    │   │           │       │       │           └── li (144) — [text]
    │   │           │       │       ├── roping (2) — attrs: [IsNull]
    │   │           │       │       ├── rotationTracker (2) — attrs: [IsNull]
    │   │           │       │       ├── royalty (2)
    │   │           │       │       │   ├── abilities (2)
    │   │           │       │       │   ├── favor (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── heirs (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── highestTitles (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── permits (2)
    │   │           │       │       │   └── titles (2)
    │   │           │       │       ├── shambler (2) — attrs: [IsNull]
    │   │           │       │       ├── shoppingArea (2) — [text]
    │   │           │       │       ├── skills (2)
    │   │           │       │       │   ├── lastXpSinceMidnightResetTimestamp (2) — [text]
    │   │           │       │       │   └── skills (2)
    │   │           │       │       │       └── li (24)
    │   │           │       │       │           ├── def (24) — [text]
    │   │           │       │       │           ├── level (22) — [text]
    │   │           │       │       │           └── passion (10) — [text]
    │   │           │       │       ├── social (2)
    │   │           │       │       │   ├── additionalPregnancyApproachData (2)
    │   │           │       │       │   │   └── partners (2)
    │   │           │       │       │   │       ├── keys (2)
    │   │           │       │       │   │       └── values (2)
    │   │           │       │       │   ├── directRelations (2)
    │   │           │       │       │   │   └── li (1)
    │   │           │       │       │   │       ├── def (1) — [text]
    │   │           │       │       │   │       ├── otherPawn (1) — [text]
    │   │           │       │       │   │       └── startTicks (1) — [text]
    │   │           │       │       │   ├── everSeenByPlayer (2) — [text]
    │   │           │       │       │   ├── pregnancyApproaches (2)
    │   │           │       │       │   │   ├── keys (2)
    │   │           │       │       │   │   └── values (2)
    │   │           │       │       │   ├── relativeInvolvedInRescueQuest (2) — [text]
    │   │           │       │       │   ├── romanceEnableTick (2) — [text]
    │   │           │       │       │   └── virtualRelations (2)
    │   │           │       │       │       └── li (2)
    │   │           │       │       │           ├── def (2) — [text]
    │   │           │       │       │           ├── record (2) — [text]
    │   │           │       │       │           └── startTicks (2) — [text]
    │   │           │       │       ├── stances (2)
    │   │           │       │       │   ├── curStance (2) — attrs: [Class]
    │   │           │       │       │   ├── stagger (2)
    │   │           │       │       │   └── stunner (2)
    │   │           │       │       │       ├── adaptationTicksLeft (2)
    │   │           │       │       │       │   ├── keys (2)
    │   │           │       │       │       │   └── values (2)
    │   │           │       │       │       └── showStunMote (2) — [text]
    │   │           │       │       ├── story (2)
    │   │           │       │       │   ├── adulthood (2) — [text]
    │   │           │       │       │   ├── birthLastName (2) — [text]
    │   │           │       │       │   ├── bodyType (2) — [text]
    │   │           │       │       │   ├── childhood (2) — [text]
    │   │           │       │       │   ├── favoriteColorDef (2) — [text]
    │   │           │       │       │   ├── hairColor (2) — [text]
    │   │           │       │       │   ├── hairDef (2) — [text]
    │   │           │       │       │   ├── headType (2) — [text]
    │   │           │       │       │   └── traits (2)
    │   │           │       │       │       └── allTraits (2)
    │   │           │       │       │           └── li (4)
    │   │           │       │       │               ├── def (4) — [text]
    │   │           │       │       │               ├── sourceGene (4) — [text]
    │   │           │       │       │               ├── suppressedBy (4) — [text]
    │   │           │       │       │               └── degree (1) — [text]
    │   │           │       │       ├── style (2)
    │   │           │       │       │   ├── beardDef (2) — [text]
    │   │           │       │       │   ├── bodyTattoo (2) — [text]
    │   │           │       │       │   └── faceTattoo (2) — [text]
    │   │           │       │       ├── styleObserver (2)
    │   │           │       │       ├── targetHolder (2) — [text]
    │   │           │       │       ├── thinker (2)
    │   │           │       │       ├── ticksToReset (2) — [text]
    │   │           │       │       ├── timetable (2) — attrs: [IsNull]
    │   │           │       │       ├── trader (2) — attrs: [IsNull]
    │   │           │       │       ├── training (2) — attrs: [IsNull]
    │   │           │       │       ├── treeSightings (2)
    │   │           │       │       │   ├── fullTreeSightings (2)
    │   │           │       │       │   ├── miniTreeSightings (2)
    │   │           │       │       │   └── superTreeSightings (2)
    │   │           │       │       ├── verbTracker (2)
    │   │           │       │       │   └── verbs (2)
    │   │           │       │       │       └── li (8) — attrs: [Class]
    │   │           │       │       │           ├── MVCF_ManagedVerb (8)
    │   │           │       │       │           │   ├── enabled (8) — [text]
    │   │           │       │       │           │   └── loadId (8) — [text]
    │   │           │       │       │           ├── canHitNonTargetPawnsNow (8) — [text]
    │   │           │       │       │           ├── currentDestination (8) — [text]
    │   │           │       │       │           ├── currentTarget (8) — [text]
    │   │           │       │       │           ├── lastShotTick (8) — [text]
    │   │           │       │       │           └── loadID (8) — [text]
    │   │           │       │       ├── vfee_honors (2)
    │   │           │       │       │   ├── honors (2)
    │   │           │       │       │   └── pendingHonors (2)
    │   │           │       │       ├── workSettings (2)
    │   │           │       │       │   └── priorities (2) — attrs: [IsNull]
    │   │           │       │       └── gender (1) — [text]
    │   │           │       ├── spawned (13) — [text]
    │   │           │       ├── choices (12)
    │   │           │       │   └── li (12)
    │   │           │       │       ├── questParts (12)
    │   │           │       │       │   └── li (4) — [text]
    │   │           │       │       └── rewards (12)
    │   │           │       │           └── li (14) — attrs: [Class]
    │   │           │       │               ├── usedOrCleanedUp (8) — [text]
    │   │           │       │               ├── amount (2) — [text]
    │   │           │       │               ├── faction (2) — [text]
    │   │           │       │               ├── itemDefs (2)
    │   │           │       │               │   └── li (6)
    │   │           │       │               │       ├── label (6) — [text]
    │   │           │       │               │       ├── stackCount (6) — [text]
    │   │           │       │               │       └── thing (6)
    │   │           │       │               │           ├── quality (6) — [text]
    │   │           │       │               │           ├── thing (6) — [text]
    │   │           │       │               │           └── stuff (1) — [text]
    │   │           │       │               ├── items (2)
    │   │           │       │               │   └── li (4) — [text]
    │   │           │       │               ├── lastTotalMarketValue (2) — [text]
    │   │           │       │               └── thingDef (1) — [text]
    │   │           │       ├── expiryInfoPart (12) — [text]
    │   │           │       ├── expiryInfoPartTip (12) — [text]
    │   │           │       ├── faction (12) — [text]
    │   │           │       ├── isBad (12) — [text]
    │   │           │       ├── thingDefs (10)
    │   │           │       │   └── li (6) — [text]
    │   │           │       ├── destroyOnCleanup (8) — [text]
    │   │           │       ├── ThreatPointsBreakdown (7) — attrs: [IsNull]
    │   │           │       ├── colonistsFromSignal (7)
    │   │           │       ├── letter (7) — attrs: [Class]
    │   │           │       │   ├── ID (7) — [text]
    │   │           │       │   ├── ThreatPointsBreakdown (7) — attrs: [IsNull]
    │   │           │       │   ├── def (7) — [text]
    │   │           │       │   ├── hyperlinkHediffDefs (7) — attrs: [IsNull]
    │   │           │       │   ├── hyperlinkThingDefs (7) — attrs: [IsNull]
    │   │           │       │   ├── label (7) — [text]
    │   │           │       │   ├── lookTargets (7) — attrs: [IsNull]
    │   │           │       │   │   └── targets (2)
    │   │           │       │   │       └── li (2) — [text]
    │   │           │       │   ├── quest (7) — [text]
    │   │           │       │   ├── relatedFaction (7) — [text]
    │   │           │       │   └── text (7) — [text]
    │   │           │       ├── useColonistsOnMap (7) — [text]
    │   │           │       ├── visitors (7) — attrs: [IsNull]
    │   │           │       ├── cell (6) — [text]
    │   │           │       ├── factionForFindingSpot (6) — [text]
    │   │           │       ├── getRaidersFromMap (6) — [text]
    │   │           │       ├── getRaidersFromMapParent (6) — [text]
    │   │           │       ├── innerSkyfallerThing (6) — [text]
    │   │           │       ├── mapParentOfPawn (6) — [text]
    │   │           │       ├── questLookTarget (6) — [text]
    │   │           │       ├── signalListenMode (6) — [text]
    │   │           │       ├── thing (6) — attrs: [Class]
    │   │           │       │   ├── contentsCanOverlap (6) — [text]
    │   │           │       │   ├── def (6) — [text]
    │   │           │       │   ├── despawnedTick (6) — [text]
    │   │           │       │   ├── id (6) — [text]
    │   │           │       │   ├── impactLetter (6) — attrs: [IsNull]
    │   │           │       │   ├── innerContainer (6) — attrs: [Class]
    │   │           │       │   │   └── innerList (6)
    │   │           │       │   │       └── li (15) — attrs: [Class]
    │   │           │       │   │           ├── def (15) — [text]
    │   │           │       │   │           ├── despawnedTick (15) — [text]
    │   │           │       │   │           ├── health (15) — [text]
    │   │           │       │   │           ├── id (15) — [text]
    │   │           │       │   │           ├── questTags (15) — attrs: [IsNull]
    │   │           │       │   │           │   └── li (1) — [text]
    │   │           │       │   │           ├── forbidden (9) — [text]
    │   │           │       │   │           ├── stackCount (5) — [text]
    │   │           │       │   │           ├── innerContainer (4)
    │   │           │       │   │           │   ├── contentsLookMode (4) — [text]
    │   │           │       │   │           │   ├── innerList (4)
    │   │           │       │   │           │   │   └── li (4) — [text]
    │   │           │       │   │           │   ├── maxStacks (4) — [text]
    │   │           │       │   │           │   └── removeContentsIfDestroyed (4) — [text]
    │   │           │       │   │           ├── operationsBillStack (4)
    │   │           │       │   │           │   └── bills (4)
    │   │           │       │   │           ├── timeOfDeath (4) — [text]
    │   │           │       │   │           ├── vanishAfterTimestamp (4) — [text]
    │   │           │       │   │           ├── gravshipName (1) — [text]
    │   │           │       │   │           ├── launchInfo (1) — attrs: [IsNull]
    │   │           │       │   │           ├── pawnsToBoard (1)
    │   │           │       │   │           └── pawnsToLeave (1)
    │   │           │       │   ├── moveAside (6) — [text]
    │   │           │       │   └── questTags (6) — attrs: [IsNull]
    │   │           │       ├── tryLandNearThing (6) — [text]
    │   │           │       ├── layerBlacklist (5) — attrs: [IsNull]
    │   │           │       ├── layerWhitelist (5) — attrs: [IsNull]
    │   │           │       ├── mapPawn (5) — [text]
    │   │           │       ├── destroyItemsOnCleanup (4) — [text]
    │   │           │       ├── dropSpot (4) — [text]
    │   │           │       ├── importantLookTarget (4) — [text]
    │   │           │       ├── inSignalDisable (4) — [text]
    │   │           │       ├── items (4)
    │   │           │       ├── outSignalElse (4) — [text]
    │   │           │       ├── pawnsInContainers (4)
    │   │           │       ├── thingsToExcludeFromHyperlinks (4)
    │   │           │       ├── factions (3)
    │   │           │       │   └── li (3) — [text]
    │   │           │       ├── inSignalChoiceUsed (3) — [text]
    │   │           │       ├── change (2) — [text]
    │   │           │       ├── inSignals (2)
    │   │           │       │   └── li (4) — [text]
    │   │           │       ├── sendStandardLetter (2) — [text]
    │   │           │       ├── signalsReceived (2)
    │   │           │       ├── timeTicks (2) — [text]
    │   │           │       ├── useTradeDropSpot (2) — [text]
    │   │           │       ├── customLetterText (1) — [text]
    │   │           │       ├── hivesCount (1) — [text]
    │   │           │       ├── loc (1) — [text]
    │   │           │       ├── lookTarget (1) — [text]
    │   │           │       ├── sendLetter (1) — [text]
    │   │           │       ├── tag (1) — [text]
    │   │           │       └── targets (1)
    │   │           │           └── li (1) — [text]
    │   │           ├── root (23) — [text]
    │   │           ├── signalsReceivedDebug (23) — attrs: [IsNull]
    │   │           ├── tags (23)
    │   │           │   └── li (1) — [text]
    │   │           ├── id (22) — [text]
    │   │           ├── description (21) — [text]
    │   │           ├── acceptanceTick (17) — [text]
    │   │           ├── initiallyAccepted (16) — [text]
    │   │           ├── cleanedUp (15) — [text]
    │   │           ├── cleanupTick (15) — [text]
    │   │           ├── endOutcome (11) — [text]
    │   │           ├── ended (11) — [text]
    │   │           ├── acceptanceExpireTick (5) — [text]
    │   │           ├── charity (4) — [text]
    │   │           ├── dismissed (2) — [text]
    │   │           └── hidden (2) — [text]
    │   ├── readingPolicyDatabase (1)
    │   │   └── readingPolicies (1)
    │   │       └── li (7)
    │   │           ├── defFilter (7)
    │   │           │   ├── allowedDefs (7)
    │   │           │   │   └── li (10) — [text]
    │   │           │   ├── allowedHitPointsPercents (7) — [text]
    │   │           │   ├── allowedMentalBreakChance (7) — [text]
    │   │           │   ├── allowedQualityLevels (7) — [text]
    │   │           │   └── disallowedSpecialFilters (7)
    │   │           ├── effectFilter (7)
    │   │           │   ├── allowedDefs (7)
    │   │           │   ├── allowedHitPointsPercents (7) — [text]
    │   │           │   ├── allowedMentalBreakChance (7) — [text]
    │   │           │   ├── allowedQualityLevels (7) — [text]
    │   │           │   ├── disallowedSpecialFilters (7)
    │   │           │   ├── onlySpecialFilters (7) — [text]
    │   │           │   └── overrideRootDef (7) — [text]
    │   │           ├── id (7) — [text]
    │   │           └── label (7) — [text]
    │   ├── relationshipRecords (1)
    │   │   └── records (1)
    │   │       ├── keys (1)
    │   │       │   └── li (7) — [text]
    │   │       └── values (1)
    │   │           └── li (7)
    │   │               ├── gender (7) — [text]
    │   │               ├── id (7) — [text]
    │   │               ├── name (7) — [text]
    │   │               └── references (7)
    │   │                   └── li (14) — [text]
    │   ├── researchManager (1)
    │   │   ├── TargetProjectQueue (1)
    │   │   ├── currentKnowledgeProjects (1)
    │   │   │   └── li (2)
    │   │   │       └── category (2) — [text]
    │   │   ├── currentProj (1) — [text]
    │   │   ├── knowledge (1)
    │   │   │   ├── keys (1)
    │   │   │   │   └── li (40) — [text]
    │   │   │   └── values (1)
    │   │   │       └── li (40) — [text]
    │   │   ├── progress (1)
    │   │   │   ├── keys (1)
    │   │   │   │   └── li (315) — [text]
    │   │   │   └── values (1)
    │   │   │       └── li (315) — [text]
    │   │   ├── tabInfoVisibility (1)
    │   │   │   └── vals (1)
    │   │   │       └── li (21) — [text]
    │   │   └── techprints (1)
    │   │       ├── keys (1)
    │   │       └── values (1)
    │   ├── rules (1)
    │   │   ├── disallowedBuildings (1)
    │   │   └── disallowedDesignatorTypes (1)
    │   ├── scenario (1)
    │   │   ├── description (1) — [text]
    │   │   ├── name (1) — [text]
    │   │   ├── parts (1)
    │   │   │   └── li (21) — attrs: [Class]
    │   │   │       ├── def (21) — [text]
    │   │   │       ├── count (15) — [text]
    │   │   │       ├── thingDef (15) — [text]
    │   │   │       ├── stuff (2) — [text]
    │   │   │       ├── animalKind (1) — [text]
    │   │   │       ├── bondToRandomPlayerPawnChance (1) — [text]
    │   │   │       ├── chance (1) — [text]
    │   │   │       ├── closeSound (1) — [text]
    │   │   │       ├── connections (1)
    │   │   │       │   └── li (1)
    │   │   │       │       ├── tag (1) — [text]
    │   │   │       │       └── zoomMode (1) — [text]
    │   │   │       ├── context (1) — [text]
    │   │   │       ├── hediff (1) — [text]
    │   │   │       ├── hide (1) — [text]
    │   │   │       ├── hideOffMap (1) — [text]
    │   │   │       ├── layer (1) — [text]
    │   │   │       ├── method (1) — [text]
    │   │   │       ├── pawnChoiceCount (1) — [text]
    │   │   │       ├── pawnCount (1) — [text]
    │   │   │       ├── settingsDef (1) — [text]
    │   │   │       ├── severityRange (1) — [text]
    │   │   │       ├── tag (1) — [text]
    │   │   │       ├── text (1)
    │   │   │       └── textKey (1) — [text]
    │   │   ├── playerFaction (1)
    │   │   │   ├── def (1) — [text]
    │   │   │   └── factionDef (1) — [text]
    │   │   ├── summary (1) — [text]
    │   │   └── surfaceLayer (1)
    │   │       ├── connections (1)
    │   │       │   └── li (1)
    │   │       │       ├── tag (1) — [text]
    │   │       │       └── zoomMode (1) — [text]
    │   │       ├── def (1) — [text]
    │   │       ├── hide (1) — [text]
    │   │       ├── layer (1) — [text]
    │   │       ├── settingsDef (1) — [text]
    │   │       └── tag (1) — [text]
    │   ├── storyWatcher (1)
    │   │   ├── statsRecord (1)
    │   │   │   ├── greatestPopulation (1) — [text]
    │   │   │   ├── numRaidsEnemy (1) — [text]
    │   │   │   └── numThreatsQueued (1) — [text]
    │   │   ├── watcherAdaptation (1)
    │   │   │   └── adaptDays (1) — [text]
    │   │   └── watcherPopAdaptation (1)
    │   │       └── adaptDays (1) — [text]
    │   ├── storyteller (1)
    │   │   ├── anomalyPlaystyleDef (1) — [text]
    │   │   ├── def (1) — [text]
    │   │   ├── difficulty (1) — [text]
    │   │   ├── incidentQueue (1)
    │   │   │   └── queuedIncidents (1)
    │   │   ├── lastIncidentTick (1) — [text]
    │   │   ├── lastQuestGiverTraderTick (1) — [text]
    │   │   ├── recentAnomalyIncidentFactor (1) — [text]
    │   │   └── recentIncidentsAnomaly (1)
    │   │       └── li (4) — [text]
    │   ├── studyManager (1)
    │   ├── taleManager (1)
    │   │   └── tales (1)
    │   │       └── li (362) — attrs: [Class]
    │   │           ├── date (362) — [text]
    │   │           ├── def (362) — [text]
    │   │           ├── surroundings (362) — attrs: [IsNull]
    │   │           │   ├── biome (347) — [text]
    │   │           │   ├── roomRole (347) — [text]
    │   │           │   ├── temperature (347) — [text]
    │   │           │   ├── tile (347) — [text]
    │   │           │   ├── weather (188) — [text]
    │   │           │   ├── roomBeauty (187) — [text]
    │   │           │   ├── roomImpressiveness (187) — [text]
    │   │           │   └── roomCleanliness (171) — [text]
    │   │           ├── id (361) — [text]
    │   │           ├── defData (308)
    │   │           │   ├── defName (300) — [text]
    │   │           │   └── defType (300) — [text]
    │   │           ├── pawnData (261)
    │   │           │   ├── age (261) — [text]
    │   │           │   ├── chronologicalAge (261) — [text]
    │   │           │   ├── everBeenColonistOrTameAnimal (261) — [text]
    │   │           │   ├── faction (261) — [text]
    │   │           │   ├── gender (261) — [text]
    │   │           │   ├── kind (261) — [text]
    │   │           │   ├── name (261) — attrs: [Class, IsNull]
    │   │           │   │   ├── first (260) — [text]
    │   │           │   │   ├── last (260) — [text]
    │   │           │   │   └── nick (242) — [text]
    │   │           │   ├── pawn (261) — [text]
    │   │           │   ├── relationInfo (261) — [text]
    │   │           │   ├── royalTitles (261) — attrs: [IsNull]
    │   │           │   ├── app (258) — [text]
    │   │           │   └── peq (248) — [text]
    │   │           ├── firstPawnData (88)
    │   │           │   ├── age (88) — [text]
    │   │           │   ├── chronologicalAge (88) — [text]
    │   │           │   ├── faction (88) — [text]
    │   │           │   ├── kind (88) — [text]
    │   │           │   ├── name (88) — attrs: [Class, IsNull]
    │   │           │   │   ├── first (67) — [text]
    │   │           │   │   ├── last (67) — [text]
    │   │           │   │   └── nick (47) — [text]
    │   │           │   ├── pawn (88) — [text]
    │   │           │   ├── relationInfo (88) — [text]
    │   │           │   ├── royalTitles (88) — attrs: [IsNull]
    │   │           │   │   └── li (6)
    │   │           │   │       ├── def (6) — [text]
    │   │           │   │       ├── faction (6) — [text]
    │   │           │   │       └── receivedTick (6) — [text]
    │   │           │   ├── gender (87) — [text]
    │   │           │   ├── app (66) — [text]
    │   │           │   ├── peq (59) — [text]
    │   │           │   └── everBeenColonistOrTameAnimal (50) — [text]
    │   │           ├── secondPawnData (88) — attrs: [IsNull]
    │   │           │   ├── age (87) — [text]
    │   │           │   ├── chronologicalAge (87) — [text]
    │   │           │   ├── faction (87) — [text]
    │   │           │   ├── gender (87) — [text]
    │   │           │   ├── kind (87) — [text]
    │   │           │   ├── name (87) — attrs: [Class, IsNull]
    │   │           │   │   ├── first (62) — [text]
    │   │           │   │   ├── last (62) — [text]
    │   │           │   │   └── nick (51) — [text]
    │   │           │   ├── pawn (87) — [text]
    │   │           │   ├── relationInfo (87) — [text]
    │   │           │   ├── royalTitles (87) — attrs: [IsNull]
    │   │           │   │   └── li (2)
    │   │           │   │       ├── def (2) — [text]
    │   │           │   │       ├── faction (2) — [text]
    │   │           │   │       └── receivedTick (2) — [text]
    │   │           │   ├── everBeenColonistOrTameAnimal (71) — [text]
    │   │           │   ├── app (60) — [text]
    │   │           │   └── peq (60) — [text]
    │   │           ├── customLabel (13) — [text]
    │   │           ├── uses (4) — [text]
    │   │           └── thirdPawnData (2)
    │   │               ├── age (2) — [text]
    │   │               ├── app (2) — [text]
    │   │               ├── chronologicalAge (2) — [text]
    │   │               ├── faction (2) — [text]
    │   │               ├── gender (2) — [text]
    │   │               ├── kind (2) — [text]
    │   │               ├── name (2) — attrs: [Class]
    │   │               │   ├── first (2) — [text]
    │   │               │   ├── last (2) — [text]
    │   │               │   └── nick (2) — [text]
    │   │               ├── pawn (2) — [text]
    │   │               ├── relationInfo (2)
    │   │               ├── royalTitles (2)
    │   │               ├── everBeenColonistOrTameAnimal (1) — [text]
    │   │               └── peq (1) — [text]
    │   ├── tickManager (1)
    │   │   ├── gameStartAbsTick (1) — [text]
    │   │   ├── startingYear (1) — [text]
    │   │   └── ticksGame (1) — [text]
    │   ├── transportShipManager (1)
    │   │   └── ships (1)
    │   ├── tutor (1)
    │   │   ├── activeLesson (1)
    │   │   │   └── activeLesson (1) — attrs: [IsNull]
    │   │   ├── learningReadout (1)
    │   │   │   └── activeConcepts (1)
    │   │   └── tutorialState (1)
    │   │       └── startingItems (1)
    │   ├── uniqueIDsManager (1)
    │   │   ├── nextAbilityID (1) — [text]
    │   │   ├── nextAncientCryptosleepCasketGroupID (1) — [text]
    │   │   ├── nextArchivedDialogID (1) — [text]
    │   │   ├── nextAreaID (1) — [text]
    │   │   ├── nextBattleID (1) — [text]
    │   │   ├── nextBillID (1) — [text]
    │   │   ├── nextFactionID (1) — [text]
    │   │   ├── nextGameConditionID (1) — [text]
    │   │   ├── nextGeneID (1) — [text]
    │   │   ├── nextHediffID (1) — [text]
    │   │   ├── nextIdeoID (1) — [text]
    │   │   ├── nextJobID (1) — [text]
    │   │   ├── nextLetterID (1) — [text]
    │   │   ├── nextLogID (1) — [text]
    │   │   ├── nextLordID (1) — [text]
    │   │   ├── nextMapID (1) — [text]
    │   │   ├── nextMessageID (1) — [text]
    │   │   ├── nextPassingShipID (1) — [text]
    │   │   ├── nextPreceptID (1) — [text]
    │   │   ├── nextPresenceDemandID (1) — [text]
    │   │   ├── nextQuestID (1) — [text]
    │   │   ├── nextRitualObligationID (1) — [text]
    │   │   ├── nextRoomID (1) — [text]
    │   │   ├── nextShipJobID (1) — [text]
    │   │   ├── nextSignalTagID (1) — [text]
    │   │   ├── nextStorageGroupID (1) — [text]
    │   │   ├── nextTaleID (1) — [text]
    │   │   ├── nextThingID (1) — [text]
    │   │   ├── nextTransportShipID (1) — [text]
    │   │   ├── nextWorldFeatureID (1) — [text]
    │   │   ├── nextWorldObjectID (1) — [text]
    │   │   └── nextZoneID (1) — [text]
    │   └── world (1)
    │       ├── components (1)
    │       │   └── li (52) — attrs: [Class]
    │       │       ├── store (3)
    │       │       │   ├── keys (3)
    │       │       │   │   └── li (464) — [text]
    │       │       │   └── values (3)
    │       │       │       └── li (464)
    │       │       │           ├── ID (59) — [text]
    │       │       │           ├── mount (59) — [text]
    │       │       │           ├── pawn (59) — [text]
    │       │       │           ├── reservedBy (59) — [text]
    │       │       │           ├── reservedMount (59) — [text]
    │       │       │           └── drawOffset (11) — [text]
    │       │       ├── tickCounter (3) — [text]
    │       │       ├── ActiveLevel (1) — [text]
    │       │       ├── AlertLevelsList (1)
    │       │       ├── AnimalActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── AnimalLinks (1)
    │       │       │   └── li (3)
    │       │       │       ├── animal (3) — [text]
    │       │       │       ├── area (3) — [text]
    │       │       │       ├── followDrafted (3) — [text]
    │       │       │       ├── followFieldwork (3) — [text]
    │       │       │       ├── foodPolicy (3) — [text]
    │       │       │       ├── mapId (3) — [text]
    │       │       │       ├── master (3) — [text]
    │       │       │       └── zone (3) — [text]
    │       │       ├── AnimalPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── AssignActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── AssignLinks (1)
    │       │       │   └── li (7)
    │       │       │       ├── colonist (7) — [text]
    │       │       │       ├── compositableState (7) — [text]
    │       │       │       ├── drugPolicy (7) — [text]
    │       │       │       ├── foodPolicy (7) — [text]
    │       │       │       ├── hostilityResponse (7) — [text]
    │       │       │       ├── loadoutId (7) — [text]
    │       │       │       ├── mapId (7) — [text]
    │       │       │       ├── medcare (7) — [text]
    │       │       │       ├── outfit (7) — [text]
    │       │       │       ├── readingPolicy (7) — [text]
    │       │       │       └── zone (7) — [text]
    │       │       ├── AssignPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── DefaultDrugPolicy (1) — [text]
    │       │       ├── DefaultFoodPolicy (1) — [text]
    │       │       ├── DefaultOutfit (1) — [text]
    │       │       ├── DefaultPrisonerFoodPolicy (1) — [text]
    │       │       ├── DefaultReadingPolicy (1) — [text]
    │       │       ├── DefaultSlaveDrugPolicy (1) — [text]
    │       │       ├── DefaultSlaveFoodPolicy (1) — [text]
    │       │       ├── DefaultSlaveOutfit (1) — [text]
    │       │       ├── DefaultSlaveReadingPolicy (1) — [text]
    │       │       ├── MechActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── MechLinks (1)
    │       │       ├── MechPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── Numbers_Numbers_MainTable (1)
    │       │       │   └── li (15) — [text]
    │       │       ├── Queue (1)
    │       │       │   └── li (12) — [text]
    │       │       ├── RestrictActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── RestrictPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── ScheduleLinks (1)
    │       │       │   └── li (7)
    │       │       │       ├── area (7) — [text]
    │       │       │       ├── colonist (7) — [text]
    │       │       │       ├── mapId (7) — [text]
    │       │       │       ├── schedule (7)
    │       │       │       │   └── li (168) — [text]
    │       │       │       └── zone (7) — [text]
    │       │       ├── TA_Expose_Numbers (1)
    │       │       │   ├── keys (1)
    │       │       │   │   └── li (14) — [text]
    │       │       │   └── values (1)
    │       │       │       └── li (14) — [text]
    │       │       ├── TA_Expose_People (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── TA_Expose_People_isSaved (1) — [text]
    │       │       ├── TA_Expose_TabCostSettings (1)
    │       │       │   ├── keys (1)
    │       │       │   │   └── li (1) — [text]
    │       │       │   └── values (1)
    │       │       │       └── li (1) — [text]
    │       │       ├── USH_PawnSkinColors (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── WeaponsActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── WeaponsLinks (1)
    │       │       │   └── li (6)
    │       │       │       ├── loadoutId (6) — [text]
    │       │       │       ├── mapId (6) — [text]
    │       │       │       ├── pawn (6) — [text]
    │       │       │       └── zone (6) — [text]
    │       │       ├── WeaponsPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── WorkActivePolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── activePolicy (1)
    │       │       │       │   ├── id (1) — [text]
    │       │       │       │   └── label (1) — [text]
    │       │       │       └── mapId (1) — [text]
    │       │       ├── WorkLinks (1)
    │       │       │   └── li (7)
    │       │       │       ├── colonist (7) — [text]
    │       │       │       ├── mapId (7) — [text]
    │       │       │       ├── settings (7)
    │       │       │       │   ├── keys (7)
    │       │       │       │   │   └── li (364) — [text]
    │       │       │       │   └── values (7)
    │       │       │       │       └── li (364) — [text]
    │       │       │       ├── settingsInner (7)
    │       │       │       │   ├── keys (7)
    │       │       │       │   │   └── li (1,554) — [text]
    │       │       │       │   └── values (7)
    │       │       │       │       └── li (1,554) — [text]
    │       │       │       └── zone (7) — [text]
    │       │       ├── WorkPolicies (1)
    │       │       │   └── li (1)
    │       │       │       ├── id (1) — [text]
    │       │       │       └── label (1) — [text]
    │       │       ├── active (1) — [text]
    │       │       ├── badSpots (1)
    │       │       ├── billsSelectedGroup (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── blueprintsFolder (1) — [text]
    │       │       ├── caravanGroups (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_and_random_mood (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_bonfire_tracker (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_booze_tracker (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_caravan_tracker (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_illness_tracker (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonist_scar_counter (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── colonyGroups (1)
    │       │       │   ├── keys (1)
    │       │       │   │   └── li (1) — [text]
    │       │       │   └── values (1)
    │       │       │       └── li (1)
    │       │       │           ├── activeWorkTypes (1)
    │       │       │           │   ├── keys (1)
    │       │       │           │   └── values (1)
    │       │       │           ├── colorFolder (1) — [text]
    │       │       │           ├── entireGroupIsVisible (1) — [text]
    │       │       │           ├── formations (1)
    │       │       │           ├── groupApparelPolicy (1) — [text]
    │       │       │           ├── groupArea (1) — [text]
    │       │       │           ├── groupBannerFolder (1) — [text]
    │       │       │           ├── groupColor (1) — attrs: [IsNull]
    │       │       │           ├── groupDrugPolicy (1) — [text]
    │       │       │           ├── groupFoodPolicy (1) — [text]
    │       │       │           ├── groupID (1) — [text]
    │       │       │           ├── groupIconFolder (1) — [text]
    │       │       │           ├── groupWorkPriorities (1)
    │       │       │           │   ├── keys (1)
    │       │       │           │   └── values (1)
    │       │       │           ├── isColonyGroup (1) — [text]
    │       │       │           ├── map (1) — [text]
    │       │       │           ├── pawnIcons (1)
    │       │       │           │   ├── keys (1)
    │       │       │           │   │   └── li (7) — [text]
    │       │       │           │   └── values (1)
    │       │       │           │       └── li (7)
    │       │       │           │           ├── pawn (7) — [text]
    │       │       │           │           └── visible (7) — [text]
    │       │       │           ├── pawns (1)
    │       │       │           │   └── li (7) — [text]
    │       │       │           └── temporaryWorkers (1)
    │       │       │               ├── keys (1)
    │       │       │               └── values (1)
    │       │       ├── currentBestLeaderPawn (1) — [text]
    │       │       ├── currentBestMeleeLeaderPawn (1) — [text]
    │       │       ├── currentPsycasterLeaderPawn (1) — [text]
    │       │       ├── currentTitleLeaderPawn (1) — [text]
    │       │       ├── currentWorldPollution (1) — [text]
    │       │       ├── cycleIndex (1) — [text]
    │       │       ├── deadCountKey (1)
    │       │       ├── enslavedPawns (1)
    │       │       ├── eventQueue (1)
    │       │       ├── extraSiteData (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── goodwillImpacts (1)
    │       │       ├── gravship (1) — [text]
    │       │       ├── hireable (1) — [text]
    │       │       ├── ignoredFactions (1)
    │       │       │   └── li (39) — [text]
    │       │       ├── initialized (1) — [text]
    │       │       ├── joblist (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── landingMap (1) — [text]
    │       │       ├── landingMarker (1) — attrs: [IsNull]
    │       │       ├── lastFoundSignal (1) — [text]
    │       │       ├── linkedBillsSets (1)
    │       │       │   └── li (7)
    │       │       │       └── Bills (7)
    │       │       │           └── li (14) — [text]
    │       │       ├── mapSeeds (1)
    │       │       │   ├── keys (1)
    │       │       │   │   └── li (1) — [text]
    │       │       │   └── values (1)
    │       │       │       └── li (1) — [text]
    │       │       ├── mapsParent (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── mostSkilledPawn (1) — [text]
    │       │       ├── partyHunt (1)
    │       │       │   └── pawns (1)
    │       │       ├── pawnGroups (1)
    │       │       │   └── li (1)
    │       │       │       ├── activeWorkTypes (1)
    │       │       │       │   ├── keys (1)
    │       │       │       │   └── values (1)
    │       │       │       ├── colorFolder (1) — [text]
    │       │       │       ├── entireGroupIsVisible (1) — [text]
    │       │       │       ├── formations (1)
    │       │       │       ├── formerPawns (1)
    │       │       │       ├── groupApparelPolicy (1) — [text]
    │       │       │       ├── groupArea (1) — [text]
    │       │       │       ├── groupBannerFolder (1) — [text]
    │       │       │       ├── groupColor (1) — attrs: [IsNull]
    │       │       │       ├── groupDrugPolicy (1) — [text]
    │       │       │       ├── groupFoodPolicy (1) — [text]
    │       │       │       ├── groupID (1) — [text]
    │       │       │       ├── groupIconFolder (1) — [text]
    │       │       │       ├── groupName (1) — [text]
    │       │       │       ├── groupWorkPriorities (1)
    │       │       │       │   ├── keys (1)
    │       │       │       │   └── values (1)
    │       │       │       ├── isPawnGroup (1) — [text]
    │       │       │       ├── pawnIcons (1)
    │       │       │       │   ├── keys (1)
    │       │       │       │   │   └── li (4) — [text]
    │       │       │       │   └── values (1)
    │       │       │       │       └── li (4)
    │       │       │       │           ├── pawn (4) — [text]
    │       │       │       │           └── visible (4) — [text]
    │       │       │       ├── pawns (1)
    │       │       │       │   └── li (4) — [text]
    │       │       │       ├── prevColonyGroup (1) — [text]
    │       │       │       └── temporaryWorkers (1)
    │       │       │           ├── keys (1)
    │       │       │           └── values (1)
    │       │       ├── pawnSquads (1)
    │       │       ├── pawns (1)
    │       │       ├── pawnsWithNightOwl (1)
    │       │       ├── plotMissions (1)
    │       │       ├── remoteMapIds (1)
    │       │       ├── savedPositions (1)
    │       │       │   └── li (7)
    │       │       │       ├── owner (7) — [text]
    │       │       │       └── positions (7)
    │       │       │           └── li (4)
    │       │       │               ├── map (4) — [text]
    │       │       │               └── positions (4)
    │       │       │                   └── li (16) — [text]
    │       │       ├── serviceQuests (1)
    │       │       ├── stripMine (1) — attrs: [IsNull]
    │       │       ├── takeoffMap (1) — [text]
    │       │       ├── tickCounterBoozeAndScars (1) — [text]
    │       │       ├── tickCounterMelee (1) — [text]
    │       │       ├── tickCounterMood (1) — [text]
    │       │       ├── tickCounterTravel (1) — [text]
    │       │       ├── ticksToNextAssault (1) — [text]
    │       │       ├── ticksToNextQuest (1) — [text]
    │       │       ├── ticksWithoutAbandoning (1) — [text]
    │       │       ├── ticksWithoutTrading (1) — [text]
    │       │       ├── titheInfo (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── titleHolders (1)
    │       │       │   └── li (136) — [text]
    │       │       ├── totalWorldPollution (1) — [text]
    │       │       ├── visiblePawns (1)
    │       │       ├── warProgressDict (1) — attrs: [IsNull]
    │       │       └── worktableRestrictionDictonary (1)
    │       │           ├── keys (1)
    │       │           │   └── li (9) — [text]
    │       │           └── values (1)
    │       │               └── li (9)
    │       │                   └── restrictionPawn (9) — [text]
    │       ├── factionManager (1)
    │       │   ├── allFactions (1)
    │       │   │   └── li (21)
    │       │   │       ├── colorFromSpectrum (21) — [text]
    │       │   │       ├── def (21) — [text]
    │       │   │       ├── ideos (21) — attrs: [IsNull]
    │       │   │       │   ├── ideosMinor (17)
    │       │   │       │   │   └── li (1) — [text]
    │       │   │       │   └── primaryIdeo (17) — [text]
    │       │   │       ├── kidnapped (21)
    │       │   │       │   └── kidnappedPawns (21)
    │       │   │       ├── leader (21) — [text]
    │       │   │       ├── loadID (21) — [text]
    │       │   │       ├── name (21) — [text]
    │       │   │       ├── predatorThreats (21)
    │       │   │       ├── questTags (21) — attrs: [IsNull]
    │       │   │       ├── randomKey (21) — [text]
    │       │   │       ├── relations (21)
    │       │   │       │   └── li (420)
    │       │   │       │       ├── other (420) — [text]
    │       │   │       │       ├── goodwill (384) — [text]
    │       │   │       │       └── kind (366) — [text]
    │       │   │       ├── naturalGoodwillTimer (5) — [text]
    │       │   │       ├── hidden (1) — [text]
    │       │   │       └── temporary (1) — [text]
    │       │   └── toRemove (1)
    │       ├── features (1)
    │       │   └── features (1)
    │       │       └── li (159)
    │       │           ├── def (159) — [text]
    │       │           ├── drawCenter (159) — [text]
    │       │           ├── layer (159) — [text]
    │       │           ├── name (159) — [text]
    │       │           ├── uniqueID (159) — [text]
    │       │           └── maxDrawSizeInTiles (147) — [text]
    │       ├── gameConditionManager (1)
    │       │   ├── activeConditions (1)
    │       │   └── mapBrightnessTracker (1) — attrs: [IsNull]
    │       ├── grid (1)
    │       │   ├── layers (1)
    │       │   │   ├── keys (1)
    │       │   │   │   └── li (2) — [text]
    │       │   │   └── values (1)
    │       │   │       └── li (2) — attrs: [Class]
    │       │   │           ├── connections (2)
    │       │   │           │   ├── keys (2)
    │       │   │           │   │   └── li (2) — [text]
    │       │   │           │   └── values (2)
    │       │   │           │       └── li (2)
    │       │   │           │           ├── origin (2) — [text]
    │       │   │           │           └── target (2) — [text]
    │       │   │           ├── def (2) — [text]
    │       │   │           ├── layerId (2) — [text]
    │       │   │           ├── radius (2) — [text]
    │       │   │           ├── scenarioTag (2) — [text]
    │       │   │           ├── subdivisions (2) — [text]
    │       │   │           ├── tileBiomeDeflate (2) — [text]
    │       │   │           ├── viewAngle (2) — [text]
    │       │   │           ├── viewCenter (2) — [text]
    │       │   │           ├── zoomInToLayer (2) — [text]
    │       │   │           ├── zoomOutToLayer (2) — [text]
    │       │   │           ├── backgroundWorldCameraOffset (1) — [text]
    │       │   │           ├── backgroundWorldCameraParallaxDistance (1) — [text]
    │       │   │           ├── extraCameraAltitude (1) — [text]
    │       │   │           ├── isRootSurface (1) — [text]
    │       │   │           ├── tileElevationDeflate (1) — [text]
    │       │   │           ├── tileFeatureDeflate (1) — [text]
    │       │   │           ├── tileHillinessDeflate (1) — [text]
    │       │   │           ├── tileMutatorDefsDeflate (1) — [text]
    │       │   │           ├── tileMutatorTilesDeflate (1) — [text]
    │       │   │           ├── tilePollutionDeflate (1) — [text]
    │       │   │           ├── tileRainfallDeflate (1) — [text]
    │       │   │           ├── tileRiverAdjacencyDeflate (1) — [text]
    │       │   │           ├── tileRiverDefDeflate (1) — [text]
    │       │   │           ├── tileRiverDistancesDeflate (1) — [text]
    │       │   │           ├── tileRiverOriginsDeflate (1) — [text]
    │       │   │           ├── tileRoadAdjacencyDeflate (1) — [text]
    │       │   │           ├── tileRoadDefDeflate (1) — [text]
    │       │   │           ├── tileRoadOriginsDeflate (1) — [text]
    │       │   │           ├── tileSwampinessDeflate (1) — [text]
    │       │   │           └── tileTemperatureDeflate (1) — [text]
    │       │   └── nextLayerId (1) — [text]
    │       ├── ideoManager (1)
    │       │   ├── ideos (1)
    │       │   │   └── li (15)
    │       │   │       ├── adjective (15) — [text]
    │       │   │       ├── colorDef (15) — [text]
    │       │   │       ├── culture (15) — [text]
    │       │   │       ├── description (15) — [text]
    │       │   │       ├── descriptionTemplate (15) — [text]
    │       │   │       ├── development (15) — attrs: [IsNull]
    │       │   │       ├── foundation (15) — attrs: [Class]
    │       │   │       │   ├── def (15) — [text]
    │       │   │       │   ├── deities (15)
    │       │   │       │   │   └── li (9)
    │       │   │       │   │       ├── gender (9) — [text]
    │       │   │       │   │       ├── iconPath (9) — [text]
    │       │   │       │   │       ├── name (9) — [text]
    │       │   │       │   │       ├── type (9) — [text]
    │       │   │       │   │       └── relatedMeme (8) — [text]
    │       │   │       │   └── place (15) — [text]
    │       │   │       ├── iconDef (15) — [text]
    │       │   │       ├── id (15) — [text]
    │       │   │       ├── leaderTitleFemale (15) — [text]
    │       │   │       ├── leaderTitleMale (15) — [text]
    │       │   │       ├── memberName (15) — [text]
    │       │   │       ├── memes (15)
    │       │   │       │   └── li (45) — [text]
    │       │   │       ├── name (15) — [text]
    │       │   │       ├── precepts (15)
    │       │   │       │   └── li (893) — attrs: [Class]
    │       │   │       │       ├── ID (893) — [text]
    │       │   │       │       ├── def (893) — [text]
    │       │   │       │       ├── name (893) — [text]
    │       │   │       │       ├── randomSeed (893) — [text]
    │       │   │       │       ├── usesDefiniteArticle (893) — [text]
    │       │   │       │       ├── activeObligations (268) — attrs: [IsNull]
    │       │   │       │       ├── behavior (268) — attrs: [Class]
    │       │   │       │       │   ├── def (268) — [text]
    │       │   │       │       │   ├── startAbility (15) — [text]
    │       │   │       │       │   └── storedLords (15)
    │       │   │       │       │       ├── keys (15)
    │       │   │       │       │       └── values (15)
    │       │   │       │       ├── completedObligations (268) — attrs: [IsNull]
    │       │   │       │       ├── generatedAttachedReward (268) — [text]
    │       │   │       │       ├── lastFinishedTick (268) — [text]
    │       │   │       │       ├── layerBlacklist (268) — attrs: [IsNull]
    │       │   │       │       │   └── li (8) — [text]
    │       │   │       │       ├── layerWhitelist (268) — attrs: [IsNull]
    │       │   │       │       ├── obligationTargetFilter (268) — attrs: [Class, IsNull]
    │       │   │       │       │   ├── def (163) — [text]
    │       │   │       │       │   └── parent (163) — [text]
    │       │   │       │       ├── outcomeEffect (268) — attrs: [Class]
    │       │   │       │       │   ├── compDatas (268)
    │       │   │       │       │   │   └── li (774) — attrs: [Class, IsNull]
    │       │   │       │       │   │       └── presentForTicks (231)
    │       │   │       │       │   │           ├── keys (231)
    │       │   │       │       │   │           └── values (231)
    │       │   │       │       │   └── def (268) — [text]
    │       │   │       │       ├── sourcePattern (268) — [text]
    │       │   │       │       ├── targetFilter (268) — attrs: [Class, IsNull]
    │       │   │       │       │   └── def (165) — [text]
    │       │   │       │       ├── triggers (268)
    │       │   │       │       │   └── li (37) — attrs: [Class]
    │       │   │       │       │       ├── mustBePlayerIdeo (37) — [text]
    │       │   │       │       │       └── triggerDaysSinceStartOfYear (20) — [text]
    │       │   │       │       ├── isAnytime (137) — [text]
    │       │   │       │       ├── ritualOnlyForIdeoMembers (112) — [text]
    │       │   │       │       ├── playsIdeoMusic (111) — [text]
    │       │   │       │       ├── thingDef (86) — [text]
    │       │   │       │       ├── attachableOutcomeEffect (56) — [text]
    │       │   │       │       ├── iconPathOverride (50) — [text]
    │       │   │       │       ├── apparelRequirements (45)
    │       │   │       │       │   └── li (53)
    │       │   │       │       │       ├── allowedFactionCategoryTags (53) — attrs: [IsNull]
    │       │   │       │       │       │   └── li (1) — [text]
    │       │   │       │       │       ├── anyMemeRequired (53) — attrs: [IsNull]
    │       │   │       │       │       │   └── li (3) — [text]
    │       │   │       │       │       ├── disallowedFactionCategoryTags (53) — attrs: [IsNull]
    │       │   │       │       │       │   └── li (3) — [text]
    │       │   │       │       │       └── requirement (53)
    │       │   │       │       │           ├── allowedTags (53) — attrs: [IsNull]
    │       │   │       │       │           ├── bodyPartGroupsMatchAny (53)
    │       │   │       │       │           │   └── li (127) — [text]
    │       │   │       │       │           ├── requiredDefs (53) — attrs: [IsNull]
    │       │   │       │       │           │   └── li (46) — [text]
    │       │   │       │       │           └── requiredTags (53) — attrs: [IsNull]
    │       │   │       │       │               └── li (7) — [text]
    │       │   │       │       ├── nameMaker (42) — [text]
    │       │   │       │       ├── generatedRelic (38) — [text]
    │       │   │       │       ├── ritualExpectedDesc (36) — [text]
    │       │   │       │       ├── chosenPawn (31)
    │       │   │       │       │   ├── abilities (31)
    │       │   │       │       │   │   └── li (211)
    │       │   │       │       │   │       ├── Id (211) — [text]
    │       │   │       │       │   │       ├── charges (211) — [text]
    │       │   │       │       │   │       ├── def (211) — [text]
    │       │   │       │       │   │       ├── maxCharges (211) — [text]
    │       │   │       │       │   │       ├── sourcePrecept (211) — [text]
    │       │   │       │       │   │       └── verbTracker (211)
    │       │   │       │       │   │           └── verbs (211)
    │       │   │       │       │   │               └── li (211) — attrs: [Class]
    │       │   │       │       │   │                   ├── MVCF_ManagedVerb (211) — attrs: [IsNull]
    │       │   │       │       │   │                   ├── ability (211) — [text]
    │       │   │       │       │   │                   ├── canHitNonTargetPawnsNow (211) — [text]
    │       │   │       │       │   │                   ├── currentDestination (211) — [text]
    │       │   │       │       │   │                   ├── currentTarget (211) — [text]
    │       │   │       │       │   │                   ├── lastShotTick (211) — [text]
    │       │   │       │       │   │                   └── loadID (211) — [text]
    │       │   │       │       │   └── pawn (31) — [text]
    │       │   │       │       ├── active (30) — [text]
    │       │   │       │       ├── canMergeGizmosFromDifferentIdeos (30) — [text]
    │       │   │       │       ├── canBeAnytime (26) — [text]
    │       │   │       │       ├── presenceDemand (25)
    │       │   │       │       │   ├── ID (25) — [text]
    │       │   │       │       │   ├── minExpectation (25) — [text]
    │       │   │       │       │   └── roomRequirements (25)
    │       │   │       │       │       └── li (86) — attrs: [Class]
    │       │   │       │       │           ├── labelKey (60) — [text]
    │       │   │       │       │           ├── buildingTags (50)
    │       │   │       │       │           │   └── li (50) — [text]
    │       │   │       │       │           ├── count (11) — [text]
    │       │   │       │       │           ├── things (11)
    │       │   │       │       │           │   └── li (55) — [text]
    │       │   │       │       │           ├── tags (10)
    │       │   │       │       │           │   └── li (20) — [text]
    │       │   │       │       │           ├── impressiveness (9) — [text]
    │       │   │       │       │           └── area (6) — [text]
    │       │   │       │       ├── restrictToSupremeGender (23) — [text]
    │       │   │       │       ├── patternGroupTag (21) — [text]
    │       │   │       │       ├── allowOtherInstances (15) — [text]
    │       │   │       │       ├── ignoreExtremeTemperatures (15) — [text]
    │       │   │       │       ├── ritualExpectedDescNoAdjective (15) — [text]
    │       │   │       │       ├── ritualExplanation (15) — [text]
    │       │   │       │       ├── stuff (15) — [text]
    │       │   │       │       ├── chosenPawns (14)
    │       │   │       │       ├── chosenPawnsCache (14)
    │       │   │       │       ├── descOverride (13) — [text]
    │       │   │       │       ├── shortDescOverride (12) — [text]
    │       │   │       │       ├── despised (6) — [text]
    │       │   │       │       ├── noble (6) — [text]
    │       │   │       │       ├── customXenotype (2) — attrs: [IsNull]
    │       │   │       │       ├── xenotype (2) — [text]
    │       │   │       │       ├── apparelDef (1) — [text]
    │       │   │       │       ├── mergeGizmosForObligations (1) — [text]
    │       │   │       │       └── minTechLevel (1) — [text]
    │       │   │       ├── style (15)
    │       │   │       │   ├── beardFrequencies (15)
    │       │   │       │   │   └── vals (15)
    │       │   │       │   │       └── li (615)
    │       │   │       │   │           ├── frequency (250) — [text]
    │       │   │       │   │           └── gender (165) — [text]
    │       │   │       │   ├── hairFrequencies (15)
    │       │   │       │   │   └── vals (15)
    │       │   │       │   │       └── li (1,200)
    │       │   │       │   │           ├── gender (915) — [text]
    │       │   │       │   │           └── frequency (348) — [text]
    │       │   │       │   ├── styleForThingDef (15)
    │       │   │       │   │   ├── keys (15)
    │       │   │       │   │   │   └── li (39) — [text]
    │       │   │       │   │   └── values (15)
    │       │   │       │   │       └── li (39)
    │       │   │       │   │           ├── category (39) — [text]
    │       │   │       │   │           └── styleDef (39) — [text]
    │       │   │       │   └── tattooFrequencies (15)
    │       │   │       │       └── vals (15)
    │       │   │       │           └── li (465)
    │       │   │       │               ├── gender (465) — [text]
    │       │   │       │               └── frequency (102) — [text]
    │       │   │       ├── thingStyleCategories (15)
    │       │   │       │   └── li (20)
    │       │   │       │       ├── category (20) — [text]
    │       │   │       │       └── priority (20) — [text]
    │       │   │       ├── usedSymbolPacks (15)
    │       │   │       │   └── li (14) — [text]
    │       │   │       ├── usedSymbols (15)
    │       │   │       │   └── li (45) — [text]
    │       │   │       ├── primaryFactionColor (14) — [text]
    │       │   │       ├── hidden (1) — [text]
    │       │   │       ├── initialPlayerIdeo (1) — [text]
    │       │   │       └── solid (1) — [text]
    │       │   ├── selectedStyleCategories (1)
    │       │   ├── ticksToNextGauranlenSpawn (1) — [text]
    │       │   └── toRemove (1)
    │       ├── info (1)
    │       │   ├── factions (1)
    │       │   │   └── li (19) — [text]
    │       │   ├── initialMapSize (1) — [text]
    │       │   ├── name (1) — [text]
    │       │   ├── overallRainfall (1) — [text]
    │       │   ├── overallTemperature (1) — [text]
    │       │   ├── persistentRandomValue (1) — [text]
    │       │   ├── planetCoverage (1) — [text]
    │       │   ├── pollution (1) — [text]
    │       │   └── seedString (1) — [text]
    │       ├── landmarks (1)
    │       │   └── landmarks (1)
    │       │       ├── keys (1)
    │       │       │   └── li (657) — [text]
    │       │       └── values (1)
    │       │           └── li (657)
    │       │               ├── def (657) — [text]
    │       │               ├── name (657) — [text]
    │       │               └── isComboLandmark (25) — [text]
    │       ├── pocketMaps (1)
    │       ├── storyState (1)
    │       │   ├── colonistCountTicks (1)
    │       │   │   ├── keys (1)
    │       │   │   │   └── li (4) — [text]
    │       │   │   └── values (1)
    │       │   │       └── li (4) — [text]
    │       │   ├── lastFireTicks (1)
    │       │   │   ├── keys (1)
    │       │   │   │   └── li (13) — [text]
    │       │   │   └── values (1)
    │       │   │       └── li (13) — [text]
    │       │   ├── lastRaidFaction (1) — [text]
    │       │   ├── lastRoyalFavorQuestTick (1) — [text]
    │       │   ├── lastThreatBigTick (1) — [text]
    │       │   ├── recentRandomDecrees (1)
    │       │   ├── recentRandomIncidents (1)
    │       │   │   └── li (2) — [text]
    │       │   └── recentRandomQuests (1)
    │       │       └── li (2) — [text]
    │       ├── worldObjects (1)
    │       │   └── worldObjects (1)
    │       │       └── li (441) — attrs: [Class]
    │       │           ├── ID (441) — [text]
    │       │           ├── def (441) — [text]
    │       │           ├── faction (441) — [text]
    │       │           ├── questTags (441) — attrs: [IsNull]
    │       │           │   └── li (9) — [text]
    │       │           ├── tile (441) — [text]
    │       │           ├── tickDelta (407) — [text]
    │       │           ├── nameInt (383) — [text]
    │       │           ├── previouslyGeneratedInhabitants (371)
    │       │           ├── trader (371)
    │       │           │   ├── lastStockGenerationTicks (371) — [text]
    │       │           │   ├── stock (371) — attrs: [IsNull]
    │       │           │   └── tmpSavedPawns (371)
    │       │           ├── expiration (357) — [text]
    │       │           ├── approximateSnapshotCost (50) — [text]
    │       │           ├── blueprintName (50) — [text]
    │       │           ├── gameName (50) — [text]
    │       │           ├── originX (50) — [text]
    │       │           ├── originZ (50) — [text]
    │       │           ├── originalFaction (50) — [text]
    │       │           ├── wealthOnEnter (50) — [text]
    │       │           ├── bedsCount (47) — [text]
    │       │           ├── poiType (46) — [text]
    │       │           ├── militaryPower (23) — [text]
    │       │           ├── isGeneratedLocation (12) — [text]
    │       │           ├── preciousResource (12) — [text]
    │       │           ├── creationGameTicks (8) — [text]
    │       │           ├── timeoutEndTick (7) — [text]
    │       │           ├── contents (6) — attrs: [Class]
    │       │           │   └── innerList (6)
    │       │           ├── core (6) — attrs: [IsNull]
    │       │           ├── expireSignal (6) — attrs: [IsNull]
    │       │           ├── mannableCount (6) — [text]
    │       │           ├── parts (6)
    │       │           │   └── li (7)
    │       │           │       ├── conditionCauser (7) — attrs: [IsNull]
    │       │           │       ├── def (7) — [text]
    │       │           │       ├── lootThings (7) — attrs: [IsNull]
    │       │           │       │   └── li (5)
    │       │           │       │       ├── count (5) — [text]
    │       │           │       │       └── thingDef (5) — [text]
    │       │           │       ├── parms (7)
    │       │           │       │   ├── ancientComplexSketch (7) — attrs: [IsNull]
    │       │           │       │   ├── relic (7) — [text]
    │       │           │       │   ├── relicThing (7) — [text]
    │       │           │       │   ├── randomValue (3) — [text]
    │       │           │       │   └── threatPoints (3) — [text]
    │       │           │       ├── relicThing (7) — attrs: [IsNull]
    │       │           │       ├── things (7) — attrs: [Class, IsNull]
    │       │           │       │   ├── dontTickContents (3) — [text]
    │       │           │       │   └── innerList (3)
    │       │           │       │       └── li (5) — attrs: [Class]
    │       │           │       │           ├── def (5) — [text]
    │       │           │       │           ├── despawnedTick (5) — [text]
    │       │           │       │           ├── id (5) — [text]
    │       │           │       │           ├── questTags (5) — attrs: [IsNull]
    │       │           │       │           ├── stackCount (5) — [text]
    │       │           │       │           ├── health (4) — [text]
    │       │           │       │           ├── verbTracker (2)
    │       │           │       │           │   └── verbs (2) — attrs: [IsNull]
    │       │           │       │           └── ingredients (1)
    │       │           │       └── expectedEnemyCount (3) — [text]
    │       │           ├── prisoner (6)
    │       │           │   ├── innerList (6)
    │       │           │   └── maxStacks (6) — [text]
    │       │           ├── refugee (6)
    │       │           │   ├── innerList (6)
    │       │           │   └── maxStacks (6) — [text]
    │       │           ├── requestingFaction (6) — [text]
    │       │           ├── rewards (6) — attrs: [Class]
    │       │           │   └── innerList (6)
    │       │           ├── successSignal (6) — attrs: [IsNull]
    │       │           ├── unlockTargetTime (6) — [text]
    │       │           ├── desiredThreatPoints (4) — [text]
    │       │           ├── factionMustRemainHostile (4) — [text]
    │       │           ├── customLabel (1) — [text]
    │       │           └── namedByPlayer (1) — [text]
    │       └── worldPawns (1)
    │           ├── gc (1)
    │           │   └── lastSuccessfulGCTick (1) — [text]
    │           ├── pawnsAlive (1)
    │           │   └── li (2)
    │           │       ├── MVCF_VerbManager (2) — attrs: [IsNull]
    │           │       │   └── currentVerb (1) — [text]
    │           │       ├── ThingsHauledToInventory (2)
    │           │       ├── abilities (2)
    │           │       │   └── abilities (2)
    │           │       ├── ageTracker (2)
    │           │       │   ├── ageBiologicalTicks (2) — [text]
    │           │       │   ├── ageReversalDemandedAtAgeTicks (2) — [text]
    │           │       │   ├── birthAbsTicks (2) — [text]
    │           │       │   ├── growth (2) — [text]
    │           │       │   └── nextGrowthCheckTick (2) — [text]
    │           │       ├── apparel (2)
    │           │       │   ├── lastApparelWearoutTick (2) — [text]
    │           │       │   ├── lockedApparel (2) — attrs: [IsNull]
    │           │       │   └── wornApparel (2)
    │           │       │       └── innerList (2)
    │           │       │           └── li (6)
    │           │       │               ├── abilities (6)
    │           │       │               ├── def (6) — [text]
    │           │       │               ├── despawnedTick (6) — [text]
    │           │       │               ├── health (6) — [text]
    │           │       │               ├── id (6) — [text]
    │           │       │               ├── quality (6) — [text]
    │           │       │               ├── questTags (6) — attrs: [IsNull]
    │           │       │               ├── sourcePrecept (6) — [text]
    │           │       │               ├── stackCount (6) — [text]
    │           │       │               ├── stuff (5) — [text]
    │           │       │               ├── codedPawn (1) — [text]
    │           │       │               ├── color (1) — [text]
    │           │       │               ├── colorActive (1) — [text]
    │           │       │               └── styleDef (1) — [text]
    │           │       ├── bed (2) — [text]
    │           │       ├── boughtItems (2)
    │           │       ├── carryTracker (2)
    │           │       │   └── innerContainer (2)
    │           │       │       ├── innerList (2)
    │           │       │       └── maxStacks (2) — [text]
    │           │       ├── connections (2)
    │           │       │   └── connectedThings (2)
    │           │       ├── creepjoiner (2) — attrs: [IsNull]
    │           │       ├── currentlyCasting (2) — [text]
    │           │       ├── currentlyCastingTargets (2)
    │           │       ├── deadlifeDustFaction (2) — [text]
    │           │       ├── def (2) — [text]
    │           │       ├── despawnedTick (2) — [text]
    │           │       ├── drafter (2) — attrs: [IsNull]
    │           │       ├── drugs (2) — attrs: [IsNull]
    │           │       ├── duplicate (2)
    │           │       ├── equipment (2)
    │           │       │   ├── bondedWeapon (2) — [text]
    │           │       │   └── equipment (2)
    │           │       │       └── innerList (2)
    │           │       │           └── li (2)
    │           │       │               ├── def (2) — [text]
    │           │       │               ├── despawnedTick (2) — [text]
    │           │       │               ├── health (2) — [text]
    │           │       │               ├── id (2) — [text]
    │           │       │               ├── quality (2) — [text]
    │           │       │               ├── questTags (2) — attrs: [IsNull]
    │           │       │               ├── sourcePrecept (2) — [text]
    │           │       │               ├── stackCount (2) — [text]
    │           │       │               ├── taleRef (2) — attrs: [IsNull]
    │           │       │               │   ├── seed (1) — [text]
    │           │       │               │   └── tale (1) — [text]
    │           │       │               ├── verbTracker (2)
    │           │       │               │   └── verbs (2)
    │           │       │               │       └── li (8) — attrs: [Class]
    │           │       │               │           ├── MVCF_ManagedVerb (8)
    │           │       │               │           │   ├── enabled (8) — [text]
    │           │       │               │           │   └── loadId (8) — [text]
    │           │       │               │           ├── canHitNonTargetPawnsNow (8) — [text]
    │           │       │               │           ├── lastShotTick (8) — [text]
    │           │       │               │           └── loadID (8) — [text]
    │           │       │               ├── biocoded (1) — [text]
    │           │       │               ├── biocodedPawnLabel (1) — [text]
    │           │       │               ├── codedPawn (1) — [text]
    │           │       │               ├── innerContainer (1) — attrs: [Class]
    │           │       │               │   └── innerList (1)
    │           │       │               └── title (1) — [text]
    │           │       ├── faction (2) — [text]
    │           │       ├── filth (2) — attrs: [IsNull]
    │           │       ├── flight (2) — attrs: [IsNull]
    │           │       ├── foodRestriction (2) — attrs: [IsNull]
    │           │       ├── gender (2) — [text]
    │           │       ├── genes (2)
    │           │       │   ├── endogenes (2)
    │           │       │   │   └── li (4)
    │           │       │   │       ├── def (4) — [text]
    │           │       │   │       ├── loadID (4) — [text]
    │           │       │   │       ├── overriddenByGene (4) — [text]
    │           │       │   │       └── pawn (4) — [text]
    │           │       │   ├── xenogenes (2)
    │           │       │   └── xenotype (2) — [text]
    │           │       ├── guest (2)
    │           │       │   ├── enabledNonExclusiveInteractions (2)
    │           │       │   ├── finalResistanceInteractionData (2) — attrs: [IsNull]
    │           │       │   ├── hostFaction (2) — [text]
    │           │       │   ├── ideoForConversion (2) — [text]
    │           │       │   ├── interactionMode (2) — [text]
    │           │       │   ├── joinStatus (2) — [text]
    │           │       │   ├── lastPrisonBreakTicks (2) — [text]
    │           │       │   ├── lastResistanceInteractionData (2) — attrs: [IsNull]
    │           │       │   ├── slaveFaction (2) — [text]
    │           │       │   ├── slaveInteractionMode (2) — [text]
    │           │       │   └── spotToWaitInsteadOfEscaping (2) — [text]
    │           │       ├── guestArea (2) — [text]
    │           │       ├── guilt (2)
    │           │       ├── healthTracker (2)
    │           │       │   ├── hediffSet (2)
    │           │       │   │   └── hediffs (2)
    │           │       │   │       └── li (7) — attrs: [Class]
    │           │       │   │           ├── abilities (7) — attrs: [IsNull]
    │           │       │   │           ├── ageTicks (7) — [text]
    │           │       │   │           ├── canBeThreateningToPart (7) — [text]
    │           │       │   │           ├── combatLogEntry (7) — [text]
    │           │       │   │           ├── def (7) — [text]
    │           │       │   │           ├── loadID (7) — [text]
    │           │       │   │           ├── severity (7) — [text]
    │           │       │   │           ├── visible (7) — [text]
    │           │       │   │           ├── part (5)
    │           │       │   │           │   ├── body (5) — [text]
    │           │       │   │           │   └── index (5) — [text]
    │           │       │   │           ├── isPermanent (4) — [text]
    │           │       │   │           ├── painCategory (4) — [text]
    │           │       │   │           ├── tickAdded (2) — [text]
    │           │       │   │           ├── disappearsAfterTicks (1) — [text]
    │           │       │   │           ├── infectionChanceFactor (1) — [text]
    │           │       │   │           ├── seed (1) — [text]
    │           │       │   │           ├── severityPerDay (1) — [text]
    │           │       │   │           └── ticksToDisappear (1) — [text]
    │           │       │   ├── immunity (2)
    │           │       │   │   └── imList (2)
    │           │       │   └── surgeryBills (2)
    │           │       │       └── bills (2)
    │           │       ├── id (2) — [text]
    │           │       ├── ideo (2)
    │           │       │   ├── babyIdeoExposure (2) — attrs: [IsNull]
    │           │       │   ├── certainty (2) — [text]
    │           │       │   ├── ideo (2) — [text]
    │           │       │   ├── previousIdeos (2)
    │           │       │   └── joinTick (1) — [text]
    │           │       ├── infectionVectors (2)
    │           │       │   ├── pathways (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   │   └── li (1) — [text]
    │           │       │   │   └── values (2)
    │           │       │   │       └── li (1)
    │           │       │   │           ├── ageTicks (1) — [text]
    │           │       │   │           ├── def (1) — [text]
    │           │       │   │           └── ownerPawn (1) — [text]
    │           │       │   └── givenPrearrival (1) — [text]
    │           │       ├── interactions (2) — attrs: [IsNull]
    │           │       ├── inventory (2)
    │           │       │   ├── innerContainer (2)
    │           │       │   │   └── innerList (2)
    │           │       │   │       └── li (3) — attrs: [Class]
    │           │       │   │           ├── def (3) — [text]
    │           │       │   │           ├── despawnedTick (3) — [text]
    │           │       │   │           ├── health (3) — [text]
    │           │       │   │           ├── id (3) — [text]
    │           │       │   │           ├── questTags (3) — attrs: [IsNull]
    │           │       │   │           ├── stackCount (3) — [text]
    │           │       │   │           ├── infectedPawns (1)
    │           │       │   │           ├── ingredients (1)
    │           │       │   │           └── verbTracker (1)
    │           │       │   │               └── verbs (1) — attrs: [IsNull]
    │           │       │   ├── itemsNotForSale (2)
    │           │       │   │   └── li (2) — [text]
    │           │       │   └── unpackedCaravanItems (2)
    │           │       ├── inventoryStock (2) — attrs: [IsNull]
    │           │       ├── isEnabled (2) — [text]
    │           │       ├── jobs (2)
    │           │       │   ├── curDriver (2) — attrs: [IsNull]
    │           │       │   ├── curJob (2) — attrs: [IsNull]
    │           │       │   ├── formingCaravanTick (2) — [text]
    │           │       │   └── jobQueue (2)
    │           │       │       └── jobs (2)
    │           │       ├── kindDef (2) — [text]
    │           │       ├── lastKeepDisplayTick (2) — [text]
    │           │       ├── lastStudiedTick (2) — [text]
    │           │       ├── learnedAbilities (2)
    │           │       ├── learning (2) — attrs: [IsNull]
    │           │       ├── loadouts (2)
    │           │       │   └── curLoadout (2) — [text]
    │           │       ├── lord (2) — [text]
    │           │       ├── mechanitor (2) — attrs: [IsNull]
    │           │       ├── meleeVerbs (2)
    │           │       │   ├── curMeleeVerb (2) — [text]
    │           │       │   ├── terrainVerbs (2) — attrs: [IsNull]
    │           │       │   └── curMeleeVerbUpdateTick (1) — [text]
    │           │       ├── mindState (2)
    │           │       │   ├── babyAutoBreastfeedMoms (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── babyCaravanBreastfeed (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── breachingTarget (2) — attrs: [IsNull]
    │           │       │   ├── canFleeIndividual (2) — [text]
    │           │       │   ├── droppedWeapon (2) — [text]
    │           │       │   ├── duty (2) — attrs: [IsNull]
    │           │       │   ├── enemyTarget (2) — [text]
    │           │       │   ├── inspirationHandler (2)
    │           │       │   │   └── curState (2) — attrs: [IsNull]
    │           │       │   ├── knownExploder (2) — [text]
    │           │       │   ├── lastAttackTargetTick (2) — [text]
    │           │       │   ├── lastCombatantTick (2) — [text]
    │           │       │   ├── lastDayInteractionTick (2) — [text]
    │           │       │   ├── lastEngageTargetTick (2) — [text]
    │           │       │   ├── lastMannedThing (2) — [text]
    │           │       │   ├── lastMeleeThreatHarmTick (2) — [text]
    │           │       │   ├── lastSelfTendTick (2) — [text]
    │           │       │   ├── meleeThreat (2) — [text]
    │           │       │   ├── mentalBreaker (2)
    │           │       │   ├── mentalFitGenerator (2)
    │           │       │   ├── mentalStateHandler (2)
    │           │       │   │   └── curState (2) — attrs: [IsNull]
    │           │       │   ├── priorityWork (2)
    │           │       │   │   └── prioritizedCell (2) — [text]
    │           │       │   ├── resurrectTarget (2) — attrs: [IsNull]
    │           │       │   ├── thinkData (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   └── hibernationEndedTick (1) — [text]
    │           │       ├── name (2) — attrs: [Class]
    │           │       │   ├── first (2) — [text]
    │           │       │   ├── last (2) — [text]
    │           │       │   └── nick (2) — [text]
    │           │       ├── natives (2) — attrs: [IsNull]
    │           │       ├── needs (2)
    │           │       │   └── needs (2)
    │           │       │       └── li (7) — attrs: [Class]
    │           │       │           ├── curLevel (7) — [text]
    │           │       │           ├── def (7) — [text]
    │           │       │           ├── lastNonStarvingTick (2) — [text]
    │           │       │           ├── recentMemory (2)
    │           │       │           │   ├── lastLightTick (1) — [text]
    │           │       │           │   └── lastOutdoorTick (1) — [text]
    │           │       │           └── thoughts (2)
    │           │       │               └── memories (2)
    │           │       │                   └── memories (2)
    │           │       ├── outfits (2) — attrs: [IsNull]
    │           │       ├── ownership (2)
    │           │       │   ├── assignedDeathrestCasket (2) — [text]
    │           │       │   ├── assignedGrave (2) — [text]
    │           │       │   ├── assignedMeditationSpot (2) — [text]
    │           │       │   ├── assignedThrone (2) — [text]
    │           │       │   └── ownedBed (2) — [text]
    │           │       ├── pather (2) — attrs: [IsNull]
    │           │       ├── playerSettings (2) — attrs: [IsNull]
    │           │       ├── psychicEntropy (2)
    │           │       │   ├── limitEntropyAmount (2) — [text]
    │           │       │   └── currentPsyfocus (1) — [text]
    │           │       ├── questTags (2) — attrs: [IsNull]
    │           │       ├── reading (2) — attrs: [IsNull]
    │           │       ├── records (2)
    │           │       │   ├── battleActive (2) — [text]
    │           │       │   └── records (2)
    │           │       │       └── vals (2)
    │           │       │           └── li (144) — [text]
    │           │       ├── roping (2) — attrs: [IsNull]
    │           │       ├── rotationTracker (2) — attrs: [IsNull]
    │           │       ├── royalty (2)
    │           │       │   ├── abilities (2)
    │           │       │   ├── favor (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── heirs (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── highestTitles (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── permits (2)
    │           │       │   └── titles (2)
    │           │       ├── shambler (2) — attrs: [IsNull]
    │           │       ├── shoppingArea (2) — [text]
    │           │       ├── skills (2)
    │           │       │   ├── lastXpSinceMidnightResetTimestamp (2) — [text]
    │           │       │   └── skills (2)
    │           │       │       └── li (24)
    │           │       │           ├── def (24) — [text]
    │           │       │           ├── level (20) — [text]
    │           │       │           ├── passion (7) — [text]
    │           │       │           ├── xpSinceLastLevel (3) — [text]
    │           │       │           └── xpSinceMidnight (3) — [text]
    │           │       ├── social (2)
    │           │       │   ├── additionalPregnancyApproachData (2)
    │           │       │   │   └── partners (2)
    │           │       │   │       ├── keys (2)
    │           │       │   │       └── values (2)
    │           │       │   ├── directRelations (2)
    │           │       │   │   └── li (1)
    │           │       │   │       ├── def (1) — [text]
    │           │       │   │       ├── otherPawn (1) — [text]
    │           │       │   │       └── startTicks (1) — [text]
    │           │       │   ├── pregnancyApproaches (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── relativeInvolvedInRescueQuest (2) — [text]
    │           │       │   ├── romanceEnableTick (2) — [text]
    │           │       │   └── virtualRelations (2)
    │           │       ├── stances (2)
    │           │       │   ├── curStance (2) — attrs: [Class]
    │           │       │   ├── stagger (2)
    │           │       │   └── stunner (2)
    │           │       │       ├── adaptationTicksLeft (2)
    │           │       │       │   ├── keys (2)
    │           │       │       │   └── values (2)
    │           │       │       └── showStunMote (2) — [text]
    │           │       ├── story (2)
    │           │       │   ├── adulthood (2) — [text]
    │           │       │   ├── birthLastName (2) — [text]
    │           │       │   ├── bodyType (2) — [text]
    │           │       │   ├── childhood (2) — [text]
    │           │       │   ├── favoriteColorDef (2) — [text]
    │           │       │   ├── hairColor (2) — [text]
    │           │       │   ├── hairDef (2) — [text]
    │           │       │   ├── headType (2) — [text]
    │           │       │   └── traits (2)
    │           │       │       └── allTraits (2)
    │           │       │           └── li (4)
    │           │       │               ├── def (4) — [text]
    │           │       │               ├── sourceGene (4) — [text]
    │           │       │               ├── suppressedBy (4) — [text]
    │           │       │               └── degree (2) — [text]
    │           │       ├── style (2)
    │           │       │   ├── beardDef (2) — [text]
    │           │       │   ├── bodyTattoo (2) — [text]
    │           │       │   └── faceTattoo (2) — [text]
    │           │       ├── styleObserver (2)
    │           │       ├── targetHolder (2) — [text]
    │           │       ├── thinker (2)
    │           │       ├── tickDelta (2) — [text]
    │           │       ├── ticksToReset (2) — [text]
    │           │       ├── timetable (2) — attrs: [IsNull]
    │           │       ├── trader (2) — attrs: [IsNull]
    │           │       ├── training (2) — attrs: [IsNull]
    │           │       ├── treeSightings (2)
    │           │       │   ├── fullTreeSightings (2)
    │           │       │   ├── miniTreeSightings (2)
    │           │       │   └── superTreeSightings (2)
    │           │       ├── verbTracker (2)
    │           │       │   └── verbs (2)
    │           │       │       └── li (8) — attrs: [Class]
    │           │       │           ├── MVCF_ManagedVerb (8)
    │           │       │           │   ├── enabled (8) — [text]
    │           │       │           │   └── loadId (8) — [text]
    │           │       │           ├── canHitNonTargetPawnsNow (8) — [text]
    │           │       │           ├── currentDestination (8) — [text]
    │           │       │           ├── currentTarget (8) — [text]
    │           │       │           ├── lastShotTick (8) — [text]
    │           │       │           └── loadID (8) — [text]
    │           │       ├── vfee_honors (2)
    │           │       │   ├── honors (2)
    │           │       │   └── pendingHonors (2)
    │           │       ├── workSettings (2)
    │           │       │   └── priorities (2) — attrs: [IsNull]
    │           │       ├── becameWorldPawnTickAbs (1) — [text]
    │           │       ├── pos (1) — [text]
    │           │       └── rot (1) — [text]
    │           ├── pawnsDead (1)
    │           │   └── li (42)
    │           │       ├── MVCF_VerbManager (42) — attrs: [IsNull]
    │           │       │   └── currentVerb (37) — [text]
    │           │       ├── ThingsHauledToInventory (42)
    │           │       ├── abilities (42) — attrs: [IsNull]
    │           │       │   └── abilities (11)
    │           │       │       └── li (3)
    │           │       │           ├── Id (3) — [text]
    │           │       │           ├── def (3) — [text]
    │           │       │           ├── sourcePrecept (3) — [text]
    │           │       │           ├── verbTracker (3)
    │           │       │           │   └── verbs (3)
    │           │       │           │       └── li (3) — attrs: [Class]
    │           │       │           │           ├── MVCF_ManagedVerb (3) — attrs: [IsNull]
    │           │       │           │           ├── ability (3) — [text]
    │           │       │           │           ├── canHitNonTargetPawnsNow (3) — [text]
    │           │       │           │           ├── currentDestination (3) — [text]
    │           │       │           │           ├── currentTarget (3) — [text]
    │           │       │           │           ├── lastShotTick (3) — [text]
    │           │       │           │           └── loadID (3) — [text]
    │           │       │           ├── charges (2) — [text]
    │           │       │           └── maxCharges (2) — [text]
    │           │       ├── ageTracker (42)
    │           │       │   ├── ageBiologicalTicks (42) — [text]
    │           │       │   ├── ageReversalDemandedAtAgeTicks (42) — [text]
    │           │       │   ├── birthAbsTicks (42) — [text]
    │           │       │   ├── growth (42) — [text]
    │           │       │   ├── nextGrowthCheckTick (42) — [text]
    │           │       │   └── lifeStageChange (34) — [text]
    │           │       ├── apparel (42) — attrs: [IsNull]
    │           │       │   ├── lastApparelWearoutTick (9) — [text]
    │           │       │   ├── lockedApparel (9)
    │           │       │   └── wornApparel (9)
    │           │       │       └── innerList (9)
    │           │       ├── becameWorldPawnTickAbs (42) — [text]
    │           │       ├── carryTracker (42) — attrs: [IsNull]
    │           │       │   └── innerContainer (1)
    │           │       │       ├── innerList (1)
    │           │       │       └── maxStacks (1) — [text]
    │           │       ├── connections (42)
    │           │       │   └── connectedThings (42)
    │           │       ├── creepjoiner (42) — attrs: [IsNull]
    │           │       ├── deadlifeDustFaction (42) — [text]
    │           │       ├── def (42) — [text]
    │           │       ├── despawnedTick (42) — [text]
    │           │       ├── drafter (42) — attrs: [IsNull]
    │           │       ├── drugs (42) — attrs: [IsNull]
    │           │       ├── duplicate (42) — attrs: [IsNull]
    │           │       ├── equipment (42) — attrs: [IsNull]
    │           │       │   ├── bondedWeapon (9) — [text]
    │           │       │   └── equipment (9)
    │           │       │       └── innerList (9)
    │           │       ├── filth (42) — attrs: [IsNull]
    │           │       ├── flight (42) — attrs: [IsNull]
    │           │       ├── foodRestriction (42) — attrs: [IsNull]
    │           │       │   ├── allowedBabyFoodTypes (2) — attrs: [IsNull]
    │           │       │   └── curRestriction (2) — [text]
    │           │       ├── genes (42) — attrs: [IsNull]
    │           │       │   ├── endogenes (5)
    │           │       │   │   └── li (25)
    │           │       │   │       ├── def (25) — [text]
    │           │       │   │       ├── loadID (25) — [text]
    │           │       │   │       ├── overriddenByGene (25) — [text]
    │           │       │   │       ├── pawn (25) — [text]
    │           │       │   │       └── passionPreAdd (2) — [text]
    │           │       │   ├── xenogenes (5)
    │           │       │   │   └── li (39) — attrs: [Class]
    │           │       │   │       ├── def (39) — [text]
    │           │       │   │       ├── loadID (39) — [text]
    │           │       │   │       ├── overriddenByGene (39) — [text]
    │           │       │   │       ├── pawn (39) — [text]
    │           │       │   │       ├── passionPreAdd (9) — [text]
    │           │       │   │       ├── bondedPawn (1) — [text]
    │           │       │   │       └── lastIngestedTick (1) — [text]
    │           │       │   └── xenotype (5) — [text]
    │           │       ├── guest (42) — attrs: [IsNull]
    │           │       │   ├── enabledNonExclusiveInteractions (5)
    │           │       │   ├── finalResistanceInteractionData (5) — attrs: [IsNull]
    │           │       │   ├── hostFaction (5) — [text]
    │           │       │   ├── ideoForConversion (5) — [text]
    │           │       │   ├── interactionMode (5) — [text]
    │           │       │   ├── joinStatus (5) — [text]
    │           │       │   ├── lastPrisonBreakTicks (5) — [text]
    │           │       │   ├── lastResistanceInteractionData (5) — attrs: [IsNull]
    │           │       │   ├── slaveFaction (5) — [text]
    │           │       │   ├── slaveInteractionMode (5) — [text]
    │           │       │   ├── spotToWaitInsteadOfEscaping (5) — [text]
    │           │       │   ├── leftAfterRescue (1) — [text]
    │           │       │   └── recruitable (1) — [text]
    │           │       ├── guilt (42) — attrs: [IsNull]
    │           │       │   └── guiltyTicksLeft (1) — [text]
    │           │       ├── healthTracker (42)
    │           │       │   ├── healthState (42) — [text]
    │           │       │   ├── hediffSet (42)
    │           │       │   │   └── hediffs (42)
    │           │       │   │       └── li (547) — attrs: [Class]
    │           │       │   │           ├── abilities (547) — attrs: [IsNull]
    │           │       │   │           ├── canBeThreateningToPart (547) — [text]
    │           │       │   │           ├── combatLogEntry (547) — [text]
    │           │       │   │           ├── def (547) — [text]
    │           │       │   │           ├── loadID (547) — [text]
    │           │       │   │           ├── severity (547) — [text]
    │           │       │   │           ├── tickAdded (540) — [text]
    │           │       │   │           ├── part (518)
    │           │       │   │           │   ├── body (518) — [text]
    │           │       │   │           │   └── index (518) — [text]
    │           │       │   │           ├── lastInjury (301) — [text]
    │           │       │   │           ├── infectionChanceFactor (204) — [text]
    │           │       │   │           ├── ageTicks (163) — [text]
    │           │       │   │           ├── visible (147) — [text]
    │           │       │   │           ├── combatLogText (146) — [text]
    │           │       │   │           ├── sourceLabel (138) — [text]
    │           │       │   │           ├── source (134) — [text]
    │           │       │   │           ├── sourceBodyPartGroup (102) — [text]
    │           │       │   │           ├── isFresh (89) — [text]
    │           │       │   │           ├── sourceToolLabel (79) — [text]
    │           │       │   │           ├── ticksUntilInfect (14) — [text]
    │           │       │   │           ├── isPermanent (9) — [text]
    │           │       │   │           ├── severityPerDay (3) — [text]
    │           │       │   │           ├── painCategory (2) — [text]
    │           │       │   │           ├── tendQuality (2) — [text]
    │           │       │   │           ├── tendTicksLeft (2) — [text]
    │           │       │   │           ├── totalTendQuality (2) — [text]
    │           │       │   │           ├── chemical (1) — [text]
    │           │       │   │           ├── intervalFactor (1) — [text]
    │           │       │   │           ├── permanentDamageThreshold (1) — [text]
    │           │       │   │           └── severityPerDayNotImmuneRandomFactor (1) — [text]
    │           │       │   ├── immunity (42)
    │           │       │   │   └── imList (42)
    │           │       │   ├── surgeryBills (42)
    │           │       │   │   └── bills (42)
    │           │       │   └── beCarriedByCaravanIfSick (37) — [text]
    │           │       ├── id (42) — [text]
    │           │       ├── ideo (42) — attrs: [IsNull]
    │           │       │   ├── babyIdeoExposure (5) — attrs: [IsNull]
    │           │       │   ├── certainty (5) — [text]
    │           │       │   ├── ideo (5) — [text]
    │           │       │   ├── previousIdeos (5)
    │           │       │   └── joinTick (4) — [text]
    │           │       ├── infectionVectors (42) — attrs: [IsNull]
    │           │       │   └── pathways (1)
    │           │       │       ├── keys (1)
    │           │       │       └── values (1)
    │           │       ├── interactions (42) — attrs: [IsNull]
    │           │       ├── inventory (42)
    │           │       │   ├── innerContainer (42)
    │           │       │   │   └── innerList (42)
    │           │       │   │       └── li (2) — attrs: [Class]
    │           │       │   │           ├── def (2) — [text]
    │           │       │   │           ├── despawnedTick (2) — [text]
    │           │       │   │           ├── health (2) — [text]
    │           │       │   │           ├── id (2) — [text]
    │           │       │   │           ├── questTags (2) — attrs: [IsNull]
    │           │       │   │           ├── stackCount (2) — [text]
    │           │       │   │           ├── rotProg (1) — [text]
    │           │       │   │           └── verbTracker (1)
    │           │       │   │               └── verbs (1) — attrs: [IsNull]
    │           │       │   ├── itemsNotForSale (42)
    │           │       │   │   └── li (1) — [text]
    │           │       │   └── unpackedCaravanItems (42)
    │           │       ├── inventoryStock (42) — attrs: [IsNull]
    │           │       ├── isEnabled (42) — [text]
    │           │       ├── jobs (42) — attrs: [IsNull]
    │           │       │   ├── curDriver (1) — attrs: [IsNull]
    │           │       │   ├── curJob (1) — attrs: [IsNull]
    │           │       │   ├── formingCaravanTick (1) — [text]
    │           │       │   └── jobQueue (1)
    │           │       │       └── jobs (1)
    │           │       ├── kindDef (42) — [text]
    │           │       ├── learning (42) — attrs: [IsNull]
    │           │       ├── loadouts (42)
    │           │       │   └── curLoadout (42) — [text]
    │           │       ├── mechanitor (42) — attrs: [IsNull]
    │           │       ├── meleeVerbs (42)
    │           │       │   ├── curMeleeVerb (42) — [text]
    │           │       │   ├── terrainVerbs (42) — attrs: [IsNull]
    │           │       │   │   ├── def (6) — [text]
    │           │       │   │   └── tracker (6)
    │           │       │   │       └── verbs (6)
    │           │       │   │           └── li (5) — attrs: [Class]
    │           │       │   │               ├── MVCF_ManagedVerb (5) — attrs: [IsNull]
    │           │       │   │               ├── canHitNonTargetPawnsNow (5) — [text]
    │           │       │   │               ├── lastShotTick (5) — [text]
    │           │       │   │               ├── loadID (5) — [text]
    │           │       │   │               ├── currentTarget (4) — [text]
    │           │       │   │               └── currentDestination (3) — [text]
    │           │       │   ├── curMeleeVerbUpdateTick (41) — [text]
    │           │       │   └── lastTerrainBasedVerbUseTick (1) — [text]
    │           │       ├── mindState (42) — attrs: [IsNull]
    │           │       │   ├── babyAutoBreastfeedMoms (1)
    │           │       │   │   ├── keys (1)
    │           │       │   │   └── values (1)
    │           │       │   ├── babyCaravanBreastfeed (1)
    │           │       │   │   ├── keys (1)
    │           │       │   │   └── values (1)
    │           │       │   ├── breachingTarget (1) — attrs: [IsNull]
    │           │       │   ├── canFleeIndividual (1) — [text]
    │           │       │   ├── droppedWeapon (1) — [text]
    │           │       │   ├── duty (1) — attrs: [IsNull]
    │           │       │   ├── enemyTarget (1) — [text]
    │           │       │   ├── inspirationHandler (1)
    │           │       │   │   └── curState (1) — attrs: [IsNull]
    │           │       │   ├── knownExploder (1) — [text]
    │           │       │   ├── lastAttackTargetTick (1) — [text]
    │           │       │   ├── lastEngageTargetTick (1) — [text]
    │           │       │   ├── lastHumanMeatIngestedTick (1) — [text]
    │           │       │   ├── lastMannedThing (1) — [text]
    │           │       │   ├── lastMeleeThreatHarmTick (1) — [text]
    │           │       │   ├── lastSelfTendTick (1) — [text]
    │           │       │   ├── meleeThreat (1) — [text]
    │           │       │   ├── mentalBreaker (1)
    │           │       │   ├── mentalFitGenerator (1)
    │           │       │   ├── mentalStateHandler (1)
    │           │       │   │   └── curState (1) — attrs: [IsNull]
    │           │       │   ├── priorityWork (1)
    │           │       │   │   └── prioritizedCell (1) — [text]
    │           │       │   ├── resurrectTarget (1) — attrs: [IsNull]
    │           │       │   └── thinkData (1)
    │           │       │       ├── keys (1)
    │           │       │       └── values (1)
    │           │       ├── name (42) — attrs: [Class, IsNull]
    │           │       │   ├── first (5) — [text]
    │           │       │   ├── last (5) — [text]
    │           │       │   └── nick (3) — [text]
    │           │       ├── natives (42) — attrs: [IsNull]
    │           │       ├── needs (42) — attrs: [IsNull]
    │           │       │   └── needs (1)
    │           │       │       └── li (4) — attrs: [Class]
    │           │       │           ├── curLevel (4) — [text]
    │           │       │           ├── def (4) — [text]
    │           │       │           ├── recentMemory (1)
    │           │       │           └── thoughts (1)
    │           │       │               └── memories (1)
    │           │       │                   └── memories (1)
    │           │       ├── outfits (42) — attrs: [IsNull]
    │           │       ├── ownership (42)
    │           │       │   ├── assignedDeathrestCasket (42) — [text]
    │           │       │   ├── assignedGrave (42) — [text]
    │           │       │   ├── assignedMeditationSpot (42) — [text]
    │           │       │   ├── assignedThrone (42) — [text]
    │           │       │   └── ownedBed (42) — [text]
    │           │       ├── pather (42) — attrs: [IsNull]
    │           │       ├── playerSettings (42) — attrs: [IsNull]
    │           │       │   ├── allowedAreas (2)
    │           │       │   │   ├── keys (2)
    │           │       │   │   └── values (2)
    │           │       │   ├── displayOrder (2) — [text]
    │           │       │   ├── joinTick (2) — [text]
    │           │       │   ├── master (2) — [text]
    │           │       │   └── medCare (2) — [text]
    │           │       ├── psychicEntropy (42) — attrs: [IsNull]
    │           │       │   ├── currentPsyfocus (38) — [text]
    │           │       │   └── limitEntropyAmount (38) — [text]
    │           │       ├── questTags (42) — attrs: [IsNull]
    │           │       │   └── li (2) — [text]
    │           │       ├── reading (42) — attrs: [IsNull]
    │           │       ├── records (42)
    │           │       │   ├── battleActive (42) — [text]
    │           │       │   ├── records (42)
    │           │       │   │   └── vals (42)
    │           │       │   │       └── li (3,024) — [text]
    │           │       │   └── battleExitTick (37) — [text]
    │           │       ├── roping (42) — attrs: [IsNull]
    │           │       ├── rotationTracker (42) — attrs: [IsNull]
    │           │       ├── royalty (42) — attrs: [IsNull]
    │           │       │   ├── abilities (5)
    │           │       │   ├── favor (5)
    │           │       │   │   ├── keys (5)
    │           │       │   │   │   └── li (1) — [text]
    │           │       │   │   └── values (5)
    │           │       │   │       └── li (1) — [text]
    │           │       │   ├── heirs (5)
    │           │       │   │   ├── keys (5)
    │           │       │   │   └── values (5)
    │           │       │   ├── highestTitles (5)
    │           │       │   │   ├── keys (5)
    │           │       │   │   │   └── li (1) — [text]
    │           │       │   │   └── values (5)
    │           │       │   │       └── li (1) — [text]
    │           │       │   ├── permits (5)
    │           │       │   └── titles (5)
    │           │       │       └── li (1)
    │           │       │           ├── conceited (1) — [text]
    │           │       │           ├── def (1) — [text]
    │           │       │           ├── faction (1) — [text]
    │           │       │           └── receivedTick (1) — [text]
    │           │       ├── shambler (42) — attrs: [IsNull]
    │           │       ├── skills (42) — attrs: [IsNull]
    │           │       │   ├── lastXpSinceMidnightResetTimestamp (5) — [text]
    │           │       │   └── skills (5)
    │           │       │       └── li (60)
    │           │       │           ├── def (60) — [text]
    │           │       │           ├── level (52) — [text]
    │           │       │           ├── passion (20) — [text]
    │           │       │           ├── xpSinceLastLevel (8) — [text]
    │           │       │           └── xpSinceMidnight (7) — [text]
    │           │       ├── social (42) — attrs: [IsNull]
    │           │       │   ├── additionalPregnancyApproachData (38)
    │           │       │   │   └── partners (38)
    │           │       │   │       ├── keys (38)
    │           │       │   │       └── values (38)
    │           │       │   ├── directRelations (38)
    │           │       │   │   └── li (2)
    │           │       │   │       ├── def (2) — [text]
    │           │       │   │       ├── otherPawn (2) — [text]
    │           │       │   │       └── startTicks (2) — [text]
    │           │       │   ├── pregnancyApproaches (38)
    │           │       │   │   ├── keys (38)
    │           │       │   │   └── values (38)
    │           │       │   ├── relativeInvolvedInRescueQuest (38) — [text]
    │           │       │   ├── romanceEnableTick (38) — [text]
    │           │       │   ├── virtualRelations (38)
    │           │       │   ├── canGetRescuedThought (2) — [text]
    │           │       │   └── everSeenByPlayer (1) — [text]
    │           │       ├── stances (42) — attrs: [IsNull]
    │           │       │   ├── curStance (1) — attrs: [Class]
    │           │       │   ├── stagger (1)
    │           │       │   └── stunner (1)
    │           │       │       ├── adaptationTicksLeft (1)
    │           │       │       │   ├── keys (1)
    │           │       │       │   └── values (1)
    │           │       │       └── showStunMote (1) — [text]
    │           │       ├── story (42) — attrs: [IsNull]
    │           │       │   ├── adulthood (5) — [text]
    │           │       │   ├── birthLastName (5) — [text]
    │           │       │   ├── bodyType (5) — [text]
    │           │       │   ├── childhood (5) — [text]
    │           │       │   ├── favoriteColorDef (5) — [text]
    │           │       │   ├── hairColor (5) — [text]
    │           │       │   ├── hairDef (5) — [text]
    │           │       │   ├── headType (5) — [text]
    │           │       │   ├── traits (5)
    │           │       │   │   └── allTraits (5)
    │           │       │   │       └── li (16)
    │           │       │   │           ├── def (16) — [text]
    │           │       │   │           ├── sourceGene (16) — [text]
    │           │       │   │           ├── suppressedBy (16) — [text]
    │           │       │   │           └── degree (3) — [text]
    │           │       │   ├── skinColorOverride (2) — [text]
    │           │       │   └── furDef (1) — [text]
    │           │       ├── style (42) — attrs: [IsNull]
    │           │       │   ├── beardDef (5) — [text]
    │           │       │   ├── bodyTattoo (5) — [text]
    │           │       │   └── faceTattoo (5) — [text]
    │           │       ├── styleObserver (42) — attrs: [IsNull]
    │           │       ├── thinker (42) — attrs: [IsNull]
    │           │       ├── timetable (42) — attrs: [IsNull]
    │           │       ├── trader (42) — attrs: [IsNull]
    │           │       ├── training (42) — attrs: [IsNull]
    │           │       │   ├── attackTarget (1) — [text]
    │           │       │   ├── countDecayFrom (1) — [text]
    │           │       │   ├── learned (1)
    │           │       │   │   └── vals (1)
    │           │       │   │       └── li (23) — [text]
    │           │       │   ├── steps (1)
    │           │       │   │   └── vals (1)
    │           │       │   │       └── li (23) — [text]
    │           │       │   └── wantedTrainables (1)
    │           │       │       └── vals (1)
    │           │       │           └── li (23) — [text]
    │           │       ├── treeSightings (42) — attrs: [IsNull]
    │           │       │   ├── fullTreeSightings (5)
    │           │       │   ├── miniTreeSightings (5)
    │           │       │   └── superTreeSightings (5)
    │           │       ├── verbTracker (42)
    │           │       │   └── verbs (42)
    │           │       │       └── li (154) — attrs: [Class]
    │           │       │           ├── MVCF_ManagedVerb (154)
    │           │       │           │   ├── enabled (154) — [text]
    │           │       │           │   └── loadId (154) — [text]
    │           │       │           ├── canHitNonTargetPawnsNow (154) — [text]
    │           │       │           ├── lastShotTick (154) — [text]
    │           │       │           ├── loadID (154) — [text]
    │           │       │           ├── currentTarget (134) — [text]
    │           │       │           └── currentDestination (125) — [text]
    │           │       ├── vfee_honors (42)
    │           │       │   ├── honors (42)
    │           │       │   └── pendingHonors (42)
    │           │       ├── workSettings (42) — attrs: [IsNull]
    │           │       │   └── priorities (1) — attrs: [IsNull]
    │           │       ├── map (41) — [text]
    │           │       ├── lastStudiedTick (38) — [text]
    │           │       ├── rot (38) — [text]
    │           │       ├── targetHolder (38) — [text]
    │           │       ├── pos (37) — [text]
    │           │       ├── huntingPackMaster (33) — [text]
    │           │       ├── huntingPackMembers (33)
    │           │       ├── gender (26) — [text]
    │           │       ├── tickDelta (25) — [text]
    │           │       ├── faction (7) — [text]
    │           │       ├── bed (5) — [text]
    │           │       ├── beenRevealed (5) — [text]
    │           │       ├── boughtItems (5)
    │           │       ├── currentlyCasting (5) — [text]
    │           │       ├── currentlyCastingTargets (5)
    │           │       ├── fertilizedBy (5) — [text]
    │           │       ├── guestArea (5) — [text]
    │           │       ├── lastKeepDisplayTick (5) — [text]
    │           │       ├── learnedAbilities (5)
    │           │       ├── lord (5) — [text]
    │           │       ├── shoppingArea (5) — [text]
    │           │       ├── ticksToReset (5) — [text]
    │           │       ├── chargerBeforeTakeoff (4) — [text]
    │           │       ├── makeTick (4) — [text]
    │           │       ├── repeatWakeUpSignalOnTick (4) — [text]
    │           │       ├── wakeUpSignalTag (4) — [text]
    │           │       ├── wakeUpSignalTags (4) — attrs: [IsNull]
    │           │       ├── wokeUpTick (4) — [text]
    │           │       ├── eggProgress (2) — [text]
    │           │       ├── addHediffOnce (1) — [text]
    │           │       ├── rescued (1) — [text]
    │           │       └── wasDowned (1) — [text]
    │           ├── pawnsForcefullyKeptAsWorldPawns (1)
    │           │   └── li (155) — [text]
    │           └── pawnsMothballed (1)
    │               └── li (178)
    │                   ├── MVCF_VerbManager (178) — attrs: [IsNull]
    │                   │   └── currentVerb (19) — [text]
    │                   ├── ThingsHauledToInventory (178)
    │                   ├── abilities (178)
    │                   │   └── abilities (178)
    │                   │       └── li (653) — attrs: [Class]
    │                   │           ├── Id (653) — [text]
    │                   │           ├── def (653) — [text]
    │                   │           ├── sourcePrecept (653) — [text]
    │                   │           ├── verbTracker (653)
    │                   │           │   └── verbs (653)
    │                   │           │       └── li (653) — attrs: [Class]
    │                   │           │           ├── MVCF_ManagedVerb (653) — attrs: [IsNull]
    │                   │           │           ├── ability (653) — [text]
    │                   │           │           ├── canHitNonTargetPawnsNow (653) — [text]
    │                   │           │           ├── currentDestination (653) — [text]
    │                   │           │           ├── currentTarget (653) — [text]
    │                   │           │           ├── lastShotTick (653) — [text]
    │                   │           │           └── loadID (653) — [text]
    │                   │           ├── charges (651) — [text]
    │                   │           └── maxCharges (651) — [text]
    │                   ├── ageTracker (178)
    │                   │   ├── ageBiologicalTicks (178) — [text]
    │                   │   ├── ageReversalDemandedAtAgeTicks (178) — [text]
    │                   │   ├── birthAbsTicks (178) — [text]
    │                   │   ├── growth (178) — [text]
    │                   │   ├── nextGrowthCheckTick (178) — [text]
    │                   │   ├── lifeStageChange (165) — [text]
    │                   │   ├── progressToNextBiologicalTick (31) — [text]
    │                   │   └── lastAgeReversalReason (3) — [text]
    │                   ├── apparel (178)
    │                   │   ├── lastApparelWearoutTick (178) — [text]
    │                   │   ├── lockedApparel (178) — attrs: [IsNull]
    │                   │   └── wornApparel (178)
    │                   │       └── innerList (178)
    │                   │           └── li (944) — attrs: [Class]
    │                   │               ├── abilities (944)
    │                   │               ├── def (944) — [text]
    │                   │               ├── despawnedTick (944) — [text]
    │                   │               ├── health (944) — [text]
    │                   │               ├── id (944) — [text]
    │                   │               ├── questTags (944) — attrs: [IsNull]
    │                   │               ├── stackCount (944) — [text]
    │                   │               ├── sourcePrecept (943) — [text]
    │                   │               ├── quality (942) — [text]
    │                   │               ├── stuff (910) — [text]
    │                   │               ├── color (477) — [text]
    │                   │               ├── colorActive (477) — [text]
    │                   │               ├── gemstone (210) — [text]
    │                   │               ├── everSeenByPlayer (8) — [text]
    │                   │               ├── codedPawn (6) — [text]
    │                   │               ├── styleDef (3) — [text]
    │                   │               ├── remainingCharges (1) — [text]
    │                   │               ├── tickDelta (1) — [text]
    │                   │               └── verbTracker (1)
    │                   │                   └── verbs (1)
    │                   │                       └── li (1) — attrs: [Class]
    │                   │                           ├── MVCF_ManagedVerb (1) — attrs: [IsNull]
    │                   │                           ├── canHitNonTargetPawnsNow (1) — [text]
    │                   │                           ├── lastShotTick (1) — [text]
    │                   │                           └── loadID (1) — [text]
    │                   ├── bed (178) — [text]
    │                   ├── boughtItems (178)
    │                   ├── carryTracker (178)
    │                   │   └── innerContainer (178)
    │                   │       ├── innerList (178)
    │                   │       └── maxStacks (178) — [text]
    │                   ├── connections (178)
    │                   │   └── connectedThings (178)
    │                   ├── creepjoiner (178) — attrs: [IsNull]
    │                   ├── currentlyCasting (178) — [text]
    │                   ├── currentlyCastingTargets (178)
    │                   ├── deadlifeDustFaction (178) — [text]
    │                   ├── def (178) — [text]
    │                   ├── despawnedTick (178) — [text]
    │                   ├── drafter (178) — attrs: [IsNull]
    │                   ├── drugs (178) — attrs: [IsNull]
    │                   │   ├── curAssignedDrugs (4) — [text]
    │                   │   └── drugTakeRecords (4)
    │                   ├── duplicate (178)
    │                   ├── equipment (178)
    │                   │   ├── bondedWeapon (178) — [text]
    │                   │   └── equipment (178)
    │                   │       └── innerList (178)
    │                   │           └── li (161)
    │                   │               ├── def (161) — [text]
    │                   │               ├── despawnedTick (161) — [text]
    │                   │               ├── health (161) — [text]
    │                   │               ├── id (161) — [text]
    │                   │               ├── quality (161) — [text]
    │                   │               ├── questTags (161) — attrs: [IsNull]
    │                   │               ├── sourcePrecept (161) — [text]
    │                   │               ├── stackCount (161) — [text]
    │                   │               ├── verbTracker (161)
    │                   │               │   └── verbs (161)
    │                   │               │       └── li (469) — attrs: [Class]
    │                   │               │           ├── MVCF_ManagedVerb (469)
    │                   │               │           │   ├── enabled (469) — [text]
    │                   │               │           │   └── loadId (469) — [text]
    │                   │               │           ├── canHitNonTargetPawnsNow (469) — [text]
    │                   │               │           ├── lastShotTick (469) — [text]
    │                   │               │           └── loadID (469) — [text]
    │                   │               ├── codedPawn (133) — [text]
    │                   │               ├── taleRef (105) — attrs: [IsNull]
    │                   │               │   ├── seed (79) — [text]
    │                   │               │   └── tale (79) — [text]
    │                   │               ├── title (79) — [text]
    │                   │               ├── name (42) — [text]
    │                   │               ├── traits (42)
    │                   │               │   └── li (69) — [text]
    │                   │               ├── biocoded (41) — [text]
    │                   │               ├── biocodedPawnLabel (41) — [text]
    │                   │               ├── stuff (18) — [text]
    │                   │               └── lastKillTick (3) — [text]
    │                   ├── filth (178) — attrs: [IsNull]
    │                   ├── flight (178) — attrs: [IsNull]
    │                   ├── foodRestriction (178) — attrs: [IsNull]
    │                   │   ├── allowedBabyFoodTypes (4) — attrs: [IsNull]
    │                   │   └── curRestriction (4) — [text]
    │                   ├── genes (178)
    │                   │   ├── endogenes (178)
    │                   │   │   └── li (582) — attrs: [Class]
    │                   │   │       ├── def (582) — [text]
    │                   │   │       ├── loadID (582) — [text]
    │                   │   │       ├── overriddenByGene (582) — [text]
    │                   │   │       ├── pawn (582) — [text]
    │                   │   │       ├── passionPreAdd (5) — [text]
    │                   │   │       └── lastIngestedTick (1) — [text]
    │                   │   ├── xenogenes (178)
    │                   │   │   └── li (655) — attrs: [Class]
    │                   │   │       ├── def (655) — [text]
    │                   │   │       ├── loadID (655) — [text]
    │                   │   │       ├── overriddenByGene (655) — [text]
    │                   │   │       ├── pawn (655) — [text]
    │                   │   │       ├── passionPreAdd (124) — [text]
    │                   │   │       ├── boundBuildings (8)
    │                   │   │       ├── cur (8) — [text]
    │                   │   │       ├── max (8) — [text]
    │                   │   │       ├── ticksToHeal (8) — [text]
    │                   │   │       └── lastIngestedTick (3) — [text]
    │                   │   └── xenotype (178) — [text]
    │                   ├── guest (178)
    │                   │   ├── enabledNonExclusiveInteractions (178)
    │                   │   ├── finalResistanceInteractionData (178) — attrs: [IsNull]
    │                   │   ├── hostFaction (178) — [text]
    │                   │   ├── ideoForConversion (178) — [text]
    │                   │   ├── interactionMode (178) — [text]
    │                   │   ├── joinStatus (178) — [text]
    │                   │   ├── lastPrisonBreakTicks (178) — [text]
    │                   │   ├── lastResistanceInteractionData (178) — attrs: [IsNull]
    │                   │   ├── slaveFaction (178) — [text]
    │                   │   ├── slaveInteractionMode (178) — [text]
    │                   │   ├── spotToWaitInsteadOfEscaping (178) — [text]
    │                   │   └── recruitable (41) — [text]
    │                   ├── guestArea (178) — [text]
    │                   ├── guilt (178)
    │                   ├── healthTracker (178)
    │                   │   ├── hediffSet (178)
    │                   │   │   └── hediffs (178)
    │                   │   │       └── li (401) — attrs: [Class]
    │                   │   │           ├── abilities (401) — attrs: [IsNull]
    │                   │   │           │   └── li (1)
    │                   │   │           │       ├── Id (1) — [text]
    │                   │   │           │       ├── charges (1) — [text]
    │                   │   │           │       ├── def (1) — [text]
    │                   │   │           │       ├── maxCharges (1) — [text]
    │                   │   │           │       ├── sourcePrecept (1) — [text]
    │                   │   │           │       └── verbTracker (1)
    │                   │   │           │           └── verbs (1)
    │                   │   │           │               └── li (1) — attrs: [Class]
    │                   │   │           │                   ├── MVCF_ManagedVerb (1) — attrs: [IsNull]
    │                   │   │           │                   ├── ability (1) — [text]
    │                   │   │           │                   ├── canHitNonTargetPawnsNow (1) — [text]
    │                   │   │           │                   ├── currentDestination (1) — [text]
    │                   │   │           │                   ├── currentTarget (1) — [text]
    │                   │   │           │                   ├── lastShotTick (1) — [text]
    │                   │   │           │                   └── loadID (1) — [text]
    │                   │   │           ├── canBeThreateningToPart (401) — [text]
    │                   │   │           ├── combatLogEntry (401) — [text]
    │                   │   │           ├── def (401) — [text]
    │                   │   │           ├── loadID (401) — [text]
    │                   │   │           ├── severity (391) — [text]
    │                   │   │           ├── part (378)
    │                   │   │           │   ├── body (378) — [text]
    │                   │   │           │   └── index (378) — [text]
    │                   │   │           ├── level (141) — [text]
    │                   │   │           ├── infectionChanceFactor (80) — [text]
    │                   │   │           ├── isPermanent (80) — [text]
    │                   │   │           ├── lastInjury (74) — [text]
    │                   │   │           ├── ageTicks (61) — [text]
    │                   │   │           ├── visible (60) — [text]
    │                   │   │           ├── tickAdded (45) — [text]
    │                   │   │           ├── painCategory (41) — [text]
    │                   │   │           ├── chemical (13) — [text]
    │                   │   │           ├── severityPerDay (13) — [text]
    │                   │   │           ├── verbTracker (11)
    │                   │   │           │   └── verbs (11) — attrs: [IsNull]
    │                   │   │           ├── tendQuality (7) — [text]
    │                   │   │           ├── tendTicksLeft (7) — [text]
    │                   │   │           ├── totalTendQuality (7) — [text]
    │                   │   │           ├── severityPerDayNotImmuneRandomFactor (2) — [text]
    │                   │   │           ├── growthMode (1) — [text]
    │                   │   │           ├── severityPerDayGrowingRandomFactor (1) — [text]
    │                   │   │           └── severityPerDayRemissionRandomFactor (1) — [text]
    │                   │   ├── immunity (178)
    │                   │   │   └── imList (178)
    │                   │   └── surgeryBills (178)
    │                   │       └── bills (178)
    │                   ├── id (178) — [text]
    │                   ├── ideo (178)
    │                   │   ├── babyIdeoExposure (178) — attrs: [IsNull]
    │                   │   ├── certainty (178) — [text]
    │                   │   ├── ideo (178) — [text]
    │                   │   ├── previousIdeos (178)
    │                   │   └── joinTick (38) — [text]
    │                   ├── infectionVectors (178)
    │                   │   ├── pathways (178)
    │                   │   │   ├── keys (178)
    │                   │   │   │   └── li (18) — [text]
    │                   │   │   └── values (178)
    │                   │   │       └── li (18)
    │                   │   │           ├── ageTicks (18) — [text]
    │                   │   │           ├── def (18) — [text]
    │                   │   │           └── ownerPawn (18) — [text]
    │                   │   └── givenPrearrival (18) — [text]
    │                   ├── interactions (178) — attrs: [IsNull]
    │                   ├── inventory (178)
    │                   │   ├── innerContainer (178)
    │                   │   │   └── innerList (178)
    │                   │   │       └── li (39) — attrs: [Class]
    │                   │   │           ├── def (39) — [text]
    │                   │   │           ├── despawnedTick (39) — [text]
    │                   │   │           ├── health (39) — [text]
    │                   │   │           ├── id (39) — [text]
    │                   │   │           ├── questTags (39) — attrs: [IsNull]
    │                   │   │           ├── stackCount (39) — [text]
    │                   │   │           ├── ingredients (30)
    │                   │   │           ├── rotProg (26) — [text]
    │                   │   │           ├── infectedPawns (12)
    │                   │   │           └── verbTracker (1)
    │                   │   │               └── verbs (1) — attrs: [IsNull]
    │                   │   ├── itemsNotForSale (178)
    │                   │   │   └── li (36) — [text]
    │                   │   └── unpackedCaravanItems (178)
    │                   ├── inventoryStock (178) — attrs: [IsNull]
    │                   │   └── stockEntries (4)
    │                   │       ├── keys (4)
    │                   │       │   └── li (12) — [text]
    │                   │       └── values (4)
    │                   │           └── li (12)
    │                   │               └── thingDef (12) — [text]
    │                   ├── isEnabled (178) — [text]
    │                   ├── jobs (178)
    │                   │   ├── curDriver (178) — attrs: [IsNull]
    │                   │   ├── curJob (178) — attrs: [IsNull]
    │                   │   ├── formingCaravanTick (178) — [text]
    │                   │   └── jobQueue (178)
    │                   │       └── jobs (178)
    │                   ├── kindDef (178) — [text]
    │                   ├── lastKeepDisplayTick (178) — [text]
    │                   ├── lastStudiedTick (178) — [text]
    │                   ├── learnedAbilities (178)
    │                   ├── learning (178) — attrs: [IsNull]
    │                   ├── loadouts (178)
    │                   │   └── curLoadout (178) — [text]
    │                   ├── lord (178) — [text]
    │                   ├── mechanitor (178) — attrs: [IsNull]
    │                   ├── meleeVerbs (178)
    │                   │   ├── curMeleeVerb (178) — [text]
    │                   │   ├── terrainVerbs (178) — attrs: [IsNull]
    │                   │   └── curMeleeVerbUpdateTick (18) — [text]
    │                   ├── mindState (178)
    │                   │   ├── babyAutoBreastfeedMoms (178)
    │                   │   │   ├── keys (178)
    │                   │   │   └── values (178)
    │                   │   ├── babyCaravanBreastfeed (178)
    │                   │   │   ├── keys (178)
    │                   │   │   └── values (178)
    │                   │   ├── breachingTarget (178) — attrs: [IsNull]
    │                   │   ├── canFleeIndividual (178) — [text]
    │                   │   ├── droppedWeapon (178) — [text]
    │                   │   ├── duty (178) — attrs: [IsNull]
    │                   │   ├── enemyTarget (178) — [text]
    │                   │   ├── inspirationHandler (178)
    │                   │   │   └── curState (178) — attrs: [IsNull]
    │                   │   ├── knownExploder (178) — [text]
    │                   │   ├── lastAttackTargetTick (178) — [text]
    │                   │   ├── lastEngageTargetTick (178) — [text]
    │                   │   ├── lastMannedThing (178) — [text]
    │                   │   ├── lastMeleeThreatHarmTick (178) — [text]
    │                   │   ├── lastSelfTendTick (178) — [text]
    │                   │   ├── meleeThreat (178) — [text]
    │                   │   ├── mentalBreaker (178)
    │                   │   │   └── ticksBelowMinor (1) — [text]
    │                   │   ├── mentalFitGenerator (178)
    │                   │   ├── mentalStateHandler (178)
    │                   │   │   └── curState (178) — attrs: [IsNull]
    │                   │   ├── priorityWork (178)
    │                   │   │   └── prioritizedCell (178) — [text]
    │                   │   ├── resurrectTarget (178) — attrs: [IsNull]
    │                   │   ├── thinkData (178)
    │                   │   │   ├── keys (178)
    │                   │   │   └── values (178)
    │                   │   ├── lastDayInteractionTick (46) — [text]
    │                   │   ├── lastCombatantTick (38) — [text]
    │                   │   ├── hibernationEndedTick (13) — [text]
    │                   │   └── lastHumanMeatIngestedTick (4) — [text]
    │                   ├── name (178) — attrs: [Class]
    │                   │   ├── first (178) — [text]
    │                   │   ├── last (178) — [text]
    │                   │   └── nick (16) — [text]
    │                   ├── natives (178) — attrs: [IsNull]
    │                   ├── needs (178)
    │                   │   └── needs (178)
    │                   │       └── li (583) — attrs: [Class]
    │                   │           ├── curLevel (583) — [text]
    │                   │           ├── def (583) — [text]
    │                   │           ├── recentMemory (178)
    │                   │           │   ├── lastLightTick (18) — [text]
    │                   │           │   └── lastOutdoorTick (18) — [text]
    │                   │           ├── thoughts (178)
    │                   │           │   └── memories (178)
    │                   │           │       └── memories (178)
    │                   │           │           └── li (81) — attrs: [Class]
    │                   │           │               ├── def (81) — [text]
    │                   │           │               ├── durationTicksOverride (81) — [text]
    │                   │           │               ├── otherPawn (81) — [text]
    │                   │           │               ├── sourcePrecept (81) — [text]
    │                   │           │               ├── age (58) — [text]
    │                   │           │               ├── moodPowerFactor (57) — [text]
    │                   │           │               ├── opinionOffset (57) — [text]
    │                   │           │               ├── titleDef (19) — [text]
    │                   │           │               └── weapon (5) — [text]
    │                   │           ├── lastNonStarvingTick (58) — [text]
    │                   │           ├── bored (4)
    │                   │           │   └── vals (4)
    │                   │           │       └── li (52) — [text]
    │                   │           └── tolerances (4)
    │                   │               └── vals (4)
    │                   │                   └── li (52) — [text]
    │                   ├── outfits (178) — attrs: [IsNull]
    │                   │   ├── curOutfit (4) — [text]
    │                   │   └── overrideHandler (4)
    │                   │       └── forcedAps (4)
    │                   ├── ownership (178)
    │                   │   ├── assignedDeathrestCasket (178) — [text]
    │                   │   ├── assignedGrave (178) — [text]
    │                   │   ├── assignedMeditationSpot (178) — [text]
    │                   │   ├── assignedThrone (178) — [text]
    │                   │   └── ownedBed (178) — [text]
    │                   ├── pather (178) — attrs: [IsNull]
    │                   ├── playerSettings (178) — attrs: [IsNull]
    │                   │   ├── allowedAreas (4)
    │                   │   │   ├── keys (4)
    │                   │   │   └── values (4)
    │                   │   ├── displayOrder (4) — [text]
    │                   │   ├── master (4) — [text]
    │                   │   └── medCare (4) — [text]
    │                   ├── psychicEntropy (178)
    │                   │   ├── limitEntropyAmount (178) — [text]
    │                   │   └── currentPsyfocus (165) — [text]
    │                   ├── questTags (178) — attrs: [IsNull]
    │                   ├── reading (178) — attrs: [IsNull]
    │                   │   └── curAssignment (4) — [text]
    │                   ├── records (178)
    │                   │   ├── battleActive (178) — [text]
    │                   │   ├── records (178)
    │                   │   │   └── vals (178)
    │                   │   │       └── li (12,816) — [text]
    │                   │   └── battleExitTick (2) — [text]
    │                   ├── roping (178) — attrs: [IsNull]
    │                   ├── rotationTracker (178) — attrs: [IsNull]
    │                   ├── royalty (178)
    │                   │   ├── abilities (178)
    │                   │   │   └── li (187)
    │                   │   │       ├── Id (187) — [text]
    │                   │   │       ├── charges (187) — [text]
    │                   │   │       ├── def (187) — [text]
    │                   │   │       ├── maxCharges (187) — [text]
    │                   │   │       ├── sourcePrecept (187) — [text]
    │                   │   │       └── verbTracker (187)
    │                   │   │           └── verbs (187)
    │                   │   │               └── li (187) — attrs: [Class]
    │                   │   │                   ├── MVCF_ManagedVerb (187) — attrs: [IsNull]
    │                   │   │                   ├── ability (187) — [text]
    │                   │   │                   ├── canHitNonTargetPawnsNow (187) — [text]
    │                   │   │                   ├── currentDestination (187) — [text]
    │                   │   │                   ├── currentTarget (187) — [text]
    │                   │   │                   ├── lastShotTick (187) — [text]
    │                   │   │                   └── loadID (187) — [text]
    │                   │   ├── favor (178)
    │                   │   │   ├── keys (178)
    │                   │   │   │   └── li (145) — [text]
    │                   │   │   └── values (178)
    │                   │   │       └── li (145) — [text]
    │                   │   ├── heirs (178)
    │                   │   │   ├── keys (178)
    │                   │   │   │   └── li (1) — [text]
    │                   │   │   └── values (178)
    │                   │   │       └── li (1) — [text]
    │                   │   ├── highestTitles (178)
    │                   │   │   ├── keys (178)
    │                   │   │   │   └── li (145) — [text]
    │                   │   │   └── values (178)
    │                   │   │       └── li (145) — [text]
    │                   │   ├── permits (178)
    │                   │   │   └── li (648)
    │                   │   │       ├── faction (648) — [text]
    │                   │   │       ├── permit (648) — [text]
    │                   │   │       └── title (648) — [text]
    │                   │   └── titles (178)
    │                   │       └── li (145)
    │                   │           ├── def (145) — [text]
    │                   │           ├── faction (145) — [text]
    │                   │           ├── conceited (144) — [text]
    │                   │           └── receivedTick (20) — [text]
    │                   ├── shambler (178) — attrs: [IsNull]
    │                   ├── shoppingArea (178) — [text]
    │                   ├── skills (178)
    │                   │   ├── lastXpSinceMidnightResetTimestamp (178) — [text]
    │                   │   └── skills (178)
    │                   │       └── li (2,136)
    │                   │           ├── def (2,136) — [text]
    │                   │           ├── level (1,832) — [text]
    │                   │           ├── passion (668) — [text]
    │                   │           ├── xpSinceLastLevel (51) — [text]
    │                   │           └── xpSinceMidnight (41) — [text]
    │                   ├── social (178)
    │                   │   ├── additionalPregnancyApproachData (178)
    │                   │   │   └── partners (178)
    │                   │   │       ├── keys (178)
    │                   │   │       └── values (178)
    │                   │   ├── directRelations (178)
    │                   │   │   └── li (25)
    │                   │   │       ├── def (25) — [text]
    │                   │   │       ├── otherPawn (25) — [text]
    │                   │   │       └── startTicks (13) — [text]
    │                   │   ├── pregnancyApproaches (178)
    │                   │   │   ├── keys (178)
    │                   │   │   └── values (178)
    │                   │   ├── relativeInvolvedInRescueQuest (178) — [text]
    │                   │   ├── romanceEnableTick (178) — [text]
    │                   │   ├── virtualRelations (178)
    │                   │   │   └── li (10)
    │                   │   │       ├── def (10) — [text]
    │                   │   │       ├── record (10) — [text]
    │                   │   │       └── startTicks (8) — [text]
    │                   │   ├── everSeenByPlayer (142) — [text]
    │                   │   └── nextMarriageNameChange (1) — [text]
    │                   ├── stances (178)
    │                   │   ├── curStance (178) — attrs: [Class]
    │                   │   ├── stagger (178)
    │                   │   │   └── staggerMoveSpeedFactor (1) — [text]
    │                   │   └── stunner (178)
    │                   │       ├── adaptationTicksLeft (178)
    │                   │       │   ├── keys (178)
    │                   │       │   └── values (178)
    │                   │       └── showStunMote (178) — [text]
    │                   ├── story (178)
    │                   │   ├── birthLastName (178) — [text]
    │                   │   ├── bodyType (178) — [text]
    │                   │   ├── childhood (178) — [text]
    │                   │   ├── favoriteColorDef (178) — [text]
    │                   │   ├── hairColor (178) — [text]
    │                   │   ├── hairDef (178) — [text]
    │                   │   ├── headType (178) — [text]
    │                   │   ├── traits (178)
    │                   │   │   └── allTraits (178)
    │                   │   │       └── li (394)
    │                   │   │           ├── def (394) — [text]
    │                   │   │           ├── sourceGene (394) — [text]
    │                   │   │           ├── suppressedBy (394) — [text]
    │                   │   │           ├── degree (95) — [text]
    │                   │   │           └── suppressedByTrait (2) — [text]
    │                   │   ├── adulthood (147) — [text]
    │                   │   ├── skinColorOverride (11) — [text]
    │                   │   └── furDef (2) — [text]
    │                   ├── style (178)
    │                   │   ├── beardDef (178) — [text]
    │                   │   ├── bodyTattoo (178) — [text]
    │                   │   └── faceTattoo (178) — [text]
    │                   ├── styleObserver (178)
    │                   ├── targetHolder (178) — [text]
    │                   ├── thinker (178)
    │                   ├── ticksToReset (178) — [text]
    │                   ├── timetable (178) — attrs: [IsNull]
    │                   │   └── times (4)
    │                   │       └── li (96) — [text]
    │                   ├── trader (178) — attrs: [IsNull]
    │                   ├── training (178) — attrs: [IsNull]
    │                   ├── treeSightings (178)
    │                   │   ├── fullTreeSightings (178)
    │                   │   ├── miniTreeSightings (178)
    │                   │   └── superTreeSightings (178)
    │                   ├── verbTracker (178)
    │                   │   └── verbs (178)
    │                   │       └── li (712) — attrs: [Class]
    │                   │           ├── MVCF_ManagedVerb (712)
    │                   │           │   ├── enabled (712) — [text]
    │                   │           │   └── loadId (712) — [text]
    │                   │           ├── canHitNonTargetPawnsNow (712) — [text]
    │                   │           ├── currentDestination (712) — [text]
    │                   │           ├── currentTarget (712) — [text]
    │                   │           ├── lastShotTick (712) — [text]
    │                   │           └── loadID (712) — [text]
    │                   ├── vfee_honors (178)
    │                   │   ├── honors (178)
    │                   │   └── pendingHonors (178)
    │                   ├── workSettings (178)
    │                   │   └── priorities (178) — attrs: [IsNull]
    │                   │       └── vals (4)
    │                   │           └── li (208) — [text]
    │                   ├── faction (175) — [text]
    │                   ├── gender (98) — [text]
    │                   ├── becameWorldPawnTickAbs (48) — [text]
    │                   ├── tickDelta (45) — [text]
    │                   ├── pos (18) — [text]
    │                   ├── rot (15) — [text]
    │                   ├── OriginMap (4) — [text]
    │                   └── wasLeftBehindStartingPawn (4) — [text]
    └── meta (1)
        ├── gameVersion (1) — [text]
        ├── modIds (1)
        │   └── li (270) — [text]
        ├── modNames (1)
        │   └── li (270) — [text]
        └── modSteamIds (1)
            └── li (270) — [text]