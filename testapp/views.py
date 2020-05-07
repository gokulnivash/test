import json
import logging

from rest_framework import generics, status
from rest_framework.response import Response

from testapp.models import NameDetails
import pytz
logger = logging.getLogger(__name__)


# Create your views here.
class ActivityPeriodView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    def get(self,request):
        try:
            name_details = NameDetails.objects.all().values('id','real_name','tz','activity')
            for i in name_details:
                i['tz'] = pytz.all_timezones[146]
                i['activity'] = json.loads(i['activity'])

            return Response({'status': 'success', 'message': 'details','another':name_details})

        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
