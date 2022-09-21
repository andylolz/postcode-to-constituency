# Extracting constituencies from postcodes

1. First, download the ONS postcode directory from here:
   https://ons.maps.arcgis.com/home/search.html?t=content&q=ONS+Postcode+Directory&sortOrder=desc&sortField=modified
   It’s a big zip file. Unzip it, and get the ONSPD CSV file out.
2. Fetch constituency lookup data from here:
   https://geoportal.statistics.gov.uk/datasets/ons::westminster-parliamentary-constituencies-december-2020-names-and-codes-in-the-united-kingdom/about
3. Finally, download petition data
4. Run app.py over the whole lot
