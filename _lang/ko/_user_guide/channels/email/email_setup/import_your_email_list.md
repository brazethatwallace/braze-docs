---
nav_title: 이메일 목록 가져오기
article_title: 이메일 목록을 Braze로 가져오기
page_order: 4
page_type: reference
description: "이 참고 문서에서는 이메일 목록을 Braze로 가져오는 모범 사례를 다룹니다."
channel: email

---

# 이메일 목록을 Braze로 가져오기 {#importing-email-lists}

> 성공적인 이메일 발신자로 자리매김하기 위한 중요한 단계는 양질의 이메일 목록을 확보하는 것입니다. 적절한 이메일 목록 관리를 통해 전달 가능성을 높이고 보다 정확하고 깔끔한 Campaign 결과를 얻을 수 있습니다.

## 가져오기 전 고려 사항 {#considerations-before-importing}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 이메일 목록 유효성 검사 {#validate-your-email-lists}

이메일 목록을 Braze로 가져오기 전에 목록에 진짜 이메일 주소만 포함되어 있는지 확인하세요. 반송률이 높으면 이메일 발신자 평판이 손상될 수 있습니다.

이메일 목록 정리 서비스는 이메일 주소가 올바른 구문을 따르고 이메일 주소의 물리적 특성을 가지고 있는지 확인하고, 이메일 도메인을 검증하며, 이메일 서버에 연결하여 이메일 주소가 존재하는지 인증하는 작업을 대신 수행할 수 있습니다.

### 이메일 주소가 이미 사용자와 연결되어 있는지 확인 {#check-if-an-email-address-is-already-associated-with-a-user}

API 또는 SDK를 통해 사용자를 생성하기 전에 [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 엔드포인트를 호출하고 사용자의 `email_address`를 지정하세요. 고객 프로필이 반환되면 해당 Braze 사용자는 이미 해당 이메일 주소와 연결되어 있는 것입니다.

새 사용자를 생성할 때는 고유한 이메일 주소를 확인하고, 동일한 이메일 주소를 가진 사용자를 전달하거나 가져오지 않는 것을 강력히 권장합니다. 그렇지 않으면 메시지 발송, 타겟팅, 보고서 및 기타 기능에 의도하지 않은 결과가 발생할 수 있습니다.

예를 들어 프로필이 중복되어 있지만 특정 커스텀 속성이나 이벤트가 하나의 프로필에만 존재한다고 가정해 보겠습니다. 여러 기준으로 Campaigns이나 Canvases를 트리거하려고 할 때, 두 개의 사용자 프로필이 있기 때문에 Braze가 해당 사용자를 적격 대상으로 식별할 수 없습니다. 또는 Campaign이 두 명의 사용자가 공유하는 이메일 주소를 타겟으로 하는 경우, **사용자 검색** 페이지에서 두 사용자 프로필 모두 Campaign을 수신한 것으로 표시됩니다.

### 참여도가 높은 사용자 식별 {#identify-your-engaged-users}

가장 참여도가 높은 사용자를 식별하려면 먼저 장기 휴면 사용자를 제거하세요. 6개월 이상 이메일에 참여하지 않은 사용자에게 이메일을 보내면 이메일 발신자 평판이 손상될 수 있으므로 이메일을 보내지 않는 것이 좋습니다. 이메일 목록을 가져올 때는 지난 6개월 이내에 이메일을 열어본 사용자만 포함하세요.

장기적으로는 [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies)을 구현하는 것도 고려해야 합니다.

### 억제 목록 가져오기 방지 {#avoid-suppression-lists}

기존 이메일 제공업체에서 전환하는 경우 억제 목록에 있는 사용자를 가져오지 않도록 주의하세요. 억제 목록에는 탈퇴했거나, 이메일을 스팸으로 표시했거나, 하드바운스된 이메일 주소가 포함되어 있습니다.

## 가져오기 방법 {#methods-for-importing}

이메일 목록이 준비되면 Braze REST API 또는 CSV 파일 등 여러 가지 방법으로 사용자를 Braze로 가져올 수 있습니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) 문서를 참조하세요.