# Methodology & Assumptions
## Kurnur (BORI) Dam – Dam Breach & Hydrograph Analysis

**Document Version:** 2.0.0
**Prepared by:** Satwik Udupi
**Date:** 2025
**Regulatory Context:** Central Water Commission (CWC) Guidelines for Dam Break Analysis; Dam Safety Act 2021

---

## 1. Objective

To perform **engineering-grade post-processing and visualization** of hydraulic time-series outputs from HEC-RAS dam breach and controlled release simulations for Kurnur (BORI) Dam, Solapur District, Maharashtra.

The outputs support:
- Dam Break Analysis (DBA) technical reporting
- Emergency Action Plan (EAP) annexure preparation
- Regulatory submission to CWC / State Dam Safety Organisation (SDSO)
- Official digital archiving of analysis results

---

## 2. Scope and Boundaries

### Within Scope
- Ingestion of HEC-RAS time-series outputs (Excel format)
- Time-series parsing, alignment, and validation
- Dual-axis hydrograph generation (elevation + discharge vs. time)
- Breach parameter visualization (width, velocity vs. time)
- Publication-grade static figure export (≥300 DPI)
- Interactive hydrograph generation (Plotly HTML)

### Outside Scope
- Dam breach hydraulic simulation (performed in HEC-RAS, external)
- Downstream flood routing or 2D inundation mapping
- Structural failure analysis
- Sediment transport or morphodynamic modelling
- Calibration or field data validation

---

## 3. Input Data

### Source
All input data are **raw, unmodified outputs** from HEC-RAS dam break simulations. Data are exported as Microsoft Excel (.xlsx) files.

### Format
- **Time resolution:** Uniform 5-minute time step
- **Time reference:** Relative time from simulation start (T = 0 hr at simulation initialization; breach initiation occurs at a specified trigger time within the run)
- **Coordinate datum:** Elevations in metres above Mean Sea Level (m MSL)
- **Discharge units:** Cubic metres per second (m³/s)

### Files

| File Name | Scenario | Parameters |
|-----------|----------|------------|
| `Piping_Breach_Hydrograph.xlsx` | Piping Failure | Time, HW elev, TW elev, Q_total, Q_breach |
| `Overtopping_Breach_Hydrograph.xlsx` | Overtopping Failure | Time, HW elev, TW elev, Q_total, Q_breach |
| `Large_Controlled_Release_Hydrograph.xlsx` | Controlled Release | Time, HW elev, TW elev, Q_total |
| `Overtopping_Piping_Breach_Parameters.xlsx` | Both breach scenarios | Time, Breach width, Breach velocity, Breach elevation |

---

## 4. Data Processing Procedure

### Step 1: Import
- Excel files loaded using `pandas.read_excel()` with `openpyxl` engine
- Sheet names verified against expected structure before loading

### Step 2: Datetime Parsing
- Time column parsed into `pandas.Timestamp` objects
- Relative time (hours or minutes from T=0) preserved as a numeric index for plotting
- Absolute datetime used only where explicitly present in source data

### Step 3: Column Validation
- Column names checked against expected schema (see Data Dictionary)
- Units verified (elevation in m, discharge in m³/s, width in m, velocity in m/s)
- Missing values flagged and reported (no imputation applied)

### Step 4: Data Integrity Check
- No smoothing, filtering, interpolation, or extrapolation applied
- Raw values plotted as-received from HEC-RAS
- SHA-256 checksums generated for all input files at time of analysis

### Step 5: Peak Parameter Extraction
- Time-to-peak discharge (T_p): time index at maximum Q_total or Q_breach
- Peak discharge (Q_peak): maximum value in Q_total or Q_breach column
- Peak headwater elevation: maximum HW value during simulation
- Breach initiation time: identified from first non-zero Q_breach value

---

## 5. Scenario-Specific Methodology

### 5.1 Piping Failure Scenario

**Physical mechanism:** Internal erosion initiates within the embankment body at a weak zone (e.g., contact between embankment and foundation, or around a conduit). Progressive piping causes a tunnel to form, enlarging over time until the roof collapses and the breach opens to daylight. Discharge increases non-linearly as the breach widens and deepens.

**HEC-RAS modelling approach:** Breach parameters (initial breach width, breach time, breach side slopes, and weir coefficient) specified based on Froehlich (1995) regression equations. Breach is modelled as a trapezoidal opening that grows linearly in time from initiation to full breach.

