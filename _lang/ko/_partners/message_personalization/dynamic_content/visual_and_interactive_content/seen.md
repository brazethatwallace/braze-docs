---
nav_title: Seen
article_title: Seen
description: "Seen은 대규모로 개인화된 비디오 경험을 제공하여 브랜드가 고객 여정 전반에서 더 높은 참여를 유도할 수 있도록 지원합니다."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io)은 브랜드가 개인화된 동영상 경험을 대규모로 제작하고 전달할 수 있도록 지원합니다. Seen을 사용하면 데이터를 중심으로 동영상을 디자인하고, 클라우드에서 대규모로 개인화한 다음, 가장 효과적인 곳에 배포할 수 있습니다.
>
> 이 통합은 Braze에서 Seen으로 사용자 데이터를 전송하고, 개인화된 동영상을 생성한 후, 고유한 플레이어 URL 및 썸네일과 같은 자산을 다시 Braze로 반환하여 Campaigns와 Canvases에서 사용할 수 있도록 합니다.


## 활용 사례 {#use-cases}

Seen은 다음을 포함하여 고객 생애주기 전반에 걸쳐 자동화된 개인화 비디오 전달을 지원합니다:

- **온보딩**: 프로필 또는 가입 상황에 맞게 개인화된 동영상으로 신규 사용자를 환영합니다
- **전환 및 활성화**: 상황별 비디오 메시징으로 주요 동작을 강화합니다
- **로열티 및 업셀**: 개인화된 오퍼 또는 사용 마일스톤을 강조합니다
- **윈백 및 고객이탈 방지**: 맞춤형 동영상 콘텐츠로 비활성 사용자의 재참여를 유도합니다


## 필수 조건 {#prerequisites}

시작하기 전에 다음 표에 나열된 액세스 권한과 데이터가 있는지 확인하세요.

| 필수 조건 | 설명 |
|--------------|-------------|
| Seen 플랫폼 액세스 | 게시된 프로젝트가 있는 Seen 플랫폼 구독 또는 활성 Seen Campaign이 필요합니다. 프로젝트 엔드포인트를 확인하고 API 토큰을 생성하려면 프로젝트에 대한 액세스 권한도 필요합니다. |
| Braze 데이터 변환 웹훅 URL | Braze 데이터 변환을 사용하여 Seen에서 수신되는 데이터를 Braze의 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에서 수락할 수 있는 형식으로 변환합니다. |
| Braze 사용자 데이터 | 비디오 개인화를 위해서는 사용자 수준의 데이터가 필요합니다. 관련 속성이 Braze에서 사용 가능한지 확인하고, 고유 식별자로 **`braze_id`**를 전달하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }




## Seen 프로젝트의 작동 방식 {#how-seen-projects-work}

Seen은 프로젝트의 [Run](https://docs.seen.io/run) 탭을 사용하여 수신 데이터를 처리하는 방법과 비디오 출력을 생성하는 방법을 제어합니다.

프로젝트 워크플로:

- 외부 시스템(예: Braze)으로부터 데이터 수신
- 로직 및 개인화 규칙 적용
- 비디오 및 관련 자산 생성
- 구성 가능한 응답 페이로드 반환

Run 탭에는 다음이 포함됩니다:

- **Create via API**: 프로젝트 API 세부 정보를 엽니다.
- **Import CSV**: 개인화 데이터를 수동으로 가져옵니다(이 안내에서는 사용하지 않음).
- **Add webhook**: Braze로 다시 전송되는 응답 페이로드를 정의합니다.
- **View videos**: 생성된 동영상과 수신 데이터의 상태를 표시합니다.

웹훅 응답은 구성할 수 있으므로, Seen에서 반환하는 출력 필드가 Braze 데이터 변환에서 예상하는 속성과 일치하는지 확인하세요.


## 사용량 제한 {#rate-limit}

Seen API는 10초당 최대 100건의 호출을 수락합니다.


## 통합 {#integration}

이 예시에서 Braze는 사용자 데이터를 Seen으로 전송하여 개인화된 동영상을 생성합니다. 그러면 Seen이 고유한 동영상 플레이어 URL과 썸네일 URL을 반환하며, 이를 Braze에 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)으로 저장하여 [메시징]({{site.baseurl}}/user_guide/messaging/)에 사용할 수 있습니다.

