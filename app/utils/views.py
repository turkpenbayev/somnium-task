from rest_framework import exceptions


class ActionSerializerViewSetMixin(object):
    """
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('list', ): MyModelListViewSerializer,
        ('create', 'update'): MyModelCreateUpdateSerializer
    }
    """
    serializer_classes = None

    def get_serializer_class(self):
        assert self.serializer_classes is not None, (
                'Expected viewset %s should contain serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        serializer_cls = self._get_serializer_class(self.serializer_classes, self.action)
        if serializer_cls is not None:
            return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)

    def _get_serializer_class(self, classes, action):
        for actions, serializer_cls in classes.items():
            if action in actions:
                return serializer_cls
        return None