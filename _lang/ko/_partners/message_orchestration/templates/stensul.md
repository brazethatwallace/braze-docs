---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "이 참고 문서에서는 여러 채널에서 모바일 반응형 이메일 템플릿을 생성하는 기업용 이메일 플랫폼인 Braze와 Stensul의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/)은 이메일 마케터가 모바일 반응형 온브랜드 이메일을 Stensul에서 구축한 후 Campaign 생성을 위해 실시간으로 Braze로 전송할 수 있는 도구를 제공합니다.

_이 통합은 Stensul에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Stensul 통합을 사용하면 HTML 형식의 Stensul 이메일을 내보내고 Braze 내에서 템플릿으로 업로드할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ------------| ----------- |
| Stensul 계정 | 이 파트너십을 이용하려면 Stensul 계정이 필요합니다. |
| Braze REST API 키 | 전체 **Templates** 권한이 있는 Braze REST API 키. <br><br> 이 키는 Braze 대시보드의 **Settings** > **API Keys**에서 생성할 수 있습니다. |
| 클러스터 인스턴스 | Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트와 일치합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Braze REST API 키와 클러스터 인스턴스를 Stensul 고객 성공 팀에 제공하세요. 팀에서 초기 통합을 설정해 드립니다.

{% alert important %}
이 설정은 일회성이며, 이후의 모든 내보내기에서 이 API 키가 자동으로 사용됩니다.
{% endalert %}

### 1단계: Stensul 이메일 생성 {#step-1-create-stensul-email}

Stensul 플랫폼에서 Stensul 이메일을 생성하고 **Complete**를 클릭합니다.

![Stensul Save Options]({% image_buster /assets/img_archive/stensul_save_options.png %})

### 2단계: Braze로 템플릿 내보내기 {#step-2-export-template-to-braze}
완료 페이지에 나타나는 새 대화 상자에서 **Upload to ESP**를 선택합니다.

![Stensul Upload Options]({% image_buster /assets/img_archive/stensul_upload_options.png %})

다음으로, 이메일의 **template name**, **subject**, **preheader**를 입력하고 **Upload**을 선택합니다. 업로드가 성공했다는 확인 메시지와 해당 파일의 이전 업로드 기록(해당하는 경우)이 표시됩니다.

![Stensul Upload Success]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 사용법 {#usage}

Braze 계정의 **Templates & Media > Email Templates** 섹션에서 업로드한 Stensul 템플릿을 찾으세요. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 발송할 수 있습니다!