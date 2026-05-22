---
nav_title: 연락처 카드
article_title: 연락처 카드
page_order: 3
description: "이 참조 문서에서는 MMS 및 SMS 메시지에 포함할 연락처 카드를 만드는 방법을 다룹니다."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# 연락처 카드 {#contact-cards}

> 연락처 카드(vCard 또는 가상 연락처 파일(VCF)이라고도 함)는 비즈니스 및 연락처 정보를 전송하기 위한 표준화된 파일 형식으로, 주소록이나 연락처 목록에 쉽게 가져올 수 있습니다.

{% alert note %}
연락처 카드를 보내면 MMS 요금이 부과됩니다. 연락처 카드를 만들 때 예상 MMS 발송량과 메시지 또는 동작 크레딧 사용량을 검토하고, Braze [청구 페이지]({{site.baseurl}}/user_guide/administer/global/billing/)에서 비용을 확인하세요.
{% endalert %}

연락처 카드는 [프로그래밍 방식으로](https://www.twilio.com/blog/send-vcard-twilio-sms) 생성하여 Braze [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library)에 업로드하거나, 기본 제공되는 연락처 카드 생성기를 통해 만들 수 있습니다. 이 카드에는 회사 이름, 전화번호, 주소, 이메일, 작은 사진 등 일반적인 속성을 할당할 수 있습니다. 연락처 카드를 만들려면 먼저 Braze에서 MMS를 사용할 수 있도록 설정되어 있는지 확인하세요.

## 연락처 카드 생성기 {#contact-card-generator}

### 1단계: 이름 할당 {#step-1-assign-name}

연락처 카드는 SMS 및 MMS 작성기에서 만들 수 있습니다. **Contact Card Generator** 탭을 선택하여 시작하세요.

다음으로 회사 이름 또는 닉네임을 입력하라는 메시지가 표시됩니다. 이 이름은 사용자가 카드를 저장할 때 표시되는 이름입니다. 사용자가 연락처 및 메시징 앱에서 전체 회사 이름 또는 별칭을 볼 수 있도록 20자 제한이 적용됩니다.

![연락처 카드 생성기 탭.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### 2단계: 전화번호 할당 {#step-2-assign-phone-number}

사용 가능한 드롭다운 옵션에서 구독 그룹과 원하는 전화번호를 선택합니다. 이 번호는 연락처 카드에 표시되며, 저장 후 사용자의 휴대폰에서 문자를 보낼 수 있습니다.

영숫자 코드는 양방향 메시징과 호환되지 않으며 연락처 카드에서 지원되지 않습니다.

### 3단계: 선택 필드 {#step-3-optional-fields}

![연락처 카드 생성기의 선택 필드.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### 연락처 카드 연락처 사진 업로드 {#upload-contact-card-contact-photo}

연락처 카드에 선택적으로 썸네일 연락처 사진을 업로드할 수 있습니다. 240 x 240&nbsp;px JPEG 또는 PNG 이미지를 권장합니다. 업로드된 고해상도 이미지는 메시지의 전달 가능성을 보장하기 위해 240 x 240&nbsp;px로 크기가 조정됩니다. 5&nbsp;MB보다 큰 MMS 메시지는 전송에 실패할 수 있습니다.

#### 추가 정보 입력 {#add-more-information}

기타 필드를 사용하면 이름, 부제목, 주소 및 사용자가 필요로 할 수 있는 기타 연락처 정보를 삽입할 수 있습니다.

### 4단계: 연락처 카드 저장 {#step-4-saving-your-contact-card}

필요한 모든 필드를 입력한 후 **Generate Contact Card**를 클릭하면 Campaign 또는 Canvas에 자동으로 첨부됩니다. 여기에서 메시지를 추가하고, 연락처 카드를 테스트하고, Campaign 또는 Canvas를 시작할 수 있습니다.

연락처 카드는 향후 Campaigns 및 Canvases에서 쉽게 재사용할 수 있도록 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library)에도 저장됩니다.

## 기존 연락처 카드 추가 {#adding-an-existing-contact-card}

기존 연락처 카드를 추가하려면 Campaign 또는 Canvas를 만들고 원하는 구독 그룹을 선택합니다. 그러면 메시지 작성기 창에 **Add Media** 옵션이 나타납니다. 여기에서 기존 연락처 카드 파일을 업로드하거나 미디어 라이브러리를 통해 찾을 수 있습니다.