Seen으로 여러 동영상 Campaign을 운영하는 경우, 각 Campaign마다 이 과정을 반복하세요.

### 1단계: 웹훅 Campaign을 만들어 Seen에 데이터 전송하기 {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Braze에서 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/)을 만듭니다.

다음과 같이 웹훅을 구성합니다:

- **Webhook URL**:
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  Seen 플랫폼 프로젝트의 Run 탭에서 프로젝트 엔드포인트를 확인합니다.

- **HTTP Method**: POST

- **Request body**: Raw Text
  다음 예시를 시작점으로 사용하세요. 필드 옵션 및 제한 사항에 대해서는 [Seen의 데이터 생성 설명서](https://docs.seen.io/create-data)를 참조하세요.

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}

- **Request headers**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  Seen 플랫폼 프로젝트의 Run 탭에서 [API 토큰](https://docs.seen.io/authorization)을 생성합니다. 도움이 필요하면 Seen 고객 성공 매니저에게 문의하세요.

- **Test** 탭에서 사용자를 대상으로 웹훅을 테스트합니다.
- 테스트가 성공하면 웹훅 설정을 완료합니다.


### 2단계: Seen 플랫폼에서 프로젝트 구성하기 {#step-2-configure-a-project-in-the-seen-platform}

Seen 프로젝트에서 [Run](https://docs.seen.io/run) 탭을 사용하여 동영상을 게시하고 아웃바운드 웹훅을 등록합니다. Run 탭의 개념적 개요는 [Seen 프로젝트의 작동 방식](#how-seen-projects-work)을 참조하세요.

1. Seen 플랫폼에서 프로젝트를 만들고, 동영상을 빌드한 다음 **Publish**를 선택합니다. 프로젝트가 게시되면 수신 데이터로부터 동영상 생성이 시작됩니다.
2. Run 탭에서 **Add a webhook**을 선택합니다.

#### 웹훅 응답 요구 사항 {#webhook-response-requirements}

응답 페이로드는 구성할 수 있습니다. 다음 단계의 Braze 데이터 변환에서 매핑할 수 있도록 다음 표의 필드를 반환하세요.

| 필드 | 설명 |
|-------|-------------|
| `id` | Braze에서 전송한 `braze_id`와 일치해야 합니다 |
| `player_url` | 개인화된 동영상 플레이어를 위한 고유 URL |
| `email_thumbnail_url` | 개인화된 동영상 썸네일의 URL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹훅 응답 요구 사항" }

추가 속성이 필요한 경우 응답에 포함시키고 Braze에서 매핑하세요.


### 3단계: 데이터 변환을 생성하여 Seen에서 데이터 수신하기 {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Braze 데이터 변환을 사용하여 Seen 응답을 처리하고 고객 프로필에 동영상 자산을 저장합니다.

1. Braze에서 다음 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)을 생성합니다:
   - `player_url`
   - `email_thumbnail_url`

2. **데이터 설정** > **데이터 변환**으로 이동한 다음 **변환 생성**을 선택합니다.

3. 변환을 구성합니다:
   - **처음부터 시작**
   - **대상** > POST: Track users

4. 생성된 웹훅 URL을 Seen과 공유하거나 프로젝트 Run 탭의 **Webhook**에 추가합니다.

5. 다음 변환 코드를 사용합니다:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. 제공된 엔드포인트로 테스트 페이로드를 전송합니다. Seen 플랫폼 프로젝트로 데이터를 전송하거나(먼저 프로젝트를 게시하세요), [Postman](https://www.postman.com/) 또는 유사한 도구를 사용하여 Braze로 직접 페이로드를 전송할 수 있습니다.
7. **검증**을 선택하여 변환이 예상대로 작동하는지 확인합니다.
8. **저장** 및 **활성화**를 선택합니다.