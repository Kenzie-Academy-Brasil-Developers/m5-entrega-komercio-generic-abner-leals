from rest_framework import views
from rest_framework import generics


class GetPostView(generics.ListCreateAPIView):
    ...


class PostCommonView(views.APIView):
    def post(self, request: views.Request) -> views.Response:

        serializer = self.view_serilizer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return views.Response(serializer.data, views.status.HTTP_201_CREATED)


class GetCommonView(views.APIView):
    def get(self, request: views.Request) -> views.Response:

        queryset = self.view_model.objects.all()

        serializer = self.view_serilizer(queryset, many=True)

        return views.Response(serializer.data)
