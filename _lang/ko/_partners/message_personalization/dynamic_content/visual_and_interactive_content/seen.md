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
> Braze와 Seen 통합을 통해 사용자 데이터를 Braze에서 Seen으로 전송하고, 개인화된 동영상을 동적으로 생성하며, 고유한 플레이어 URL 및 썸네일과 같은 동영상 자산을 다시 Braze로 반환하여 Campaigns와 Canvases에서 사용할 수 있습니다.


## 활용 사례 {#use-cases}

Seen은 다음을 포함하여 고객 생애주기 전반에 걸쳐 자동화된 개인화 비디오 전달을 지원합니다:

- **온보딩**: 프로필 또는 가입 상황에 맞게 개인화된 동영상으로 신규 사용자를 환영합니다
- **전환 및 활성화**: 상황별 비디오 메시징으로 주요 동작을 강화합니다
- **로열티 및 업셀**: 개인화된 오퍼 또는 사용 마일스톤을 강조합니다
- **윈백 및 고객이탈 방지**: 맞춤형 동영상 콘텐츠로 비활성 사용자의 재참여를 유도합니다


## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
|--------------|-------------|
| Seen 플랫폼 액세스 | Seen 플랫폼 구독 또는 활성 Seen Campaign이 필요합니다. 워크스페이스 ID를 확인하고 API 토큰을 생성하려면 워크스페이스 설정에 액세스해야 합니다. |
| Braze 데이터 변환 웹훅 URL | Braze 데이터 변환은 Seen에서 수신되는 데이터를 Braze의 /users/track 엔드포인트에서 수락할 수 있는 형식으로 변환합니다. |
| Braze 사용자 데이터 | 비디오 개인화를 위해서는 사용자 수준의 데이터가 필요합니다. 관련 속성이 Braze에서 사용 가능한지 확인하고, 고유 식별자로 **braze_id**를 전달해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }




## Seen 여정의 작동 방식 {#how-seen-journeys-work}

