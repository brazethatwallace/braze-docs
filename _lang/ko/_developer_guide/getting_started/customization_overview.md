---
nav_title: 커스터마이징 개요
article_title: 커스터마이징 개요
page_order: 10
description: "이 참조 문서에서는 SDK 메시징 채널을 커스터마이징하고 확장하는 데 필요한 핵심 개념을 다룹니다."
hidden: true
layout: redirect
redirect_to: /docs/developer_guide/getting_started/
---

# 커스터마이징 개요 {#customization-overview}

> Braze의 거의 모든 기능은 완벽하게 커스터마이징할 수 있습니다! 이 커스터마이징 가이드의 문서에서는 구성과 커스터마이징의 조합을 통해 Braze 경험을 개선하는 방법을 보여줍니다. 이 과정에서 마케팅 팀과 엔지니어링 팀은 긴밀히 협력하여 Braze 메시징 채널을 정확히 어떻게 커스터마이징할지 조율해야 합니다.

{% alert note %}
Braze SDK는 강력한 툴킷이지만, 크게 두 가지 중요한 기능을 제공합니다. 여러 플랫폼에서 통합 고객 프로필로 사용자 데이터를 수집 및 동기화하고, 인앱 메시지, 푸시 알림, Content Cards와 같은 메시징 채널을 처리합니다. 커스터마이징 가이드의 문서에서는 이미 [SDK 구현 프로세스]({{site.baseurl}}/developer_guide/home)를 완료했다고 가정합니다.
{% endalert %}

모든 Braze 구성요소는 접근성, 적응성 및 커스터마이징이 가능하도록 설계되었습니다. 따라서 기본 `BrazeUI` 구성요소로 시작하여 브랜드 요구 사항과 사용 사례에 맞게 커스터마이징하는 것을 권장합니다. Braze에서는 관련 노력과 제공되는 유연성 수준에 따라 커스터마이징을 세 가지 접근 방식으로 분류합니다. 이러한 접근 방식을 "Crawl", "Walk", "Run"이라고 합니다.

- **Crawl:** 기본 스타일링 옵션을 활용하여 빠르고 적은 노력으로 구현합니다.
- **Walk:** 기본 템플릿에 커스텀 스타일을 추가하여 브랜드 경험에 더 잘 어울리도록 합니다.
- **Run:** 스타일부터 동작, 크로스채널 연결에 이르기까지 메시징의 모든 부분을 커스터마이징합니다.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Crawl %}

![캡션 이미지 및 이미지 전용 Content Cards를 보여주는 샘플 금융 앱]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Crawl 접근 방식은 커스터마이징의 권한을 마케터에게 직접 부여합니다. 앱이나 사이트에 Braze 메시징 채널을 통합하기 위해 사전에 약간의 개발 작업이 필요하지만, 이 접근 방식을 사용하면 더 빠르게 시작하고 실행할 수 있습니다.

마케터는 대시보드를 통해 메시지의 콘텐츠, 오디언스 및 타이밍을 결정합니다. 하지만 스타일링 옵션은 제한적입니다. 이 접근 방식은 개발자 리소스가 제한적이거나 간단한 콘텐츠를 빠르게 공유하려는 팀에 가장 적합합니다.

<table aria-label="커스터마이징 개요">
  <caption>커스터마이징 개요</caption>
<thead>
  <tr>
    <th>커스터마이징</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>낮음</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>0~1시간</td>
  </tr>
  <tr>
    <td><b>카드 스타일</b></td>
    <td>기본 Braze 템플릿을 사용합니다.</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>기본 동작 옵션 중에서 선택합니다.</td>
  </tr>
  <tr>
    <td><b>분석 추적</b></td>
    <td>분석은 Braze에서 캡처됩니다.</td>
  </tr>
  <tr>
    <td><b>키-값 페어</b></td>
    <td>선택 사항이며, 추가 UI/UX 커스터마이징을 지원합니다.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Walk %}

![커스터마이징된 Content Cards를 보여주는 샘플 금융 앱]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

하이브리드 구현 방식인 Walk 접근 방식에서는 마케팅 팀과 개발자 팀이 함께 참여하여 앱 또는 사이트의 브랜딩에 맞춥니다.

구현 과정에서 개발자는 메시지 채널의 모양과 느낌을 브랜드에 더 부합하도록 업데이트하는 커스텀 코드를 작성합니다. 여기에는 글꼴 유형, 글꼴 크기, 둥근 모서리 및 색상 변경이 포함됩니다. 이 접근 방식은 여전히 기본 옵션을 사용하되, 프로그래밍 방식의 템플릿 스타일링을 적용합니다.

마케터는 Braze 대시보드에서 직접 오디언스, 콘텐츠, 클릭 시 동작 및 만료를 계속 관리할 수 있습니다.

<table aria-label="커스터마이징 개요">
  <caption>커스터마이징 개요</caption>
<thead>
  <tr>
    <th>커스터마이징</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>낮음</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>0~4시간</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>Braze 템플릿을 사용하거나 개발자가 직접 만든 템플릿을 사용합니다.</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>기본 동작 옵션 중에서 선택합니다.</td>
  </tr>
  <tr>
    <td><b>분석 추적</b></td>
    <td>기본 분석은 Braze에서 캡처됩니다.</td>
  </tr>
  <tr>
    <td><b>키-값 페어</b></td>
    <td>선택 사항이며, 추가 UI/UX 커스터마이징을 지원합니다.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Run %}

![이메일 캡처가 포함된 커스텀 Content Cards를 보여주는 샘플 금융 앱]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Run 접근 방식에서는 개발자가 주도적으로 사용자 경험을 완전히 제어합니다. 커스텀 코드가 메시지의 모양, 동작 방식, 다른 메시징 채널과의 상호 작용 방식(예: 푸시 알림을 기반으로 Content Card 트리거)을 결정합니다.

새로운 유형의 Content Cards나 맞춤형 UI가 포함된 인앱 메시지 등 완전히 새로운 커스텀 콘텐츠를 생성하는 경우, Braze SDK는 자동으로 [분석을 추적하지]({{site.baseurl}}/developer_guide/analytics) 않습니다. 마케터가 Braze 대시보드에서 노출 횟수, 클릭 수, 해제 등의 측정기준에 계속 액세스할 수 있도록 프로그래밍 방식으로 분석을 처리해야 합니다. SDK에서 이 데이터를 Braze에 다시 전달하도록 Braze SDK의 분석 메서드를 호출하세요. 각 메시징 채널에는 이를 용이하게 하는 분석 문서가 있습니다.

<table aria-label="커스터마이징 개요">
  <caption>커스터마이징 개요</caption>
<thead>
  <tr>
    <th>커스터마이징</th>
    <th>설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>노력</b></td>
    <td>사용 사례에 따라 다릅니다.</td>
  </tr>
    <tr>
    <td><b>개발자 작업</b></td>
    <td>적은 노력: 1~4시간<br>보통 노력: 4~8시간<br>많은 노력: 8시간 이상</td>
  </tr>
  <tr>
    <td><b>UI</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>동작</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>분석 추적</b></td>
    <td>커스텀</td>
  </tr>
  <tr>
    <td><b>키-값 페어</b></td>
    <td>필수</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
개발자와 구현자가 Braze용 커스텀 콘텐츠를 만들 때 마케터와 부서 간 협업의 기회가 생깁니다. 예를 들어 특정 구성요소에 대한 새로운 UI나 새로운 기능을 개발하는 경우, 새로운 동작과 백엔드와의 통합 방법을 문서화하여 팀이 성공할 수 있도록 준비하세요.
{% endalert %}