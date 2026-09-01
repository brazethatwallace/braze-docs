(function () {
  if (!window.EventSource) {
    return;
  }

  var pageLoadedAt = Date.now() / 1000;
  var eventSource;
  var indicator;

  function createIndicator() {
    var element = document.createElement('div');
    element.id = 'dev-build-status-indicator';
    element.setAttribute('role', 'status');
    element.setAttribute('aria-live', 'polite');
    element.hidden = true;
    element.textContent = 'Rebuilding…';
    Object.assign(element.style, {
      position: 'fixed',
      bottom: '16px',
      left: '16px',
      zIndex: '10000',
      padding: '8px 12px',
      borderRadius: '4px',
      background: '#3d2d5e',
      color: '#fff',
      fontSize: '14px',
      fontFamily: 'system-ui, sans-serif',
      boxShadow: '0 2px 8px rgba(0, 0, 0, 0.2)',
    });
    document.body.appendChild(element);
    return element;
  }

  function showIndicator() {
    if (!indicator) {
      indicator = createIndicator();
    }
    indicator.hidden = false;
  }

  function hideIndicator() {
    if (indicator) {
      indicator.hidden = true;
    }
  }

  function isRecentEvent(timestamp) {
    return timestamp && timestamp >= pageLoadedAt;
  }

  try {
    eventSource = new EventSource('/sse/build-status');
  } catch (error) {
    return;
  }

  eventSource.addEventListener('build-started', function (event) {
    try {
      var data = JSON.parse(event.data);
      if (isRecentEvent(data.started_at)) {
        showIndicator();
      }
    } catch (error) {
      // Ignore malformed payloads.
    }
  });

  eventSource.addEventListener('build-complete', function (event) {
    try {
      var data = JSON.parse(event.data);
      hideIndicator();
      if (isRecentEvent(data.completed_at)) {
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
