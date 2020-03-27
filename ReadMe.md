# COVID-19 case numbers from Robert Koch-Institut in Germany

Python scripts for collecting historical case numbers of the spread of COVID-19 in Germany from Robert Koch-Institut.
https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html

Data is updated on a daily basis and published in a csv file here:
https://github.com/Milanowicz/COVID-19-Dataset/blob/master/data/rki/time_series_confirmed_and_death.csv


## Description of columns

<table>
<tr>
<th>State</th><th>Date</th><th>Confirmed</th><th>Deaths</th>
</tr>
<tr>
<td>Name of federal state (German Bundesland)</td>
<td>Date in %Y-%m-%d format</td>
<td>Numbers of confirmed cases</td>
<td>Numbers of deaths</td>
</tr>
</table>

Dataset [rki_data.csv](https://raw.githubusercontent.com/Milanowicz/COVID-19-RKI/master/csv/rki_data.csv)


## Install Python environment

Create environment and install Python libs for a GNU/Linux operation system:

    $ . env.sh
    $ pip3 install pandas numpy BeautifulSoup4 requests lxml
   

### Usage from Python scripts

Python script for downloading current case numbers from the RKI server:

`rki_get_cases.py`
 
Python script combine cases to one single csv file with the following structure:

`rki_merge_cases.py`


or execute by this shell script:

    $ . update.sh

The Robert-Koch-Institut frequently changes the structure of the data table. This script tackles resulting problems with the historical csvs to fit the new structure.

`clean_archive.py` 
