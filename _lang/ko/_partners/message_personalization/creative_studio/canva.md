---
nav_title: Canva
article_title: Canva
description: "이 참조 문서에서는 Braze와 Canva 간의 파트너십을 설명하며, 미디어 자산을 Braze 미디어 라이브러리로 푸시하고 Canva 이메일 디자인을 Braze 이메일 템플릿으로 게시하는 방법을 다룹니다."
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> [Canva](https://www.canva.com/)는 소셜 미디어 게시물, 프레젠테이션, 동영상 등을 위한 시각적 콘텐츠를 만들 수 있는 그래픽 디자인 플랫폼 및 도구입니다. Canva의 Braze 앱은 정적 디자인을 미디어 라이브러리로 전송하는 것 외에도 **이메일** 디자인을 Braze 이메일 템플릿으로 내보내는 기능을 지원합니다.

## 통합 소개 {#about-the-integration}

Braze와 Canva 통합은 두 가지 내보내기 경로를 지원합니다.

| 내보내기 유형 | 기능 |
| --- | --- |
| **이미지 또는 디자인을 미디어 라이브러리로** | 디자인을 자산으로 Braze 미디어 라이브러리에 전송합니다. |
| **이메일 디자인을 Braze로** | Canva **이메일** 문서를 제목란 메타데이터를 포함하여 Braze 이메일 템플릿으로 게시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="통합 소개" }

## Braze와 Canva 통합하기 {#integrate-braze-with-canva}

### 1단계: Canva에 Braze 앱 설치하기 {#step-1-install-the-braze-app-in-canva}

Braze 앱은 [Canva 앱 마켓플레이스](https://www.canva.com/your-apps/AAG1cO7kIyc)에서 찾을 수 있습니다.

앱을 설치하면 디자인 내 **Apps** 메뉴에서 사용할 수 있습니다.

![Canva Apps 메뉴의 Braze 앱.]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### 2단계: Braze 계정 인증하기 {#step-2-authorize-your-braze-account}

Braze 앱을 처음 사용할 때—**Apps** 메뉴(미디어 라이브러리 내보내기)에서 열든 **Share** 메뉴(이메일 내보내기)에서 열든—**Connect**를 선택하여 인증을 시작합니다. 이를 통해 Canva가 접근 가능한 Braze 워크스페이스를 나열하고 사용자를 대신하여 미디어 라이브러리 자산을 생성할 수 있습니다.

**이메일** 내보내기의 경우, Canva에서 다시 로그인하고 **이메일 템플릿 생성** 권한을 포함한 추가 접근 권한을 승인하도록 요청할 수 있습니다. 해당 권한을 수락하면 이메일 디자인을 Braze에 게시할 수 있습니다.

![Canva를 Braze에 연결하기 위한 Connect 버튼 및 인증 흐름.]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## 미디어 라이브러리로 이미지 내보내기 {#export-images-to-the-media-library}

Braze 미디어 라이브러리에 파일을 저장하려는 표준 Canva 디자인에 이 흐름을 사용합니다.

1. 디자인의 **Apps** 메뉴에서 Braze 앱을 엽니다. 아직 연결되지 않은 경우 **Connect**를 선택하고 [Braze 계정 인증하기](#step-2-authorize-your-braze-account)의 단계를 완료합니다.
2. 대상 워크스페이스를 선택하고, 필요에 따라 파일 이름을 입력한 후 **Start Export**를 선택합니다.

![대상 워크스페이스와 Start Export 버튼이 있는 Canva 내보내기 화면.]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. 내보내기가 완료되면 새 자산이 **미디어 라이브러리**에서 소스가 "Canva"로 표시되어 사용할 수 있습니다.

![Braze 미디어 라이브러리에 내보내진 Canva 자산.]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## 이메일 디자인을 Braze 템플릿으로 내보내기 {#export-email-designs-as-braze-templates}

Canva 파일이 **이메일** 디자인 유형인 경우 이 흐름을 사용합니다. HTML을 Braze에 템플릿으로 게시합니다(이미지 흐름과 유사한 메타데이터이지만, **Apps** 대신 **Share**에서 시작합니다).

1. Canva에서 **이메일** 디자인을 만들거나 엽니다. 처음부터 메시지를 작성하거나 Canva 이메일 템플릿을 사용합니다.
2. 에디터 오른쪽 상단의 **Share**를 클릭하고 **Braze**를 선택합니다. Braze가 목록에 없으면 **See more**를 열고 **More options**로 스크롤하여 Braze를 찾습니다.

![Canva의 추가 게시 방법에서 More options 아래의 Braze.]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. 연결 또는 다시 로그인하라는 메시지가 표시되면 Braze 패널에서 **Connect**를 선택하여(또는 브라우저 로그인 흐름을 완료하여) Canva가 워크스페이스에 템플릿을 생성할 수 있도록 합니다.

![이메일 내보내기를 위해 Connect를 요청하는 Canva의 Braze 사이드바.]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. Braze 패널에서 게시할 **이메일** 페이지를 선택하고(디자인에 여러 페이지가 있는 경우), **Braze workspace**를 선택하고, **Template name**과 **Subject line**을 입력한 후 **Publish now**를 선택합니다. 디자인이 게시되는 동안 Canva에서 진행 상황을 표시합니다.

![워크스페이스, 템플릿 이름, 제목란 및 Publish now가 있는 Canva의 Braze 패널.]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. 게시가 완료되면 성공 메시지가 나타납니다. **Check it out**을 선택하여 Braze에서 이메일 템플릿을 엽니다.

![Canva 이메일 디자인을 Braze에 게시한 후 Check it out이 포함된 성공 메시지.]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. Braze에서 Campaign 또는 Canvas에서 템플릿을 사용하기 전에 **From** 주소, 프리헤더, 탈퇴 링크 등 필요한 이메일 설정을 완료합니다.

![Canva에서 열린 Braze의 이메일 템플릿으로, 발송 정보와 미리보기가 표시됩니다.]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})