var $messages = $(".messages-content"),
  d,
  h,
  m;

$(window).on("load", function () {
  $messages.mCustomScrollbar();
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar("scrollTo", "bottom", {
    scrollInertia: 10,
    timeout: 0,
  });
}

function setDate() {
  d = new Date();
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ":" + m + "</div>").appendTo(
      $(".message:last")
    );
  }
}

function insertMessage() {
  let msg = $(".message-input").val();
  if ($.trim(msg) == "") {
    return false;
  }

  // Display user message
  $('<div class="message message-personal">' + msg + "</div>")
    .appendTo($(".mCSB_container"))
    .addClass("new");
  setDate();
  $(".message-input").val(null);
  updateScrollbar();

  // Insert loading animation for bot
  $('<div class="message loading new"><span></span><span></span><span></span></div>')
    .appendTo($(".mCSB_container"));
  updateScrollbar();

  // Send to FastAPI backend
  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg }),
  })
    .then((res) => res.json())
    .then((data) => {
      // Remove loading
      $(".message.loading").remove();

      // Display bot response
      $(
        '<div class="message new"><figure class="avatar"><img src="/static/images/image.png" /></figure>' +
          data.reply +
          "</div>"
      )
        .appendTo($(".mCSB_container"))
        .addClass("new");
      setDate();
      updateScrollbar();
    })
    .catch((err) => {
      console.error("Error:", err);
      $(".message.loading").remove();
    });
}


  // Display user message
  $('<div class="message message-personal">' + msg + "</div>")
    .appendTo($(".mCSB_container"))
    .addClass("new");
  setDate();
  $(".message-input").val(null);
  updateScrollbar();

  // Send to FastAPI backend
  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg }),
  })
    .then((res) => res.json())
    .then((data) => {
      // Remove loading if any
      $(".message.loading").remove();

      // Display bot response
      $(
        '<div class="message new"><figure class="avatar"><img src="/static/images/image.png" /></figure>' +
          data.reply +
          "</div>"
      )
        .appendTo($(".mCSB_container"))
        .addClass("new");
      setDate();
      updateScrollbar();
    })
    .catch((err) => {
      console.error("Error:", err);
    });
}

$(".message-submit").click(function () {
  insertMessage();
});

$(window).on("keydown", function (e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
});
