(function () {
  if (!window.EventSource) {
    return;
  }

  var pageLoadedAt = Date.now() / 1000;
  var eventSource;

  try {
    eventSource = new EventSource('/sse/build-status');
  } catch (error) {
    return;
  }

  eventSource.addEventListener('build-complete', function (event) {
    try {
      var data = JSON.parse(event.data);
      if (data.completed_at && data.completed_at >= pageLoadedAt) {
        window.location.reload();
      }
    } catch (error) {
      // Ignore malformed payloads; manual refresh still works.
    }
  });

  window.addEventListener('beforeunload', function () {
    eventSource.close();
  });
})();
