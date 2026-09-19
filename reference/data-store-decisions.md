# Data store decision table

Confirm the actual situation with Matt before assuming Dataverse — this has burned him before
(Dataverse for Teams' missing global-choice support forced a rework on Transfer Log).

| Situation | Use | Why |
|---|---|---|
| Full Dataverse license available, needs global choices, multi-app reuse | **Dataverse (full)** | Global choices work; needed for anything with shared option sets across tables/apps. |
| Teams-only app, free tier, small team | **Dataverse for Teams** | No global choices support — model any choice-like field (Priority, Status, Type) as a **Lookup table** instead, per Transfer Log precedent. Flows are more limited than full Dataverse. |
| No Power Platform admin buy-in yet, quick prototype, under ~5 users | **SharePoint list, or an Excel-backed staging table** | Fastest path to something usable; has a clear upgrade path to Dataverse later once the shape is proven. |
| Needs Power Automate flows, SLA/escalation timers, scheduled email | **Full Dataverse** | Dataverse for Teams flow triggers/actions are more restricted. |

## Known constraints once a store is picked

- **Dataverse for Teams**: no global choices — use Lookup tables. Confirm this before designing
  any "Priority" / "Status" / "Type"-style column.
- **Full Dataverse**: publisher prefix is environment-specific — always confirm the real prefix
  with Matt, never carry over a placeholder like `cr917_` from a different environment.
- **Schema build order**: design and build tables in dependency order (parent tables before
  children) to avoid reference errors during manual table creation in Dataverse.