Seen은 [여정](https://docs.seen.io/journey)을 사용하여 수신 데이터를 처리하는 방법과 비디오 출력을 생성하는 방법을 제어합니다.

여정은 다음과 같은 기능을 수행하는 구성 가능한 워크플로입니다:
- 외부 시스템(예: Braze)으로부터 데이터 수신
- 로직 및 개인화 규칙 적용
- 비디오 및 관련 자산 생성
- 구성 가능한 응답 페이로드 반환

여정은 각각 특정 기능을 가진 **노드**로 구성됩니다:

- **트리거 노드**: 여정이 시작되는 방법과 시기를 정의합니다(Braze 통합의 경우 `On Create` 트리거 사용)
- **조건부 노드**: 데이터 값에 따라 다양한 로직 경로를 통해 사용자를 라우팅합니다
- **프로젝트 노드**: 수신 데이터를 사용하여 동적 비디오 개인화를 적용합니다
- **플레이어 노드**: 고유한 동영상 플레이어 URL을 생성합니다
- **웹훅 노드**: Braze로 다시 전송되는 응답 페이로드를 정의합니다

여정 응답은 구성할 수 있으므로, Seen에서 반환되는 출력 필드가 Braze 데이터 변환에서 예상하는 속성과 일치하는지 확인하세요.


## 사용량 제한 {#rate-limit}
Seen API는 10초마다 최대 100건의 호출을 수락합니다.


## 통합 {#integration}

이 예시에서 Braze는 사용자 데이터를 Seen으로 전송하여 개인화된 동영상을 생성합니다. 그러면 Seen이 고유한 동영상 플레이어 URL과 썸네일 URL을 반환하며, 이는 메시징에 사용할 수 있도록 Braze에 커스텀 속성으로 저장됩니다.

Seen을 사용하는 동영상 Campaign이 여러 개 있는 경우, 이 과정을 반복하여 모든 동영상 Campaign에 Braze를 연결합니다.

### 1단계: 웹훅 Campaign을 만들어 Seen에 데이터 전송하기 {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Braze에서 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/)을 만듭니다.

다음과 같이 웹훅을 구성합니다:

- **Webhook URL**:
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`
  Seen 플랫폼 설정에서 워크스페이스 ID를 확인합니다.

- **HTTP Method**: POST
- **Request Body**: Raw Text
  다음 예시를 시작점으로 사용하세요. 자세한 내용은 [Seen의 데이터 생성 설명서](https://docs.seen.io/create-data)를 참조하세요.

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
- **Request Headers**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > 워크스페이스 설정의 Seen 플랫폼에서 [API 토큰](https://docs.seen.io/authorization)을 생성합니다. 도움이 필요하면 Seen 고객 성공 매니저에게 문의할 수 있습니다.

- 사용자를 대상으로 웹훅을 테스트하려면 **Test** 탭으로 전환합니다.
- 테스트가 의도한 대로 작동하는지 확인한 후 웹훅 설정을 완료합니다.


### 2단계: Seen 플랫폼에서 여정 구성하기 {#step-2-configure-a-journey-in-the-seen-platform}

Seen은 [여정](https://docs.seen.io/journey)을 사용하여 수신 데이터를 처리하고 개인화하여 Braze로 반환하는 방법을 정의합니다.
각 여정은 비디오 생성 로직과 응답 페이로드를 모두 제어할 수 있는 노드로 구성된 구성 가능한 워크플로입니다.

여정을 구성하려면:

1. Seen 플랫폼에서 새로운 여정을 만듭니다.
2. **트리거 노드**를 추가하고 `On Create` 트리거를 선택합니다.
   이렇게 하면 Braze가 Seen에 데이터를 전송할 때 여정이 시작됩니다. 필요한 경우 워크스페이스 내에서 [세분화](https://docs.seen.io/segments) 로직을 만들고 추가하세요.
3. 필요에 따라 다음 노드를 사용하여 로직을 구축하세요:
   - **조건부 노드**: 속성 값(예: 요금제 유형 또는 지역)을 기반으로 사용자를 라우팅합니다
   - **프로젝트 노드**: 수신 데이터를 사용하여 동적 비디오 개인화를 적용합니다
   - **플레이어 노드**: 고유한 동영상 플레이어 URL을 생성합니다
4. **웹훅 노드**를 추가하여 Braze로 다시 전송되는 응답을 정의합니다.

#### 웹훅 노드 응답 요구 사항 {#webhook-node-response-requirements}

응답 페이로드는 구성할 수 있으므로, 다음 단계에서 설명하는 Braze 데이터 변환을 지원하기 위해 다음 필드가 반환되는지 확인하세요:

| 필드 | 설명 |
|------|-------------|
| `id` | Braze에서 전송한 `braze_id`와 일치해야 합니다 |
| `player_url` | 개인화된 동영상 플레이어를 위한 고유 URL |
| `email_thumbnail_url` | 생성된 동영상 썸네일의 URL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook node response requirements" }

사용 사례에 추가 속성이 필요한 경우 해당 속성을 응답에 포함시키고 Braze에서 매핑하세요.


### 3단계: 데이터 변환을 생성하여 Seen에서 데이터 수신하기 {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Braze 데이터 변환을 사용하여 Seen 여정 응답을 수집하고 고객 프로필에 동영상 자산을 저장하세요.

1. Braze에서 다음 [커스텀 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)을 생성하세요:
   - `player_url`
   - `email_thumbnail_url`
2. **Data Settings** → **Data Transformation**으로 이동하여 **Create transformation**을 클릭합니다.
3. 변환을 구성합니다:
   - **Start from scratch**
   - **Destination** → POST: Track users
4. 생성된 웹훅 URL을 Seen과 공유하거나 여정 **웹훅 노드**에 직접 추가합니다.
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
6. 제공된 엔드포인트로 테스트 페이로드를 전송합니다. 데이터를 Seen 플랫폼으로 전송하여 여정을 실행하거나, [Postman](https://www.postman.com/) 또는 다른 유사한 서비스를 통해 직접 Braze로 페이로드를 전송할 수 있습니다.
7. **Validate**를 선택하여 모든 것이 의도한 대로 작동하는지 확인합니다.
8. **Save** 및 **Activate**를 선택합니다.