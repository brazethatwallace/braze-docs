전역 리디렉션 파일(`assets/js/broken_redirect_list.js`)에서 [설정한 리디렉션](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md)이 작동하지 않는 경우, URL 문자열에 대문자가 포함되어 있는지 다시 확인하세요. 대문자가 있다면 소문자로 변환하세요(`_docs` 디렉토리의 해당 파일 이름에 대문자가 포함되어 있더라도 마찬가지입니다).

{% tabs local %}
{% tab 이전 %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab 이후 %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}