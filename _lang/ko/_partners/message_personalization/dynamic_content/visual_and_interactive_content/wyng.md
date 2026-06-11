---
nav_title: Wyng
article_title: Wyng
description: "이 참고 문서에서는 마이크로 경험, 고객 선호도 포털 및 API 플랫폼을 통해 고객 선호도와 속성을 수집, 사용 및 통합하는 데 사용되는 제로파티 데이터 플랫폼인 Braze와 Wyng의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/)은 중요한 순간에 소비자의 참여를 유도하고, 선호도 및 기타 제로파티 데이터를 수집하며, 실시간으로 개인화할 수 있는 대화형 디지털 경험(퀴즈, 환경설정 센터, 프로모션)을 구축하는 도구를 제공합니다.

_이 통합은 Wyng에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Wyng 통합을 사용하면 Wyng 경험을 통해 수집한 제로파티 데이터를 활용하여 Braze Campaigns 및 Braze Canvas에서 상호작용을 개인화할 수 있습니다. Wyng은 환경설정 센터를 지원하여 소비자가 브랜드와 공유하는 데이터 및 선호도(커뮤니케이션 선호도 포함)를 직접 제어할 수 있도록 합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Wyng 계정 | 이 파트너십을 활용하려면 Wyng 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Braze 통합 연결 {#step-1-connect-the-braze-integration}

Wyng에서 [**Integrations**](https://wyng.com/dashboard/integrations/)로 이동하여 **Add** 탭을 선택합니다. 다음으로, **Braze** 위로 마우스를 가져가서 통합을 위해 **Connect**를 클릭합니다.

![Wyng 플랫폼의 Braze 파트너 타일.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### 2단계: Braze 커넥터 구성 {#step-2-configure-the-braze-connector}

1. 열리는 구성 창에서 Braze REST API 키를 입력합니다.
![자격 증명 프롬프트의 모습을 보여주는 이미지.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. 다음으로, 드롭다운을 사용하여 Braze와 공유할 Wyng 캠페인을 선택합니다.![Braze와 공유할 기존 Wyng 캠페인을 선택하라는 Braze 커넥터 프롬프트를 보여주는 이미지.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로, 구독, 속성 및 이벤트 오브젝트, 커스텀 이벤트를 설정해야 합니다.<br><br>
- **구독 설정(필수)**<br>
사용자를 구독 그룹에 가입시키려면 **Add Subscription**을 클릭하고 구독 그룹 이름과 ID를 추가합니다. 여러 그룹 이름과 ID를 추가하려면 **Add Subscription** 버튼을 다시 클릭합니다.<br>![구독 그룹 이름과 ID를 입력하라는 이미지.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **사용자 추적 설정**<br>
**Add custom property**를 클릭하여 `/users/track` 엔드포인트로 전송할 속성 및 이벤트 오브젝트 쌍을 추가합니다. 이를 사용하여 통합을 위해 전송되는 각 데이터 트랜잭션에 하드코딩된 속성 값을 추가할 수 있습니다. 여러 속성을 추가하려면 **Add custom property** 버튼을 다시 클릭합니다.<br>![속성 커스텀 속성을 추가하라는 프롬프트가 표시된 이미지.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **커스텀 이벤트 전송**<br>
선택적으로 **Sending custom event**를 활성화할 수 있습니다. 활성화된 경우 이벤트 이름과 해당 앱 ID를 포함해야 합니다.<br>![필요한 경우 커스텀 이벤트를 전송하라는 프롬프트가 표시된 이미지.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. 마지막으로, 사용 사례에 따라 Wyng 필드를 Braze API 필드에 매핑해야 합니다. **Select a field**를 클릭하여 매핑할 필드를 선택한 다음 통합을 **Save**합니다. 저장되면 이러한 매핑된 필드는 **Integrations > Manage** 아래에서 확인할 수 있습니다.
![다양한 Wyng 필드를 특정 Braze 필드에 매핑할 수 있는 예시.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![사용 가능한 동기화 필드 목록.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### 3단계: 통합 테스트 {#step-3-test-your-integration}

Wyng에서 Wyng 캠페인의 양식 제출을 테스트합니다. 메인 프로덕션 캠페인에 레코드를 추가하지 않으려면 미리보기 캠페인에서 제출할 수도 있습니다. **Integration** 대시보드에서 성공적인 트랜잭션을 확인할 수 있습니다.

## 이 통합 사용하기 {#using-this-integration}

데이터 커넥터가 설정되면 Wyng에서 생성되어 Braze에 추가된 모든 필드를 다른 데이터 필드와 마찬가지로 캠페인 트리거, 오디언스 세분화 또는 개인화된 콘텐츠 제공에 사용할 수 있습니다.

활용 범위는 광범위하며, 구체적인 질문은 [contact@wyng.com](mailto:contact@wyng.com) 또는 담당 계정 매니저에게 문의할 수 있습니다.

## 문제 해결 {#troubleshooting}

### 제출 실패 {#failed-submission}

Braze에 데이터를 전송할 때 제출이 실패한 경우, **View Log** 링크를 클릭하여 실패한 제출 및 관련 오류 메시지를 검토합니다.

![작업 헤더 아래에 있는 "View Log" 링크.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

로그 페이지에는 실패한 제출, 재시도 횟수, 제출 데이터, 오류 및 제출을 다시 푸시하는 링크가 표시됩니다.

![실패한 제출이 표시되는 예시.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

**View Error** 섹션에는 오류 코드와 오류 원인에 대한 추가 정보가 표시됩니다. 그런 다음 오류 코드를 Braze와 대조하여 원인을 확인할 수 있습니다.

![Wyng 플랫폼에 표시된 예시 오류 로그.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

추가 질문이 있는 경우 Wyng 고객지원팀([support@wyng.com](mailto:contact@wyng.com))에 문의하여 도움을 받으세요.