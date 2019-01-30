# Materials Cloud Discover Section for Covalent Organic Frameworks

Using

 * bokeh server
 * sqlite database backend
   (AiiDA database backend in alpha)
 * jsmol for structure visualization

## Prerequisites

 * python
 * nodejs >= 6

## Installation

```
pip install -e .     # install python dependencies
./prepare.sh         # download the data (run only once)
bokeh serve --show figure detail   # run app
```

## Configuration

Feel free to adapt this app to your own needs:

### Input data
 * a set of structures in `data/structures`
   * Allowed file extensions: `cif`, `xyz`
 * a CSV file `data/properties.csv` with their properties
   * has a column `name` whose value `<name>` links each row to a file in `structures/<name>.<extension>xyz`.

### Plots

The plots can be configured using a few YAML files:
 * `figure/columns.yml`: defines metadata for columns of CSV file
 * `figure/filters.yml`: defines filters available in plot
 * `figure/presets.yml`: defines presets for axis + filter settings

## Docker

```
pip install -e .
./prepare.sh
docker-compose build
docker-compose up
# open http://localhost:3245/select-figure
```

### Added comments ###

Download the structures at: https://drive.google.com/open?id=1lcB8jNXpgm22Tu1F9uym4Oa54daxV-Yo 
Download the allcomplexes.csv file at: https://drive.google.com/open?id=16G0aF7s0_nldhJX6wzY8P_SsFenBbLLv
Add "export PYTHONPATH=$PYTHONPATH:/current-location/lsmo-bokeh-app" in the bashrc
For creating the databse: python import_db.py 
For running the app: bokeh serve --show figure detail select-figure
