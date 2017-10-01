window.onload = function () {
    $('.message-container').infiniteScroll({
      path: '#next_page',
      append: '.panel-group',
      history: false,
      arg: '1',
    });
};