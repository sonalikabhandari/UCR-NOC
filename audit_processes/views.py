from rest_framework import serializers
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
# from rest_framework import viewsets, status, views
# from .serializers import aletheia_rancidSerializer


# from .serializers import db_processSerializer

# from rest_framework import views

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
# from.models import ProcessStatusAudit
from django.views.generic.detail import DetailView

import itertools
import json
from datetime import datetime
# Create your views here.

class LDAPLogin(APIView):
    """
    Class to authenticate a user via LDAP and
    then creating a login session
    """
    authentication_classes = ()

    def post(self, request):
        """
        Api to login a user
        :param request:
        :return:
        """
        user_obj = authenticate(username=request.data['username'],
                                password=request.data['password'])
        login(request, user_obj)
        data={'detail': 'User logged in successfully'}
        return Response(data, status=200)



class LDAPLogout(APIView):
    """
    Class for logging out a user by clearing his/her session
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Api to logout a user
        :param request:
        :return:
        """
        logout(request)
        data={'detail': 'User logged out successfully'}
        return Response(data, status=200)


aletheia_query = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
 FROM Process_Order a INNER JOIN Process_Status_Audit b
  WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 1) = 1
  GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""

dp_query = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
FROM Process_Order a INNER JOIN Process_Status_Audit b
WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 1) = 2
GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""

du_query_RRD = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
FROM Process_Order a INNER JOIN Process_Status_Audit b
WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 2) = 3.1
GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""


du_query_RP95 = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
FROM Process_Order a INNER JOIN Process_Status_Audit b
WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 2) = 3.2
GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""

du_query_WAE = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
FROM Process_Order a INNER JOIN Process_Status_Audit b
WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 2) = 3.3
GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""

du_query_UCR = """SELECT a.SeqNum,a.ProcessName,MAX(b.Polldate) AS PollDate, b.ProcessStatus, MAX(b.LastUpdate) AS LastUpdated
FROM Process_Order a INNER JOIN Process_Status_Audit b
WHERE a.SeqNum = b.SeqNum AND SUBSTRING_INDEX(a.SeqNum, '.', 2) = 3.4
GROUP BY (a.ProcessName) ORDER BY (a.SeqNum);"""


# class AuditDetailView(TemplateView):
#     template_name = "aletheia.html"

def Aletheia(request):
    c = connection.cursor()

    c.execute(aletheia_query )

    desc = c.description



    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'

        # result = json.dumps(db_data,indent=4, sort_keys=True,  default=str)
        #
        # context = {
        #
        # 'data': result
        #
        # }
        #
        # return(context)

    return JsonResponse(db_data, safe=False)


def DailyPrep(request):
    c = connection.cursor()

    c.execute(dp_query )

    desc = c.description


    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'


    return JsonResponse(db_data, safe=False)


def DailyUpdate_RRD(request):
    c = connection.cursor()

    c.execute(du_query_RRD)

    desc = c.description


    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'


    return JsonResponse(db_data, safe=False)


def DailyUpdate_RP95(request):
    c = connection.cursor()

    c.execute(du_query_RP95)

    desc = c.description


    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'


    return JsonResponse(db_data, safe=False)



def DailyUpdate_WAE(request):

    c = connection.cursor()

    c.execute(du_query_WAE)

    desc = c.description



    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'


    return JsonResponse(db_data, safe=False)


def DailyUpdate_UCR(request):
    c = connection.cursor()

    c.execute(du_query_UCR)

    desc = c.description


    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    for x in db_data:
        if (x['ProcessStatus']== -1):
            x['ProcessStatus'] = 'Not Started'
        elif (x['ProcessStatus']== 1):
            x['ProcessStatus'] = 'Completed'
        else:
            x['ProcessStatus'] = 'Running'


    return JsonResponse(db_data, safe=False)
        # print(column_names)

                # row = cursor.fetchall()


    # queryset = ProcessStatusAudit.objects.all()
    # serializer_class = db_processSerializer
    # permission_classes = (AllowAny,)
    #
    # def db_process_info(request):
    #     context = {
    #
    #      'queryset':queryset
    #
    #
    #
    #     }
    #
    #     return (context)
