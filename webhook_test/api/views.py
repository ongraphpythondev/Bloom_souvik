from rest_framework.response import Response
from rest_framework.decorators import APIView


class Authorize(APIView):

    def post(self, request, format=None):
        # Get the request body
        request_body = request.data
        cardID = request_body["cardAuthorization"]["cardId"]
        accountID = request_body["cardAuthorization"]["accountId"]
        availableBalance = request_body["cardAuthorization"]["availableBalance"]
        responseCode = request_body["cardAuthorization"]["responseCode"]
        settledBalance = request_body["cardAuthorization"]["settledBalance"]
        entryModeType = request_body["cardAuthorization"]["entryModeType"]
        transactionType = request_body["cardAuthorization"]["transactionType"]
        transactionAmount = request_body["cardAuthorization"]["transactionAmount"]
        mccCode = request_body["cardAuthorization"]["mccCode"]
        billingAmount = request_body["cardAuthorization"]["billingAmount"]
        holderAmount = request_body["cardAuthorization"]["holderAmount"]
        print(transactionAmount)
        if transactionAmount >= 1000 or mccCode == 1520:

            return Response({
                "status": "success",
                "data": {
                    "responseCode": 61,
                    "billingAmount": billingAmount,
                    "holderAmount": holderAmount,
                    "availableBalance": availableBalance,
                    "settledBalance": settledBalance
                }
            }, status=200)

        # Process the request body as needed
        # ...

        return Response({
            "status": "success",
            "data": {
                "responseCode": responseCode,
                "billingAmount": billingAmount,
                "holderAmount": holderAmount,
                "availableBalance": availableBalance,
                "settledBalance": settledBalance
            }
        }, status=200)
