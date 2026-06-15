Se um [redirecionamento configurado](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) no arquivo de redirecionamento global (`assets/js/broken_redirect_list.js`) não estiver funcionando, verifique se há caracteres maiúsculos na string do URL. Se encontrar algum, converta-os para letras minúsculas (mesmo que o nome de arquivo correspondente no diretório `_docs` contenha caracteres maiúsculos).

{% tabs local %}
{% tab Antes %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab Depois %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}