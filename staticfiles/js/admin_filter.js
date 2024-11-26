$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);
    let selectedValue = selector.val();

    if (selectedValue != 'reset') {
        let filterParam = selectedValue;

        currentUrl.searchParams.set('refine', filterParam);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('refine');
        window.location.replace(currentUrl);
    }
});