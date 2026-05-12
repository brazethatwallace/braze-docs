---
nav_title: "Playable"
article_title: "Playable"
description: "이 참조 문서에서는 Braze 이메일 Campaigns에 비디오 콘텐츠를 추가할 수 있는 비디오 플랫폼인 Playable과 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/playable/
page_type: partner
search_tag: Partner

---

# Playable

> [Playable](https://playable.video)을 사용하면 Braze 이메일 Campaigns에 자동 재생 비디오 콘텐츠를 추가할 수 있습니다.

_이 통합은 Playable에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Playable 통합을 사용하면 최고의 콘텐츠(고품질 비디오)를 최고의 오디언스(이메일)에게 전달하여 받은편지함에서 자동으로 재생되는 흥미로운 고품질 콘텐츠로 클릭률 및 클릭 후 측정기준을 높일 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Playable 계정 | 이 파트너십을 활용하려면 Playable 계정이 필요합니다. 아직 Playable 계정이 없다면 [여기](https://signup.playable.video)에서 가입하세요.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }
| 비디오 콘텐츠 | Playable에 비디오 파일을 업로드하거나 Facebook, Instagram, YouTube, X(구 Twitter), TikTok 등의 웹사이트에서 비디오 URL을 제공하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 구현 {#implementation}

### 1단계: Playable에 비디오 추가 {#step-1-add-your-video-to-playable}

Playable 플랫폼에서 비디오 파일을 업로드하거나 Facebook, Instagram, YouTube, X(구 Twitter), TikTok 등에서 비디오 URL을 제공하여 비디오를 추가합니다.

### 2단계: Playable에서 임베드 코드 복사 {#step-2-copy-the-embed-code-from-playable}

업로드가 완료되면 Playable에서 코드를 생성합니다. 이 코드를 Braze Campaign에 삽입하면 이메일을 열 때 비디오가 자동으로 재생되도록 임베드됩니다. 이메일이 열리면 Playable 서버가 이메일 클라이언트, 기기, 화면 크기 및 네트워크 조건에 따라 최적의 비디오 버전을 전달합니다.

{% alert tip %}
비디오는 iPhone Mail, Gmail, Apple Mail, Outlook for iOS, Outlook for Android, Outlook for Mac, 최신 버전의 Outlook 365 for Windows를 포함하여 98% 이상의 받은편지함에서 자동 재생됩니다. 레거시 Outlook for Windows 사용자에게는 정적 이미지가 대신 표시됩니다.
{% endalert %}

### 3단계: Braze에 임베드 코드 붙여넣기 {#step-3-paste-the-embed-code-into-braze}

마지막으로 Braze 이메일 Campaign에 코드를 붙여넣은 다음 이메일 Campaign을 계속 디자인하고 테스트하고 게시합니다.