**Visualization outputs:**
- Dual-axis hydrograph: HW elevation (m), TW elevation (m), Q_total (m³/s), Q_breach (m³/s) vs. time
- Breach parameter plot: Breach width (m) and breach velocity (m/s) vs. time

### 5.2 Overtopping Failure Scenario

**Physical mechanism:** Reservoir level exceeds the dam crest elevation. Water flows over the crest, eroding the downstream face. Erosion causes a head-cut to migrate upstream until the crest fails, producing a rapid breach and sharp discharge peak.

**HEC-RAS modelling approach:** Same breach parameter framework as piping, but with shorter breach formation time, reflecting the more sudden nature of overtopping failure. Initial breach width and side slopes adjusted to reflect overtopping-dominated erosion mechanics.

**Visualization outputs:**
- Dual-axis hydrograph: HW elevation (m), TW elevation (m), Q_total (m³/s), Q_breach (m³/s) vs. time
- Breach parameter plot shared with piping scenario for direct comparison

### 5.3 Large Controlled Release Scenario

**Physical mechanism:** No dam failure. Controlled gate or spillway operation releases water from the reservoir. No breach forms.

**HEC-RAS modelling approach:** Gate operations specified as boundary conditions. Tailwater computed from downstream channel rating curve.

**Visualization outputs:**
- Hydrograph: HW elevation (m), TW elevation (m), Q_total (m³/s) vs. time
- Used as reference baseline for comparison with breach scenarios

---

## 6. Plotting Standards

### Dual-Axis Hydrograph Layout

```
Y-axis (left)   : Elevation (m MSL)
Y-axis (right)  : Discharge (m³/s)
X-axis          : Time (hours from simulation start)
```

### Color Convention

| Trace | Color | Description |
|-------|-------|-------------|
| Headwater elevation | Blue (#1f77b4) | Upstream water surface |
| Tailwater elevation | Cyan (#17becf) | Downstream water surface |
| Total discharge | Red (#d62728) | All outflows |
| Breach discharge | Orange (#ff7f0e) | Flow through breach only |
| Breach width | Purple (#9467bd) | Opening size at base |
| Breach velocity | Green (#2ca02c) | Mean breach flow velocity |

### Figure Export Specifications

| Format | Resolution | Use |
|--------|-----------|-----|
| PNG | 300 DPI minimum | DBA report, EAP annexure, regulatory submission |
| HTML (Plotly) | Vector/interactive | Technical review meetings, presentations |

### Annotation Standards
- Peak discharge value and time-to-peak annotated on each hydrograph
- Breach initiation time marked with vertical dashed line
- Crest elevation marked with horizontal dashed line on elevation axis
- All axis labels include units in parentheses

---

## 7. Assumptions

The following assumptions apply to this analysis:

| # | Assumption | Basis |
|---|-----------|-------|
| A1 | Reservoir inflow during breach event is negligible compared to breach outflow | Conservative assumption; standard for dam break analysis |
| A2 | Breach formation time and final breach geometry follow Froehlich (1995) regression | CWC guidelines; widely accepted empirical approach |
| A3 | Tailwater effects are as computed by HEC-RAS downstream boundary condition | Model-dependent |
| A4 | No sediment transport or morphological change modelled | Post-processing only scope |
| A5 | Embankment structural behaviour simplified to hydraulic response | Hydraulic post-processing only |
| A6 | Velocity data not available for controlled release case | Gate-controlled operation; breach velocity not applicable |
| A7 | All time steps are uniformly spaced at 5-minute intervals | Verified from input data |
| A8 | Breach parameters are deterministic, not probabilistic | Follows deterministic DBA approach per CWC guidelines |

---

## 8. Limitations

1. **No 2D inundation extent:** This analysis does not include downstream flood mapping. A separate 2D HEC-RAS or MIKE FLOOD model is required for inundation delineation.
2. **No calibration:** HEC-RAS model outputs have not been calibrated against observed flood data. Results are indicative, not validated.
3. **Deterministic approach:** A single deterministic breach scenario is modelled per failure mode. Probabilistic breach analysis (sensitivity to breach parameters) is not included.
4. **No structural analysis:** Embankment stability, seepage analysis, and geotechnical failure modes are not within scope.
5. **Model dependency:** All outputs are contingent on the fidelity of the upstream HEC-RAS model, including boundary condition specification and breach parameter selection.

---

## 9. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Feb 2026 | Initial release — basic hydrograph visualization |
| 2.0.0 | Mar 2026 | Repository restructure; methodology formalized; regulatory alignment added; interactive outputs added |
