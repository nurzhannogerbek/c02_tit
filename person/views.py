from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from person.models import Person
from person.serializers import PersonSerializer


class PersonView(APIView):
    def get(self, request, pk=None):
        data = []
        error = {}
        result = {"data": data, "error": error}

        try:
            if pk:
                try:
                    person = Person.objects.get(id=pk)
                except Person.DoesNotExist as err:
                    error['non_field_errors'] = [str(err)]
                    return Response(result, status=status.HTTP_404_NOT_FOUND)

                person_serializer = PersonSerializer(person)
                data.append(person_serializer.data)
                return Response(result, status=status.HTTP_200_OK)

            else:
                persons = Person.objects.all()
                person_serializer = PersonSerializer(persons, many=True)
                result["data"] = person_serializer.data
                return Response(result, status=status.HTTP_200_OK)

        except Exception as err:
            error['non_field_errors'] = [str(err)]
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = []
        error = {}
        result = {"data": data, "error": error}

        try:
            person_serializer = PersonSerializer(data=request.data)

            if not person_serializer.is_valid():
                result["error"] = person_serializer.errors
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            person_serializer.save()
            data.append(person_serializer.data)
            result["data"] = data
            return Response(result, status=status.HTTP_201_CREATED)

        except Exception as err:
            error['non_field_errors'] = [str(err)]
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk=None):
        data = []
        error = {}
        result = {"data": data, "error": error}

        try:
            try:
                person = Person.objects.get(id=pk)
            except Person.DoesNotExist as err:
                error['non_field_errors'] = [str(err)]
                return Response(result, status=status.HTTP_404_NOT_FOUND)

            person_serializer = PersonSerializer(instance=person, data=request.data)

            if not person_serializer.is_valid():
                result["error"] = person_serializer.errors
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            person_serializer.save()
            data.append(person_serializer.data)
            return Response(result, status=status.HTTP_200_OK)

        except Exception as err:
            error['non_field_errors'] = [str(err)]
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        data = []
        error = {}
        result = {"data": data, "error": error}

        try:
            try:
                person = Person.objects.get(id=pk)
            except Person.DoesNotExist as err:
                error['non_field_errors'] = [str(err)]
                return Response(result, status=status.HTTP_404_NOT_FOUND)

            person_serializer = PersonSerializer(person)
            data.append(person_serializer.data)
            person.delete()
            return Response(result, status=status.HTTP_204_NO_CONTENT)

        except Exception as err:
            error['non_field_errors'] = [str(err)]
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

