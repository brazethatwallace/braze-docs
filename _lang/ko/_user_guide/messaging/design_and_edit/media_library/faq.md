---
nav_title: FAQ
article_title: 미디어 라이브러리 FAQ
page_order: 2
page_type: FAQ
tool: Media
description: "이 문서에서는 Braze의 미디어 라이브러리에 대해 자주 묻는 질문에 대한 답변을 제공합니다."

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 Braze의 미디어 라이브러리에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 일반 {#general}

### 미디어 라이브러리 내 이미지의 저장 용량 제한이 있나요? {#are-there-storage-limits-for-images-within-the-media-library}

아니요, 미디어 라이브러리 내 에셋에 대한 저장 용량 제한은 없습니다. 다만, 에셋의 크기 제한은 있습니다(최대 5 MB).

### 업로드된 에셋에 만료일이 있나요? {#are-there-expiration-dates-for-uploaded-assets}

아니요, 미디어 라이브러리에 업로드된 에셋은 Braze와의 계약 기간 동안 유지됩니다.

### 비디오 에셋을 업로드할 수 있나요? {#can-i-upload-video-assets}

아니요, 미디어 라이브러리는 비디오 파일을 지원하지 않습니다. 외부에서 호스팅하거나 YouTube와 같은 플랫폼을 사용하는 것을 권장합니다.

### 모든 이미지 유형을 자를 수 있나요? {#can-i-crop-all-image-types}

아니요, 미디어 라이브러리는 GIF 이미지 자르기를 지원하지 않습니다.

### 미디어 라이브러리에 업로드된 이미지의 URL을 어떻게 복사하나요? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

미디어 라이브러리에 업로드된 이미지의 URL을 복사하려면 **콘텐츠** > **미디어 라이브러리**로 이동하세요. 참조하려는 이미지 위에 마우스를 올린 다음 **이미지 URL 복사** 아이콘을 선택하여 이미지 URL을 클립보드에 복사하세요.

### 이메일에서 SVG 이미지를 사용할 수 있나요? {#can-i-use-svg-images-in-email}

SVG 이미지는 이메일 클라이언트 간 지원이 제한적이므로 이메일에 권장되지 않습니다. Gmail 및 기타 주요 이메일 제공업체에서는 SVG 이미지를 렌더링하지 않으므로 수신자에게 이미지가 깨지거나 누락될 수 있습니다. 안정적인 이메일 렌더링을 위해 PNG, JPEG 또는 GIF 형식을 사용하세요.

### 기존 이미지를 어떻게 자르나요? {#how-do-i-crop-an-existing-image}

미디어 라이브러리에서 이미지를 선택하고 **자르기 및 새 이미지로 저장**을 클릭하여 기존 이미지를 자를 수 있습니다.

![미디어 라이브러리 이미지 미리보기.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

그러면 비율 유형을 선택하고 새 이미지의 이름을 편집할 수 있는 자르기 편집기로 리디렉션됩니다. **저장**을 선택하면 새 이미지를 사용할 수 있습니다.

![미디어 라이브러리 이미지를 자르고 저장하는 창.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### 이미지를 업로드하려고 할 때 계속 시간 초과가 발생합니다. 어떻게 해야 하나요? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

다양한 이유로 발생할 수 있지만, 일반적인 해결 방법은 업로드를 시도하기 전에 이미지를 최적화하는 것입니다. [ImageOptim](https://imageoptim.com/mac)과 같은 이미지 최적화 도구를 통해 이미지를 처리하세요.

또한 이미지가 Photoshop(또는 유사한 소프트웨어)에서 만들어졌고 레이어가 많은 경우, 레이어를 병합하고 수를 줄이는 것도 도움이 될 수 있습니다.

### 이미지가 5 MB 미만이고 지원되는 형식인데도 업로드 시 "예기치 않은 오류"가 표시됩니다. 무엇이 문제인가요? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

이 문제는 주로 두 가지 이유로 발생할 수 있습니다:

1. **파일의 잘못된 메타데이터:** Braze가 이미지를 처리하는 데 사용하는 소프트웨어가 유효하지 않거나 호환되지 않는 메타데이터가 있는 파일을 거부할 수 있습니다. 경우에 따라 파일이 처리되는 과정에서 5 MB 제한을 초과할 수도 있습니다. 다른 이미지를 사용하거나(예: 이미지 편집기에서 다시 내보내기 또는 다시 저장) 다른 소스의 이미지를 사용해 보세요.
2. **파일 이름의 특수 문자:** `&`나 `%`와 같은 특수 문자가 포함된 파일 이름은 업로드 실패를 유발할 수 있습니다. 파일 이름을 문자, 숫자, 하이픈 또는 밑줄만 사용하도록 변경한 후 다시 업로드해 보세요.

### 푸시 작성기에 원하는 이미지를 업로드할 수 없는 이유는 무엇인가요? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

대부분의 작성기에는 허용되는 이미지 비율 크기에 대한 제한이 있기 때문입니다.

### AI를 사용하여 이미지 생성 {#generate-an-image-using-ai}

**콘텐츠** > **미디어 라이브러리**에서 **AI 이미지 생성기**를 선택하여 이미지를 생성할 수 있습니다. **미디어 라이브러리 에셋 편집** 권한이 필요합니다. 옵션이 보이지 않으면 Braze 고객 팀에 문의하세요. 단계 및 정책 세부 사항은 [BrazeAI로 이미지 생성]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) 및 [BrazeAI로 이미지 생성하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai)를 참조하세요.

### 미디어 라이브러리 이미지 에셋에 대한 커스텀 URL을 만들 수 있나요? {#can-i-create-vanity-urls-for-media-library-image-assets}

미디어 라이브러리 에셋에 대한 커스텀 URL은 지원되지 않습니다. 커스텀 URL은 CDN 전달을 중단시킬 수 있기 때문입니다. Campaigns에서 이미 해당 URL을 참조하고 있는 경우 기존 URL의 이미지를 교체할 수 있습니다. 자세한 내용은 [파일 교체]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file)를 참조하세요.

### Chrome에서 JPEG 또는 PNG 이미지를 WebP 파일로 저장하는 이유는 무엇인가요? {#why-does-chrome-save-jpeg-or-png-images-as-webp-files}

Chrome을 사용하여 미디어 라이브러리에서 이미지를 저장할 때, 브라우저가 JPEG 또는 PNG 파일을 자동으로 WebP 형식으로 변환할 수 있습니다. 이는 이미지 다운로드에 대한 Chrome의 기본 동작이며 Braze에만 해당되는 것은 아닙니다. 원본 형식으로 이미지를 저장해야 하는 경우 Safari 또는 Firefox와 같은 다른 브라우저를 사용해 보세요.