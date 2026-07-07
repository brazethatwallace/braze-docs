---
nav_title: Digioh
article_title: Digioh
description: "이 참조 문서에서는 Braze Campaigns를 통해 참여를 유도하는 팝업, 양식, 설문조사 및 커뮤니케이션 환경설정 센터를 만들 수 있는 설문조사 플랫폼인 Braze와 Digioh의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/)는 리스트 성장, 퍼스트파티 데이터 수집, 그리고 해당 데이터를 Braze Campaigns에 사용할 수 있도록 지원합니다.

_이 통합은 Digioh에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Digioh 통합을 통해 드래그 앤 드롭 빌더를 사용하여 온브랜드 양식, 팝업, 환경설정 센터, 랜딩 페이지, 설문조사를 만들어 고객과 연결할 수 있습니다. Digioh는 통합 설정을 지원하고 첫 번째 캠페인을 구축, 디자인 및 실행할 수 있습니다.

!["Digioh로 유연한 이메일 및 커뮤니케이션 환경설정 센터 만들기"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Digioh 계정 | 이 파트너십을 활용하려면 [Digioh 계정](https://www.digioh.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze API `/users/track/` 엔드포인트 | `/users/track/` 세부 정보가 추가된 REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/api/basics/#endpoints)에 따라 달라집니다.<br><br>예를 들어, REST API 엔드포인트가 `https://rest.iad-01.braze.com`이면 `/users/track/` 엔드포인트는 `https://rest.iad-01.braze.com/users/track/`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Digioh를 통합하려면 먼저 Braze 커넥터를 구성해야 합니다. 완료되면 라이트박스(위젯)에 통합을 적용해야 합니다. 통합 기본 사항에 대해 자세히 알아보려면 [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/)를 방문하세요.

### 1단계: Digioh 통합 생성 {#step-1-create-digioh-integration}

Digioh에서 **Integrations** 탭을 클릭한 다음 **New Integration** 버튼을 클릭합니다. **Integration** 드롭다운에서 **Braze**를 선택하고 통합의 이름을 지정합니다.

!["드롭다운에서 올바른 통합 선택"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

다음으로, Braze REST API 키와 Braze API `/users/track/` 엔드포인트를 입력합니다.

마지막으로, 필드 매핑 섹션을 사용하여 이메일과 이름 외에 추가 커스텀 필드를 매핑합니다. 다음 코드 스니펫은 예시 페이로드를 보여줍니다. 완료되면 **Create Integration**을 선택합니다.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### 2단계: Digioh 라이트박스 생성 {#step-2-create-a-digioh-lightbox}

Digioh [디자인 편집기](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)를 사용하여 라이트박스(위젯)를 만듭니다. <br>
디자인 편집기를 활용하는 다양한 방법의 갤러리를 보고 싶으신가요? Digioh [테마 갤러리](https://www.digioh.com/theme-gallery)를 방문하세요.

### 3단계: 통합 적용 {#step-3-apply-integration}

이 통합을 Digioh [라이트박스](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)에 적용하려면 **Boxes** 페이지로 이동하여 **Integrations** 열에서 **Add** 또는 **Edit** 링크를 선택합니다. 편집기의 **Integration** 섹션에서도 추가할 수 있습니다.

!["라이트박스에 통합 추가"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

여기에서 **Add Integration**을 선택하고 원하는 통합을 선택한 다음 **Save**를 클릭합니다. 이제 Digioh가 캡처한 리드를 실시간으로 Braze에 전달합니다.