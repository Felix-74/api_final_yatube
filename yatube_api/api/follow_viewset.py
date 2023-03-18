from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import FollowUserOrReadOnly
from .serializers import FollowSerializer
from posts.models import Follow


class FollowViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (FollowUserOrReadOnly, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('following',)
    pagination_class = None
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)