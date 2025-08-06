from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        ordering = self.request.GET.get('order', 'title')
        qs = Book.objects.all().order_by(ordering)
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['discounted_price'] = book.get_discounted_price()
        return context

class AdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('books:book_list')
        return super().dispatch(request, *args, **kwargs)

class BookCreateView(AdminRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'discount_percentage']
    template_name = 'books/book_form.html'

class BookUpdateView(AdminRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'discount_percentage']
    template_name = 'books/book_form.html'

class BookDeleteView(AdminRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
