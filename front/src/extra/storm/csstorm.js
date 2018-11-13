window.onload = function() {

    document.querySelectorAll('[size]').forEach(function($this) {
        var dimensions = $this.getAttribute('size').split(';')
        var w = dimensions[0]
        var h = dimensions[1]

        if (w != null && w != 0) {
            $this.style.width = w
        }
        if (h != null && w != 0) {
            $this.style.height = h
        }
    })

    $('[fields-width]').each(function () {
        let width = $(this).attr('fields-width');
        $(this).find(':input:not([type=checkbox]):not([type=radio])')
        .css('width', width)
    })

}

function HTML(html) {
    let template = document.createElement('template');
    html = html.trim();
    template.innerHTML = html;
    return template.content.firstChild;
}