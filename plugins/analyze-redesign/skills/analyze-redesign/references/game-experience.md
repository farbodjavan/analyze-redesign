# Game and Interactive Experience Lens

Use this module for games, playful learning, spatial puzzles, interactive stories, simulations, or any product whose value depends on moment-to-moment control, challenge, feedback, progression, and return. Pair it with platform, accessibility, visual-prototyping, implementation, and verification modules.

## Start with the player promise

Define:

- fantasy or role: who the player gets to be;
- verbs: what the player repeatedly does;
- tension: what makes action uncertain or meaningful;
- mastery: what skill or understanding grows;
- reward: what changes in capability, knowledge, world, expression, or relationship;
- signature: what makes this loop distinct rather than a themed copy;
- guardrails: accessibility, cultural, ethical, technical, and monetization constraints.

Check that opening, tutorial, level structure, interface, story, audio, visual effects, progression, and monetization all reinforce the same promise.

## Loop stack

Model each layer explicitly:

1. **Input loop:** gesture/button/control → immediate response → correction.
2. **Challenge loop:** perceive → plan → act → feedback → learn → retry/succeed.
3. **Encounter/level loop:** enter → understand objective → engage → resolution → reward → exit.
4. **Session loop:** choose goal → play → progress/save → review → next intent → safe stop.
5. **Progression loop:** unlock/master/collect/restore/build → new possibility → rising meaning.
6. **Return loop:** remember context → resume quickly → recover skill → see next desire.

For each loop record duration, state, failure cost, feedback latency, persistence, interruption behavior, and metric. A strong meta layer cannot compensate for an unclear or unrewarding input/challenge loop.

## First-run and tutorial

Measure launch-to-first-meaningful-control and launch-to-first-earned-result. Inventory mandatory screens, loads, permissions, account prompts, story text, menus, tutorials, and confirmations.

- Teach in the context of a real goal, then let the player act.
- One prompt should teach one decision or motor pattern.
- Require demonstration only when failure cost or later complexity justifies it.
- Keep help skippable where safe, resumable, and available later.
- Do not narrate every visible action or lock control behind long exposition.
- Distinguish accessibility setup and essential consent from optional account, lore, marketing, or settings.
- Teach failure and recovery before high-cost failure occurs.
- Test first run, returning run, reinstall/restore, and interrupted tutorial separately.

Use a tutorial ledger:

`learning_goal · prerequisite · prompt/affordance · player action · feedback · mastery evidence · skip/resume · later recall · accessibility alternative`

## Challenge and difficulty

Describe the skill model: perception, knowledge, planning, timing, precision, memory, language, numeracy, spatial reasoning, strategy, or social coordination.

For each challenge specify:

- objective and success/failure conditions;
- information available before commitment;
- action space and meaningful choice;
- randomness and player control;
- feedback and error diagnosis;
- retry cost, checkpoint, undo, hint, and alternate path;
- difficulty variables and their interaction;
- accessibility options that remove barriers without erasing the intended skill.

Avoid difficulty that comes mainly from illegibility, control ambiguity, unskippable repetition, unpredictable input, hidden rules, performance instability, or missing feedback. Support changing difficulty without avoidable progress loss when the platform/domain expectation calls for it; verify current accessibility guidance at use time.

## Controls and feel

Map every action across touch, pointer, keyboard, controller, switch/voice/alternate input where supported.

- Input must cause immediate, proportional, and readable feedback.
- Define tap/hold/drag/swipe/multitouch thresholds, cancellation, accidental activation protection, and one-handed/reach behavior.
- Provide alternatives to path-based, multipoint, motion, rapid, or precise gestures when required.
- Support remapping and conflict detection when the control surface warrants it.
- Separate camera and object manipulation when simultaneous gestures create ambiguity.
- Handle focus, selection, cursor capture, controller disconnect, input-method switching, and platform Back explicitly.
- Tune haptics, sound, animation, and visual response as one feedback system; each critical cue needs an alternative channel.

Judge feel in the running build on target hardware. A storyboard or animation mockup cannot verify latency, hit detection, gesture recognition, camera behavior, or frame pacing.

## State, save, pause, and recovery

Define a persistence contract for:

- settings, accessibility, audio, language, and control mapping;
- tutorial completion and help state;
- current encounter, puzzle, inventory, world change, reward, and progression;
- local/cloud/guest identity, version migration, conflict, and offline state;
- interruption by system UI, call, backgrounding, process death, battery loss, crash, or update.

Pause must communicate what stops, what continues, whether timers/network/social state continue, and how to return. Platform Back must follow a documented hierarchy and never trap the player or discard progress silently.

Test save creation, atomicity, corruption handling, retry, conflict choice, restore, migration, rollback, and idempotent reward delivery. Never show a lock or completion state that contradicts the persisted source of truth.

