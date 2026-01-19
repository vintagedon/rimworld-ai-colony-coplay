# RimWorld Save Schema Discovery

**Source:** `the-fringe-benefit#§#Autosave-129.rws`
**Generated:** 2026-01-18 10:20:21
**File Size:** 17.1 MB

## Summary

| Metric | Value |
|--------|-------|
| Total XML Elements | 168,796 |
| Unique Tag Paths | 1,611 |
| Maximum Depth | 6 |

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
    │   │   │           └── areas (1)
    │   │   └── pawns (1)
    │   │       ├── keys (1)
    │   │       │   └── li (10) — [text]
    │   │       └── values (1)
    │   │           └── li (10)
    │   │               └── areaStatesByMap (10)
    │   ├── battleLog (1)
    │   │   └── battles (1)
    │   │       └── li (114)
    │   │           ├── absorbedBy (114) — [text]
    │   │           ├── creationTimestamp (114) — [text]
    │   │           ├── entries (114)
    │   │           │   └── li (322) — attrs: [Class]
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
    │   │       │       ├── pawns (5)
    │   │       │       ├── defenders (4)
    │   │       │       ├── initTime (4) — [text]
    │   │       │       └── raiders (4)
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
    │   │       ├── QuestLog (1)
    │   │       ├── absentMindedWithLastDiscardedTick (1)
    │   │       │   ├── keys (1)
    │   │       │   └── values (1)
    │   │       ├── achievementList (1)
    │   │       │   └── li (212)
    │   │       │       ├── def (212) — [text]
    │   │       │       ├── tracker (212) — attrs: [Class]
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
    │   │       │   │   ├── allowedHitPointsPercents (1) — [text]
    │   │       │   │   ├── allowedMentalBreakChance (1) — [text]
    │   │       │   │   ├── allowedQualityLevels (1) — [text]
    │   │       │   │   └── disallowedSpecialFilters (1)
    │   │       │   ├── id (1) — [text]
    │   │       │   └── label (1) — [text]
    │   │       ├── draftedActions (1)
    │   │       │   ├── keys (1)
    │   │       │   │   └── li (7) — [text]
    │   │       │   └── values (1)
    │   │       │       └── li (7)
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
    │   │       │       └── values (1)
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
    │   │       │       └── values (1)
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
    │   │           │   ├── allowedHitPointsPercents (11) — [text]
    │   │           │   ├── allowedMentalBreakChance (11) — [text]
    │   │           │   ├── allowedQualityLevels (11) — [text]
    │   │           │   └── disallowedSpecialFilters (11)
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
    │   │   ├── historyEventsManager (1)
    │   │   │   ├── colonistEvents (1)
    │   │   │   │   └── vals (1)
    │   │   │   │       └── li (193)
    │   │   │   └── eventsAffectingFaction (1)
    │   │   │       ├── keys (1)
    │   │   │       │   └── li (5) — [text]
    │   │   │       └── values (1)
    │   │   │           └── li (5)
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
    │   │       ├── attackTargetReservationManager (1)
    │   │       │   └── reservations (1)
    │   │       ├── autoSlaughterManager (1)
    │   │       │   └── configs (1)
    │   │       │       └── li (455)
    │   │       ├── components (1)
    │   │       │   └── li (77) — attrs: [Class]
    │   │       │       ├── LWMDS_settingsForBPandFrames (1)
    │   │       │       ├── PatientFoodPolicy (1) — [text]
    │   │       │       ├── QuestLog (1)
    │   │       │       ├── TA_Expose_Numbers (1)
    │   │       │       ├── TA_Expose_People (1)
    │   │       │       ├── TA_Expose_People_isSaved (1) — [text]
    │   │       │       ├── acceptSurgery (1) — [text]
    │   │       │       ├── allMapTeleports (1)
    │   │       │       ├── animalsToCarry (1)
    │   │       │       ├── awaitingIngredients (1)
    │   │       │       ├── awaitingPickup (1)
    │   │       │       ├── biomeGrid (1) — attrs: [IsNull]
    │   │       │       ├── cannons (1)
    │   │       │       ├── colonist_junk_tracker_backup (1)
    │   │       │       ├── colonist_obelisk_tracker_backup (1)
    │   │       │       ├── controller (1) — [text]
    │   │       │       ├── defaultAreaRestriction (1) — [text]
    │   │       │       ├── defaultAreaShopping (1) — [text]
    │   │       │       ├── destroyedBuildings (1)
    │   │       │       ├── drugPolicy (1)
    │   │       │       ├── durabilities (1)
    │   │       │       ├── fleshmassDestroyTicks (1)
    │   │       │       ├── fleshmassToDestroy (1)
    │   │       │       ├── growZoneRegistry (1)
    │   │       │       ├── hediffOverlays (1)
    │   │       │       ├── incidentQueue (1)
    │   │       │       ├── lastQuest (1) — attrs: [IsNull]
    │   │       │       ├── lastRenderedCounter (1) — [text]
    │   │       │       ├── lastRenderedHour (1) — [text]
    │   │       │       ├── launcherTargets (1)
    │   │       │       ├── listeners (1)
    │   │       │       ├── lootables_InMap (1)
    │   │       │       ├── nextQueueInspection (1) — [text]
    │   │       │       ├── obelisks_InMap (1)
    │   │       │       ├── objectives (1)
    │   │       │       ├── openingHours (1)
    │   │       │       ├── paragonsToCarry (1)
    │   │       │       ├── patients (1)
    │   │       │       ├── pawnsDesiringSuicide (1)
    │   │       │       ├── questTags (1) — attrs: [IsNull]
    │   │       │       ├── refuseGuestsUntilWeHaveBeds (1) — [text]
    │   │       │       ├── refusedOperations (1)
    │   │       │       ├── restaurants (1)
    │   │       │       ├── roadEdgeTiles (1)
    │   │       │       ├── roofMaintenanceGrid (1)
    │   │       │       ├── rsTargetEndX (1) — [text]
    │   │       │       ├── rsTargetEndZ (1) — [text]
    │   │       │       ├── rsTargetStartX (1) — [text]
    │   │       │       ├── rsTargetStartZ (1) — [text]
    │   │       │       ├── signaledCaravanArriving (1) — [text]
    │   │       │       ├── stores (1)
    │   │       │       ├── studiables_InMap (1)
    │   │       │       ├── surfaceResourceGrid (1)
    │   │       │       ├── terrains (1)
    │   │       │       ├── terrorism (1)
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
    │   │       │       └── values (1)
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
    │   │       │   └── map (1) — [text]
    │   │       ├── storyState (1)
    │   │       │   ├── colonistCountTicks (1)
    │   │       │   │   ├── keys (1)
    │   │       │   │   └── values (1)
    │   │       │   ├── lastFireTicks (1)
    │   │       │   │   ├── keys (1)
    │   │       │   │   └── values (1)
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
    │   │       │       ├── huntingPackMaster (81) — [text]
    │   │       │       ├── huntingPackMembers (81)
    │   │       │       ├── newGraphicPath (80) — [text]
    │   │       │       ├── newGraphicSinglePath (80) — [text]
    │   │       │       ├── quality (73) — [text]
    │   │       │       ├── abilities (61) — attrs: [IsNull]
    │   │       │       ├── MVCF_VerbManager (60) — attrs: [IsNull]
    │   │       │       ├── ThingsHauledToInventory (60)
    │   │       │       ├── ageTracker (60)
    │   │       │       ├── apparel (60) — attrs: [IsNull]
    │   │       │       ├── carryTracker (60)
    │   │       │       ├── connections (60)
    │   │       │       ├── creepjoiner (60) — attrs: [IsNull]
    │   │       │       ├── deadlifeDustFaction (60) — [text]
    │   │       │       ├── drafter (60) — attrs: [IsNull]
    │   │       │       ├── drugs (60) — attrs: [IsNull]
    │   │       │       ├── duplicate (60)
    │   │       │       ├── equipment (60) — attrs: [IsNull]
    │   │       │       ├── filth (60)
    │   │       │       ├── flight (60)
    │   │       │       ├── foodRestriction (60) — attrs: [IsNull]
    │   │       │       ├── genes (60) — attrs: [IsNull]
    │   │       │       ├── guest (60) — attrs: [IsNull]
    │   │       │       ├── guilt (60) — attrs: [IsNull]
    │   │       │       ├── healthTracker (60)
    │   │       │       ├── ideo (60) — attrs: [IsNull]
    │   │       │       ├── infectionVectors (60) — attrs: [IsNull]
    │   │       │       ├── interactions (60) — attrs: [IsNull]
    │   │       │       ├── inventory (60)
    │   │       │       ├── inventoryStock (60) — attrs: [IsNull]
    │   │       │       ├── isEnabled (60) — [text]
    │   │       │       ├── jobs (60)
    │   │       │       ├── kindDef (60) — [text]
    │   │       │       ├── learning (60) — attrs: [IsNull]
    │   │       │       ├── loadouts (60)
    │   │       │       ├── mechanitor (60) — attrs: [IsNull]
    │   │       │       ├── meleeVerbs (60)
    │   │       │       ├── mindState (60)
    │   │       │       ├── name (60) — attrs: [Class, IsNull]
    │   │       │       ├── natives (60)
    │   │       │       ├── needs (60)
    │   │       │       ├── outfits (60) — attrs: [IsNull]
    │   │       │       ├── ownership (60)
    │   │       │       ├── pather (60)
    │   │       │       ├── playerSettings (60) — attrs: [IsNull]
    │   │       │       ├── psychicEntropy (60) — attrs: [IsNull]
    │   │       │       ├── reading (60) — attrs: [IsNull]
    │   │       │       ├── records (60)
    │   │       │       ├── roping (60)
    │   │       │       ├── rotationTracker (60)
    │   │       │       ├── royalty (60) — attrs: [IsNull]
    │   │       │       ├── shambler (60) — attrs: [IsNull]
    │   │       │       ├── skills (60) — attrs: [IsNull]
    │   │       │       ├── social (60) — attrs: [IsNull]
    │   │       │       ├── stances (60)
    │   │       │       ├── story (60) — attrs: [IsNull]
    │   │       │       ├── style (60) — attrs: [IsNull]
    │   │       │       ├── styleObserver (60) — attrs: [IsNull]
    │   │       │       ├── thinker (60) — attrs: [Class]
    │   │       │       ├── timetable (60) — attrs: [IsNull]
    │   │       │       ├── trader (60) — attrs: [IsNull]
    │   │       │       ├── training (60) — attrs: [IsNull]
    │   │       │       ├── treeSightings (60) — attrs: [IsNull]
    │   │       │       ├── vfee_honors (60)
    │   │       │       ├── workSettings (60) — attrs: [IsNull]
    │   │       │       ├── lastStudiedTick (59) — [text]
    │   │       │       ├── targetHolder (59) — [text]
    │   │       │       ├── innerContainer (50) — attrs: [Class]
    │   │       │       ├── rotProg (50) — [text]
    │   │       │       ├── overrideGraphicIndex (40) — [text]
    │   │       │       ├── thickness (38) — [text]
    │   │       │       ├── operationsBillStack (36)
    │   │       │       ├── timeOfDeath (36) — [text]
    │   │       │       ├── vanishAfterTimestamp (36) — [text]
    │   │       │       ├── approachingPawn (31) — [text]
    │   │       │       ├── glowOn (31) — [text]
    │   │       │       ├── lastFriendlyTouchTick (31) — [text]
    │   │       │       ├── nextSpawnTimestamp (31) — [text]
    │   │       │       ├── styleDef (31) — [text]
    │   │       │       ├── forbidden (29) — [text]
    │   │       │       ├── taleRef (28) — attrs: [Class, IsNull]
    │   │       │       ├── gender (27) — [text]
    │   │       │       ├── assignedPawns (25)
    │   │       │       ├── uninstalledAssignedPawns (25)
    │   │       │       ├── alreadySetDefaultMed (21) — [text]
    │   │       │       ├── settings (21)
    │   │       │       ├── storageGroup (21) — [text]
    │   │       │       ├── diningSpots (16)
    │   │       │       ├── billStack (14)
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
    │   │       │       ├── stunHandler (8)
    │   │       │       ├── RRPawnBadge_Badge1 (7) — [text]
    │   │       │       ├── gun (7) — attrs: [Class]
    │   │       │       ├── lastSleepDisturbedTick (7) — [text]
    │   │       │       ├── title (7) — [text]
    │   │       │       ├── active (6) — [text]
    │   │       │       ├── authorName (6) — [text]
    │   │       │       ├── infectedPawns (6)
    │   │       │       ├── ingredients (6)
    │   │       │       ├── fertilizedBy (5) — [text]
    │   │       │       ├── lastAttackTargetTick (4) — [text]
    │   │       │       ├── storageSettings (4)
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
    │   ├── outfitDatabase (1)
    │   │   └── outfits (1)
    │   │       └── li (7)
    │   │           ├── filter (7)
    │   │           │   ├── allowedDefs (7)
    │   │           │   ├── allowedHitPointsPercents (7) — [text]
    │   │           │   ├── allowedMentalBreakChance (7) — [text]
    │   │           │   ├── allowedQualityLevels (7) — [text]
    │   │           │   └── disallowedSpecialFilters (7)
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
    │   │           │   ├── pawn (88) — [text]
    │   │           │   ├── relationInfo (88) — [text]
    │   │           │   ├── royalTitles (88) — attrs: [IsNull]
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
    │   │           │   ├── pawn (87) — [text]
    │   │           │   ├── relationInfo (87) — [text]
    │   │           │   ├── royalTitles (87) — attrs: [IsNull]
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
    │       │       │   └── values (3)
    │       │       ├── tickCounter (3) — [text]
    │       │       ├── ActiveLevel (1) — [text]
    │       │       ├── AlertLevelsList (1)
    │       │       ├── AnimalActivePolicies (1)
    │       │       │   └── li (1)
    │       │       ├── AnimalLinks (1)
    │       │       │   └── li (3)
    │       │       ├── AnimalPolicies (1)
    │       │       │   └── li (1)
    │       │       ├── AssignActivePolicies (1)
    │       │       │   └── li (1)
    │       │       ├── AssignLinks (1)
    │       │       │   └── li (7)
    │       │       ├── AssignPolicies (1)
    │       │       │   └── li (1)
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
    │       │       ├── MechLinks (1)
    │       │       ├── MechPolicies (1)
    │       │       │   └── li (1)
    │       │       ├── Numbers_Numbers_MainTable (1)
    │       │       │   └── li (15) — [text]
    │       │       ├── Queue (1)
    │       │       │   └── li (12) — [text]
    │       │       ├── RestrictActivePolicies (1)
    │       │       │   └── li (1)
    │       │       ├── RestrictPolicies (1)
    │       │       │   └── li (1)
    │       │       ├── ScheduleLinks (1)
    │       │       │   └── li (7)
    │       │       ├── TA_Expose_Numbers (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── TA_Expose_People (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── TA_Expose_People_isSaved (1) — [text]
    │       │       ├── TA_Expose_TabCostSettings (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── USH_PawnSkinColors (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── WeaponsActivePolicies (1)
    │       │       │   └── li (1)
    │       │       ├── WeaponsLinks (1)
    │       │       │   └── li (6)
    │       │       ├── WeaponsPolicies (1)
    │       │       │   └── li (1)
    │       │       ├── WorkActivePolicies (1)
    │       │       │   └── li (1)
    │       │       ├── WorkLinks (1)
    │       │       │   └── li (7)
    │       │       ├── WorkPolicies (1)
    │       │       │   └── li (1)
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
    │       │       │   └── values (1)
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
    │       │       ├── mapSeeds (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── mapsParent (1)
    │       │       │   ├── keys (1)
    │       │       │   └── values (1)
    │       │       ├── mostSkilledPawn (1) — [text]
    │       │       ├── partyHunt (1)
    │       │       │   └── pawns (1)
    │       │       ├── pawnGroups (1)
    │       │       │   └── li (1)
    │       │       ├── pawnSquads (1)
    │       │       ├── pawns (1)
    │       │       ├── pawnsWithNightOwl (1)
    │       │       ├── plotMissions (1)
    │       │       ├── remoteMapIds (1)
    │       │       ├── savedPositions (1)
    │       │       │   └── li (7)
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
    │       │           └── values (1)
    │       ├── factionManager (1)
    │       │   ├── allFactions (1)
    │       │   │   └── li (21)
    │       │   │       ├── colorFromSpectrum (21) — [text]
    │       │   │       ├── def (21) — [text]
    │       │   │       ├── ideos (21) — attrs: [IsNull]
    │       │   │       ├── kidnapped (21)
    │       │   │       ├── leader (21) — [text]
    │       │   │       ├── loadID (21) — [text]
    │       │   │       ├── name (21) — [text]
    │       │   │       ├── predatorThreats (21)
    │       │   │       ├── questTags (21) — attrs: [IsNull]
    │       │   │       ├── randomKey (21) — [text]
    │       │   │       ├── relations (21)
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
    │       │   │       ├── iconDef (15) — [text]
    │       │   │       ├── id (15) — [text]
    │       │   │       ├── leaderTitleFemale (15) — [text]
    │       │   │       ├── leaderTitleMale (15) — [text]
    │       │   │       ├── memberName (15) — [text]
    │       │   │       ├── memes (15)
    │       │   │       ├── name (15) — [text]
    │       │   │       ├── precepts (15)
    │       │   │       ├── style (15)
    │       │   │       ├── thingStyleCategories (15)
    │       │   │       ├── usedSymbolPacks (15)
    │       │   │       ├── usedSymbols (15)
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
    │       │           ├── tile (441) — [text]
    │       │           ├── tickDelta (407) — [text]
    │       │           ├── nameInt (383) — [text]
    │       │           ├── previouslyGeneratedInhabitants (371)
    │       │           ├── trader (371)
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
    │       │           ├── core (6) — attrs: [IsNull]
    │       │           ├── expireSignal (6) — attrs: [IsNull]
    │       │           ├── mannableCount (6) — [text]
    │       │           ├── parts (6)
    │       │           ├── prisoner (6)
    │       │           ├── refugee (6)
    │       │           ├── requestingFaction (6) — [text]
    │       │           ├── rewards (6) — attrs: [Class]
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
    │           │       ├── ThingsHauledToInventory (2)
    │           │       ├── abilities (2)
    │           │       ├── ageTracker (2)
    │           │       ├── apparel (2)
    │           │       ├── bed (2) — [text]
    │           │       ├── boughtItems (2)
    │           │       ├── carryTracker (2)
    │           │       ├── connections (2)
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
    │           │       ├── faction (2) — [text]
    │           │       ├── filth (2) — attrs: [IsNull]
    │           │       ├── flight (2) — attrs: [IsNull]
    │           │       ├── foodRestriction (2) — attrs: [IsNull]
    │           │       ├── gender (2) — [text]
    │           │       ├── genes (2)
    │           │       ├── guest (2)
    │           │       ├── guestArea (2) — [text]
    │           │       ├── guilt (2)
    │           │       ├── healthTracker (2)
    │           │       ├── id (2) — [text]
    │           │       ├── ideo (2)
    │           │       ├── infectionVectors (2)
    │           │       ├── interactions (2) — attrs: [IsNull]
    │           │       ├── inventory (2)
    │           │       ├── inventoryStock (2) — attrs: [IsNull]
    │           │       ├── isEnabled (2) — [text]
    │           │       ├── jobs (2)
    │           │       ├── kindDef (2) — [text]
    │           │       ├── lastKeepDisplayTick (2) — [text]
    │           │       ├── lastStudiedTick (2) — [text]
    │           │       ├── learnedAbilities (2)
    │           │       ├── learning (2) — attrs: [IsNull]
    │           │       ├── loadouts (2)
    │           │       ├── lord (2) — [text]
    │           │       ├── mechanitor (2) — attrs: [IsNull]
    │           │       ├── meleeVerbs (2)
    │           │       ├── mindState (2)
    │           │       ├── name (2) — attrs: [Class]
    │           │       ├── natives (2) — attrs: [IsNull]
    │           │       ├── needs (2)
    │           │       ├── outfits (2) — attrs: [IsNull]
    │           │       ├── ownership (2)
    │           │       ├── pather (2) — attrs: [IsNull]
    │           │       ├── playerSettings (2) — attrs: [IsNull]
    │           │       ├── psychicEntropy (2)
    │           │       ├── questTags (2) — attrs: [IsNull]
    │           │       ├── reading (2) — attrs: [IsNull]
    │           │       ├── records (2)
    │           │       ├── roping (2) — attrs: [IsNull]
    │           │       ├── rotationTracker (2) — attrs: [IsNull]
    │           │       ├── royalty (2)
    │           │       ├── shambler (2) — attrs: [IsNull]
    │           │       ├── shoppingArea (2) — [text]
    │           │       ├── skills (2)
    │           │       ├── social (2)
    │           │       ├── stances (2)
    │           │       ├── story (2)
    │           │       ├── style (2)
    │           │       ├── styleObserver (2)
    │           │       ├── targetHolder (2) — [text]
    │           │       ├── thinker (2)
    │           │       ├── tickDelta (2) — [text]
    │           │       ├── ticksToReset (2) — [text]
    │           │       ├── timetable (2) — attrs: [IsNull]
    │           │       ├── trader (2) — attrs: [IsNull]
    │           │       ├── training (2) — attrs: [IsNull]
    │           │       ├── treeSightings (2)
    │           │       ├── verbTracker (2)
    │           │       ├── vfee_honors (2)
    │           │       ├── workSettings (2)
    │           │       ├── becameWorldPawnTickAbs (1) — [text]
    │           │       ├── pos (1) — [text]
    │           │       └── rot (1) — [text]
    │           ├── pawnsDead (1)
    │           │   └── li (42)
    │           │       ├── MVCF_VerbManager (42) — attrs: [IsNull]
    │           │       ├── ThingsHauledToInventory (42)
    │           │       ├── abilities (42) — attrs: [IsNull]
    │           │       ├── ageTracker (42)
    │           │       ├── apparel (42) — attrs: [IsNull]
    │           │       ├── becameWorldPawnTickAbs (42) — [text]
    │           │       ├── carryTracker (42) — attrs: [IsNull]
    │           │       ├── connections (42)
    │           │       ├── creepjoiner (42) — attrs: [IsNull]
    │           │       ├── deadlifeDustFaction (42) — [text]
    │           │       ├── def (42) — [text]
    │           │       ├── despawnedTick (42) — [text]
    │           │       ├── drafter (42) — attrs: [IsNull]
    │           │       ├── drugs (42) — attrs: [IsNull]
    │           │       ├── duplicate (42) — attrs: [IsNull]
    │           │       ├── equipment (42) — attrs: [IsNull]
    │           │       ├── filth (42) — attrs: [IsNull]
    │           │       ├── flight (42) — attrs: [IsNull]
    │           │       ├── foodRestriction (42) — attrs: [IsNull]
    │           │       ├── genes (42) — attrs: [IsNull]
    │           │       ├── guest (42) — attrs: [IsNull]
    │           │       ├── guilt (42) — attrs: [IsNull]
    │           │       ├── healthTracker (42)
    │           │       ├── id (42) — [text]
    │           │       ├── ideo (42) — attrs: [IsNull]
    │           │       ├── infectionVectors (42) — attrs: [IsNull]
    │           │       ├── interactions (42) — attrs: [IsNull]
    │           │       ├── inventory (42)
    │           │       ├── inventoryStock (42) — attrs: [IsNull]
    │           │       ├── isEnabled (42) — [text]
    │           │       ├── jobs (42) — attrs: [IsNull]
    │           │       ├── kindDef (42) — [text]
    │           │       ├── learning (42) — attrs: [IsNull]
    │           │       ├── loadouts (42)
    │           │       ├── mechanitor (42) — attrs: [IsNull]
    │           │       ├── meleeVerbs (42)
    │           │       ├── mindState (42) — attrs: [IsNull]
    │           │       ├── name (42) — attrs: [Class, IsNull]
    │           │       ├── natives (42) — attrs: [IsNull]
    │           │       ├── needs (42) — attrs: [IsNull]
    │           │       ├── outfits (42) — attrs: [IsNull]
    │           │       ├── ownership (42)
    │           │       ├── pather (42) — attrs: [IsNull]
    │           │       ├── playerSettings (42) — attrs: [IsNull]
    │           │       ├── psychicEntropy (42) — attrs: [IsNull]
    │           │       ├── questTags (42) — attrs: [IsNull]
    │           │       ├── reading (42) — attrs: [IsNull]
    │           │       ├── records (42)
    │           │       ├── roping (42) — attrs: [IsNull]
    │           │       ├── rotationTracker (42) — attrs: [IsNull]
    │           │       ├── royalty (42) — attrs: [IsNull]
    │           │       ├── shambler (42) — attrs: [IsNull]
    │           │       ├── skills (42) — attrs: [IsNull]
    │           │       ├── social (42) — attrs: [IsNull]
    │           │       ├── stances (42) — attrs: [IsNull]
    │           │       ├── story (42) — attrs: [IsNull]
    │           │       ├── style (42) — attrs: [IsNull]
    │           │       ├── styleObserver (42) — attrs: [IsNull]
    │           │       ├── thinker (42) — attrs: [IsNull]
    │           │       ├── timetable (42) — attrs: [IsNull]
    │           │       ├── trader (42) — attrs: [IsNull]
    │           │       ├── training (42) — attrs: [IsNull]
    │           │       ├── treeSightings (42) — attrs: [IsNull]
    │           │       ├── verbTracker (42)
    │           │       ├── vfee_honors (42)
    │           │       ├── workSettings (42) — attrs: [IsNull]
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
    │                   ├── ThingsHauledToInventory (178)
    │                   ├── abilities (178)
    │                   ├── ageTracker (178)
    │                   ├── apparel (178)
    │                   ├── bed (178) — [text]
    │                   ├── boughtItems (178)
    │                   ├── carryTracker (178)
    │                   ├── connections (178)
    │                   ├── creepjoiner (178) — attrs: [IsNull]
    │                   ├── currentlyCasting (178) — [text]
    │                   ├── currentlyCastingTargets (178)
    │                   ├── deadlifeDustFaction (178) — [text]
    │                   ├── def (178) — [text]
    │                   ├── despawnedTick (178) — [text]
    │                   ├── drafter (178) — attrs: [IsNull]
    │                   ├── drugs (178) — attrs: [IsNull]
    │                   ├── duplicate (178)
    │                   ├── equipment (178)
    │                   ├── filth (178) — attrs: [IsNull]
    │                   ├── flight (178) — attrs: [IsNull]
    │                   ├── foodRestriction (178) — attrs: [IsNull]
    │                   ├── genes (178)
    │                   ├── guest (178)
    │                   ├── guestArea (178) — [text]
    │                   ├── guilt (178)
    │                   ├── healthTracker (178)
    │                   ├── id (178) — [text]
    │                   ├── ideo (178)
    │                   ├── infectionVectors (178)
    │                   ├── interactions (178) — attrs: [IsNull]
    │                   ├── inventory (178)
    │                   ├── inventoryStock (178) — attrs: [IsNull]
    │                   ├── isEnabled (178) — [text]
    │                   ├── jobs (178)
    │                   ├── kindDef (178) — [text]
    │                   ├── lastKeepDisplayTick (178) — [text]
    │                   ├── lastStudiedTick (178) — [text]
    │                   ├── learnedAbilities (178)
    │                   ├── learning (178) — attrs: [IsNull]
    │                   ├── loadouts (178)
    │                   ├── lord (178) — [text]
    │                   ├── mechanitor (178) — attrs: [IsNull]
    │                   ├── meleeVerbs (178)
    │                   ├── mindState (178)
    │                   ├── name (178) — attrs: [Class]
    │                   ├── natives (178) — attrs: [IsNull]
    │                   ├── needs (178)
    │                   ├── outfits (178) — attrs: [IsNull]
    │                   ├── ownership (178)
    │                   ├── pather (178) — attrs: [IsNull]
    │                   ├── playerSettings (178) — attrs: [IsNull]
    │                   ├── psychicEntropy (178)
    │                   ├── questTags (178) — attrs: [IsNull]
    │                   ├── reading (178) — attrs: [IsNull]
    │                   ├── records (178)
    │                   ├── roping (178) — attrs: [IsNull]
    │                   ├── rotationTracker (178) — attrs: [IsNull]
    │                   ├── royalty (178)
    │                   ├── shambler (178) — attrs: [IsNull]
    │                   ├── shoppingArea (178) — [text]
    │                   ├── skills (178)
    │                   ├── social (178)
    │                   ├── stances (178)
    │                   ├── story (178)
    │                   ├── style (178)
    │                   ├── styleObserver (178)
    │                   ├── targetHolder (178) — [text]
    │                   ├── thinker (178)
    │                   ├── ticksToReset (178) — [text]
    │                   ├── timetable (178) — attrs: [IsNull]
    │                   ├── trader (178) — attrs: [IsNull]
    │                   ├── training (178) — attrs: [IsNull]
    │                   ├── treeSightings (178)
    │                   ├── verbTracker (178)
    │                   ├── vfee_honors (178)
    │                   ├── workSettings (178)
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