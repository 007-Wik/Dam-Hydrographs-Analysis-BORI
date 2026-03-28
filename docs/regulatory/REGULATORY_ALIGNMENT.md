# Regulatory Alignment
## Kurnur (BORI) Dam – Compliance Framework

**Document Version:** 2.0.0
**Prepared for:** CWC / SDSO Maharashtra Submission

---

## Governing Standards & Compliance Matrix

| Standard | Issuing Body | Year | Compliance Aspect |
|---------|-------------|------|------------------|
| Guidelines for Dam Break Analysis | Central Water Commission (CWC) | Latest | Primary analytical framework; breach parameter methodology |
| Dam Safety Act | Government of India | 2021 | Statutory obligation for dam safety reporting |
| National Dam Safety Guidelines | NDSA | 2020 | Emergency Action Plan (EAP) requirements |
| Guidelines for EAP | NDSA | 2020 | EAP trigger levels; inundation mapping requirements |
| Federal Guidelines for Dam Safety | FEMA P-946 | 2014 | Breach parameter selection; hydrograph analysis |
| HEC-RAS User Manual | USACE | 2021 | Hydraulic model documentation |
| ICOLD Bulletin 72 | ICOLD | 1995 | Dam failure statistics and breach formation |
| ICOLD Bulletin 99 | ICOLD | 2011 | Risk assessment framework |

---

## CWC Guidelines – Specific Compliance Points

### Breach Parameter Selection
- Froehlich (1995) regression equations adopted for breach width, formation time, and side slopes — as recommended by CWC Guidelines Section 4.
- Separate analysis conducted for piping and overtopping failure modes — as required by CWC.

### Hydrograph Presentation
- Dual-axis hydrographs showing both water level and discharge — meeting CWC reporting format expectations.
- Peak discharge clearly annotated with time-to-peak — standard for EAP trigger level determination.

### Scenario Coverage
Per CWC Guidelines, the following scenarios are addressed:
- [x] Piping failure scenario
- [x] Overtopping failure scenario
- [x] Controlled/non-failure reference case

### Data Traceability
- All input data preserved without modification
- SHA-256 checksums provided for data integrity verification
- Model source (HEC-RAS) documented with version reference

---

## Submission Checklist for GOV/CWC Record

- [x] Dam identification (name, location, river, district, state)
- [x] Failure scenarios documented (piping, overtopping)
- [x] Breach parameters referenced to established regression equations
- [x] Hydrographs plotted at appropriate resolution (300 DPI)
- [x] Peak discharge and time-to-peak annotated
- [x] Governing standards cited throughout
- [x] Assumptions explicitly listed
- [x] Limitations explicitly stated
- [x] Author credentials and contact provided
- [x] Version control record available (git history)
- [x] Digital record integrity verifiable (checksums)
