Wenn eine [von Ihnen eingerichtete Weiterleitung](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) in der globalen Weiterleitungsdatei (`assets/js/broken_redirect_list.js`) nicht funktioniert, überprüfen Sie Ihren URL-String auf Großbuchstaben. Wenn Sie welche finden, konvertieren Sie sie in Kleinbuchstaben (auch wenn der entsprechende Dateiname im Verzeichnis `_docs` Großbuchstaben enthält).

{% tabs local %}
{% tab Vor %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab Nach %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}