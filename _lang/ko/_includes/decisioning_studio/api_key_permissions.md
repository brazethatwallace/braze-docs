| 권한 | 목적 | 필수 여부 |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | 고객 프로필의 커스텀 속성을 업데이트하며, 테스트 전송 시 임시 고객 프로필을 생성합니다. | &#10003; |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | 테스트 전송을 사용하는 동안 생성된 임시 고객 프로필을 삭제합니다. | 테스트 전송 전용 |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | 선택한 각 Segment에서 사용자 목록을 내보내 매일 아침 사용 가능한 오디언스 커뮤니케이션을 업데이트합니다. | &#10003; |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Segment 대신 `external_id`를 사용하여 사용자를 타겟팅할 때 식별자 목록을 검색합니다. Decisioning Studio는 개인 식별 정보(PII)를 허용하지 않으므로, `fields_to_export` 매개변수가 비PII 필드만 반환하도록 해야 합니다. | `external_ids`를 사용하는 경우에만 |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Decisioning Studio의 실험자에 맞게 구성된 API Campaigns를 사용하여 추천된 시간에 추천된 배리언트를 전송합니다. | &#10003; |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns#prerequisites) | 활성 Campaigns 목록을 검색하고 실험용으로 사용 가능한 이메일 콘텐츠를 추출합니다. | &#10003; |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 집계된 Campaign 데이터를 내보내 Decisioning Studio에서 보고, 검증 및 문제 해결을 수행할 수 있도록 하여 보고 값을 비교하고 기준 성능을 분석할 수 있습니다.<br><br>필수는 아니지만 권장되는 권한입니다. |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 실험을 위해 기존 Campaigns에서 HTML 콘텐츠, 제목란 및 이미지 리소스를 검색합니다. | &#10003; |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | 활성 Canvases 목록을 검색하여 실험에 사용할 수 있는 이메일 콘텐츠를 추출합니다. | &#10003; |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 특히 BAU가 Canvas를 통해 오케스트레이션되는 경우, 보고 및 검증을 위해 집계된 Canvas 데이터를 내보냅니다.<br><br>필수는 아니지만 권장되는 권한입니다. |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details#prerequisites) | 실험을 위해 기존 Canvases에서 HTML 콘텐츠, 제목란 및 이미지 리소스를 검색합니다. | &#10003; |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Decisioning Studio 실험자를 위한 잠재적 타겟 오디언스로서 모든 기존 Segments를 검색합니다. | &#10003; |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 오디언스를 선택할 때 Decisioning Studio에 표시되는 Segment 크기 정보를 내보냅니다. | &#10003; |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details#prerequisites) | 오디언스 규모 또는 성능 변화를 이해하는 데 도움이 되는 진입 및 퇴장 기준과 같은 Segment 세부 정보를 검색합니다. |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | 원본을 변경하지 않으면서, [동적 입력 안내]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)(Braze Liquid 태그)를 사용하여 실험을 위해 선택한 기본 HTML 템플릿의 복사본을 생성합니다. | &#10003; |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | 행동 유도(call-to-action) 등 실험 기준이 변경될 때 Decisioning Studio에서 생성된 템플릿 복사본에 업데이트를 푸시합니다. | &#10003; |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information#prerequisites) | Braze 인스턴스에서 Decisioning Studio가 생성한 템플릿에 대한 정보를 검색합니다. | &#10003; |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 템플릿이 Braze 인스턴스에 성공적으로 복사되었는지 확인합니다. | &#10003; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="테이블" }