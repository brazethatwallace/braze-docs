---
nav_title: "구독 그룹"
article_title: "구독 그룹"
page_order: 4
description: "이 문서에서는 WhatsApp 구독 그룹, 제공되는 구독 상태, 구독 그룹 설정 방법에 대해 설명합니다."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp


---

# WhatsApp 구독 그룹 {#whatsapp-subscription-groups}

> WhatsApp 구독 그룹은 **기술 파트너 포털**을 통해 WhatsApp을 앱과 통합할 때 생성됩니다. 크로스채널 구독 그룹 개요는 [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)을 참조하세요.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## WhatsApp 구독 상태 {#whatsapp-subscription-states}
{: #whatsapp-subscription-states}

WhatsApp 구독 상태 정의 및 Meta 옵트인 요구 사항과의 관계에 대해서는 [구독 상태]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp)를 참조하세요.

### 사용자의 WhatsApp 구독 그룹 설정하기 {#setting-users-whatsapp-subscription-groups}

- **REST API:** [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 사용하여 Braze REST API로 고객 프로필을 프로그래밍 방식으로 설정할 수 있습니다.
- **웹 SDK:** [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), 또는 [웹](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)용 `addToSubscriptionGroup` 메서드를 사용하여 이메일, 단문 메시지 서비스 또는 WhatsApp 구독 그룹에 사용자를 추가할 수 있습니다.
- **사용자 가져오기**: **Import Users**를 통해 이메일 또는 단문 메시지 서비스 구독 그룹에 사용자를 추가할 수 있습니다. 구독 그룹 상태를 업데이트할 때 CSV에 `subscription_group_id`와 `subscription_state` 두 개의 열이 있어야 합니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)를 참조하세요.

### 사용자의 WhatsApp 구독 그룹 확인하기 {#checking-a-users-whatsapp-subscription-group}

- **고객 프로필:** Braze 대시보드에서 **오디언스** > **Search Users**를 통해 개별 고객 프로필에 접근할 수 있습니다. 이메일 주소, 전화번호 또는 외부 사용자 ID로 고객 프로필을 검색할 수 있습니다. 고객 프로필 내 **Engagement** 탭에서 사용자의 WhatsApp 구독 그룹과 상태를 확인할 수 있습니다.

- **REST API:** [사용자의 구독 그룹 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) 또는 [사용자의 구독 그룹 상태 목록 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)를 사용하여 Braze REST API로 개별 고객 프로필의 구독 그룹을 확인할 수 있습니다.

## 구독 그룹 보관하기 {#archive-subscription-groups}

WhatsApp 구독 그룹 사용을 중단해야 하는 경우, 보관하여 비활성 상태로 표시할 수 있습니다.

구독 그룹을 보관하면 비활성 상태로 표시되지만 워크스페이스에서 삭제되지는 않습니다. WhatsApp 전화번호 또는 구독 그룹을 완전히 제거해야 하는 경우, Braze 지원팀에 삭제를 요청하기 전에 먼저 구독 그룹 매니저에서 해당 구독 그룹을 보관해야 합니다.

구독 그룹을 보관하려면:

1. **오디언스** > **구독 그룹 관리**로 이동합니다.
2. 보관하려는 WhatsApp 구독 그룹을 찾습니다.
3. 해당 구독 그룹의 상태 위에 마우스를 올리고 <i class="fa-solid fa-box-archive" aria-label="보관하기"></i> **보관**을 선택합니다.

## WhatsApp 옵트인 및 옵트아웃 프로세스 {#whatsapp-opt-in-and-opt-out-process}

WhatsApp 구독 상태, 옵트인 요구 사항, 옵트아웃 동작에 대한 개요는 [구독 상태]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp)를 참조하세요.

현재 사용자는 [단문 메시지 서비스](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), 웹사이트, WhatsApp 스레드, 전화 또는 대면 등 다양한 방법으로 WhatsApp 메시징에 가입하고 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)할 수 있습니다. 옵트인은 필수입니다.

현재 WhatsApp 채널에서는 옵트인 키워드가 지원되지 않으므로, 사용자 목록을 직접 관리해야 합니다. WhatsApp은 옵트인 및 사용량 제한에 대해 소급적 접근 방식을 취합니다. 사용자가 신고하거나 차단하기 시작하면 사용량 제한이 낮아집니다.

## WhatsApp Canvas에 대한 사용자의 구독 상태 업데이트 {#update-subscription-status}

사용하는 옵트인 및 옵트아웃 방법에 관계없이 다음 업데이트 방법 중 하나를 사용하여 사용자 프로필의 구독 상태를 업데이트할 수 있습니다:

- 다음 예시와 같이 REST API를 통해 구독 상태를 업데이트하는 [Braze-to-Braze 웹훅]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations)을 생성합니다:

![POST 메서드를 사용하는 메시지가 포함된 웹훅 작성기.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

경합 조건을 방지하기 위해 웹훅 이후의 후속 메시징은 첫 번째 Canvas의 결과(예: 사용자가 Canvas 배리언트에 진입하고 WhatsApp 구독 그룹에 속해 있는 경우)에 의해 트리거되는 두 번째 Canvas에 포함되어야 합니다.

- 고급 JSON 편집기를 사용하여 다음 템플릿으로 사용자 프로필을 업데이트합니다:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![고급 JSON 편집기 단계가 포함된 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
사용자의 구독 상태 업데이트는 최대 60초가 소요될 수 있습니다.
{% endalert %}