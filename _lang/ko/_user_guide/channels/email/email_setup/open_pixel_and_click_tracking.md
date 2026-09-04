---
nav_title: 오픈 픽셀 및 클릭 추적
article_title: 이메일 오픈 픽셀 및 클릭 추적
page_order: 9
page_type: reference
description: "이 참조 문서에서는 오픈 픽셀 및 클릭 추적을 구현하는 방법을 다룹니다."

---

# 이메일 오픈 픽셀 및 클릭 추적 {#email-open-pixel-and-click-tracking}

> [오픈 픽셀 추적]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement) 및 클릭 추적은 각 고객 프로필별로 켜거나 끌 수 있습니다. 이러한 유연성은 개별 고객 프로필이 더 이상 추적을 원하지 않는다고 표시한 경우 지역 개인정보 보호법을 준수하는 데 도움이 됩니다.

## 열람 픽셀 또는 클릭 추적 기술 활성화 {#turning-on-open-pixel-or-click-tracking}

[API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv), 또는 [클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해 고객 프로필을 가져오거나 업데이트할 때, 수정할 수 있는 두 가지 필드가 있습니다.

- `email_open_tracking_disabled`: `true` 또는 `false`를 허용합니다. `false`로 설정하면 이 사용자에게 발송되는 모든 향후 이메일에 열람 추적 픽셀이 추가됩니다.
- `email_click_tracking_disabled`: `true` 또는 `false`를 허용합니다. `false`로 설정하면 이 사용자에게 발송되는 향후 이메일 내 모든 링크에 클릭 추적 기술이 추가됩니다.

참고로, 이 정보는 고객 프로필의 **인게이지먼트** 탭에 있는 이메일 **연락처 설정**에 반영됩니다.

![사용자 프로필의 인게이지먼트 탭에 있는 이메일 열람 및 클릭 추적 픽셀 필드]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## 클릭 추적 기술 링크 요구 사항 {#click-tracking-link-requirements}

Braze 클릭 추적 기술은 `http://` 또는 `https://` URL을 사용하는 링크만 재작성합니다. `mailto:` 또는 `tel:`과 같은 다른 스킴을 사용하는 링크는 클릭 추적이 되지 않습니다.

전화번호나 이메일 주소의 클릭을 추적하려면 `tel:` 또는 `mailto:` 대상으로 전달되는 `https://` 리디렉트 URL을 대신 사용하세요.

### 클릭 추적 기술 URL 패턴 {#click-tracking-url-patterns}

이메일 서비스 공급자(ESP)가 클릭 추적 기술을 위해 링크를 재작성하면, 결과 URL에는 클릭 추적 기술 도메인과 ESP별 경로 접두사가 사용됩니다. 방화벽 규칙 및 보안 허용 목록에 필요한 각 ESP가 생성하는 패턴은 [클릭 및 열람 추적 기술 URL 패턴]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#click-and-open-tracking-url-patterns)을 참조하세요.