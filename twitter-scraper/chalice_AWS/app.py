from chalice import Chalice
import os
from chalice.app import Request
import pandas as pd

app = Chalice(app_name="vurku_v2_scraper")


@app.route("/", methods=["POST"])
def index():
    request = app.current_request.json_body
    os.system(
        f"snscrape --jsonl --max-results {request['max_results']} {request['scraper']} 'quaz9' > output.json"
    )
    json_obj = pd.read_json("output.json", lines=True)
    json_obj = json_obj.to_json()

    return json_obj