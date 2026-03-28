# Data Sources & Provenance
## Kurnur (BORI) Dam – Data Documentation

---

## Source Model

| Attribute | Detail |
|-----------|--------|
| **Model** | HEC-RAS (Hydrologic Engineering Center – River Analysis System) |
| **Version** | 6.x |
| **Developed by** | U.S. Army Corps of Engineers (USACE) |
| **Analysis type** | 1D Unsteady Flow – Dam Break |
| **Breach method** | User-specified breach (Froehlich 1995 parameters) |

---

## Data Files – Provenance Record

| File | Scenario | Received From | Date Received | Modified? |
|------|----------|--------------|--------------|----------|
| `Piping_Breach_Hydrograph.xlsx` | Piping Failure | HEC-RAS simulation output | Feb 2026 | No |
| `Overtopping_Breach_Hydrograph.xlsx` | Overtopping Failure | HEC-RAS simulation output | Feb 2026 | No |
| `Large_Controlled_Release_Hydrograph.xlsx` | Controlled Release | HEC-RAS simulation output | Feb 2026 | No |
| `Overtopping_Piping_Breach_Parameters.xlsx` | Both breach | HEC-RAS simulation output | Feb 2026 | No |

**Modification status:** All files are preserved exactly as exported from HEC-RAS. No editing, rounding, or reformatting has been applied.

---

## Data Integrity Verification

SHA-256 checksums for all raw data files are stored in:
```
data/metadata/checksums.sha256
```

To verify:
```bash
sha256sum -c data/metadata/checksums.sha256
```

All files must return `OK`. Any failure indicates file corruption or unintended modification.

---

## Limitations of Source Data

1. HEC-RAS model not calibrated against observed flood events
2. Breach parameters are deterministic (single value per parameter, not probabilistic)
3. Downstream channel geometry simplified in HEC-RAS model
4. No sediment transport — clear water assumption throughout
