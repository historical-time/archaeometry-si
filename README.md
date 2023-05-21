---

<p align="center"> 
🚧 README page under construction 🚧  
</p>

---

# Archaeometry Special Issue
> Publication of an Archaeometry Special Issue on Chronological Modeling


- [time table](https://github.com/historical-time/archaeometry-si#timeline)
- [data samples](https://github.com/historical-time/archaeometry-si#data-samples)
- [standards and isostandards](https://github.com/historical-time/archaeometry-si#standards-and-isostandards)

## Timeline

```mermaid
gantt
    title Archaeometry Special Issue
    dateFormat  YYYY-MM-DD
    section Invited Papers
    Formal invite                    : milestone, m0, 2023-05-17, 1d
    Formal response                  : milestone, m0, 2023-06-17, 1d
    section Short paper description
    Request short paper description  : milestone, m0, 2023-06-19, 1d
    Deadline short paper description : milestone, m0, 2023-07-18, 1d
    Editor feedback letter           : milestone, m1, 2023-07-21, 1d
    section Paper submission
    Paper writing                    : active, a0, 2023-06-17, 2023-11-17
    Submission deadline              : milestone, m9, 2023-11-17, 1d %% Soft deadline
    %% Hard deadline                 : milestone, m9, 2023-11-30, 1d %% Hard deadline
    section Reviewing
    Reviewing process                  : active, a1, 2023-11-17, 2024-01-31
    Submission of reviews to editors   : milestone, m1, 2024-01-31, 1d
    section 1st Editor decision
    Editors' decision making              : active, a1, 2024-01-31, 2024-02-16
    Editors' decision                     : milestone, m2, 2024-02-16, 1d
    Reviews and decision sent to authors: milestone, m2, 2024-02-16, 1d
    section Revision
    Authors review their papers       : active, a1, 2024-02-16, 2024-04-29
    Deadline for revised papers       : milestone, m2, 2024-04-29, 1d
    section Proofs
    Proofs to authors                : milestone, m2, 2024-05-17, 1d
    Revised proofs                   : milestone, m2, 2024-05-31, 1d
    section Issue
    Issue compilation                : milestone, m2, 2024-06-03, 1d
    Issue published                  : milestone, m2, 2024-06-17, 1d
```

## Data samples
> Use of standards to share dates between different research projects

We invite authors to deposit samples of their data on this GitHub: [data-samples/](https://github.com/historical-time/data-samples#examples-of-historical-time-representation). The aim is to line-up heterogeneous chronological data coming from the special issue outlet using [CIDOC-CRM](https://github.com/historical-time/projects-tools-standards/tree/main/standards/cidoc-crm) and [EDTF](https://github.com/historical-time/projects-tools-standards/tree/main/standards/edtf). 

## Building LOD

In order  time data in a FAIR perspective[^4], 

For each archaeological event or duration, dated by **absolute chronology**, the minimal required information for each sample are the Peuquet's triad dimensions (What, When, Where):

| What | When | Where |
|------|------|-------|
| Thera-Santorini volcano eruption | -2000/-1500 | Egean sea |

If the archeological event has a relative chronology, i.e. is dated relatively to another event, this relationship should be mentionned using temporal logic:

| What | When | Where |
|------|------|-------|
| Thera-Santorini volcano eruption | *before* Minoean palace collapse | Egean sea |
| Minoean palace collapse | -1450 | Egean sea |

In both cases the format for temoral data (*When*) should be, as possible, the [EDTF](https://github.com/historical-time/archaeometry-si#edtf)

[^3]: The original dataset is a XLSX file, [data.xlsx](https://github.com/eamena-project/eamena-arches-dev/blob/main/data/lod/data.xlsx) that can be downloaded.
[^4]: Findable, Accessible, Interoperable, Reusable
