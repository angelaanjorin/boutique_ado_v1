$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);
    let selectedValue = selector.val();

    if (selectedValue != 'reset') {
        let filterParam = selectedValue.split('_');

        currentUrl.searchParams.set('sort', filterParam[0]);
        currentUrl.searchParams.set('direction', filterParam[1]);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');
        window.location.replace(currentUrl);
    }
});