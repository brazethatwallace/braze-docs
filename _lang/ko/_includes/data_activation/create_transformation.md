Braze 대시보드에서 **데이터 설정** > **데이터 변환**으로 이동합니다.

**변환 생성**을 선택하여 변환 이름을 지정한 다음 편집 환경을 선택합니다.

![편집 환경으로 "템플릿 사용" 또는 "처음부터 시작"을 선택할 수 있는 옵션이 있는 변환 세부 정보.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

**템플릿 사용**을 선택하여 데이터 변환 사용 사례를 포함한 템플릿 라이브러리를 탐색합니다. 또는 **처음부터 시작**을 선택하여 기본 코드 템플릿을 로드합니다.

처음부터 시작하는 경우, 변환의 대상을 선택하세요. 템플릿 라이브러리에서 코드 템플릿을 삽입할 수도 있습니다.

{% details 대상에 대해 자세히 알아보기 %}
* **POST: Track users:** 소스 플랫폼의 웹훅을 속성, 이벤트 또는 구매와 같은 고객 프로필 업데이트로 변환합니다.
* **PUT: Update multiple catalog items:** 소스 플랫폼의 웹훅을 카탈로그 항목 업데이트로 변환합니다.
* **DELETE: Delete multiple catalog items:** 소스 플랫폼의 웹훅을 카탈로그 항목 삭제로 변환합니다.
* **PATCH: Edit multiple catalog items:** 소스 플랫폼의 웹훅을 카탈로그 항목 편집으로 변환합니다.
* **POST: Send messages immediately via API Only:** 소스 플랫폼의 웹훅을 변환하여 지정된 사용자에게 즉시 메시지를 전송합니다.
{% enddetails %}

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional templates or destinations" %}
{% endalert %}

변환을 생성한 후 변환의 상세 보기가 표시됩니다. 여기에서 **웹훅 세부 정보** 아래에서 이 변환에 대해 가장 최근에 수신된 웹훅을 확인할 수 있으며, **변환 코드** 아래에 변환 코드를 작성할 수 있는 공간이 있습니다.

{% if include.location == "typeform" %}

![웹훅 세부 정보 및 변환 코드의 예시.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

다음 단계에서 사용할 **웹훅 URL**을 복사하세요.