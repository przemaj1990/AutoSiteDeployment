from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from lbeportal.forms import SiteVendorForm
from lbeportal.models import SiteVendor
from django.views.generic.edit import FormView


class SiteVendorCreateView(FormView):
    template_name = 'sitevendor_create.html'
    form_class = SiteVendorForm
    queryset = SiteVendor.objects.all()
    success_message = 'Site successfully added!'
    # success_url = reverse_lazy('lbeportal:list')


    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        # send_mail('Subject here', 'Here is the message.', 'przemaj1990@gmail.com', ['przemyslaw.majdanski@dsv.com'], fail_silently=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lbeportal:detail', kwargs={'pk': self.object.pk})



class SiteVendorListView(ListView):
    template_name = 'sitevendor_list.html'
    # queryset = SiteVendor.objects.all().order_by('-pk')
    paginate_by = 20
    ordering = ['-pk']
    model = SiteVendor

    # Def that allow search to work
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = SiteVendor.objects.filter(
                Q(site_code__icontains=query)|
                Q(address__icontains=query)
            ).distinct()
        else:
            object_list = SiteVendor.objects.all()
        return object_list



class SiteVendorDetailView(DetailView):
    template_name = 'sitevendor_detail.html'
    # queryset = SiteVendor.objects.all()
    model = SiteVendor

class SiteVendorUpdateView(UpdateView):
    template_name = 'sitevendor_update.html'
    queryset = SiteVendor.objects.all()
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lbeportal:detail', kwargs={'pk': self.object.pk})

    # template_name_suffix = '_update_form'

class SiteVendorDeleteView(DeleteView):
    template_name = 'sitevendor_delete.html'
    queryset = SiteVendor.objects.all()

