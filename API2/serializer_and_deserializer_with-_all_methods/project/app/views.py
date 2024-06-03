from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def my_form_view(request):
    if request.method == "POST":
        name = request.data.get("name")
        email = request.data.get("email")

        # Save the form data to the database or perform other actions
        # ...

        return Response(
            {"message": "Form submitted successfully"},
            status=status.HTTP_200_OK,
        )