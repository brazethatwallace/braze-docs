---
nav_title: Segment 데이터
article_title: Segment 데이터 내보내기
page_order: 4
page_type: reference
description: "이 참조 문서에서는 Segment 데이터를 CSV로 내보내는 방법, 필요한 사용자 데이터 내보내기 권한, 캔버스 단계 내보내기, 내보내기에 포함되는 필드에 대해 설명합니다."
---

# Segment 데이터를 CSV로 내보내기 {#export-segment-data-to-csv}

> 이 페이지에서는 Segment에서 사용자 데이터의 CSV 내보내기를 요청하는 방법과 내보내기에 포함된 데이터에 대해 설명합니다.

{% alert note %}
CSV 내보내기 옵션은 해당 워크스페이스에 대해 ["사용자 데이터 내보내기" 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있는 회사 사용자에게만 **사용자 데이터** 드롭다운에 표시됩니다.
{% endalert %}

Segment 데이터를 CSV로 내보내려면 Segment를 편집하는 동안 **사용자 데이터** 드롭다운을 선택하고 Segment의 사용자 데이터 또는 이메일 주소 중 하나를 선택하여 내보냅니다.

![내보내기 옵션이 표시된 사용자 데이터 드롭다운이 있는 Segment 세부 정보 섹션.]({% image_buster /assets/img_archive/csvexport.png %})

메인 **Segments** 페이지에서 Segment의 <i class="fas fa-gear" aria-label="설정"></i> **설정** 드롭다운을 선택하여 CSV 내보내기를 요청할 수도 있습니다.

![메인 Segments 페이지의 설정 드롭다운.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
모든 고객 프로필에서 데이터를 내보내려면 필터가 없는 Segment를 생성한 다음 CSV 내보내기를 요청하세요.
{% endalert %}

CSV 출력에는 내보내기 시점에 Segment에서 캡처된 각 고객 프로필의 데이터가 포함되어 있습니다. 기어 아이콘과 CSV 내보내기를 선택하여 모든 Segment를 내보낼 수 있습니다. Braze는 보고서를 백그라운드에서 생성하고 현재 로그인한 사용자에게 이메일로 전송합니다.

## Segment CSV 내보내기 세부 정보 {#segment-csv-export-details}

{% alert note %}
대시보드 사용자가 CSV 내보내기 옵션을 사용하려면 **Export user data** 권한이 필요합니다. 이 권한이 없으면 CSV 내보내기 옵션이 표시되지 않습니다.
{% endalert %}

**CSV Export Email Addresses**는 Segment 내에서 이메일 주소가 있는 사용자의 행만 포함합니다. 예를 들어, Segment에 100,000명의 사용자가 있지만 그 중 50,000명만 이메일 주소를 가지고 있다면, **CSV Export Email Addresses**는 약 50,000개의 행을 생성합니다. **CSV Export User Data**는 해당 Segment의 모든 사용자 데이터를 내보냅니다.

{% alert important %}
파일 크기 제한으로 인해 Segment의 예상 크기가 500,000명을 초과하면 내보내기가 실패할 수 있습니다. 이 제한은 정확한 계산이 아닌 Segment의 예상 크기를 기준으로 합니다. 자세한 내용은 [대규모 Segment 내보내기](#exporting-large-segments)를 참조하세요.
{% endalert %}

[Amazon S3 인증정보]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration)를 Braze에 연결한 경우, CSV는 대신 S3 버킷의 `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` 키 아래에 업로드됩니다. 이메일로 전송된 다운로드 링크에 접근하려면 대시보드에 로그인되어 있어야 합니다.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## 내보내기에 포함되는 데이터 {#data-included-in-export}

선택 항목에 따라 내보내기에 다음이 포함됩니다.

### CSV 내보내기 사용자 데이터 {#csv-export-user-data}

| 필드 이름                   | 설명                                                     |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | 내부 ID(변경 불가)                                        |
| country                     | 국가                                                     |
| created_at                  | 고객 프로필이 생성된 날짜 및 시간                         |
| created_from                | 고객 프로필을 생성하는 데 사용된 메서드(예: REST API, SDK 또는 CSV 가져오기) |
| devices                     | 기기 정보                                                |
| date_of_birth               | 생년월일                                                 |
| email                       | 이메일 주소                                              |
| unsubscribed_from_emails_at | 이메일 탈퇴 날짜                                         |
| user_id                     | 외부 ID                                                  |
| first_name                  | 이름                                                     |
| first_session               | 첫 번째 세션 날짜 및 시간                                |
| gender                      | 성별                                                     |
| google_ad_ids               | 사용자에게 연결된 Google 광고 ID                         |
| city                        | 구/군/시                                                 |
| IDFAs                       | 광고 식별자(IDFA) 값                                     |
| IDFVs                       | 공급업체 식별자(IDFV) 값                                 |
| language                    | ISO-639-1 표준 언어                                      |
| last_app_version_used       | 마지막으로 사용한 앱 버전                                |
| last_name                   | 성                                                       |
| last_session                | 마지막 세션 날짜 및 시간                                 |
| number_of_google_ad_ids     | 연결된 Google 광고 ID 수                                 |
| number_of_IDFAs             | 연결된 IDFA 수                                           |
| number_of_IDFVs             | 연결된 IDFV 수                                           |
| number_of_push_tokens       | 연결된 푸시 알림 토큰 수                                 |
| number_of_roku_ad_ids       | 연결된 Roku 광고 ID 수                                   |
| number_of_windows_ad_ids    | 연결된 Windows 광고 ID 수                                |
| phone_number                | 전화번호                                                 |
| opted_into_push_at          | 푸시 알림 옵트인 날짜                                    |
| unsubscribed_from_push_at   | 푸시 알림 탈퇴 날짜                                      |
| random_bucket               | 무작위 버킷 번호                                         |
| roku_ad_ids                 | Roku 광고 ID                                             |
| session_count               | 총 세션 수                                               |
| timezone                    | IANA 시간대 데이터베이스와 동일한 형식의 사용자 시간대   |
| in_app_purchase_total       | 인앱 구매에 지출한 총 금액                               |
| user_aliases                | 사용자 별칭(있는 경우)                                   |
| windows_ad_ids              | Windows 광고 ID                                          |
| Custom events               | 내보내기 시 선택 항목에 따라 결정                        |
| Custom attributes           | 내보내기 시 선택 항목에 따라 결정                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV 내보내기 사용자 데이터" }

{% alert note %}
캔버스 단계에서 사용자 데이터를 내보내면 CSV에는 해당 캔버스 단계의 전체 수명 동안 해당 단계에 포함된 모든 사용자가 포함됩니다. 날짜 범위나 기타 시간 범위로 내보내기를 제한할 수 없습니다. 이러한 내보내기를 실행하는 방법은 [Canvas 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)를 참조하세요.
{% endalert %}

### CSV 내보내기 이메일 주소 {#csv-export-email-addresses}

| 필드 이름                   | 설명                  |
| --------------------------- | --------------------- |
| user_id                     | 사용자의 외부 ID      |
| first_name                  | 이름                  |
| last_name                   | 성                    |
| email                       | 이메일                |
| unsubscribed_from_emails_at | 이메일 탈퇴 날짜      |
| opted_in_to_emails_at       | 이메일 옵트인 날짜    |
| user_aliases                | 사용자 별칭(있는 경우)|
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV 내보내기 이메일 주소" }

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting) 문서를 참조하세요.
{% endalert %}

{% alert note %}
구독 그룹 데이터는 Segment 내보내기를 통해 사용할 수 없습니다. 구독 상태별로 사용자를 식별하려면 구독 그룹 멤버십을 기반으로 별도의 Segment를 만들고 해당 Segment를 내보내세요.
{% endalert %}

## 대규모 Segments 내보내기 {#exporting-large-segments}

500,000명 이상의 사용자를 포함하는 대규모 사용자 Segment를 내보내는 방법에는 여러 가지가 있습니다.

{% tabs %}
{% tab 여러 Segments %}

대규모 Segment를 더 작은 Segments로 분할한 다음 각각의 작은 Segments를 Braze에서 내보낼 수 있습니다.

{% endtab %}
{% tab 무작위 버킷 번호 %}

[무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)를 사용하여 사용자 기반을 여러 Segments로 나눈 다음, 내보내기 후 결합할 수도 있습니다. 예를 들어, Segment를 두 개의 서로 다른 Segments로 나누어야 하는 경우 다음 필터를 사용할 수 있습니다:
- Segment 1: 무작위 버킷 번호가 5000 미만 (0-4999 포함)
- Segment 2: 무작위 버킷 번호가 4999 초과 (5000-9999 포함)

{% endtab %}
{% tab 엔드포인트 %}

다음 엔드포인트를 활용하여 특정 Segment에 대한 사용자 데이터를 내보낼 수도 있습니다. 이러한 엔드포인트에는 데이터 제한 및 [사용량 제한]({{site.baseurl}}/api/basics)이 적용됩니다.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

[Amazon S3 인증정보]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration)를 연결한 경우, [Segment CSV 내보내기 세부 정보](#segment-csv-export-details)에 설명된 대로 이메일 다운로드 링크 외에도 대규모 내보내기를 버킷으로 전달할 수 있습니다.

{% endtab %}
{% endtabs %}