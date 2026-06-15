---
nav_title: 9월
page_order: 5
noindex: true
page_type: update
description: "이 문서에는 2018년 9월의 릴리스 노트가 포함되어 있습니다."
---
# 2018년 9월 {#september-2018}

## iOS 12 알림 그룹: 추가 기능 {#ios-12-notification-groups-additional-abilities}

이제 Braze를 사용하여 [Apple의 알림 그룹 기능]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)에 액세스할 수 있습니다! 요약 인수 및 그룹을 추가하고, 중요 경고를 활용하고, 임시 인증된 사용자를 필터링하고, 고객 프로필에서 임시 인증 상태를 확인할 수 있습니다.

## 방해금지 시간 {#quiet-time}

고객은 이제 Canvas에 대해 [방해금지 시간]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings)(메시지가 전송되지 않는 시간)을 지정할 수 있습니다. **Canvas 발송 설정**으로 이동하여 "방해금지 시간 활성화"를 선택하세요. 그런 다음 사용자의 현지 시간에 맞춰 방해금지 시간을 선택하고, 메시지가 해당 방해금지 시간 내에 트리거될 경우 어떤 동작이 수행될지 선택합니다.

Campaigns에서도 이제 "하루 중 특정 시간에 이 메시지를 보내기" 대신 방해금지 시간을 사용합니다.

## Adjust 고객 {#adjust-customers}

[Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)를 사용하는 Braze 고객은 이제 Braze API 키와 Braze 인스턴스 URL을 확인할 수 있으며, 이를 Adjust 플랫폼에서 통합하는 데 사용할 수 있습니다.

## Segment 미포함 필터 {#not-in-segment-filter}

고객은 이제 [특정 Segment에 포함되지 않은]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) 사용자로 Segment를 생성할 수 있습니다.

## Canvas 수신자 CSV 내보내기 {#canvas-recipient-csv-exports}

고객은 이제 Canvas에 진입한 사용자에 대한 [데이터를 내보낼]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/) 수 있습니다. 생성된 CSV는 Campaign CSV와 유사합니다.

## 임시 인증된 iOS 12 Segment 필터 {#provisionally-authorized-ios-12-segment-filter}

iOS 12에서 특정 앱에 대해 임시 인증된 사용자를 찾을 수 있는 [Segment 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other)가 추가되었습니다.

## 인앱 메시지 이미지 업로더 {#in-app-message-image-uploader}

인앱 메시지용 이미지 업로더가 디자인 패널에서 작성 패널로 이동했습니다.

## 고객 프로필 페이지의 읽기 전용 권한 {#read-only-permissions-on-user-profile-page}

이 릴리스 이전에는 고객이 [읽기 전용 권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)으로 고객 프로필에서 구독 상태 및 이메일 주소를 변경할 수 있었습니다. `import_user` 권한의 이름이 `import_and_update_user` 권한으로 변경되었으며, 구독 상태 및 이메일 주소에 대한 편집 액세스가 제한되었습니다. 이제 개발자가 읽기 전용으로 가장하거나 이 권한이 없는 경우 구독 상태나 이메일 주소를 변경할 수 없습니다.