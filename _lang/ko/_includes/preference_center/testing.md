## 환경설정 센터 테스트 {#testing-preference-centers}

환경설정 센터 링크는 발송 시점에 각 사용자별로 생성되며, 실시간 Campaign 또는 Canvas 발송에 연결됩니다. 테스트 발송 및 에디터 미리보기에서는 구독 변경 사항 저장이 지원되지 않습니다. 이는 의도된 동작입니다.

### 표시되는 내용 {#what-youll-see}

- **테스트 발송:** 환경설정 센터 Liquid 태그가 유효한 링크로 변환되지 않을 수 있습니다. 페이지가 로드되더라도 **환경설정 저장** 버튼이 비활성화되어 있으며, 구독 변경 사항이 저장되지 않습니다.
- **드래그 앤 드롭 에디터 미리보기 탭:** 레이아웃과 스타일링을 미리 볼 수 있지만, 에디터에서 환경설정 저장을 테스트할 수는 없습니다.

### 포괄적인 테스트 방법 {#how-to-test-end-to-end}

전체 발송 전에 환경설정 센터 링크와 버튼이 올바르게 작동하는지 확인하려면 다음 단계를 따르세요.

1. 환경설정 센터 Liquid 태그가 포함된 Campaign 또는 Canvas 이메일 단계를 생성합니다.
2. 테스트 사용자 또는 소규모 내부 Segment만 타겟팅합니다.
3. 메시지를 발송하고 실제 받은편지함에서 이메일을 엽니다(**테스트 전송**이 아닌 실제 수신).
4. 환경설정 센터 링크를 선택하고, 구독 그룹을 업데이트한 다음 **환경설정 저장**을 선택합니다.
5. Braze 대시보드에서 해당 사용자의 프로필에 변경 사항이 반영되었는지 확인합니다.

{% if include.section == "api" %}
API로 구축한 환경설정 센터의 경우, [환경설정 센터 URL 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)를 사용하여 테스트 발송 외부에서 특정 사용자에 대한 작동 가능한 URL을 가져올 수 있습니다.
{% endif %}

기타 테스트 발송 제한 사항은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations)를 참조하세요.

### 미리보기, 테스트 발송 및 실시간 발송 {#preview-test-send-and-live-send}

| 방법 | 레이아웃 미리보기 | 구독 변경 사항 저장 |
| --- | --- | --- |
| 드래그 앤 드롭 에디터 **미리보기** 탭 | 예 | 아니요 |
| Campaign 또는 Canvas **테스트 전송** | 부분적 (이메일 수신됨) | 아니요 |
| 테스트 사용자 또는 Segment에 실시간 발송 | 예 | 예 |
| [환경설정 센터 URL 생성]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) API | 예 | 예 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="미리보기, 테스트 발송 및 실시간 발송" }