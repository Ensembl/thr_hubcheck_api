## Hub Check Utility's API

The Hub Check Utility API is used to check that the submitted hub files are valid and correctly formatted.

Under the hood, this API uses `hubCheck` utility developped by UCSC.

### Prequisites:
* Python 3.8+

### Local deployment

Clone the project

```
git clone https://github.com/Ensembl/thr_hubcheck_api.git
cd thr_hubcheck_api
```

Create, activate the virtual environment and install the required packages

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run

```
uvicorn main:app --reload
```

### Usage:

Curl
```
curl -X 'GET' \
  'http://127.0.0.1:8000/hubcheck?hub_url=<hub_url>' \
  -H 'accept: application/json'
```

Request URL
```
http://127.0.0.1:8000/hubcheck?hub_url=<hub_url>
```

### Useful Links:
Hubs can be checked for valid file configuration, trackDb keywords, and composite or super track settings with [the Hub Development tool](https://genome.ucsc.edu/cgi-bin/hgHubConnect?#hubDeveloper).

You can also use [hubCheck utility command-line](http://hgdownload.soe.ucsc.edu/admin/exe/).
Take a look at [Debugging Track Hubs Documentation](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html#Debug) for more details.

GitHub URL: https://github.com/ucscGenomeBrowser/kent/tree/master/src/hg/utils/hubCheck

