グローバルリダイレクトファイル（`assets/js/broken_redirect_list.js`）で[設定したリダイレクト](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md)が機能していない場合は、URL文字列に大文字が含まれていないか再確認してください。大文字が見つかった場合は、（`_docs`ディレクトリの対応するファイル名に大文字が含まれていても）小文字に変換してください。

{% tabs local %}
{% tab 導入前 %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab 変更後 %}
`````````javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}