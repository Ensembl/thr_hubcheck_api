"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from fastapi import FastAPI, Query
from hub_check import hub_check

description = """
The Hub Check Utility API is used to check that the submitted hub files are valid and correctly formatted.

Under the hood, this API uses `hubCheck` utility developped by UCSC.

##### Useful Links:
Hubs can be checked for valid file configuration, trackDb keywords, and composite or super track settings with [the Hub Development tool](https://genome.ucsc.edu/cgi-bin/hgHubConnect?#hubDeveloper).

You can also use [hubCheck utility command-line](http://hgdownload.soe.ucsc.edu/admin/exe/).
Take a look at [Debugging Track Hubs Documentation](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html#Debug) for more details.

GitHub URL: [https://github.com/ucscGenomeBrowser/kent/tree/master/src/hg/utils/hubCheck](https://github.com/ucscGenomeBrowser/kent/tree/master/src/hg/utils/hubCheck).
"""

app = FastAPI(
    title="Hub Check Utility's API",
    description=description,
    version="0.6.0",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ensembl Applications Team",
        "email": "apps@ebi.ac.uk",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/")
async def root():
    return {"message": "Welcome to hubCheck utility API"}


@app.get("/hubcheck")
def hubcheck(
    hub_url: str = Query(
        title="Query string",
        description="Hub URL to check, for example: `ftp://ftp.ebi.ac.uk/pub/databases/Rfam/12.0/genome_browser_hub/hub.txt`"
    )
):
    # TODO: add the possibility for the user to disable/enable hubCheck when submitting new Hub(s)
    # run the USCS hubCheck tool found in kent tools on the submitted hub
    hub_check_result = hub_check(hub_url)
    return hub_check_result