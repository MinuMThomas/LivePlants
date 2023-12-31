from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import Review
from .forms import ReviewForm


def reviews(request, item_id):
    """A view to show all available reviews for the current item"""
    item = get_object_or_404(Item, pk=item_id)
    reviews = Review.objects.filter(item=item)
    template = 'reviews/reviews.html'
    context = {'reviews': reviews, 'item': item}
    return render(request, template, context)


@login_required
def add_review(request, item_id):
    """Allow users to add a review"""
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.user = request.user
            review.save()
            messages.success(request, f"Your review for '{item.name}' has"
                             "been submitted!")
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request, "Oops!!, something went wrong."
                           "Please ensure your fields are valid")
            return redirect(reverse('item_detail', args=[item.id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {'form': form,
               'item': item,
               'reviews': reviews,
               }
    return render(request, template, context)
