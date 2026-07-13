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

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| "View Media Library Assets" 권한 | 미디어 라이브러리 자산 보기 |
| "Edit Media Library Assets" 권한 | 미디어 라이브러리 자산 생성 및 업데이트 |
| "Delete Media Library Assets" 권한 | UI에서 미디어 라이브러리 자산을 삭제합니다. 삭제된 자산은 해당 자산을 참조하는 메시지가 깨지지 않도록 Braze에서 계속 호스팅됩니다. 자산을 영구적으로 삭제하려면 Braze 지원팀에 문의하세요. |
| "Replace Media Library Assets" 권한 | URL과 자산 ID를 유지하면서 기존 미디어 라이브러리 자산의 파일 교체 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="미디어 라이브러리 권한" }

자세한 내용은 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.

## 미디어 라이브러리 vs CDN {#media-library-versus-cdn}

CDN(Content Delivery Network) 대신 미디어 라이브러리를 사용하면 인앱 메시지에 대해 더 나은 캐싱과 성능을 제공합니다. 인앱 메시지에 포함된 모든 미디어 라이브러리 자산은 더 빠른 표시를 위해 사전 캐싱되며 오프라인 표시에도 사용할 수 있습니다. 또한 미디어 라이브러리는 Braze 작성기와 통합되어 있어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그를 지정할 수 있습니다.

## 미디어 라이브러리 액세스하기 {#accessing-the-media-library}

미디어 라이브러리에서 자산 유형, 크기, 치수, URL, 라이브러리에 추가된 날짜 및 기타 정보를 확인할 수 있습니다. Braze 미디어 라이브러리에 액세스하려면 **콘텐츠** > **미디어 라이브러리**로 이동합니다. 여기에서 다음을 수행할 수 있습니다:

* 한 번에 여러 이미지 업로드
* 가상 연락처 파일(.vcf) 업로드
* WhatsApp 메시지에 사용할 동영상 파일 업로드
* 이미지가 포함된 폴더 업로드(최대 50개 이미지)
* [AI를 사용하여 이미지 생성](#generate-ai) 후 미디어 라이브러리에 저장
* 기존 이미지를 잘라서 메시지에 적합한 비율 만들기
* URL을 유지하면서 기존 자산의 파일 교체
* 태그 또는 팀을 추가하여 이미지를 더 잘 정리
* 미디어 라이브러리 그리드에서 태그 또는 팀으로 검색
* 이미지 또는 폴더를 드래그 앤 드롭하여 업로드
* 이미지 삭제

![파일을 드래그 앤 드롭하거나 업로드할 수 있는 '라이브러리에 업로드' 섹션이 포함된 미디어 라이브러리 페이지. 미디어 라이브러리에 업로드된 콘텐츠 목록도 있습니다.]({% image_buster /assets/img_archive/media_library_main.png %})

나중에 Braze에서 메시지를 작성할 때 미디어 라이브러리에서 이미지를 가져올 수 있습니다.

![메시지 작성기에 따라 미디어 라이브러리에 액세스하는 두 가지 일반적인 방법. 하나는 '이미지 및 GIF'라는 제목과 '미디어 라이브러리에서 추가' 버튼이 있는 이메일 드래그 앤 드롭 편집기입니다. 다른 하나는 '미디어'라는 제목과 '이미지 추가' 버튼이 있는 푸시 및 인앱 메시지와 같은 표준 편집기입니다.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} 미디어 라이브러리에 대한 추가 도움이 필요하면 [미디어 라이브러리 FAQ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq)를 확인하세요. {% endalert %}

## 파일 교체 {#replace-a-file}

URL과 자산 ID를 유지하면서 미디어 라이브러리의 기존 자산 파일을 교체할 수 있습니다. URL이 변경되지 않으므로 해당 자산을 참조하는 모든 메시지 또는 Campaign(이미 발송된 이메일 포함)에 업데이트된 파일이 자동으로 반영됩니다. 이 기능은 각 Campaign을 개별적으로 업데이트하는 대신 공유 자산(예: 로고)을 한 곳에서 업데이트하려는 경우에 유용합니다.

자산을 교체하려면 "Replace Media Library Assets" 권한이 필요합니다:

1. **콘텐츠** > **미디어 라이브러리**로 이동합니다.
2. 교체할 자산을 선택합니다.
3. Modal에서 **Replace file**을 선택합니다.
4. 교체할 파일을 업로드합니다.

![자산에 대한 Replace file, Crop image, Delete 버튼이 표시된 미디어 라이브러리 편집 Modal.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### 요구 사항 및 제한 사항 {#requirements-and-limitations}

- 교체 파일은 원본과 동일한 파일 확장자를 가져야 합니다. 예를 들어, `.png` 자산을 `.jpg` 파일로 교체할 수 없습니다.
- 동영상 자산은 교체할 수 없습니다.
- 교체 후 CDN 캐싱으로 인해 업데이트된 파일이 모든 소비자에게 표시되기까지 시간이 걸릴 수 있습니다.

### 처리된 이미지 사본이 있는 채널 {#channels-with-processed-image-copies}

일부 채널은 메시지 설정 시 이미지의 최적화된 사본을 생성하여 별도의 URL을 만듭니다. 원본 미디어 라이브러리 자산을 교체해도 해당 채널을 사용하여 생성된 메시지에서 소비자에게 표시되는 내용은 업데이트되지 않습니다. 여기에는 인앱 메시지, Content Cards, 푸시 알림, 배너가 포함됩니다.

[`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) 엔드포인트를 사용하여 프로그래밍 방식으로 자산을 교체할 수도 있습니다.

## 이미지 사양 {#image-specifications}

미디어 라이브러리에 업로드되는 모든 이미지는 5&nbsp;MB 미만이어야 합니다. 지원되는 파일 형식은 PNG, JPEG, GIF, SVG, WebP입니다. 메시징 채널별 권장 이미지 크기 및 사양은 [이미지 사양]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications)을 참조하세요.

{% alert important %}
매우 길쭉한 형태의 GIF(예: 3000 x 2 픽셀) 또는 300프레임 이상의 GIF는 전체 파일 크기가 작더라도 업로드에 실패할 수 있습니다.
{% endalert %}

## BrazeAI<sup>TM</sup>로 이미지 생성하기 {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
이 기능을 사용하기 전에 [데이터가 OpenAI로 어떻게 사용되고 전송되는지]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#ai-policy) 검토하세요.
{% endalert %}

**미디어 라이브러리** 페이지에 **AI Image Generator**가 표시되지 않는 경우, **Edit Media Library Assets** 권한이 있는지 확인하세요. 옵션이 여전히 표시되지 않으면 Braze 고객 팀에 문의하여 워크스페이스에서 BrazeAI 이미지 생성에 액세스할 수 있는지 확인하세요. 생성에 실패하면 [OpenAI 콘텐츠 정책]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#ai-policy)을 검토하세요.