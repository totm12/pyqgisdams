# Quick Start Guide

## Prerequisites (See Appendix B for data links)
* GeoDAR Dams and Reservoirs shapefile 
* Regional dams shapefile (for the area you intend to test in)
* Hydrorivers shapefile 
* Hydrobasins shapefile clipped to the regional basin of the reginal dams (see above)
* QGIS (V3.4 or greater)
* UTM zone of the regional dams

## Running Script
1. Open QGIS.
2. Open Python pane, as shown in Figure 1.
![Figure 1](/img/qgis_py0.PNG)
*Figure 1: Opening Python pane QGIS.*
3. Select the open script button, as shown below in Figures 2-3.
![Figure 2](/img/qgis_py1.PNG)

*Figure 2: Opened Python pane QGIS.*

![Figure 3](/img/qgis_py2.PNG)

*Figure 3: Navigating to the open external script tab.*
4. A file prompt will open and then navigate to the directory where you downloaded 'dam_qgis.py' and select it and hit 'Open'.
5. Change inputs (Lines 85-89) to match your directory path.
6. Change reproject UTM zone (Lines 103-106) to match the UTM of your regional dams.
7. Click run button and wait.
