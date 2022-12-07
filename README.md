# pyqgisdams

> **DISCLAIMER**: This study is intended for Carleton University’s Geom4005; Undergraduate Directed Study in Geomatics with Dr. Kevin Hamdan, and
in partnership with United Nations University Professor Dr. Charlotte Macalister to provide data innovation for the INWEH project while using the data in geospatial applications to produce a directed study in geomatics. This study is the property of Carleton University and may not be used for business
purposes. The provided GeoDAR v1.1 is proprietary data whose distribution is prohibited and whose accuracy is independent of the study. Datasets such as
HydroSHEDS, Ontario Dam Inventory and subsequent map layers are not produced by the study, and as a result the findings pertain to the geospatial constraints of the datasets. Accurate up to date data may not all be available to the general public.

## Table of Contents

1. [Introduction](#Introduction)
2. [Objectives](#Objectives)
3. [Methodology](#Methodology)
4. [Application](#Application)
5. [Discussion](#Discussion)
6. [Conclusion](#Conclusion)
7. [References](#References)
8. [Appendix A: Maps and Charts](#appendix-a-maps-and-charts)
9. [Appendix B: Data Sources and Documentation](#appendix-b-data-sources-and-documentation)

## Introduction

Dams and water resources have become a quintessential part of modern society, with an ever-growing reliance on them to support our complex infrastructures. As resources wain and begin to decrease many of the world’s governments and top scientists have collaborated with the objective to better increase dam data on a global scale. Some current efforts include: World Registers of Dams (WRD), GRanD national inventories, GOODD, and ICOLD. From these initial datasets the idea for GeoDAR v1.1 was conceived with the notion of harmonizing global dam data across regions. The method to harmonize GeoDAR v1.1 is conceived such that an inverse geospatial analysis   is tested and verified by updating the Mekong Basin’s regional dataset, then subsequently employed in the Outaouais Basin (Godse, 2022). This repository provides a framework for the semi-autonomous implemetation in Python of the dedeuplication by proximity methodology proposed in:
>Godse, P. (2022). Improving Dam Datasets To Identify Micro-hydro Suitibility: Spatial Data Driven Approach. GEOM4005: Undergraduate Directed Study In Geomatics, Carleton University, student paper.

Whilst attempting to reduce the number of barriers to access or use this data as current workflows are heavily dependent on paid subscriptions or similar micro-transaction-based services such as ArcGIS Pro, which requires a license for concurrent use. Thus, gatekeeping the tools required, which can decrease the number of people that can interact with and disseminate the data on their own, further limiting the effectiveness of open-source citizen-science outreach. Current de-clustering methods rely on a manually observed 2km proximity-based approach, which although effective in the tested regions of the Mekong and Outaouais Basin’s, raises the conceptual question of: ‘is buffering by this specific amount unintentionally introducing errors?’.

## Objectives

The primary objective of this directed study is to adapt the current semi-automated model-based approach to an automated open-sourced script that can be run from the command line or QGIS. The current ArcPro model-builder illustation can be seen in Figure 1. Additionally, by providing a script as a deliverable, it will become easier to disseminate upon completion, via the establishment of an openly accessible repository on GitHub or a similar service. The goal is to produce a publicly available, easily accessible script that can be ran from QGIS or the CLI and stored within a GitHub repository (Repositories, n.d.) or similar.

![Figure 1](./img/Model_to_code.png)

*Figure 1: ArcGIS Pro Model Builder for GeoDAR v1.1*

## Methodology

The brunt of this project was to convert the current semi-automated model-builder approach to a scriptable format for easier automation capabilities, future scalability, and quality of life upgrades regarding minimizing GUI interaction. The model-based logic and geo-processing tools used previously in ArcGIS Pro will be converted using the QGIS toolset. A script will be uploaded and shared publicly once completed, with appropriate documentation, so that anyone who wishes to explore it for themselves, can do so; thereby increasing the potential for citizen scientists to record their own dam data. Once adapted, accuracy will first look to be replicated in the original region of study by cross comparing methods of replicant removal and overall region accuracy, before attempting to expand further and possibly improve accuracy by applying a geodesic buffering (Flater, n.d.) or similar algorithmic approach (tanawatl, 2016) to a new study area/catchment. This method ensures that an adequate level of open-source outreach and accessibility is still achieved, whilst still allowing for the potential improvement of accuracy to pre-existing methods if a more accurate technique is encountered during the duration of the study.

## Application

Markdown is a super-friendly plain text format that can be easily converted to a bunch of other formats like PDF, Word and LaTeX. You'll enjoy working in Markdown because:
- it is a clean, plain-text format...
- ...but you can use LaTeX when you need it (for example, in laying out mathematical formula).
- it doesn't suffer from the freezes and crashes that some of us experience when working with large, image-heavy Word documents.
- it automatically handles the table of contents, bibliography etc with Pandoc.
- comments, drafts of text, etc can be added to the document by wrapping them in &lt;!--  --&gt;
- it works well with Git, so keeping backups is straightforward. Just commit the changes and then push them to your repository.
- it is able to take advantage of autocompletion capabilities for figures and citations in several text editors (VSCode, Sublime, etc.)
- there is no lock-in. If you decide that Markdown isn't for you, then just output to Word, or whatever, and continue working in the new format.

## Discussion

There are some minor annoyances:
- if you haven't worked with Markdown before then you'll find yourself referring to the style-guide fairly often at first.
- it isn't possible to add a short caption to tables ~~and figures~~ ([figures are now fixed](https://github.com/tompollard/phd_thesis_markdown/pull/47), thanks to @martisak). This means that /listoftables includes the long-caption, which probably isn't what you want. If you want to include the list of tables, then you'll need to write it manually.

## Conclusion

For this project the harmonization between two regionally independent datasets, in conjunction with GeoDAR v1.1 was completed; in the Mekong Basin and the Outaouais Basin, whilst the subsequent analysis of the manually observed distance of the latter two allowed for confirmation that the distance of 2km is not causing unneeded error. Utilizing the deduplication by proximity methodology and supporting script, GeoDARs dam counts were consequently improved from 105 to 159 points in the Mekong Basin and 56 to 271 within the Outaouais Basin. By applying varying buffering proximities at increments of 0.5 km on each iteration via the QGIS script, I was able to confirm that the optimal buffering distance without introducing more unwanted errors is 2km or 2000m. The corresponding plots for Outaouais and Mekong can be seen in Figure 4,5. There seems to be a linear relationship between the increasing buffering proxies and duplicate features, whereas in the Mekong basin, any attempts to model it linearly are significantly inaccurate.

![Figure 4](./img/Ottawa_varying_buffer.png)

*Figure 4: Showing buffering proximities at increasing increments of 0.5km within the Outaouais Basin*

![Figure 5](./img/Mekong_varying_buffer.png)

*Figure 5: Showing buffering proximities at increasing increments of 0.5km within the Mekong Basin*

## References

> J. Wang, B. A. Walter, F. Yao, C. Song, M. Ding, A. S. Maroof, J. Zhu, C. Fan, J. M. McAlister, M. S. Sikder, Y. Sheng, G. H. Allen, J.-F. Crétaux, and Y. Wada, “Geodar: Georeferenced global dams and reservoirs dataset for bridging attributes and geolocations,” Zenodo [Online]. Available: https://zenodo.org/record/6163413#.YsUIJezMIjg. [Accessed: 12-Sept-2022].

>Godse, P. (2022). Improving Dam Datasets To Identify Micro-hydro Suitibility: Spatial Data Driven Approach. GEOM4005: Undergraduate Directed Study In Geomatics, Carleton University, student paper.

>Flater, D. Understanding Geodesic Buffering. (n.d.). Available: https://www.esri.com/news/arcuser/0111/geodesic.html. [Accessed 18-Oct-2022].

>tanawatl. (2016, February 3). For which real world data sets does DBSCAN surpass K-means.? [Forum post]. Data Science Stack
Exchange. Available: https://datascience.stackexchange.com/q/10063. [Accessed: 25-Sept-2022].

>Repositories. (n.d.). GitHub Docs. Available: https://ghdocs-prod.azurewebsites.net/en/repositories. [Accessed: 25-Sept-2022].

## Appendix A: Maps and Charts

**Figure 1:**
![Figure 1](./img/Model_to_code.png)

**Figure 1:**
![Figure 1](./img/Ottawa_Basin_01.png)

**Figure 2:**
![Figure 2](./img/Ottawa_Basin_Harmony_01.png)

**Figure 3:**
![Figure 3](./img/Mekong_Basin_01.png)

**Figure 4:**
![Figure 4](./img/Mekong_Basin_Harmony_01.png)

## Appendix B: Data Sources and Documentation


