# prime-numbers-task

### Overview
Write a Python program to Scrape the below-mentioned site and bring in the list of the first 5 postings under the "Search Postings" heading containing the following fields: Est. Value Notes, Description, Closing Date https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787

### Usage
You can install the dependencies using the following:

```bash
pip install -r requirements.txt
```

### Configuration
- The script uses Chrome WebDriver, and webdriver_manager is employed to handle the driver setup. Ensure you have Google Chrome installed.
- The script is currently configured to extract only "closing date", "Est. Value notes" & "Description". This can be altered to extract any of the available data by modifying the parameters of the "dataFinder" function.
-  The script is currently configured to extract data from the first five rows. You can modify the script to scrape more or fewer rows based on your requirements.

### Output
The script exports the scraped data into a CSV file named output.csv. Each row in the CSV file corresponds to data extracted from a specific section of the website.
