---
nav_title: 퍼지 수신 거부
article_title: 퍼지 수신 거부
description: "이 참조 문서에서는 인바운드 메시지가 수신 거부 키워드와 일치하지 않는 경우를 인식하려고 시도하는 설정인 퍼지 수신 거부를 구성하는 방법을 다룹니다."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 4

---

# 퍼지 수신 거부 {#fuzzy-opt-out}

![인바운드 퍼지 수신 거부 메시지 "Please stopppp"에 대한 응답으로 아웃바운드 수신 거부 메시지를 보여주는 iOS 메시지 채팅.]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Braze를 통해 단문 메시지 서비스, MMS, RCS를 전송하는 사용자는 정의된 관련 법률, 규정 및 업계 표준을 준수해야 합니다. 수신 거부와 관련하여, TCPA와 같은 법률은 사용자가 동의 철회를 합리적으로 구성하는 메시지(예: "STOP", "STOPALL", "UNSUBSCRIBE", "CANCEL", "END", "QUIT"과 같은 인식된 수신 거부 키워드)를 보내면 해당 메시징 프로그램과 관련된 모든 후속 메시지가 중단되어야 한다고 규정합니다. Braze는 인식된 수신 거부 키워드를 자동으로 처리하고 사용자의 구독을 해지합니다.<br><br> 퍼지 수신 거부는 구독 그룹의 **수신 거부** 카테고리에 대해 구성된 **수신 거부 키워드**(즉, [기본 수신 거부 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) 또는 [커스텀 수신 거부 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling))와 일치하지 않지만 수신 거부 의도를 나타내는 인바운드 메시지를 인식하려고 시도하여 이 기능을 확장합니다. 예를 들어, "goodbye" 또는 "leave me alone"과 같은 메시지가 해당됩니다.

퍼지 수신 거부는 기본적으로 비활성화되어 있습니다. 퍼지 수신 거부가 활성화되어 있고 인바운드 메시지가 "퍼지"로 판단되면, Braze가 자동으로 사용자의 구독을 해지하거나 수동으로 수신 거부하는 방법을 안내하는 메시지를 전송하도록 구성할 수 있습니다. 미국 브랜드의 경우, TCPA 요건을 준수하기 위해 사용자의 구독을 자동으로 해지하는 것이 강력히 권장됩니다.

{% alert note %}
현재 영어를 [로컬 언어]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling#multi-language-support)로 사용하여 생성된 수신 거부 키워드(기본값 및 커스텀)만 지원됩니다.
{% endalert %}

## 퍼지로 판단되는 기준 {#what-is-deemed-as-fuzzy}

인바운드 응답이 "퍼지"로 판단되는 기준은 다음과 같습니다(비교는 기본값 및 커스텀 키워드를 포함하여 **수신 거부** 카테고리의 모든 키워드를 사용합니다):
- QWERTY 키보드에서 한 글자를 인접한 키로 바꿨을 때 일치하는 수신 거부 키워드가 생성되는 경우.
- 메시지의 부분 문자열이 수신 거부 키워드와 일치하는 경우.

예를 들어, "Stpo" 또는 "Please stopppp"은 퍼지로 판단되며, 퍼지 수신 거부 응답이 전송됩니다. 이후 사용자가 수신 거부 키워드로 응답하면 구독 해지 이벤트가 트리거됩니다.

## 퍼지 수신 거부 구성 {#configure-fuzzy-opt-out}

퍼지 수신 거부를 구성하려면 구독 그룹 키워드 관리 페이지로 이동합니다.

1. **Audience** > **Subscription Group Management**로 이동하여 **단문 메시지 서비스/MMS/RCS** 구독 그룹을 선택합니다.
2. **Global Keywords**에서 **Opt-out** 카테고리를 찾아 연필 아이콘을 선택합니다.
3. **Fuzzy Opt-Out**을 **On**으로 토글합니다.
4. 원하는 **Fuzzy Opt-Out Logic** 옵션을 선택합니다:
   - **Automatically unsubscribe:** 사용자가 수신 거부 키워드와 유사한 메시지를 보내면, 별도의 안내 없이 즉시 구독이 해지됩니다. 그런 다음 표준 수신 거부 확인 메시지가 전송됩니다.
   - **Send opt-out instructions:** 사용자가 수신 거부 키워드와 유사한 메시지를 보내면, Braze가 구독 해지 방법을 설명하는 커스텀 답장(**Opt-out instruction message**)을 전송합니다.
