$(->
    $('p.description').each((index, desc) ->
        $(desc).before('<span class="info"><a href="#">Info</a></span>')
        $(desc).hide()
    )
    $('span.info').click((event) ->
        $(event.target).parent().parent().find('p.description').toggle()
    )
)
