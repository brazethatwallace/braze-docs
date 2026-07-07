---
nav_title: Postman 및 샘플 요청
article_title: Postman 및 샘플 요청
page_order: 3
description: "이 참조 문서에서는 Braze Postman 컬렉션이 무엇인지, 컬렉션을 설정하고 사용하는 방법, 요청을 편집하고 보내는 방법을 다룹니다."
page_type: reference

---

# Postman 및 샘플 요청 {#postman-and-sample-requests}

> Braze를 사용하면 Postman 컬렉션을 통해 모든 엔드포인트에 대한 샘플 API 요청을 생성할 수 있습니다. 이 참조 문서에서는 Braze Postman 컬렉션이 무엇인지, 컬렉션을 설정하고 사용하는 방법, 요청을 편집하고 보내는 방법을 다룹니다.

## Postman이란 무엇인가요? {#what-is-postman}

Postman은 API 요청을 구축하고 테스트할 수 있는 무료 시각적 편집 도구입니다. 다른 방법(예: cURL 사용)에 비해 Postman을 사용하면 API 요청을 편집하고 헤더 정보를 확인하는 등 다양한 작업을 수행할 수 있습니다. 컬렉션(미리 만들어진 API 요청 샘플 라이브러리)을 저장할 수 있습니다. REST API 설정을 빠르게 시작할 수 있도록 모든 엔드포인트에 대해 미리 만들어진 예제가 포함된 컬렉션을 제공합니다.

시작하려면 [Postman 문서](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)에서 **Run in Postman**을 클릭하여 Postman 컬렉션을 확인하거나 다운로드하세요.

## Braze Postman 컬렉션 사용하기 {#using-the-braze-postman-collection}

Postman 계정이 있는 경우(macOS, Windows, Linux 버전은 [Postman 웹사이트](https://www.getpostman.com)에서 다운로드할 수 있습니다) 주황색 **Run in Postman** 버튼을 클릭하여 자신의 Postman 앱에서 Postman 문서를 열 수 있습니다. 그런 다음 [환경을 만들거나](#setting-up-your-postman-environment) Braze REST API 환경을 템플릿으로 사용하여 사용 가능한 `POST` 및 `GET` 요청을 필요에 맞게 편집할 수 있습니다.

### Postman 환경 설정하기 {#setting-up-your-postman-environment}

{% raw %}
Braze Postman 컬렉션은 템플릿 변수 `{{instance_url}}`을 사용하여 Braze 인스턴스의 REST API URL을 미리 빌드된 요청에 대입하고, `{{api_key}}` 변수를 API 키로 대입합니다. 컬렉션의 모든 요청을 수동으로 편집할 필요 없이 Postman 환경에서 이 변수를 설정할 수 있습니다. 드롭다운에서 템플릿 환경(Braze REST API Environment Template)을 선택하고 변수 값을 자신의 값으로 바꾸거나, 직접 환경을 설정할 수 있습니다.
{% endraw %}

나만의 환경을 설정하려면 다음 단계를 수행하세요:

1. **워크스페이스** 탭에서 **환경**을 선택합니다.
2. **+** 더하기 버튼을 클릭하여 새 환경을 만듭니다.
3. 이 환경에 이름을 지정하고(예: "Braze API Requests"), [Braze 인스턴스]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) 및 [Braze REST API 키]({{site.baseurl}}/api/api_key)에 해당하는 값으로 `instance_url` 및 `api_key` 키를 추가합니다.
4. **저장**을 클릭합니다.

{% alert note %}
`POST` 요청 본문에서 `api_key`는 따옴표로 묶어야 합니다: `"MY-API-KEY-EXAMPLE"`. `GET` URL에서는 따옴표로 묶지 않아야 합니다. 이 문서의 `POST` 요청 본문, `GET` URL, `YOUR-API-KEY-HERE` 환경 템플릿에서 이미 이 형식을 제공하고 있습니다.
{% endalert %}

![Postman의 Braze REST API 환경에 API 키 및 인스턴스 URL 변수를 추가하는 화면]({% image_buster /assets/img_archive/postman_variable.png %})

### 컬렉션에서 미리 작성된 요청 사용하기 {#using-the-pre-built-requests-from-the-collection}

환경을 구성한 후에는 컬렉션에 미리 작성된 요청 중 하나를 새 API 요청을 작성하기 위한 템플릿으로 사용할 수 있습니다. 미리 작성된 요청을 사용하려면 Postman의 **Collections** 메뉴에서 해당 요청을 클릭하세요. 그러면 요청이 Postman 앱의 기본 창에 새 탭으로 열립니다.

일반적으로 Braze API 엔드포인트가 수락하는 요청 유형은 `GET`과 `POST` 두 가지입니다. 엔드포인트가 사용하는 `HTTP` 메서드에 따라 미리 빌드된 요청을 다르게 편집해야 합니다.

#### POST 요청 편집하기 {#edit-a-post-request}

`POST` 요청을 편집할 때는 요청을 열고 요청 편집기에서 **Body** 섹션으로 이동합니다. 가독성을 위해 **raw** 라디오 버튼을 선택하여 `JSON` 요청 본문의 형식을 지정합니다.

![Postman에서 POST User Track 요청을 편집할 때의 Body 탭]({% image_buster /assets/img_archive/postman_post.png %})

#### GET 요청 편집하기 {#edit-a-get-request}

`GET` 요청을 편집할 때는 요청 URL에 전달되는 매개변수를 편집합니다. 이렇게 하려면 **Params** 탭을 선택하고 표시되는 필드에서 키-값 페어를 편집합니다.

![Postman에서 수신 거부된 이메일 주소 쿼리 목록 GET 요청을 편집할 때의 Params 탭]({% image_buster /assets/img_archive/postman_get.png %})

### 요청 보내기 {#send-your-request}

API 요청이 준비되면 **Send**를 클릭합니다. 요청이 전송되고 응답 데이터가 요청 편집기 아래 섹션에 표시됩니다. 여기에서 Braze API에서 반환된 원시 데이터를 확인하고, HTTP 응답 코드를 보고, 요청 처리에 걸린 시간을 확인하고, 헤더 정보를 볼 수 있습니다.

![상태가 201 Created이고 응답 시간이 269밀리초인 POST 요청의 본문 응답 데이터 예시]({% image_buster /assets/img_archive/postman_response.png %})