---
nav_title: 미디어 라이브러리
article_title: 미디어 라이브러리
page_order: 2
page_type: reference
description: "이 참조 문서에서는 미디어 라이브러리를 다룹니다. 여기에서 단일 중앙 집중식 위치에서 자산을 관리하고, AI를 사용하여 이미지를 생성하고, 메시지 작성기에서 미디어에 액세스하는 방법을 알아볼 수 있습니다."
tool: Media

---

# 미디어 라이브러리 {#media-library}

> 미디어 라이브러리를 사용하면 단일 중앙 집중식 위치에서 자산을 관리할 수 있습니다.

## 미디어 라이브러리 vs CDN {#media-library-versus-cdn}

CDN(Content Delivery Network) 대신 미디어 라이브러리를 사용하면 인앱 메시지에 대해 더 나은 캐싱과 성능을 제공합니다. 인앱 메시지에 포함된 모든 미디어 라이브러리 자산은 더 빠른 표시를 위해 사전 캐싱되며 오프라인 표시에도 사용할 수 있습니다. 또한 미디어 라이브러리는 Braze 작성기와 통합되어 있어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그를 지정할 수 있습니다.

## 미디어 라이브러리 액세스하기 {#accessing-the-media-library}

미디어 라이브러리에서 자산 유형, 크기, 크기 및 위치, URL, 라이브러리에 추가된 날짜 및 기타 정보를 확인할 수 있습니다. Braze 미디어 라이브러리에 액세스하려면 **콘텐츠** > **미디어 라이브러리**로 이동합니다. 여기에서 다음을 수행할 수 있습니다:

* 한 번에 여러 이미지 업로드
* 가상 연락처 파일(.vcf) 업로드
* WhatsApp 메시지에 사용할 동영상 파일 업로드
* 이미지가 포함된 폴더 업로드(최대 50개 이미지)
* [AI를 사용하여 이미지 생성](#generate-ai) 후 미디어 라이브러리에 저장
* 기존 이미지를 잘라서 메시지에 적합한 비율 만들기
* 태그 또는 Teams를 추가하여 이미지를 더 잘 정리
* 미디어 라이브러리 그리드에서 태그 또는 Teams로 검색
* 이미지 또는 폴더를 드래그 앤 드롭하여 업로드
* 이미지 삭제

![파일을 드래그 앤 드롭하거나 업로드할 수 있는 "라이브러리에 업로드" 섹션이 포함된 미디어 라이브러리 페이지. 미디어 라이브러리에 업로드된 콘텐츠 목록도 있습니다.]({% image_buster /assets/img_archive/media_library_main.png %})

나중에 Braze에서 메시지를 작성할 때 미디어 라이브러리에서 이미지를 가져올 수 있습니다.

![메시지 작성기에 따라 미디어 라이브러리에 액세스하는 두 가지 일반적인 방법. 하나는 "이미지 및 GIF"라는 제목과 "미디어 라이브러리에서 추가" 버튼이 있는 이메일 드래그 앤 드롭 편집기입니다. 다른 하나는 "미디어"라는 제목과 "이미지 추가" 버튼이 있는 푸시 및 인앱 메시지와 같은 표준 편집기입니다.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} 미디어 라이브러리에 대한 추가 도움이 필요하면 [미디어 라이브러리 FAQ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/)를 확인하세요. {% endalert %}

## 이미지 사양 {#image-specifications}

미디어 라이브러리에 업로드되는 모든 이미지는 5&nbsp;MB 미만이어야 합니다. 지원되는 파일 형식은 PNG, JPEG, GIF, SVG, WebP입니다. 메시징 채널별 권장 이미지 크기 및 사양은 [이미지 사양]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/)을 참조하세요.

{% alert important %}
매우 길쭉한 형태의 GIF(예: 3000 x 2 픽셀) 또는 300프레임 이상의 GIF는 전체 파일 크기가 작더라도 업로드에 실패할 수 있습니다.
{% endalert %}

## BrazeAI<sup>TM</sup>로 이미지 생성하기 {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
이 기능을 사용하기 전에 [데이터가 OpenAI로 어떻게 사용되고 전송되는지]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy) 검토하세요.
{% endalert %}