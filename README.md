# test
* Created a simple model for the given sample template, and populated the model with the sample data.
* Retrieved the value from the model (table/database) by hitting/calling the respective URL.

Model Name : NameDetails

View Name : ActivityPeriodView

URL : http://127.0.0.1:8000/activity/names/

Sample Response :
       {
    "status": "success",
    "message": "details",
    "another": [
        {
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity": [
                {
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        },
        {
            "id": "W07QCRPA4",
            "real_name": "Glinda Southgood",
            "tz": "America/Los_Angeles",
            "activity": [
                {
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        }
    ]
}
