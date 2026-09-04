---
nav_title: Amazon SES 설정
article_title: Amazon SES 설정
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Amazon SES를 이메일 서비스 제공업체로 설정하는 방법을 다룹니다."
channel: email
---

# Amazon SES 설정 {#amazon-ses-setup}

> Braze는 새 이메일 설정 시 기본 이메일 서비스 제공업체로 Amazon Simple Email Service(SES)를 사용합니다. 필요한 설정이 Amazon SES의 기능과 맞지 않는 경우, Braze 고객지원에 연락하여 SparkPost 또는 SendGrid에서 설정을 완료하는 옵션을 문의하세요.

## 사전 요구 사항 {#prerequisites}

Amazon SES 설정을 시작하기 전에 다음 사항을 확인하세요:

- 발신 도메인 이름
- IP 풀 이름(예: 마케팅, 트랜잭션, 스테이징)
- 각 IP 풀의 IP 주소 수
- 클릭 추적 도메인에 사용할 선호 접미사(예: "clicks" 또는 "click", "links" 또는 "link")

## 설정 예시 {#setup-example}

일반적인 Amazon SES 설정은 다음과 같습니다.

- **하위 계정 이름:** braze
- **클러스터:** eu-02

| IP 풀 | IP 수 | 구성 세트 | 발신 도메인 | 클릭 추적 도메인 |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="설정 예시" }

{% alert note %}
클러스터 및 하위 계정 이름은 IP 풀과 구성 세트에 자동으로 추가됩니다.
{% endalert %}

## 클릭 추적 도메인 구성 예시 {#click-tracking-domain-configuration-examples}

다음 표는 브랜딩 선호도에 따라 가능한 클릭 추적 도메인 구성의 예시입니다.

### 각 발송 도메인에 대해 하나의 클릭 추적 도메인 사용 {#one-click-tracking-domain-for-each-sending-domain}

| 마케팅 IP 풀 | 구성 세트 | 발송 서브도메인 | 클릭 추적 도메인 |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="각 발송 도메인에 대해 하나의 클릭 추적 도메인 사용" }

### 모든 발송 도메인에 대해 하나의 클릭 추적 도메인 사용 {#one-click-tracking-domain-for-all-sending-domains}

이 구성은 클릭 추적 도메인이 구성 세트에 포함된 발송 도메인 중 하나 이상과 일치해야 한다는 규칙을 기반으로 합니다.

| 마케팅 IP 풀 | 구성 세트 | 발송 서브도메인 | 클릭 추적 도메인 |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="모든 발송 도메인에 대해 하나의 클릭 추적 도메인 사용" }

## 고려 사항 {#considerations}

- Amazon SES의 IP 풀은 IP 주소 자체만 호스팅하며, 구성 세트는 발신 도메인과 클릭 추적 도메인을 호스팅합니다.
- 각 구성 세트에는 한 번에 하나의 IP 풀만 할당할 수 있지만, 동일한 IP 풀을 사용하면서 서로 다른 발신 도메인을 가진 여러 구성 세트를 생성할 수 있습니다.
- Amazon SES는 받은편지함 제공업체와 긴밀한 관계를 유지하여 IP 주소를 인식할 수 있도록 rDNS 및 A 레코드를 내부적으로 처리합니다.
- 각 발신 도메인에는 SPF 검증을 지원하기 위한 MAIL FROM 식별자가 연결되어 있습니다.
    - 각 발신 도메인의 값은 "e"입니다.
    - MAIL FROM 값은 고객에게 표시되는 발신(From) 주소를 변경하지 않습니다.
- Amazon SES를 이메일 서비스 공급자로 사용하는 경우, 트랩 메시지 기간 시작과 트랩 메시지 기간 종료는 사용할 수 없습니다.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: SSL 설정
  link: /docs/user_guide/channels/email/email_setup/ssl
{% endarticle_tiles %}