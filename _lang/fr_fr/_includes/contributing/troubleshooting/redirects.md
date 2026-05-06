Si une [redirection que vous avez définie](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) dans le fichier de redirection global (`assets/js/broken_redirect_list.js`) ne fonctionne pas, vérifiez que votre chaîne de caractères URL ne contient pas de majuscules. Si vous en trouvez, convertissez-les en minuscules (même si le nom de fichier correspondant dans le répertoire `_docs` contient des caractères majuscules).

{% tabs local %}
{% tab Avant %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab Après %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}