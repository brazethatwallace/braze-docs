---
nav_title: 메시지 크레딧 - Lambda
permalink: "/message_credits_lambda_k5gh/"
hidden: true
noindex: true
hide_toc: true
---

# 메시지 크레딧 - Lambda (기밀) {#message-credits-lambda-confidential}

> 메시지 크레딧은 Braze의 네이티브 에이전트 콘솔, SMS, MMS, RCS, WhatsApp, LINE 제품을 아우르는 크로스 제품 패키징 구조입니다. 메시지 크레딧은 Braze 메시징 채널과 특정 AI 기능을 활용할 때 유연하고 투명한 경험을 제공합니다. 크레딧을 통해 이 페이지의 표에 제시된 모든 채널에 접근할 수 있습니다.

{% alert note %}
제품마다 리포팅에서 사용하는 측정 단위가 다릅니다.<br><br>
<b>에이전트 콘솔:</b> 호출(Invocations)<br>
<b>SMS:</b> Segments<br>
<b>MMS:</b> 발송<br>
<b>WhatsApp:</b> 메시지<br>
<b>RCS:</b> Segments, 발송<br>
<b>LINE:</b> 발송<br>
<b>KakaoTalk:</b> 발송<br>

마지막으로, SMS, MMS, RCS와 관련된 통신사 수수료는 별도로 후불 청구되며 이 메시지 크레딧 SKU의 일부로 간주되지 않습니다.
{% endalert %}

## 정의 {#definitions}

열 정의는 다음과 같습니다.

|---------|-------------------------------------------------|
| **대상** | Braze 플랫폼을 통해 발송되는 특정 최종 지역, 국가 또는 동작 유형 |
| **1회 발송당 크레딧** | 1회 발송을 수행하는 데 필요한 정확한 메시지 크레딧 수<br>(발송당 크레딧 = 크레딧 비율 × 대상 배수) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## 메시지 크레딧 - Lambda 크레딧 비율 표 {#credit-ratio-table-for-message-credits-lambda}

{% details 펼치려면 클릭하세요 %}
<table class="credits-table" aria-label="메시지 크레딧 - Lambda 크레딧 비율 표">
    <colgroup>
        <col span="3">
        <col class="col-highlight">
    </colgroup>
    <thead>
    <tr>
        <th><b>채널</b></th>
        <th><b>대상</b></th>
        <th class="credits-column"><b>1회 발송당 크레딧</b></th>
    </tr>
    <tr>
        <td>에이전트 콘솔</td>
        <td>Braze Auto</td>
        <td>1.60</td>
    </tr>
    </thead>
    <tbody>
