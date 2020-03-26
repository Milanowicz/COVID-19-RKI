# COVID-19 case numbers Germany from Robert-Koch-Institut

Python scripts for collecting historical case numbers of the spread of COVID-19 in Germany from Robert Koch Institut.
https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html

Data is updated on a daily basis and published in a csv file here: http://www.nexolin.de/data/covid-19/rki/rki_data.csv

Description of columns:

* State - Bundesland
* Update
* Confirmed
* Deaths


## Install Python environment

Create environment and install Python libs for a GNU/Linux operation system:

    $ . env.sh
    $ pip3 install pandas numpy BeautifulSoup4 requests lxml
   

### included files:

- `rki_get_cases.py`: script for downloading current case numbers from the RKI server
- `rki_merge_cases.py`: combine cases to one single csv file with the following structure:

or by script:

    $ . update.sh


<table>
<tr>
<th>Bundesland</th><th>date</th><th>confirmed</th><th>deaths</th>
</tr>
<tr>
<td>name of federal state</td>
<td>date in %Y-%m-%d format</td>
<td># of confirmed cases</td>
<td># of deaths</td>
</tr>
</table>

http://github.com/normannexo/COVID-19-RKI/blob/master/csv/rki_data.csv

- `clean_archive.py` - The Robert-Koch-Institut frequently changes the structure of the data table. This script tackles resulting problems with the historical csvs to fit the new structure.
