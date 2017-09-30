function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toogleAddCommentPanel(id) {
    $('#add-comment-panel-' + id).toggle()
}

function hideAddCommentPanel(id) {
    $('#add-comment-panel-' + id).hide()
}

function addNewComment(event) {
    $.ajax({
       url: '/message_feed/add_message' + event.target.id,
       data: {
          parent: event.target.id,
          text: $('#message-text-' + event.target.id).val(),
          depth: parseInt(event.target.getAttribute('data-depth')) + 1,
       },
       headers: {
           'X-CSRFToken': getCookie('csrftoken')
       },
       error: function() {alert('error')},
       success: function(data) {
           $("#target-new-comment-" + event.target.id).append(data);
       },
       type: 'POST'
    });
}


window.onload = function () {
    document.addEventListener("click", function(event){
        if ($(event.target).hasClass('show-comment-panel-button')) {
            toogleAddCommentPanel(event.target.id);
        } else if ($(event.target).hasClass('add-comment-button')) {
            addNewComment(event);
            toogleAddCommentPanel(event.target.id);
        } else if ($(event.target).hasClass('cancel-comment-button')) {
            hideAddCommentPanel(event.target.id);
        }
    });
    $('.message-container').infiniteScroll({
      path: '#next_page',
      append: '.panel-group',
      history: false,
      arg: '1',
    });
};


