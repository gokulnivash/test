import json
import logging

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from testapp.models import NameDetails, DateDetails
import pytz
logger = logging.getLogger(__name__)


# Create your views here.
class ActivityPeriodView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    def get(self,request):

        """
        URL - http://127.0.0.1:8000/activity/names/

        # Sample Response
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
        """
        try:
            name_details = NameDetails.objects.all().values('id','real_name','tz')
            for i in name_details:
                i['activity_periods'] = DateDetails.objects.filter(namedetails_id=i['id']).values('start_time','end_time')
                for j in i['activity_periods']:
                    j['start_time'] = j['start_time'].strftime("%b %d %Y %I:%M%p")
                    j['end_time'] = j['end_time'].strftime("%b %d %Y %I:%M%p")
            data = {
                'ok':True,
                'members': name_details
            }
            return Response({'status': 'success', 'message': 'details','data':data})

        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
