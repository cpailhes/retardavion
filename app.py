# import main Flask class and request object
from flask import Flask, request
import pandas as pd
import numpy as np
import math

print("read csv")
predict_flight = pd.read_csv('predict_flight.csv')
print ("end read csv")
# create the Flask app
app = Flask(__name__)


@app.route('/recommandation' , methods=['GET', 'POST'])

def recommandation():
       
        def predict_delay(departure_date, carrier,origin,destination,predict_flight):
            from datetime import datetime
            try:
                departure_date_parsed = datetime.strptime(departure_date, '%d/%m/%Y')
            except ValueError as e:
                return 'Error parsing date/time - {}'.format(e)

        
            month = departure_date_parsed.month
            day = departure_date_parsed.day
            day_of_week = departure_date_parsed.isoweekday()
            print("carrier" , carrier)
            print("day ", day_of_week,month )
            selected= predict_flight[(predict_flight["MONTH"]==month)& (predict_flight["DAY_OF_WEEK"] ==day_of_week)
                        &(predict_flight["UNIQUE_CARRIER1"]==int(carrier))
                                   &(predict_flight["ORIGIN_AIRPORT_ID"]==int(origin))
                                   &(predict_flight["DEST_AIRPORT_ID"]==int(destination))
                                  ]
        
            return selected.to_html()
            

   #printing top-10 recommendations
        try:
            departure_date =request.args.get('departure_date')
            carrier =request.args.get('carrier')
            origin =request.args.get('origin')
            destination =request.args.get('destination') 
            output = predict_delay(departure_date,carrier,origin,destination,predict_flight)
            
            return output
        except ValueError as e:
            return e
 
if __name__ == '__main__':
    # run app in debug mode on port 5000
   
    app.run(debug=True, port=5000)
    