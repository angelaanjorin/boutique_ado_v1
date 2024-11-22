from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse

from .models import Review
from products.models import Product
from .forms import ReviewForm

@login_required()
def add_review(request, product_id):
    """
    Renders form to add review.
    Logged in Users Only (redirects to log in).
    Adds new review to database.
    """

    # Sets product based on product_id
    product = get_object_or_404(Product, pk=product_id)

    # confirms user
    user = request.user.userprofile

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()

            # Updates product rating on product object
            if product.reviews.exists():
                product.rating = round(product.reviews.aggregate(Avg('rating'))['rating__avg'], 2)
            else:
                product.rating = 0
            product.save()

            reviews = product.reviews.all()
            review_count = reviews.count()

            if review_count > 0:
                avg_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 1)
            else:
                avg_rating = 0

            product.rating = avg_rating
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(request, "Review added successfully.")

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm()

    # Calculate average rating and review count
    reviews = product.reviews.all()
    review_count = reviews.count()

    if review_count > 0:
        avg_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 1)
    else:
        avg_rating = 0

    # Sets page template
    template = 'reviews/add_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
        'avg_rating': avg_rating,
        'review_count': review_count,
    }

    return render(request, template, context)
