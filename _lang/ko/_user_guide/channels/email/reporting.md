---
nav_title: 보고
article_title: 이메일 보고
page_order: 21
description: "이 참조 문서에서는 이메일 보고의 다양한 구성요소와 대시보드에서 확인할 수 있는 위치를 다룹니다."
tool:
  - Reports
channel:
  - email

---

# 이메일 보고

> 이 문서에서는 이메일 보고의 다양한 구성요소와 대시보드에서 확인할 수 있는 위치를 다룹니다.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## 문제 해결

### 반송된 이메일

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** 다른 주소를 시도하거나, 다른 채널을 통해 다시 참여를 유도하거나, 본인의 테스트 주소에 한해서만 억제 목록에서 해당 주소를 제거하세요. 실제 사용자 억제를 제거하면 발신 평판에 악영향을 줄 수 있으므로 피하세요.
- **Mailbox full / invalid account:** 주로 목록 품질 관련 신호입니다. 최근에 열람하거나 클릭한 사용자(예: 최근 30~60일)를 우선시하면서 비활성 또는 잘못된 주소를 정리하세요.

### 유효하지 않은 도메인

`unable to get mx info`와 같은 오류는 많은 타겟이 잘못된 도메인(예: 오타)을 사용하고 있음을 의미하는 경우가 많습니다. 해당 프로필을 세그먼트로 분류하고, 내보내기한 후 수정하여 다시 가져오기하세요.

### 제한된 IP

수신자 서버가 IP를 제한하는 경우, 해당 도메인으로의 발송량을 줄이고 참여도를 개선하세요. 제한이 지속되면 전달 가능성 고객지원팀에 문의하세요.