---
nav_title: Zapier를 통한 Facebook Lead Ads
article_title: Zapier를 통한 Facebook Lead Ads
description: "이 참조 문서에서는 Zapier를 통한 Braze와 Facebook Lead Ads 간의 통합을 설명합니다. 이 통합을 통해 Facebook에서 Braze로 리드 데이터 전송을 자동화하여 실시간 참여와 개인화된 후속 동작을 수행할 수 있습니다."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner
---

# Zapier를 통한 Facebook Lead Ads 통합 {#facebook-lead-ads-via-zapier-integration}

> <a href="https://zapier.com/" target="_blank">Zapier</a> 를 통한 Facebook Lead Ads 통합을 사용하면 Facebook에서 Braze로 리드를 가져오고 리드가 캡처될 때 커스텀 이벤트를 추적할 수 있습니다.

Facebook Lead Ads는 비즈니스가 Facebook 내에서 직접 리드 정보를 수집할 수 있는 광고 형식입니다. 이 광고는 리드 생성 프로세스를 쉽고 원활하게 만들도록 설계되었습니다. Zapier 통합과 Braze를 활용하면 Facebook에서 Braze로 리드 데이터 전송을 자동화하여 실시간 참여와 개인화된 후속 동작을 수행할 수 있습니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Zapier 계정 | 이 파트너십을 활용하려면 Zapier 계정이 필요합니다. 이 통합은 <a href="https://zapier.com/app/pricing/" target="_blank">프리미엄 Zapier 앱</a> 을 사용해야 하므로, 사용 중인 Zapier 플랜이 프리미엄 앱에 접근할 수 있는지 확인하세요. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook Leads 액세스</a> | Braze와 함께 사용할 각 광고 계정에 대해 Facebook Leads 액세스가 필요합니다. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | 이 통합의 일부로 브랜드의 Facebook 자산(예: 광고 계정, 페이지, 앱)을 관리하는 중앙 집중식 도구인 Facebook Business Manager를 사용하게 됩니다. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook 광고 계정</a> | 브랜드의 비즈니스 매니저에 연결된 활성 Facebook 광고 계정이 필요합니다. <br><br>Braze와 함께 사용할 각 광고 계정에 대해 "Manage ad accounts" 권한이 있는지, 광고 계정 이용약관에 동의했는지 확인하세요. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebook 페이지</a> | 브랜드의 비즈니스 매니저에 연결된 활성 Facebook 페이지가 필요합니다. <br><br>Braze와 함께 사용할 각 Facebook 페이지에 대해 "Manage Pages" 권한이 있는지 확인하세요. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#api-definitions)을 알고 있는지 확인하세요. API 엔드포인트는 Braze 인스턴스의 대시보드 URL과 일치합니다. <br><br> 예를 들어, 대시보드 URL이 `https://dashboard-03.braze.com`인 경우 엔드포인트는 `dashboard-03`이 됩니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 있는지 확인하세요. <br><br> 이 키는 Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: 인스턴트 양식이 포함된 리드 광고 캠페인 만들기 {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Facebook 광고 관리자에서 <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook 리드 캠페인과 Facebook 리드 광고 양식</a> 을 만드세요.

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에 요청을 보내 사용자 프로필을 업데이트하거나 생성할 때 이메일 주소 또는 전화번호를 사용할 수 있습니다. 이러한 이유로 리드 광고 양식에 **이메일** 또는 **전화번호**에 대한 **연락처 필드**를 포함하세요. 이름이나 성을 수집하는 경우 전체 이름을 사용하는 대신 양식에서 별도로 수집하세요.

### 2단계: Facebook 계정을 Zapier에 연결하기 {#step-2-connect-your-facebook-account-to-zapier}

#### 2a단계: Zapier에서 연결 방법 선택하기 {#step-2a-select-your-connection-method-in-zapier}

Zapier에서 **앱**으로 이동하여 사용 가능한 Facebook 앱을 검색합니다. **Facebook Lead Ads** 또는 **Facebook Lead Ads (for Business admins)**를 선택합니다.

Facebook 계정을 Zapier에 연결하는 이 두 가지 방법에 대한 자세한 내용은 다음을 참고하세요:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Facebook Lead Ads 연결 옵션을 보여주는 Zapier 앱 검색 화면.]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### 2b단계: Facebook 비즈니스 관리자에서 리드 액세스에 Zapier 추가하기 {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

Facebook 비즈니스 관리자에서 내비게이션 메뉴의 **통합** > **리드 액세스**로 이동합니다. Facebook 페이지를 선택한 다음 **CRM**을 클릭합니다. CRM 탭에서 **CRM 할당**을 선택하고 **Zapier**를 추가합니다.

![Zapier가 CRM 통합으로 할당된 Facebook 비즈니스 관리자 리드 액세스 페이지.]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Zapier를 CRM 통합으로 할당하는 단계는 Facebook의 <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">설명서</a> 를 참고하세요.

### 3단계: Zap 만들기 {#step-3-create-your-zap}

#### 3a단계: 트리거 만들기 {#step-3a-create-the-trigger}

Facebook 계정을 연결한 후 Zap을 만들 수 있습니다. **트리거**의 경우 2단계에서 선택한 항목에 따라 **Facebook Lead Ads** 또는 **Facebook Lead Ads (for Business Admins)**를 선택합니다.

