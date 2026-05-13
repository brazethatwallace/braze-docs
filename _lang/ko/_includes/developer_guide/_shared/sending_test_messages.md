# 테스트 메시지 보내기 {#sending-test-messages}

> 사용자에게 메시징 캠페인을 보내기 전에, 메시지가 올바르게 표시되고 의도한 대로 작동하는지 테스트해 볼 수 있습니다. 대시보드를 사용하여 푸시 알림, 인앱 메시지(IAM) 또는 이메일로 테스트 메시지를 생성하고 보낼 수 있습니다.

## 테스트 메시지 보내기 {#sending-a-test-message}

### 1단계: 지정된 테스트 세그먼트 만들기 <a class="margin-fix" name="test-segment"></a> {#step-1-create-a-designated-test-segment}

테스트 세그먼트를 설정한 후에는 이를 사용하여 모든 Braze 메시징 채널을 테스트할 수 있습니다. 올바르게 설정하면 이 작업은 한 번만 수행하면 됩니다.

테스트 세그먼트를 설정하려면 **Segments**로 이동하여 새 세그먼트를 만듭니다. **Add Filter**를 선택한 다음 테스트 필터 중 하나를 선택합니다.

![타겟팅 단계에서 사용 가능한 필터를 표시하는 Braze 테스트 캠페인]({% image_buster /assets/img_archive/testmessages1.png %})

테스트 필터를 사용하면 특정 이메일 주소 또는 [외부 사용자 ID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids)를 가진 사용자에게만 테스트 메시지를 보내도록 할 수 있습니다.

![테스트라는 제목 아래에 나열된 여러 필터를 표시하는 드롭다운 메뉴]({% image_buster /assets/img_archive/testmessages2.png %})

이메일 주소와 외부 사용자 ID 필터 모두 다음과 같은 옵션을 제공합니다:

| 연산자 | 설명 |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals` | 입력한 이메일 또는 사용자 ID와 정확히 일치하는 항목을 찾습니다. 단일 이메일 또는 사용자 ID와 연결된 기기로만 테스트 캠페인을 보내려는 경우 이 옵션을 사용합니다. |
| `does not equal` | 특정 이메일 또는 사용자 ID를 테스트 캠페인에서 제외하려는 경우 이 옵션을 사용합니다. |
| `matches` | 입력한 검색어의 일부와 일치하는 이메일 주소 또는 사용자 ID를 가진 사용자를 찾습니다. 이를 사용하여 `@yourcompany.com` 주소를 가진 사용자만 찾아서 팀의 모든 사람에게 메시지를 보낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create a designated test segment a class="margin-fix" name="test-segment"/a" }

"`matches`" 옵션을 사용하고 이메일 주소를 &#124; 문자로 구분하여 여러 개의 특정 이메일을 선택할 수 있습니다. 예: "`matches`" "`email1@braze.com` &#124; `email2@braze.com`". 여러 연산자를 함께 결합할 수도 있습니다. 예를 들어 테스트 세그먼트에는 "`matches`" "`@braze.com`"인 이메일 주소 필터와 "`does not equal`" "`sales@braze.com`"인 다른 필터가 포함될 수 있습니다.

테스트 세그먼트에 테스트 필터를 추가한 후 **Preview**를 선택하거나 **Settings** > **CSV Export All User Data**를 선택하여 해당 세그먼트의 사용자 데이터를 CSV 파일로 내보내서 올바르게 작동하는지 확인할 수 있습니다.

![Segment Details라는 제목의 Braze 캠페인 섹션]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
미리보기에는 사용자의 샘플만 표시되고 모든 사용자가 포함되지 않을 수 있으므로, 세그먼트의 사용자 데이터를 CSV 파일로 내보내는 것이 가장 정확한 확인 방법입니다.
{% endalert %}

### 2단계: 메시지 보내기 {#step-2-send-the-message}

Braze 대시보드 또는 명령줄을 사용하여 메시지를 보낼 수 있습니다.

{% tabs local %}
{% tab 대시보드 사용 %}
{% subtabs %}
{% subtab 푸시 또는 인앱 메시지 %}
테스트 푸시 알림 또는 인앱 메시지를 보내려면 이전에 생성한 테스트 세그먼트를 타겟팅해야 합니다. Campaign을 생성하고 일반적인 단계를 따라 시작하세요. **Target Audiences** 단계에 도달하면 드롭다운 메뉴에서 테스트 세그먼트를 선택합니다.

![타겟팅 단계에서 사용 가능한 세그먼트를 표시하는 Braze 테스트 캠페인]({% image_buster /assets/img_archive/test_segment.png %})

Campaign을 확인하고 실행하여 푸시 알림 및 인앱 메시지를 테스트합니다.

{% alert note %}
하나의 Campaign을 사용하여 자신에게 테스트 메시지를 두 번 이상 보내려는 경우, Campaign 작성기의 **Schedule** 부분에서 **Allow users to become re-eligible to receive campaign**을 선택해야 합니다.
{% endalert %}
{% endsubtab %}

{% subtab 이메일 메시지 %}
이메일 메시지만 테스트하는 경우에는 반드시 테스트 세그먼트를 설정할 필요는 없습니다. Campaign의 이메일 메시지를 작성하는 Campaign 작성기의 첫 번째 단계에서 **Send Test**를 클릭하고 테스트 이메일을 보낼 이메일 주소를 입력합니다.

![테스트 전송 탭이 선택된 Braze 캠페인]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
테스트 메시지에 [TEST(또는 SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) 추가를 활성화하거나 비활성화할 수도 있습니다.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 명령줄 사용 %}
또는 cURL과 [Braze 메시징 API]({{site.baseurl}}/api/endpoints/messaging/)를 사용하여 단일 알림을 보낼 수도 있습니다. 이 예제에서는 `US-01` 인스턴스를 사용하여 요청합니다. 사용 중인 인스턴스를 확인하려면 [API 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요.

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

다음 항목을 교체합니다:

| 플레이스홀더 | 설명 |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY` | 인증에 사용되는 Braze API 키입니다. Braze에서 **Settings** > **API Keys**로 이동하여 키를 찾습니다. |
| `EXTERNAL_USER_ID` | 특정 사용자에게 메시지를 보내는 데 사용되는 외부 사용자 ID입니다. Braze에서 **Audience** > **Search Users**로 이동한 다음 사용자를 검색합니다. |
| `CUSTOM_KEY` | (선택 사항) 추가 데이터를 위한 커스텀 키입니다. |
| `CUSTOM_VALUE` | (선택 사항) 커스텀 키에 할당된 커스텀 값입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Send the message" }
{% endtab %}
{% endtabs %}

## 테스트 제한 사항 {#test-limitations}

테스트 메시지가 실제 사용자 집합을 대상으로 Campaign이나 Canvas를 실행하는 것과 기능적으로 완전히 동등하지 않은 몇 가지 상황이 있습니다. 이 경우 이 동작을 검증하려면 제한된 테스트 사용자 집합을 대상으로 Campaign 또는 Canvas를 실행해야 합니다.

- **테스트 메시지**에서 Braze [환경설정 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)를 보면 제출 버튼이 회색으로 표시됩니다.
- 목록 탈퇴 헤더는 테스트 메시지 기능으로 보낸 이메일에는 포함되지 않습니다.
- 인앱 메시지 및 Content Cards의 경우 타겟 사용자에게 대상 기기에 대한 푸시 토큰이 있어야 합니다.