<tr>
        <td>에이전트 콘솔</td>
        <td>BYO LLM API 키</td>
        <td>0.16</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>캐나다</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>캐나다 수신자 부담</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>미국</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>미국 수신자 부담</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>캐나다 긴 코드</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>캐나다 짧은 코드</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>캐나다 수신자 부담</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>미국</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>미국 수신자 부담</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>압하지야</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아프가니스탄</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>알바니아</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>알제리</td>
        <td>32.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아메리칸사모아</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>안도라</td>
        <td>11.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>앙골라</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>앵귈라</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>앤티가 바부다</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아르헨티나</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아르메니아</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아루바</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>호주 SMS</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>오스트리아</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아제르바이잔</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>바하마</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>바레인</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>방글라데시</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>바베이도스</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>벨라루스</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>벨기에</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>벨리즈</td>
        <td>16.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>베냉</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>버뮤다</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>부탄</td>
        <td>25.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>볼리비아</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>보스니아 헤르체고비나</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>보츠와나</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>브라질</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>브루나이</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>불가리아</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>부르키나파소</td>
        <td>14.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>부룬디</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>캄보디아</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>카메룬</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>카보베르데</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>카리브 네덜란드</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>케이맨 제도</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>중앙아프리카공화국</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>차드</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>칠레</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>중국</td>
        <td>1.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>콜롬비아</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>코모로</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>콩고</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>쿡 제도</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>코스타리카</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>크로아티아</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>쿠바</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>퀴라소</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>키프로스</td>
        <td>2.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>체코</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>덴마크</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>지부티</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>도미니카</td>
        <td>9.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>도미니카공화국</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>콩고민주공화국</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>에콰도르</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>이집트</td>
        <td>21.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>엘살바도르</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>적도 기니</td>
        <td>5.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>에리트레아</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>에스토니아</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>에스와티니</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>에티오피아</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>포클랜드 제도</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>페로 제도</td>
        <td>2.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>피지</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>핀란드</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>프랑스</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>프랑스령 기아나</td>
        <td>20.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>프랑스령 폴리네시아</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>가봉</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>감비아</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>조지아</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>독일</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>가나</td>
        <td>17.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>지브롤터</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>그리스</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>그린란드</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>그레나다</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>과들루프</td>
        <td>20.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>괌</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>과테말라</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>건지</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>기니</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>기니비사우</td>
        <td>14.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>가이아나</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아이티</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>온두라스</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>홍콩</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>헝가리</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아이슬란드</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>인도</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>인도네시아</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>이란</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>이라크</td>
        <td>23.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아일랜드</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>맨섬</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>이스라엘</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>이탈리아</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>코트디부아르</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>자메이카</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>일본</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>저지</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>요르단</td>
        <td>25.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>카자흐스탄</td>
        <td>25.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>케냐</td>
        <td>22.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>키리바시</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>대한민국</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>코소보</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>쿠웨이트</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>키르기스스탄</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>라오스</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>라트비아</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>레바논</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>레소토</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>라이베리아</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>리비아</td>
        <td>26.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>리히텐슈타인</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>리투아니아</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>룩셈부르크</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>마카오</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>마다가스카르</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>말라위</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>말레이시아</td>
        <td>7.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몰디브</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>말리</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몰타</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>마르티니크</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>모리타니</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>모리셔스</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>마요트</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>멕시코</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>미크로네시아</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몰도바</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>모나코</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몽골</td>
        <td>19.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몬테네그로</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>몬트세랫</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>모로코</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>모잠비크</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>미얀마</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>나미비아</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>나우루</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>네팔</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>네덜란드</td>
        <td>18.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>뉴칼레도니아</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>뉴질랜드</td>
        <td>14.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>니카라과</td>
        <td>12.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>니제르</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>나이지리아</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>북마케도니아</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>북키프로스</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>노르웨이</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>오만</td>
        <td>16.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>파키스탄</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>팔라우</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>파나마</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>파푸아뉴기니</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>파라과이</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>페루</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>필리핀</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>폴란드</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>포르투갈</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>푸에르토리코</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>카타르</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>레위니옹/마요트</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>루마니아</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>러시아</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>르완다</td>
        <td>12.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세인트키츠 네비스</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세인트루시아</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>생피에르 미클롱</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세인트빈센트 그레나딘</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>사모아</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>상투메 프린시페</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>사우디아라비아</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세네갈</td>
        <td>20.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세르비아</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>세이셸</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>시에라리온</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>싱가포르</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>신트마르턴</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>슬로바키아</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>슬로베니아</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>솔로몬 제도</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>소말리아</td>
        <td>17.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>남아프리카공화국</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>남오세티야</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>남수단</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>스페인</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>스리랑카</td>
        <td>25.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>수단</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>수리남</td>
        <td>7.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>스웨덴</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>스위스</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>대만</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>타지키스탄</td>
        <td>34.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>탄자니아</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>태국</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>동티모르</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>토고</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>통가</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>트리니다드 토바고</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>튀니지</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>튀르키예</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>투르크메니스탄</td>
        <td>19.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>터크스 케이커스 제도</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>우간다</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>우크라이나</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>아랍에미리트</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>영국</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>우루과이</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>우즈베키스탄</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>바누아투</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>베네수엘라</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>베트남</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>영국령 버진아일랜드</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>왈리스 푸투나</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>예멘</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>잠비아</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>짐바브웨</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아르헨티나 인증</td>
        <td>7.67</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아르헨티나 마케팅</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아르헨티나 마케팅 - 최적화 전달</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아르헨티나 유틸리티</td>
        <td>7.67</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>브라질 인증</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>브라질 마케팅</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>브라질 마케팅 - 최적화 전달</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>브라질 유틸리티</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>칠레 인증</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>칠레 마케팅</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>칠레 마케팅 - 최적화 전달</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>칠레 유틸리티</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>콜롬비아 인증</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>콜롬비아 마케팅</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>콜롬비아 마케팅 - 최적화 전달</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>콜롬비아 유틸리티</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이집트 인증</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이집트 인증 국제</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이집트 마케팅</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이집트 마케팅 - 최적화 전달</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이집트 유틸리티</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>프랑스 인증</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>프랑스 마케팅</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>프랑스 마케팅 - 최적화 전달</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>프랑스 유틸리티</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>독일 인증</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>독일 마케팅</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>독일 마케팅 - 최적화 전달</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>독일 유틸리티</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도 인증</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도 인증 국제</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도 마케팅</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도 마케팅 - 최적화 전달</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도 유틸리티</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도네시아 인증</td>
        <td>6.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도네시아 인증 국제</td>
        <td>36.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도네시아 마케팅</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도네시아 마케팅 - 최적화 전달</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>인도네시아 유틸리티</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이스라엘 인증</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이스라엘 마케팅</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이스라엘 마케팅 - 최적화 전달</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이스라엘 유틸리티</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이탈리아 인증</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이탈리아 마케팅</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이탈리아 마케팅 - 최적화 전달</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>이탈리아 유틸리티</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>말레이시아 인증</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>말레이시아 인증 국제</td>
        <td>11.09</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>말레이시아 마케팅</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>말레이시아 마케팅 - 최적화 전달</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>말레이시아 유틸리티</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>멕시코 인증</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>멕시코 마케팅</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>멕시코 마케팅 - 최적화 전달</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>멕시코 유틸리티</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>네덜란드 인증</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>네덜란드 마케팅</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>네덜란드 마케팅 - 최적화 전달</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>네덜란드 유틸리티</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>나이지리아 인증</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>나이지리아 인증 국제</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>나이지리아 마케팅</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>나이지리아 마케팅 - 최적화 전달</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>나이지리아 유틸리티</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>북미 인증</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>북미 마케팅</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>북미 마케팅 - 최적화 전달</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>북미 유틸리티</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 인증</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 마케팅</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 마케팅 - 최적화 전달</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 유틸리티</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>파키스탄 인증</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>파키스탄 인증 국제</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>파키스탄 마케팅</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>파키스탄 마케팅 - 최적화 전달</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>파키스탄 유틸리티</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>페루 인증</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>페루 마케팅</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>페루 마케팅 - 최적화 전달</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>페루 유틸리티</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아프리카 인증</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아프리카 마케팅</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아프리카 마케팅 - 최적화 전달</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아프리카 유틸리티</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아시아 태평양 인증</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아시아 태평양 마케팅</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아시아 태평양 마케팅 - 최적화 전달</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 아시아 태평양 유틸리티</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중앙 및 동유럽 인증</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중앙 및 동유럽 마케팅</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중앙 및 동유럽 마케팅 - 최적화 전달</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중앙 및 동유럽 유틸리티</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 라틴 아메리카 인증</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 라틴 아메리카 마케팅</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 라틴 아메리카 마케팅 - 최적화 전달</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 라틴 아메리카 유틸리티</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중동 인증</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중동 마케팅</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중동 마케팅 - 최적화 전달</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 중동 유틸리티</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 서유럽 인증</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 서유럽 마케팅</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 서유럽 마케팅 - 최적화 전달</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>기타 서유럽 유틸리티</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>러시아 인증</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>러시아 마케팅</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>러시아 마케팅 - 최적화 전달</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>러시아 유틸리티</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>사우디아라비아 인증</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>사우디아라비아 인증 국제</td>
        <td>15.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>사우디아라비아 마케팅</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>사우디아라비아 마케팅 - 최적화 전달</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>사우디아라비아 유틸리티</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>남아프리카공화국 인증</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>남아프리카공화국 인증 국제</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>남아프리카공화국 마케팅</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>남아프리카공화국 마케팅 - 최적화 전달</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>남아프리카공화국 유틸리티</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>스페인 인증</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>스페인 마케팅</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>스페인 마케팅 - 최적화 전달</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>스페인 유틸리티</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>튀르키예 인증</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>튀르키예 마케팅</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>튀르키예 마케팅 - 최적화 전달</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>튀르키예 유틸리티</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아랍에미리트 인증</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아랍에미리트 인증 국제</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아랍에미리트 마케팅</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아랍에미리트 마케팅 - 최적화 전달</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>아랍에미리트 유틸리티</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>영국 인증</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>영국 마케팅</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>영국 마케팅 - 최적화 전달</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>영국 유틸리티</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>전 지역</td>
        <td>0.15</td>
    </tr>
    <tr>
        <td>KakaoTalk</td>
        <td>전 지역</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>웹훅</td>
        <td>표준</td>
        <td>0.08</td>
    </tr>
    <tr>
        <td>BYO SMS 커넥터</td>
        <td>Infobip - 전 지역</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>BYO SMS 커넥터</td>
        <td>Twilio - 전 지역</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>브라질 - Basic</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>브라질 - Single</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>콜롬비아 - Basic</td>
        <td>1.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>콜롬비아 - Single</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>프랑스 - Basic</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>프랑스 - Single</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>독일 - Basic</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>독일 - Single</td>
        <td>12.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>이탈리아 - Basic</td>
        <td>4.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>이탈리아 - Single</td>
        <td>6.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>멕시코 - Basic</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>멕시코 - Single</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>싱가포르 - Basic</td>
        <td>4.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>싱가포르 - Single</td>
        <td>8.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>스페인 - Basic</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>스페인 - Single</td>
        <td>13.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>스웨덴 - Basic</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>스웨덴 - Single</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>영국 - Basic</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>영국 - Single</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>미국 - Basic - 지원 중단</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>미국 - Rich</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>미국 - Rich Media</td>
        <td>1.30</td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## 에이전트 콘솔 세부 정보 {#agent-console-details}
