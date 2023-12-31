from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item, Category


def all_items(request):
    """ A view to show all items, including sorting and search queries """

    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't"
                               "enter any search criteria!")
                return redirect(reverse('items'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ Shows each item details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)


@login_required
def add_item(request):
    """ Add an item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Item added to the store!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request, 'Failed to add item. Please check your form is valid')
    else:
        form = ItemForm()
    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """ Edit a item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been updated!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request, 'Failed to update item.'
                ' Please ensure your form is valid.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    """ Delete a item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('items'))
