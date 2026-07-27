- **Screen recording:** A recording of the steps you took before seeing the error, including any page transitions.
- **Timestamp and time zone:** The exact time the error occurred and your time zone.
- **Browser and version:** The browser you're using (for example, Chrome 120, Safari 17) and whether you've tried reproducing the error in a different browser.
{% if include.context == 'canvas' -%}
- **Steps to reproduce:** A clear description of the actions that trigger the error, including any specific Canvas steps or configurations involved.
{% elsif include.context == 'campaign' -%}
- **Steps to reproduce:** A clear description of the actions that trigger the error, including any specific campaign or Canvas settings involved.
{% endif -%}
- **Network logs (optional):** Open your browser developer tools (**Network** tab), reproduce the error, and export the network log as an HTTP Archive (HAR) log file. This helps the support team identify which API call is timing out.