Braze는 Braze 플랫폼에서 발송된 에이전트 콘솔 호출(Invocations)에 대해 메시지 크레딧을 청구합니다. 호출은 에이전트가 LLM에 대한 호출을 시작할 때 기록됩니다. 기본적으로 계약에는 구독 기간의 각 기간당 1만 건의 호출이 포함되어 있습니다.

## SMS/MMS 채널 세부 정보 {#smsmms-channel-details}

### SMS 세그먼트 {#sms-segments}

SMS 메시지 세그먼트는 SMS 업계에서 메시지를 계산하는 방식입니다. 메시지 세그먼트는 정해진 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)까지의 그룹으로, 단일 SMS 발송으로 전송됩니다. GSM-7 인코딩을 사용하여 161자의 SMS를 발송하면 두(2)개의 메시지 세그먼트가 전송된 것을 확인할 수 있습니다. 여러 메시지 세그먼트를 발송하면 추가 요금이 발생합니다.

### MMS 세그먼트 {#mms-segments}

MMS의 경우 메시지 제한은 5MB입니다(멀티미디어 자산과 메시지 본문 크기 포함). 안전을 위해 Braze는 멀티미디어 자산을 600KB 이하로 유지하면서 메시지 본문도 함께 포함할 것을 권장합니다.

### RCS 유형 {#rcs-types}

RCS는 SMS와 MMS의 차세대 버전입니다. SMS와 같은 직접적이고 높은 참여도의 채널 장점을 제공하면서, 리치 콘텐츠(이미지, 동영상, 문서), 인증 및 브랜드 발신, 추천 답장 및 동작과 같은 인터랙티브 기능 등 현대 소비자가 기대하는 더 풍부한 기능을 갖추고 있습니다.

- RCS 과금은 두 가지 메시지 유형을 중심으로 합니다(미국의 경우 구분이 있음):
    - **Basic RCS:** 텍스트 전용, 최대 160자
    - **Single RCS:** 리치 콘텐츠를 포함하는 메시지 또는 160자를 초과하는 텍스트 전용 메시지
    - **Rich RCS (미국 전용):** 텍스트 전용, 제한된 제안/버튼(quickReply, dialPhone, 웹뷰 없는 openURL)을 포함할 수 있으며, 160 UTF-8 바이트 단위로 세그먼트 분할
    - **Rich Media RCS (미국 전용):** 모든 미디어 또는 더 풍부한 제안/버튼(웹뷰, 위치, 캘린더 등)이 포함된 텍스트, 하나의 메시지로 계산

## WhatsApp 채널 세부 정보 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## 추가 채널 세부 정보 {#additional-channel-details}

### 웹훅 {#webhooks}

웹훅은 2024년 12월 9일부터 메시지 크레딧에 포함되었습니다. Braze는 Braze 플랫폼에서 발송된 모든 웹훅에 대해 메시지 크레딧을 청구합니다. 기본적으로 계약에는 구독 기간의 각 기간당 10만 건의 웹훅이 포함되어 있습니다. 추가 웹훅은 주문서에 따라 청구됩니다.

### BYO(Bring Your Own) SMS 커넥터 {#bring-your-own-byo-sms-connectors}

Braze는 고객이 "BYO SMS 커넥터" 모델을 통해 서드파티 제공업체와 통합하여 SMS 메시지를 발송할 수 있도록 합니다. Braze는 BYO SMS 커넥터를 통해 Braze 플랫폼에서 발송된 각 메시지에 대해 메시지 크레딧을 청구합니다.

### LINE

Braze는 Braze 플랫폼에서 발송된 모든 LINE 메시지에 대해 메시지 크레딧을 청구합니다.

## 과금 지역 분류 {#billing-region-breakdown}

### 북미 {#north-america}

미국, 캐나다

### 기타 아프리카 {#rest-of-africa}

알제리, 앙골라, 베냉, 보츠와나, 부르키나파소, 부룬디, 카메룬, 차드, 콩고, 에리트레아, 에티오피아, 가봉, 감비아, 가나, 기니비사우, 코트디부아르, 케냐, 레소토, 라이베리아, 리비아, 마다가스카르, 말라위, 말리, 모리타니, 모로코, 모잠비크, 나미비아, 니제르, 르완다, 세네갈, 시에라리온, 소말리아, 남수단, 수단, 에스와티니, 탄자니아, 토고, 튀니지, 우간다, 잠비아

### 기타 아시아 태평양 {#rest-of-asia-pacific}

아프가니스탄, 호주, 방글라데시, 캄보디아, 중국, 홍콩, 일본, 라오스, 몽골, 네팔, 뉴질랜드, 파푸아뉴기니, 필리핀, 싱가포르, 스리랑카, 대만, 타지키스탄, 태국, 투르크메니스탄, 우즈베키스탄, 베트남

### 기타 중앙 및 동유럽 {#rest-of-central-eastern-europe}

알바니아, 아르메니아, 아제르바이잔, 벨라루스, 불가리아, 크로아티아, 체코, 조지아, 그리스, 헝가리, 라트비아, 리투아니아, 북마케도니아, 몰도바, 폴란드, 루마니아, 세르비아, 슬로바키아, 슬로베니아, 우크라이나

### 기타 라틴 아메리카 {#rest-of-latin-america}

볼리비아, 코스타리카, 도미니카공화국, 에콰도르, 엘살바도르, 과테말라, 아이티, 온두라스, 자메이카, 니카라과, 파나마, 파라과이, 푸에르토리코, 우루과이, 베네수엘라

### 기타 중동 {#rest-of-middle-east}

바레인, 이라크, 요르단, 쿠웨이트, 레바논, 오만, 카타르, 예멘

### 기타 서유럽 {#rest-of-western-europe}

오스트리아, 벨기에, 덴마크, 핀란드, 아일랜드, 노르웨이, 포르투갈, 스웨덴, 스위스