5. **Send opt-out instructions**를 선택한 경우, **Opt-out instruction message** 필드에 커스텀 텍스트를 입력합니다. 이 설정에서는 이 필드가 필수입니다.
6. **Save**를 선택합니다.

![수신 거부 키워드를 편집하고 수신 거부 안내 메시지를 제공하는 섹션.]({% image_buster /assets/img/sms/fuzzy2.png %})

## 퍼지 수신 거부 메시지 모범 사례 {#best-practices-for-fuzzy-opt-out-messages}

구독자에게 명확하고 규정을 준수하며 긍정적인 경험을 보장하려면, 퍼지 수신 거부 메시지를 신중하게 구성하는 것이 중요합니다. 퍼지 수신 거부 메시지의 주요 목적은 **지정된 수신 거부 키워드와 유사하지만 정확히 일치하지 않는 메시지를 보낸 사용자를 안내하는 것**입니다. 이 메시지는 사용자가 성공적으로 구독을 해지하는 방법을 안내합니다.

### 중요 고려 사항 {#critical-considerations}

{% alert warning %}
**Send opt-out instructions**를 선택한 경우, 퍼지 수신 거부 메시지를 구독 해지 확인으로 구성하지 **마세요**. 퍼지 수신 거부 메시지에는 사용자가 이미 성공적으로 구독을 해지했음을 암시하는 문구가 포함되어서는 안 됩니다. 예를 들어, "구독이 해지되었습니다", "이 번호에서 더 이상 메시지를 받지 않습니다", "수신 거부가 완료되었습니다"와 같은 문구를 사용하지 **마세요**.
{% endalert %}

퍼지 수신 거부 메시지는 사용자가 성공적으로 수신 거부하기 전에 전송됩니다. 확인 문구(예: "구독이 해지되었습니다")를 사용하면 구독자가 실제로는 구독이 해지되지 않았는데 해지된 것으로 오해하게 되어, 원치 않는 메시지가 계속 전송되고 구독자 불만 및 심각한 규정 준수 위험이 발생할 수 있습니다.

퍼지 일치 시 사용자의 구독을 즉시 해지하려면 **Automatically unsubscribe** 설정을 대신 사용하세요.

{% alert warning %}
퍼지 수신 거부 메시지를 정확한 수신 거부 키워드와 동일하거나 유사하게 구성하지 **마세요**.
{% endalert %}

퍼지 메시지가 정확한 수신 거부 키워드와 동일하거나 너무 유사한 경우(예: "STOP"이 정확한 키워드이고 퍼지 메시지가 "Text STOP to unsubscribe"인 경우), 사용자의 초기 메시지가 실제로 구독 해지로 이어졌는지 아니면 추가 조치가 필요한지에 대해 혼란을 야기할 수 있습니다. 퍼지 메시지는 항상 사용자가 취해야 할 조치를 명확히 안내해야 합니다.

### 퍼지 수신 거부 메시지 예시 {#examples-of-fuzzy-opt-out-messages}

**Send opt-out instructions**를 선택한 경우, 사용자를 안내하는 데 초점을 맞추세요. 예를 들어, 수신 거부 키워드가 "STOP"인 경우, 다음은 생성할 수 있는 퍼지 수신 거부 메시지의 좋은 예시와 나쁜 예시입니다:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        좋은 예시 <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        나쁜 예시 <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"모든 메시지 수신을 거부하려면 STOP이라고 답장해 주세요."</td>
      <td>"구독이 성공적으로 해지되었습니다. 이 번호에서 더 이상 메시지를 받지 않습니다. 다시 가입하려면 START라고 답장하세요." (이것은 구독 해지에 대한 직접적인 확인으로, 퍼지 수신 거부 시나리오에서는 오해를 유발합니다.)</td>
    </tr>
    <tr>
      <td>"메시지를 수신했습니다. 문자 수신을 중단하려면 STOP이라고 문자를 보내주세요."</td>
      <td>"STOP." (이것은 정확한 키워드 자체일 뿐이며, 사용자를 안내하지 않습니다.)</td>
    </tr>
    <tr>
      <td>"구독을 해지하시겠습니까? 향후 모든 메시지 수신을 거부하려면 STOP이라고 답장하세요."</td>
      <td>"Text STOP to unsubscribe." ("STOP"이 정확한 키워드이기도 한 경우, 이것은 중복되며 초기 메시지가 퍼지였을 때 조치를 명확히 하지 않습니다.)</td>
    </tr>
  </tbody>
</table>