---
nav_title: Braze 액션 크레딧 설명
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Braze 액션 크레딧 설명 {#braze-action-credits-descriptions}

> 액션 크레딧은 마케팅 예산을 극대화하면서 멀티채널 메시징과 고급 AI 제품에 쉽게 접근할 수 있는 유연한 구조를 제공합니다. 단일 채널이나 지역에서 참여를 시작하고, 비즈니스 모델, 고객 기반, 인게이지먼트 전략이 발전함에 따라 AI 에이전트를 포함하도록 원활하게 확장할 수 있습니다.

액션 크레딧은 이 페이지에 제시된 모든 채널과 기능에 적용할 수 있습니다.

이 페이지에서 참조하는 "크레딧 비율"은 지정된 동작을 수행하는 데 필요한 정확한 액션 크레딧 수로 정의됩니다.

## 목차 {#table-of-contents}

- [이메일 채널 세부 정보](#email-channel-details)
- [SMS, MMS, RCS 채널 세부 정보](#sms-mms-and-rcs-channel-details)
  - [SMS 메시지 세그먼트](#sms-segments)
  - [MMS 메시지](#mms-messages)
  - [RCS 유형](#rcs-types)
- [WhatsApp 채널 세부 정보](#whatsapp-channel-details)
  - [청구 지역 분류](#billing-region-breakdown)
- [Agent Console 세부 정보](#agent-console-details)
- [추가 채널 세부 정보](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [배너](#banners)
  - [오디언스 동기화](#audience-sync)
  - [메시지 아카이빙](#message-archiving)
  - [웹훅](#webhooks)

## 이메일 채널 세부 정보 {#email-channel-details}

이메일 크레딧 비율은 Braze 플랫폼에서 발송된 이메일 1,000건 단위(CPM)로 산정됩니다.

{% alert note %}
이메일 채널에 대해 자세히 알아보려면 [이메일 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/email)를 참조하세요.
{% endalert %}

## SMS, MMS, RCS 채널 세부 정보 {#sms-mms-and-rcs-channel-details}

SMS 및 MMS 크레딧 비율은 Braze 플랫폼에서 발송된 세그먼트 단위로 산정됩니다. RCS 크레딧 비율은 Braze 플랫폼에서 전달된 Basic 및 Rich Media 유형, 또는 Single 및 Rich Media 유형 단위로 산정됩니다. 인바운드 및 아웃바운드 유형 모두 과금 대상입니다.

{% alert note %}
해당 채널에 적용되는 경우, 통신사 수수료는 별도로(후불) 청구되며 Action Credits의 일부로 간주되지 않습니다.
{% endalert %}

### SMS 세그먼트 {#sms-segments}

SMS 업계에서는 메시지를 SMS 메시지 세그먼트 단위로 계산합니다. 메시지 세그먼트는 단일 SMS 발송으로 전송되는 정해진 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자) 이내의 문자 그룹입니다. GSM-7 인코딩을 사용하여 161자의 SMS를 발송하면 두(2)개의 메시지 세그먼트가 전송됩니다. 여러 메시지 세그먼트를 전송하면 추가 요금이 발생합니다.

### MMS 메시지 {#mms-messages}

MMS의 경우 메시지 제한은 5MB입니다(멀티미디어 에셋과 메시지 본문 크기 포함). 안전을 위해 Braze에서는 메시지 본문을 포함하면서 멀티미디어 에셋을 600KB 이하로 유지할 것을 권장합니다.

### RCS 유형 {#rcs-types}

RCS는 SMS와 MMS의 차세대 버전입니다. SMS와 같은 직접적이고 높은 인게이지먼트 채널의 장점을 제공하면서, 현대 소비자가 기대하는 리치 콘텐츠(이미지, 비디오, 문서), 인증 및 브랜드 발신, 추천 답장 및 액션과 같은 인터랙티브 기능 등 더욱 풍부한 기능을 갖추고 있습니다.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
SMS 제품군 오퍼링에 대해 자세히 알아보려면 [SMS 및 MMS 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/sms)를 참조하세요.
{% endalert %}

## WhatsApp 채널 세부 정보 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## 청구 지역 분류 {#billing-region-breakdown}

### 북미 {#north-america}

미국, 캐나다

### 기타 아프리카 {#rest-of-africa}

알제리, 앙골라, 베냉, 보츠와나, 부르키나파소, 부룬디, 카메룬, 차드, 콩고, 에리트레아, 에티오피아, 가봉, 감비아, 가나, 기니비사우, 코트디부아르, 케냐, 레소토, 라이베리아, 리비아, 마다가스카르, 말라위, 말리, 모리타니, 모로코, 모잠비크, 나미비아, 니제르, 르완다, 세네갈, 시에라리온, 소말리아, 남수단, 수단, 에스와티니, 탄자니아, 토고, 튀니지, 우간다, 잠비아

### 기타 아시아 태평양 {#rest-of-asia-pacific}

아프가니스탄, 호주, 방글라데시, 캄보디아, 중국, 일본, 라오스, 몽골, 네팔, 뉴질랜드, 파푸아뉴기니, 필리핀, 스리랑카, 대만, 타지키스탄, 태국, 투르크메니스탄, 우즈베키스탄, 베트남

### 기타 중앙 및 동유럽 {#rest-of-central-eastern-europe}

알바니아, 아르메니아, 아제르바이잔, 벨라루스, 불가리아, 크로아티아, 체코, 조지아, 그리스, 라트비아, 리투아니아, 마케도니아, 몰도바, 세르비아, 슬로바키아, 슬로베니아, 우크라이나

### 기타 라틴 아메리카 {#rest-of-latin-america}

볼리비아, 코스타리카, 도미니카 공화국, 에콰도르, 엘살바도르, 과테말라, 아이티, 온두라스, 자메이카, 니카라과, 파나마, 파라과이, 푸에르토리코, 우루과이, 베네수엘라

### 기타 중동 {#rest-of-middle-east}

바레인, 이라크, 요르단, 쿠웨이트, 레바논, 오만, 예멘

### 기타 서유럽 {#rest-of-western-europe}

오스트리아, 벨기에, 덴마크, 핀란드, 아일랜드, 노르웨이, 포르투갈, 스웨덴, 스위스

{% alert note %}
Braze의 WhatsApp 오퍼링에 대해 자세히 알아보려면 [WhatsApp 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp)를 참조하세요.
{% endalert %}

## Agent Console 세부 사항 {#agent-console-details}

Agent Console 크레딧 비율은 Braze 플랫폼에서 수행된 1,000건의 호출(Invocation) 단위로 산정됩니다. 호출은 에이전트가 LLM에 대한 호출을 시작할 때 기록됩니다. 기본적으로 계약에는 구독 기간의 각 기간별로 플랫폼 에디션에 명시된 호출 할당량이 포함되어 있습니다. 추가 호출은 주문서에 따라 청구됩니다.

{% alert note %}
Agent Console에 대해 자세히 알아보려면 [Braze Agents 설명서]({{site.baseurl}}/user_guide/brazeai/agents)를 참조하세요.
{% endalert %}

## 추가 채널 세부 정보 {#additional-channel-details}

### LINE {#line}

LINE 크레딧 비율은 Braze 플랫폼에서 전송된 LINE 메시지 단위로 산정됩니다.

{% alert note %}
Braze에서 LINE을 사용하는 방법에 대해 자세히 알아보려면 [LINE 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/line)를 참조하세요.
{% endalert %}

### KakaoTalk {#kakaotalk}

KakaoTalk 크레딧 비율은 Braze 플랫폼에서 전송된 KakaoTalk 메시지 단위로 산정됩니다.

{% alert note %}
Braze에서 KakaoTalk을 사용하는 방법에 대해 자세히 알아보려면 [KakaoTalk 설명서]({{site.baseurl}}/kakaotalk)를 참조하세요.
{% endalert %}

### Content Cards {#content-cards}

Content Cards 크레딧 비율은 일일 고유 노출 횟수 1,000회 단위로 산정됩니다.

Braze는 고객이 Braze의 안내에 따라 고유 노출 횟수를 기록하도록 Content Cards를 설정하지 않은 경우, 전송된 Content Cards 수를 기준으로 크레딧을 청구할 권리를 보유합니다. 이는 Content Cards 최초 전송 후 6개월 이내에 고객이 다음 조건에 해당하는 경우 적용됩니다:
- 5,000,000건 이상의 Content Cards를 전송했으며, 다음 중 하나에 해당하는 경우
    - 기록된 노출 횟수가 0건인 경우
    - 전송 대비 일일 고유 노출 횟수 비율이 100을 초과하는 경우

{% alert note %}
Braze Content Cards에 대해 자세히 알아보려면 [Content Cards 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)를 참조하세요.
{% endalert %}

### 배너 {#banners}

배너 크레딧 비율은 일일 고유 노출 횟수 1,000회 단위로 산정됩니다.

{% alert note %}
Braze 배너에 대해 자세히 알아보려면 [배너 설명서]({{site.baseurl}}/developer_guide/banner_cards)를 참조하세요.
{% endalert %}

### 오디언스 동기화 {#audience-sync}

오디언스 동기화 크레딧 비율은 총 사용자 동기화 1,000건 단위로 산정됩니다. 기본적으로 계약에는 구독 기간의 각 기간당 5,000,000건의 사용자 동기화가 포함됩니다. 추가 사용자 동기화는 주문서에 따라 청구됩니다.

{% alert note %}
Canvas 오디언스 동기화 및 사용 가능한 파트너에 대해 자세히 알아보려면 [Canvas 설명서]({{site.baseurl}}/partners/canvas_steps)를 참조하세요.
{% endalert %}

### 메시지 보관 {#message-archiving}

메시지 보관 크레딧 비율은 푸시, 이메일, SMS/MMS 채널에 걸쳐 보관된 메시지 1,000건 단위로 산정됩니다.

{% alert note %}
메시지 보관에 대해 자세히 알아보려면 [메시지 보관 설명서]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving)를 참조하세요.
{% endalert %}

### 웹훅 {#webhooks}

웹훅 크레딧 비율은 Braze 플랫폼에서 성공적으로 전송된 웹훅 1,000건 단위로 산정됩니다. 기본적으로 계약에는 구독 기간의 각 기간당 100,000건의 웹훅이 포함됩니다. 추가 웹훅은 주문서에 따라 청구됩니다.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Braze 웹훅에 대해 자세히 알아보려면 [웹훅 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks)를 참조하세요.
{% endalert %}