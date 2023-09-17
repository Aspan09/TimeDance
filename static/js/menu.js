$(document).ready(function(){
    $('.div-burger').click(function(event){
        $('.div-burger,.links-head').toggleClass('active');
    });
});

$(document).ready(function(){
  $('.links-head-js').click(function(event){
      $('.links-head').addClass('jsclose');
      $('.div-burger,.links-head').removeClass('active');
      $('.links-head').removeClass('jsclose');
  });
});



$(document).ready(function(){
  $('.btn1').click(function(event){
      $('.c3').removeClass('show-red');
      $('.c2').removeClass('show-red');
      $('.c4').removeClass('show-red');
      $('.c5').removeClass('show-red');
      $('.c1').toggleClass('show-red');
  });
});

$(document).ready(function(){
  $('.btn2').click(function(event){
      $('.c1').removeClass('show-red');
      $('.c3').removeClass('show-red');
      $('.c4').removeClass('show-red');
      $('.c5').removeClass('show-red');
      $('.c2').toggleClass('show-red');
  });
});

$(document).ready(function(){
  $('.btn3').click(function(event){
      $('.c1').removeClass('show-red');
      $('.c2').removeClass('show-red');
      $('.c4').removeClass('show-red');
      $('.c5').removeClass('show-red');
      $('.c3').toggleClass('show-red');
  });
});

$(document).ready(function(){
  $('.btn4').click(function(event){
      $('.c1').removeClass('show-red');
      $('.c3').removeClass('show-red');
      $('.c2').removeClass('show-red');
      $('.c5').removeClass('show-red');
      $('.c4').toggleClass('show-red');
  });
});

$(document).ready(function(){
  $('.btn5').click(function(event){
      $('.c1').removeClass('show-red');
      $('.c2').removeClass('show-red');
      $('.c3').removeClass('show-red');
      $('.c4').removeClass('show-red');
      $('.c5').toggleClass('show-red');
  });
});



// Cookie
function checkCookies(){
  let cookieDate = localStorage.getItem('cookieDate');
  let cookieNotification = document.getElementById('cookie_notification');
  let cookieBtn = cookieNotification.querySelector('.cookie_accept');

  // Если записи про кукисы нет или она просрочена на 1 год, то показываем информацию про кукисы
  if( !cookieDate || (+cookieDate + 31536000000) < Date.now() ){
      cookieNotification.classList.add('show');
  }

  // При клике на кнопку, в локальное хранилище записывается текущая дата в системе UNIX
  cookieBtn.addEventListener('click', function(){
      localStorage.setItem( 'cookieDate', Date.now() );
      cookieNotification.classList.remove('show');
  })
}
checkCookies();