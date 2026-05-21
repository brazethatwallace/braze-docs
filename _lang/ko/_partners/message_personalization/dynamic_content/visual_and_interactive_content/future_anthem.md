---
nav_title: Future Anthem
article_title: Future Anthem
description: "이 참조 문서에서는 스포츠 베팅 및 iGaming 개인화를 위한 실시간 AI 플랫폼인 Future Anthem과 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> [Future Anthem](https://www.futureanthem.com/) 실시간 AI 플랫폼은 스포츠, 카지노, 빙고, 복권 전반에 걸쳐 개인화를 지원합니다. Braze 고객은 좋아하는 게임, 좋아하는 팀, 참여 점수, 다음 베팅 추천, 예상 다음 베팅 등 업계별 속성으로 플레이어 프로필을 강화할 수 있습니다.
>
> Real-time Experiences, Dynamic Audiences, Content Recommendations를 통해 제공되는 모든 속성은 실시간 플레이어 행동을 기반으로 구축되므로, Braze 고객은 즉각적으로 행동할 수 있습니다.

_이 통합은 Future Anthem에서 유지 관리합니다._

{% alert important %}
이 기능은 현재 얼리 액세스 단계입니다. 시작하려면 Future Anthem 고객 성공 팀에 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Future Anthem 계정 | Future Anthem 계정이 필요합니다. |
| Braze REST API 키 | [`users.track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 대한 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | 인스턴스에 맞는 Braze [REST 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)(예: `rest.iad-01.com`). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

이 통합을 통해 다음을 수행할 수 있습니다.

- 참여 점수가 높은 플레이어를 식별하고 독점 프로모션이나 VIP 보상과 같은 개인화된 오퍼로 타겟팅합니다.
- 플레이어가 이미 좋아하는 게임을 기반으로 유사한 게임을 추천합니다.

## 통합 {#integration}

Future Anthem 고객 성공 팀이 통합 설정을 도와드립니다. Future Anthem 고객 성공 담당자에게 문의하면 Braze에 전송할 가장 관련성 높은 속성을 식별하는 데 도움을 받을 수 있습니다.

| Future Anthem의 속성 예시 | Braze의 속성 예시 |
| ----------------------------------- | --------------------------- |
| ![플레이어의 프로필 속성을 보여주는 Future Anthem 대시보드.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Future Anthem에서 동기화된 커스텀 오브젝트 속성을 보여주는 Braze 고객 프로필.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integration" }

## Braze 커스텀 속성 {#braze-custom-attributes}

사용 가능한 Braze 커스텀 속성은 다음과 같습니다. 자세한 내용은 [Future Anthem: 시작하기](https://knowledge.futureanthem.com/getting-started)를 참조하세요.

{% tabs local %}
{% tab 베팅 추천 %}

| 하위 카테고리 | 예시 (JSON) | 데이터 유형 |
| ----------- | ---------------- | --------- |
| 사용자 선호도 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | 오브젝트 |
| 단일 베팅 추천 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | 오브젝트 |
| 누적 베팅 추천 (이벤트 라벨) | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | 오브젝트 |
| 누적 베팅 추천 (숫자 배당률) | `{"Bet_1": 1.5, "Bet_2": 2}` | 오브젝트 |
| 베팅 빌더 베팅 추천 | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | 오브젝트 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab 보너스 추천 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ----------- | ------- | --------- |
| NGR (순 게임 매출, 전체 기간) | 2232 | 숫자 |
| NGR14 (순 게임 매출, 최근 14일 활동) | 42 | 숫자 |
| 플레이어 수익성 점수 | 130 | 숫자 |
| 참여 점수 | 0.78 | 숫자 |
| 고객이탈 위험 점수 | 0.02 | 숫자 |
| 예상 다음 베팅 날짜 | 2024-08-29 | 시간 |
| Bet and Get 보너스 가치 추천 | 20 | 숫자 |
| 기타 보너스 가치 추천 | 0 | 숫자 |
| 미래 CLTV | 3126 | 숫자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab 게임 추천 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ----------- | ------- | --------- |
| 당신을 위한 추천 | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | 배열 |
| 좋아하는 게임 | Fishin' Frenzy | 배열 |
| 추천 신규 게임 | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | 배열 |
| 비슷한 플레이어가 플레이 중 (협업 필터링) | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | 배열 |
| 플레이한 게임 기반 추천 (게임 유사성) | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | 배열 |
| 다음 추천 (게임 시퀀싱) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | 배열 |
| 인기 게임 | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | 배열 |
| 트렌딩 게임 | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | 배열 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab 플레이어 클러스터 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ----------- | ------- | --------- |
| 플레이어가 속한 클러스터 표시 | High Value Game Diverse | 문자열 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab 플레이어 유지 (플레이어 잠재 위험) %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ----------- | ------- | --------- |
| 위험 점수 | 0.5 | 숫자 |
| 위험 플레이어 | True | 부울 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% endtabs %}