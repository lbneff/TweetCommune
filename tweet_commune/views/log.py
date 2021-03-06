from django.views.generic import ListView, DetailView

from ..models.log_entry import LogEntry


class LogListView(ListView):
    queryset = LogEntry.objects.all().order_by('-timestamp')
    context_object_name = 'log_entries'


class LogDetailView(DetailView):
    model = LogEntry