![Facebook Lead Ads가 선택된 Zapier 트리거 단계.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

**이벤트**에서 **New Leads** > **Continue**를 선택합니다.

![New Leads가 표시된 Zapier 트리거 이벤트 선택 화면.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Facebook 계정을 선택한 다음 **Continue**를 클릭합니다.

![트리거에 대한 Zapier Facebook 계정 연결 단계.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

이전에 만든 Facebook 페이지와 인스턴트 양식을 선택한 다음 **Continue**를 클릭합니다.

![Facebook 페이지와 인스턴트 양식을 선택하는 Zapier 트리거 설정 화면.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

다음으로, 이 트리거를 테스트합니다. 양식 출력을 확인한 후 **Continue with selected record**를 선택합니다.

#### 3b단계: 액션 만들기 {#step-3b-create-an-action}

새 단계를 추가한 다음 **Webhooks by Zapier**를 선택합니다. 그런 다음 **이벤트** 필드에서 **Custom Request**를 선택하고 **Continue**를 클릭합니다.

![Webhooks by Zapier와 Custom Request로 설정된 Zapier 액션 단계.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

마지막으로, 페이로드에 필드를 삽입하여 커스텀 요청을 설정합니다. 다음 코드 스니펫은 페이로드 예시를 보여줍니다.

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

다음은 Zapier에서 이것이 어떻게 보이는지에 대한 예시입니다:

![Facebook 리드 필드를 Braze로 전송하기 위한 Zapier 웹훅 페이로드 매핑 예시.]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

웹훅을 설정한 후 **Continue and test**를 선택합니다. 테스트가 성공하면 Zap을 게시할 수 있습니다.

### 4단계: Facebook Lead Ads Zap 테스트하기 {#step-4-test-your-facebook-lead-ads-zap}

포괄적인 테스트를 수행하려면 Facebook 개발자 콘솔에서 Facebook의 리드 광고 테스트 도구를 사용하세요. 자세한 내용은 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">테스트 및 문제 해결</a> 을 참고하세요.

## 사용자 신원 관리 {#user-identity-management}

이 통합을 사용하면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)를 통해 이메일로 Facebook 리드를 귀속시킬 수 있습니다.

* 이메일이 기존 고객 프로필과 일치하면, Braze는 해당 프로필을 Facebook 리드 데이터로 업데이트합니다.
* 동일한 이메일을 가진 고객 프로필이 여러 개인 경우, Braze는 외부 ID가 있는 가장 최근에 업데이트된 프로필을 우선적으로 업데이트합니다.
* 외부 ID가 존재하지 않으면, Braze는 일치하는 이메일을 가진 가장 최근에 업데이트된 프로필을 우선시합니다.
* 제공된 이메일을 가진 프로필이 없으면, Braze는 새 프로필을 생성하며 새로운 별칭 고객 프로필이 생성됩니다. 새로 생성된 별칭 고객 프로필을 식별하려면 [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 사용하세요.

{% alert note %}
해당 필드를 사용할 수 있고 통합에 사용하려는 기본 식별자인 경우, Braze에 대한 요청의 일부로 전화번호 또는 외부 ID를 사용할 수도 있습니다. 이를 위해 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에 명시된 대로 요청 페이로드를 수정하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

{% details 트리거와 액션을 성공적으로 테스트했는데, 왜 Zapier Zap을 게시할 수 없나요? %}
이 통합을 사용하려면 프리미엄 앱을 지원하는 <a href="https://zapier.com/app/pricing/" target="_blank">Zapier 플랜</a> 이 필요합니다.
{% enddetails %}

{% details Facebook 리드가 Braze에 동기화되지 않는 이유는 무엇인가요? %}
1. Facebook 페이지, 광고 계정, 리드 액세스에 대한 관리자 권한이 있는지 확인하세요. 그런 다음 Zapier에서 계정을 다시 연결하세요.
2. Facebook에서 만든 인스턴트 양식이 트리거 단계에서 선택한 양식에 매핑되는지 확인하세요.
3. **Facebook Business Manager** > **Integrations** > **Lead Access**로 이동하여 Zapier에 리드 액세스를 할당했는지 확인하세요.
{% enddetails %}

{% details 동일한 이메일을 가진 중복 고객 프로필이 표시되는 이유는 무엇인가요? %}
Braze에서는 [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)에 따라 고객 프로필을 생성하고 관리하는 고유한 방법이 있습니다.

내부 프로세스와 고객이 Braze 내에서 생성되는 트리거 시점에 따라, 통합에 의해 고객 프로필이 생성되는 시점과 시스템에서 사용자가 생성되는 시점 사이의 경합 조건으로 인해 중복 고객 프로필이 발생할 수 있습니다. Braze에서 [고객 프로필을 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)할 수 있습니다.
{% enddetails %}

{% details Zapier 계정이 없습니다. Facebook Lead Ads 웹훅을 Braze로 트리거하려면 어떻게 해야 하나요? %}
Zapier를 사용하지 않고 사용할 계획이 없다면, Facebook에서 Braze로 직접 통합을 구축할 수 있습니다. 자세한 내용은 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Lead Ads 설명서</a> 를 참조하세요.

Facebook에서 리드를 가져오려면 <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">웹훅</a> 을 사용하세요. Facebook에서 웹훅을 시작하려면 <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">웹훅 설명서</a> 를 참조하세요.

Facebook에서 웹훅 URL을 설정한 후 팀과 협력하여 데이터를 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)로 전달하는 가장 적합한 경로를 결정하세요. Zapier 접근 방식과 마찬가지로, `users/track` 엔드포인트를 통해 [이메일로 요청]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)하는 것을 권장합니다.
{% enddetails %}

{% alert tip %}
추가 문제 해결 팁은 Zapier의 <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebook 리드 문제 해결 가이드</a> 를 참조하세요.
{% endalert %}