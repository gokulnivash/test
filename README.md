# test
A Simple application in which i have,
* Created a simple model for the given sample template, and populated the model with the sample data.
* Retrieved the values from the model (table/database) by hitting/calling the respective URL.

Model Name : NameDetails

View Name : ActivityPeriodView

URL : http://127.0.0.1:8000/activity/names/

Sample Response:

{
      "status": "success",
      "message": "details",
      "data": {
          "ok": true,
          "members": [
              {
                  "id": "W012A3CDE",
                  "real_name": "Egon Spengler",
                  "tz": "UTC",
                  "activity_periods": [
                      {
                          "start_time": "Aug 07 2020 01:00PM",
                          "end_time": "Aug 08 2020 01:00AM"
                      },
                      {
                          "start_time": "Aug 01 2020 07:00PM",
                          "end_time": "Aug 05 2020 01:00AM"
                      }
                  ]
              },
              {
                  "id": "W07QCRPA4",
                  "real_name": "Glinda Southgood",
                  "tz": "America/Aruba",
                  "activity_periods": [
                      {
                          "start_time": "Aug 08 2020 05:21AM",
                          "end_time": "Aug 08 2020 01:00AM"
                      },
                      {
                          "start_time": "Aug 11 2020 05:22AM",
                          "end_time": "Aug 11 2020 07:00PM"
                      }
                  ]
              }
          ]
      }
  }
