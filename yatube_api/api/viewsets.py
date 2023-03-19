from rest_framework import mixins, viewsets


class MainFollowViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass
