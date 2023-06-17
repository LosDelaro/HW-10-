# Import the dependencies.
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text

from flask import Flask, jsonify
import json

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"""<h1>Available Routes:<h1/><br/>"""
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Get Precipitation"""
    query = text("""
                SELECT
                   date,
                   station,
                   prcp
                FROM
                    measurement
                where 
                    date >= '2016-08-23';
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)



#run the website
if __name__ == '__main__':
    app.run(debug=True)
