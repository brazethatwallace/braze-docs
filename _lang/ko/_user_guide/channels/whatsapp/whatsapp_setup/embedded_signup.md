---
nav_title: 임베디드 가입
article_title: WhatsApp 임베디드 가입
page_order: 1
description: "이 참조 문서에서는 Braze의 WhatsApp 임베디드 가입 워크플로를 단계별로 안내합니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 임베디드 가입 {#whatsapp-embedded-signup}

> 이 참조 문서에서는 Braze의 WhatsApp 임베디드 가입 워크플로를 단계별로 안내합니다.

WhatsApp 임베디드 가입 워크플로는 Braze 워크스페이스에 처음 [WhatsApp을 통합]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)할 때, 그리고 기존 WhatsApp 통합에 [WhatsApp Business 계정을 추가]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)할 때 접근할 수 있습니다.

{% alert note %}
Braze 워크스페이스에 [여러 WhatsApp Business 계정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)을 추가할 수 있습니다. 그러나 각 특정 WhatsApp Business 계정은 하나의 Braze 워크스페이스에만 추가할 수 있습니다.
{% endalert %}

## 워크플로 접근하기 {#accessing-the-workflow}

**파트너 통합** > **기술 파트너**로 이동한 다음 **WhatsApp**을 검색하여 선택합니다. 다음 선택은 사용 사례에 따라 달라집니다:

- 워크스페이스에 WhatsApp을 통합하는 경우 **Begin Integration**을 선택합니다. <br><br>![통합을 시작하는 버튼이 있는 WhatsApp 파트너 페이지.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- 기존 WhatsApp 통합에 WhatsApp Business 계정을 추가하는 경우 **Add WhatsApp Business Account**를 선택합니다. <br><br>![WhatsApp Business 계정 또는 구독 그룹 및 번호를 추가하는 옵션이 있는 "WhatsApp Messaging Integration".]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

이후 워크플로는 두 사용 사례 모두 동일합니다.

## WhatsApp 임베디드 가입 워크플로 {#whatsapp-embedded-signup-workflow}

1. Meta(Facebook) 로그인 창에서 **Login as** 또는 **Continue**를 선택합니다. <br><br>![Meta 로그인 창.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Braze와 공유할 권한을 확인한 다음 **Get Started**를 선택합니다. <br><br>![통합을 위해 Braze와 공유할 권한 목록.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. 이 화면에서 다음을 설정한 후 **Next**를 선택합니다:
- **Business portfolio** 드롭다운에서 비즈니스 포트폴리오를 선택합니다. 이것은 WhatsApp Business 계정에 연결되므로, 예상한 비즈니스 포트폴리오가 보이지 않으면 권한을 확인하세요.
- **WhatsApp business account** 필드에서 **Create a new WhatsApp Business Account**를 선택합니다. 워크스페이스에 다른 WhatsApp Business 계정을 추가하거나 해당 계정이 이미 Meta에 존재하는 경우에도 이 옵션을 선택하세요. 드롭다운에서 기존 WhatsApp Business 계정을 선택하는 대신 이 옵션을 선택합니다. <br><br>![비즈니스 포트폴리오 이름을 포함한 비즈니스 정보를 입력하는 필드가 있는 창.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. 드롭다운 필드에서 다음을 선택한 후 **Next**를 선택합니다.
- **Choose a WhatsApp Business account**: WhatsApp Business 계정 생성
- **Create or select a WhatsApp Business profile**: 새 WhatsApp Business 프로필 생성 <br><br>![WhatsApp Business 계정 및 프로필을 선택하거나 생성할지 지정하는 필드.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. 다음 정보를 입력한 후 **Next**를 선택합니다.
- WhatsApp Business 계정 이름
- WhatsApp Business 표시 이름
- 카테고리 <br><br>![새 WhatsApp Business 계정의 세부 정보를 입력하는 필드.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. 전화번호를 입력하고 **Text message** 또는 **Phone call**을 선택합니다. 새 번호의 경우, 다른 WhatsApp 계정에 등록되어 있지 않아야 하는 것을 포함하여 WhatsApp의 전화번호 요구 사항을 충족해야 합니다. 기존 번호를 마이그레이션하는 경우(3단계 참조) Meta에서 해당 번호가 이미 사용 중이라고 표시하더라도 경고를 무시하고 계속 진행하여 마이그레이션을 완료하세요. <br><br>![전화번호를 추가하는 필드.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. 2단계 인증 코드를 입력한 다음 **Next**를 선택합니다. <br><br>![2단계 인증 코드 입력 필드.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. WhatsApp Business 계정이 받게 될 권한을 검토한 다음 **Continue**를 선택합니다. <br><br>![WhatsApp Business 계정이 요청하는 권한 목록.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. 완료되었습니다! <br><br>![메시지 전송을 시작할 준비가 되었다는 창.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}