## Progression, reward, and economy

Trace every reward from earning rule to visible grant, persistence, use, duplicate handling, and recovery. Separate:

- skill mastery;
- content access;
- narrative/world progression;
- collection/customization;
- social recognition;
- currency/economy;
- monetized entitlement.

Avoid rewards that interrupt play more than they motivate it, unclear currencies, dead-end unlocks, loss aversion that punishes safe exit, or streaks/scarcity that exploit vulnerable players. Disclose chance, odds, price, recurrence, expiry, ads, sponsorship, and parental constraints as required by market and platform.

## Narrative, world, and cultural integrity

Use the story architecture module. Verify that narrative beats arise from player action where intended, that lore supports rather than blocks control, and that rewards carry meaning in the world.

For historical, cultural, educational, or museum-like material:

- identify source, interpretation, reconstruction, fiction, and uncertainty separately;
- preserve attribution, rights, and cultural context;
- do not present generated reconstruction as an authenticated artifact;
- explain deviations made for playability or accessibility;
- test names, chronology, geography, symbolism, clothing, architecture, objects, audio, and translation with qualified sources when consequential.

## 2D, 3D, camera, and spatial UI

Define which information belongs in world space, screen space, or an accessible alternative. Inspect scale, camera, occlusion, depth, navigation, object placement, collision, lighting, material response, and readable distance.

- Keep critical prompts within safe and legible regions without covering the target action.
- Prevent labels, effects, and geometry from depth-sorting through one another.
- Make interactable objects distinguishable without relying only on glow/color.
- Define camera sensitivity, inversion, recenter, shake, motion blur, field of view, and reduced-motion options as applicable.
- Preserve consistent spatial mapping between 2D representation and 3D placement.
- Use level-of-detail, texture, lighting, post-processing, and effects budgets appropriate to supported hardware.

Concept art approves direction; engine captures and device tests verify spatial implementation.

## Audio, music, narration, and subtitles

Specify music states, transitions, priority, loop points, ducking, pause/background behavior, persistence of settings, and recovery after audio focus changes. Verify actual packaged assets and licenses.

For speech and cues define:

- caption/subtitle text, speaker, timing, sound identification, direction, contrast/background, size, and safe area;
- transcript and replay where needed;
- narration synchronization and interruption;
- independent volume categories and mute behavior;
- visual/haptic alternatives for critical audio cues;
- audio alternatives for critical visual cues.

Do not mark audio “fixed” from file presence alone; test launch, settings changes, pause/resume, route/scene transition, background/foreground, interruption, and packaged release build.

## Performance and device experience

Treat frame pacing, input latency, loading, memory, thermal behavior, battery, asset streaming, and crash/ANR state as UX. Set budgets by game type, supported device tier, and current platform guidance.

- Measure average and tail frame performance; a good average can hide severe stutter.
- Measure launch, first interaction, scene/level transition, resume, and retry load times.
- Test sustained sessions for thermal throttling, memory growth, battery impact, and degraded asset quality.
- Avoid UI animation or loading work that competes with input and rendering.
- Define a graceful quality ladder for resolution, effects, shadows, texture, particles, audio, and background work.

Verify current Android/Play or target-platform thresholds before citing them. Do not generalize a store program's reference-device target to every supported game without context.

## Game accessibility matrix

Use current platform accessibility guidance and test:

- text size/readability, contrast, backgrounds, subtitles, and language;
- non-color and multi-sensory cues;
- remapping, alternative input, timing, holds/repeats, precision, and gesture alternatives;
- camera motion, flashing, shake, blur, parallax, and reduced motion;
- difficulty, assists, hints, checkpoints, retry, and progress preservation;
- objective clarity, tutorials, cognitive load, pause, history, and reminders;
- screen-reader/semantic access for menus and relevant gameplay paths;
- accessible support, reporting, and account recovery.

Do not claim accessibility because options exist; verify they affect the real gameplay path and persist correctly.

## Game redesign deliverable

For a deep game redesign include:

1. Player promise, anti-goals, audience, and evidence limits
2. Current and proposed loop stack
3. Story/beat and first-run pacing maps
4. Control vocabulary and feedback contract
5. Challenge/skill/difficulty model
6. Level/encounter, failure, retry, hint, and recovery contracts
7. Progression, reward, economy, and monetization map
8. State/save/pause/back/interruption model
9. UI/HUD/menu/help/settings and platform flows
10. Art, 2D/3D, camera, audio, music, narration, motion, and asset direction
11. Accessibility, localization, cultural, safety, and age considerations
12. Performance/device budgets and technical risks
13. Visual review pack, implementation slices, acceptance criteria, and QA matrix

The owner should be able to see how the intended feeling, player action, screen, scene, system, code requirement, and test connect.
