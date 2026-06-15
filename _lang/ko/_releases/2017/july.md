---
nav_title: 7월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2017년 7월의 릴리스 노트가 포함되어 있습니다."
---

# 2017년 7월 {#july-2017}

## 웹 푸시에서 큰 이미지 {#large-images-in-web-push}

Windows 및 Android의 Chrome에서 웹 푸시용 대형 이미지 지원을 추가하여 풍부하고 매력적인 고객 경험을 만들 수 있습니다. [웹 푸시]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/)에 대해 자세히 알아보세요.

## 이메일 필드 업데이트 {#updates-to-email-fields}

이제 이메일을 특정 발신 주소 세트로 잠글 수 있어 잘못된 주소를 실수로 입력하는 것을 방지할 수 있습니다. 이메일 작성 양식은 프로세스를 간소화하기 위해 지난 6개월 동안 사용된 주소로 미리 채워집니다. 자세한 내용은 [이메일 모범 사례]({{site.baseurl}}/user_guide/channels/email/best_practices/)를 확인하세요.

## 캠페인 세부 정보 API 업데이트 {#updates-to-campaign-details-api}

`/campaign/details` 엔드포인트는 이제 메시지에 대한 정보를 제공하여 API를 사용해 제목, HTML 본문, 발신 주소 및 회신 주소 필드를 가져올 수 있습니다. [Braze API]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api)에 대해 자세히 알아보세요.

## Liquid 템플릿 업데이트 {#updates-to-liquid-templating}

Canvases와 Campaigns에서 배리언트 속성을 템플릿화할 수 있는 기능을 추가했습니다. Canvas에서는 이제 배리언트의 API ID뿐만 아니라 배리언트의 이름도 템플릿할 수 있으며, Campaigns에서는 메시지의 `message_api_id` 및 `message_name`을 템플릿할 수 있습니다. 두 업데이트 모두 메시징에서 더 많은 유연성을 제공하여 개인화된 캠페인을 구축할 수 있습니다. [개인화된 메시징]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)에 대해 자세히 알아보세요.

## 새 HTML 이메일 편집기 {#new-html-email-editor}

이제 라이브 프리뷰, Liquid를 통한 개인화, 줄 번호와 구문 강조가 포함된 개선된 전체화면 텍스트 편집기를 갖춘 전체화면 HTML 편집기로 이메일을 쉽게 작성하고 테스트할 수 있습니다. [이메일 작성]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template)에 대해 자세히 알아보세요.

## 미리보기 업데이트 {#updates-to-previews}

이제 Campaigns와 Canvases에서 메시지 미리보기를 스크롤할 때 화면 창이 함께 따라오므로 변경 사항이 항상 반영되는 것을 확인할 수 있습니다. [미리보기 및 테스트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message)에 대해 자세히 알아보세요.

## 새로운 Segment 멤버십 필터 {#new-segment-membership-filter}

[Segment 멤버십 필터]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters)를 추가하여 기존 Segments의 멤버십을 기반으로 사용자를 타겟팅할 수 있습니다. 또한 Segment 필터에서 "And" 및 "Or" 논리를 모두 사용할 수 있는 기능과 Segments를 서로 중첩할 수 있는 기능을 추가했습니다. 이 업데이트를 통해 고객에게 더 정확하게 맞춤형 메시지를 보낼 수 있습니다.

## Android 미리보기 업데이트 {#update-to-android-preview}

Android N 이후의 최신 버전을 반영하도록 [Android 미리보기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message)를 업데이트했습니다.