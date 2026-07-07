---
nav_title: "이메일 오브젝트"
article_title: 이메일 메시징 오브젝트
page_order: 5
page_type: reference
channel: email
description: "이 참조 문서에서는 Braze 이메일 오브젝트의 다양한 구성요소에 대해 설명합니다."

---

# 이메일 오브젝트 {#email-object}

> `email` 오브젝트를 사용하면 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 통해 이메일을 수정하거나 생성할 수 있습니다.

## 이메일 오브젝트

```json
{
  "app_id": (required, string), see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <user@example.com>"),
  "reply_to": (optional, valid email address in the format "user@example.com" - defaults to your workspace's default reply to if not set) - use "NO_REPLY_TO" to set reply-to address to null,
  "bcc": (optional, one of the BCC addresses defined in your workspace's email settings) if provided and the BCC feature is enabled for your account, this address gets added to your outbound message as a BCC address,
  "body": (required unless email_template_id is given, valid HTML),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "preheader": (optional*, string) recommended length 50-100 characters,
  "email_template_id": (optional, string) if provided, Braze uses the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case Braze overrides the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash) extra hash - for SendGrid users, this is passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash) hash of custom extensions headers (available for SparkPost, SendGrid, or Amazon SES),
  "should_inline_css": (optional, boolean) whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
    "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
}
```

- [앱 식별자]({{site.baseurl}}/api/identifier_types)
  - 워크스페이스에 구성된 앱의 유효한 `app_id`는 사용자의 프로필에 해당 앱이 있는지 여부와 관계없이 워크스페이스의 모든 사용자에게 적용됩니다.
- 프리헤더에 대한 자세한 정보와 모범 사례는 [이메일 스타일링]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling)을 참조하세요.

{% alert warning %}
첨부파일의 `url`에 Google 드라이브 링크를 사용하면 파일을 가져오기 위한 서버 호출이 차단되어 이메일 메시지가 전송되지 않을 수 있으므로 사용하지 않는 것이 좋습니다.
{% endalert %}

유효한 첨부 파일 유형은 다음과 같습니다: `txt`, `csv`, `log`, `css`, `ics`, `jpg`, `jpe`, `jpeg`, `gif`, `png`, `bmp`, `psd`, `tif`, `tiff`, `svg`, `indd`, `ai`, `eps`, `doc`, `docx`, `rtf`, `odt`, `ott`, `pdf`, `pub`, `pages`, `mobi`, `epub`, `mp3`, `m4a`, `m4v`, `wma`, `ogg`, `flac`, `wav`, `aif`, `aifc`, `aiff`, `mp4`, `mov`, `avi`, `mkv`, `mpeg`, `mpg`, `wmv`, `xls`, `xlsx`, `ods`, `numbers`, `odp`, `ppt`, `pptx`, `pps`, `key`, `zip`, `vcf`, `pkpass`.

`email_template_id`는 HTML 편집기로 생성한 이메일 템플릿 하단에서 확인할 수 있습니다. 다음은 이 ID가 어떻게 표시되는지 보여주는 예시입니다:

![HTML 이메일 템플릿의 API 식별자 섹션.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:70%;"}

## 첨부 파일이 포함된 이메일 오브젝트 예시 {#example-email-object-with-attachment}

```json
{
  "external_user_ids": ["YOUR_EXTERNAL_USER_ID"],
  "messages":{
     "email":{
        "app_id":"YOUR_APP_ID",
        "attachments":[{
            "file_name":"YourFileName",
            "url":"https://exampleurl.com/YourFileName.pdf"
         }]
     }
  }
}
```

## 이메일 첨부 파일 인증 {#authentication-for-email-file-attachments}

1. **설정** > **연결된 콘텐츠**로 이동하고 **자격 증명 추가**를 클릭하여 인증 자격 증명을 추가합니다.
2. 이름을 입력하고 사용자 이름과 비밀번호를 추가합니다.
3. `/messages/send` 엔드포인트의 이메일 오브젝트에 첨부 파일 세부 정보에서 자격 증명 이름을 지정하는 `basic_auth_credential` 속성을 포함합니다. 자격 증명 이름이 `company_basic_auth_credential_name`인 다음 예시를 참조하세요:

```json
{
  "external_user_ids": ["recipient_user_id"],
  "messages":{
    "email":{
      "app_id": "153e8a29-fd6d-4f77-ade7-1a4ca08d457a",
      "subject": "Basis auth attachment test",
      "from": "mail <mail@example.com>",
      "body": "my attachment test",
      "attachments":[
        { "file_name":"checkout_receipt.pdf",
        "url":"https://fileserver.company.com/user123-checkout_receipt.pdf",
        "basic_auth_credential": "company_basic_auth_credential_name" }
      ]
    }
  }
}
```

## 첨부 파일 검색, 캐싱 및 성능 {#attachment-retrieval-caching-and-performance}

Braze가 첨부 파일 `url`에서 파일을 가져올 때:

- **캐싱:** Braze는 최근에 가져온 파일을 약 24시간 동안 재사용할 수 있습니다. 매 발송 시 새 버전의 파일을 즉시 가져와야 하는 경우, 버전별로 고유한 URL을 사용하세요(예: 파일이 변경될 때 경로 또는 쿼리가 변경되도록 설정).
- **타임아웃:** 호스트는 빠르게 응답해야 합니다. 첨부 파일 URL이 느리거나 응답하지 않으면 메시지 발송이 실패할 수 있습니다. 약 2분 이내에 응답하는 것을 목표로 하세요.
- **보안:** 첨부 파일 URL(쿼리 문자열 포함)에 개인 식별 정보(PII)나 비밀 정보를 포함하지 마세요. URL이 로그나 다운스트림 시스템에 노출될 수 있습니다.
- **방화벽:** URL이 특정 네트워크에서만 접근 가능한 경우, [연결된 콘텐츠 IP 허용 목록]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)에 따라 Braze의 트래픽을 허용하세요. 파일에 로그인이 필요한 경우 [기본 인증 자격 증명](#authentication-for-email-file-attachments)을 사용하세요.