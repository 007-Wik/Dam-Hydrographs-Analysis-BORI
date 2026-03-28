# Data Dictionary
## Kurnur (BORI) Dam – Parameter Definitions & Units

**Document Version:** 2.0.0 | **Repository:** BORI-DAM-breach-plots

---

## Primary Variables

| Variable Name | Short Code | Unit | Data Type | Description |
|--------------|-----------|------|-----------|-------------|
| Time | T | hr (or min) | float | Simulation time from start (T = 0 at simulation initialization) |
| Headwater Elevation | HW | m MSL | float | Upstream reservoir water surface elevation above Mean Sea Level |
| Tailwater Elevation | TW | m MSL | float | Downstream water surface elevation at the dam toe |
| Total Discharge | Q_total | m³/s | float | Total outflow from the reservoir through all outlets and breach |
| Breach Discharge | Q_breach | m³/s | float | Discharge specifically through the breach opening |
| Breach Width | B_w | m | float | Width of the breach at its base (trapezoidal breach geometry) |
| Breach Velocity | V_b | m/s | float | Mean cross-sectional flow velocity through the breach section |
| Breach Elevation | Z_b | m MSL | float | Elevation of the breach invert (bottom of breach opening) |

---

## Derived/Computed Parameters

| Parameter | Formula | Unit | Description |
|-----------|---------|------|-------------|
| Drawdown Rate | ΔHW/Δt | m/hr | Rate of reservoir level decline during breach |
| Time to Peak | T_p | hr | Time from breach initiation to maximum Q_breach |
| Peak Discharge | Q_peak | m³/s | Maximum value of Q_breach or Q_total in the simulation |
| Breach Growth Rate | ΔB_w/Δt | m/hr | Rate of breach width increase over time |

---

## File-to-Variable Mapping

| Excel File | Available Variables |
|-----------|-------------------|
| `Piping_Breach_Hydrograph.xlsx` | T, HW, TW, Q_total, Q_breach |
| `Overtopping_Breach_Hydrograph.xlsx` | T, HW, TW, Q_total, Q_breach |
| `Large_Controlled_Release_Hydrograph.xlsx` | T, HW, TW, Q_total |
| `Overtopping_Piping_Breach_Parameters.xlsx` | T, B_w, V_b, Z_b |

---

## Units Reference

| Quantity | Unit | SI Symbol |
|---------|------|-----------|
| Elevation | Metres above Mean Sea Level | m MSL |
| Discharge | Cubic metres per second | m³/s |
| Time | Hours (or minutes, see file header) | hr / min |
| Width | Metres | m |
| Velocity | Metres per second | m/s |

---

## Data Quality Notes

- All data are raw, unmodified outputs from HEC-RAS — no processing artifacts introduced
- Missing values: none expected; flag and report any NaN values before analysis
- Time step: 5 minutes (uniform) — verify with `data.index.diff().value_counts()` before analysis
- Negative discharges: not physically meaningful; treat as model artefacts if encountered
