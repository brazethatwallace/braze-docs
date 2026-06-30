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

## 기본설정 {#general}

### 미디어 라이브러리 내 이미지에 대한 저장 용량 제한이 있나요? {#are-there-storage-limits-for-images-within-the-media-library}

아니요, 미디어 라이브러리 내 자산에 대한 저장 용량 제한은 없습니다. 다만, 자산의 크기 제한은 있습니다(최대 5 MB).

### 업로드된 자산에 만료일이 있나요? {#are-there-expiration-dates-for-uploaded-assets}

아니요, 미디어 라이브러리에 업로드된 자산은 Braze와의 계약 기간 동안 유지됩니다.

### 동영상 자산을 업로드할 수 있나요? {#can-i-upload-video-assets}

아니요, 미디어 라이브러리는 동영상 파일을 지원하지 않습니다. 외부에서 호스팅하거나 YouTube와 같은 플랫폼을 이용하는 것을 권장합니다.

### 모든 이미지 유형을 자를 수 있나요? {#can-i-crop-all-image-types}

아니요, 미디어 라이브러리는 GIF 이미지 자르기를 지원하지 않습니다.

### 기존 이미지를 어떻게 자르나요? {#how-do-i-crop-an-existing-image}

미디어 라이브러리에서 이미지를 선택하고 **Crop & Save New Image**를 클릭하면 기존 이미지를 자를 수 있습니다.

![미디어 라이브러리 이미지 미리보기.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

그러면 비율 유형을 선택하고 새 이미지의 이름을 편집할 수 있는 자르기 작성기로 이동합니다. **Save**를 선택하면 새 이미지를 사용할 수 있습니다.

![미디어 라이브러리 이미지를 자르고 저장하는 창.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### 이미지를 업로드하려고 할 때 계속 시간 초과가 발생합니다. 어떻게 해야 하나요? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

이 문제는 다양한 이유로 발생할 수 있지만, 일반적인 해결 방법은 업로드를 시도하기 전에 이미지를 최적화하는 것입니다. [ImageOptim](https://imageoptim.com/mac)과 같은 이미지 최적화 도구를 사용하여 이미지를 처리해 보세요.

또한, Photoshop(또는 유사한 소프트웨어)에서 만든 이미지에 레이어가 많은 경우, 레이어를 병합하고 줄이는 것도 도움이 될 수 있습니다.

### 이미지가 5 MB 미만이고 지원되는 형식인데도 업로드할 때 "예기치 않은 오류"가 표시됩니다. 무엇이 문제인가요? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

이 문제는 주로 두 가지 이유로 발생할 수 있습니다:

1. **파일의 잘못된 메타데이터:** Braze가 이미지를 처리하는 데 사용하는 소프트웨어가 유효하지 않거나 호환되지 않는 메타데이터가 있는 파일을 거부할 수 있습니다. 경우에 따라 파일이 처리되면서 5 MB 제한을 초과할 수도 있습니다. 다른 이미지를 사용하거나(예: 이미지 편집기에서 다시 내보내기 또는 다시 저장) 다른 소스의 이미지를 사용해 보세요.
2. **파일 이름의 특수 문자:** `&`나 `%`와 같은 특수 문자가 포함된 파일 이름은 업로드 실패를 유발할 수 있습니다. 파일 이름을 문자, 숫자, 하이픈 또는 밑줄만 사용하도록 변경한 후 다시 업로드해 보세요.

### 푸시 작성기에서 원하는 이미지를 아무거나 업로드할 수 없는 이유는 무엇인가요? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

대부분의 작성기에는 허용되는 이미지 비율 크기에 대한 제한이 있기 때문입니다.

### AI를 사용하여 이미지 생성 {#generate-an-image-using-ai}

**콘텐츠** > **미디어 라이브러리**에서 **AI Image Generator**를 선택하여 이미지를 생성할 수 있습니다. **미디어 라이브러리 자산 편집** 권한이 필요합니다. 해당 옵션이 보이지 않으면 Braze 고객지원 팀에 문의하세요. 단계 및 정책 세부 정보는 [BrazeAI로 이미지 생성]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) 및 [BrazeAI로 이미지 생성하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai)를 참조하세요.

### 미디어 라이브러리 이미지 자산에 대해 커스텀 URL을 만들 수 있나요? {#can-i-create-vanity-urls-for-media-library-image-assets}

미디어 라이브러리 자산에 대한 커스텀 URL은 지원되지 않습니다. 커스텀 URL을 사용하면 CDN 전달이 중단되기 때문입니다. Campaign에서 이미 해당 URL을 참조하고 있는 경우 기존 URL에서 이미지를 교체할 수 있습니다. 자세한 내용은 [파일 교체]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file)를 참조하세요.