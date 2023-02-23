# Extracting constituencies from postcodes

1. Get some data to geocode. It should be in a CSV file, with a column named “postcode”
2. First, download the ONS postcode directory from here:
   https://ons.maps.arcgis.com/home/search.html?t=content&q=%22ONS+Postcode+Directory%22+-User&sortOrder=desc&sortField=modified&showFilters=true
   It’s a big zip file. Unzip it, and get the ONSPD CSV file out.
3. Fetch constituency lookup data from here:
   https://geoportal.statistics.gov.uk/datasets/westminster-parliamentary-constituencies-dec-2020-names-and-codes-in-the-united-kingdom/about
4. Run `python app.py [filename] --refresh`
