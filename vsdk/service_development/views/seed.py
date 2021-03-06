from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..models import Seed, CallSession


class Seed(TemplateView):

    def get(self, request, session_id):
        session = get_object_or_404(CallSession, pk=session_id)
        return request, session
