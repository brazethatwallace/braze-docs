---
nav_title: 메시지 크레딧 - Gamma
permalink: "/message_credits_gamma_0dhr/"
hidden: true
noindex: true
hide_toc: true
---

# 메시지 크레딧 - Gamma (기밀) {#message-credits-gamma-confidential}

> 메시지 크레딧은 Braze의 네이티브 에이전트 콘솔, SMS, MMS, RCS, WhatsApp, LINE 제품을 아우르는 크로스 제품 패키징 구조입니다. 메시지 크레딧은 Braze 메시징 채널과 특정 AI 기능을 활용할 때 유연하고 투명한 경험을 제공합니다. 크레딧을 통해 이 페이지의 표에 제시된 모든 채널에 접근할 수 있습니다.

{% alert note %}
제품마다 리포팅에서 사용하는 측정 단위가 다릅니다.<br><br>
<b>에이전트 콘솔:</b> 호출(Invocations)<br>
<b>SMS:</b> Segments<br>
<b>MMS:</b> 발송<br>
<b>WhatsApp:</b> 전달된 메시지<br>
<b>RCS:</b> 전달된 Segments, 전달된 발송<br>
<b>LINE:</b> 발송<br>
<b>KakaoTalk:</b> 발송<br>

마지막으로, SMS, MMS, RCS와 관련된 통신사 수수료는 별도로 후불 청구되며 이 메시지 크레딧 SKU에 포함되지 않습니다.
{% endalert %}

## 정의 {#definitions}

열 정의는 다음과 같습니다.

|---------|-------------------------------------------------|
| **대상** | Braze 플랫폼을 통해 발송되는 특정 최종 지역, 국가 또는 동작 유형 |
| **1회 발송당 크레딧** | 1회 발송을 수행하는 데 필요한 정확한 메시지 크레딧 수<br>(발송당 크레딧 = 크레딧 비율 × 대상 배수) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## 메시지 크레딧 - Gamma 크레딧 비율 표 {#credit-ratio-table-for-message-credits-gamma}

{% details 펼치려면 클릭하세요 %}
<table class="credits-table" aria-label="메시지 크레딧 - Gamma 크레딧 비율 표">
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
    </thead>
    <tbody>
<tr>
        <td>에이전트 콘솔</td>
        <td>Braze Auto</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>에이전트 콘솔</td>
        <td>BYO LLM API Key</td>
        <td>0.16</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>Canada</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>Canada Toll Free</td>
        <td>0.52</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>United States</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>United States Toll Free</td>
        <td>0.60</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>Canada Long Code</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>Canada Short Code</td>
        <td>4.80</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>Canada Toll Free</td>
        <td>1.56</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>United States</td>
        <td>1.20</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>United States Toll Free</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Abkhazia</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Afghanistan</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Albania</td>
        <td>22.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Algeria</td>
        <td>52.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>American Samoa</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Andorra</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Angola</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Anguilla</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Antigua and Barbuda</td>
        <td>24.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Argentina</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Armenia</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Aruba</td>
        <td>26.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Australia MMS</td>
        <td>31.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Australia SMS</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Austria</td>
        <td>17.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Azerbaijan</td>
        <td>97.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bahamas</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bahrain</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bangladesh</td>
        <td>58.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Barbados</td>
        <td>30.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Belarus</td>
        <td>63.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Belgium</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Belize</td>
        <td>69.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Benin</td>
        <td>36.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bermuda</td>
        <td>29.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bhutan</td>
        <td>101.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bolivia</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bosnia and Herzegovina</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Botswana</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Brazil</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Brunei</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Bulgaria</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Burkina Faso</td>
        <td>33.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Burundi</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cambodia</td>
        <td>43.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cameroon</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cape Verde</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Caribbean Netherlands</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cayman Islands</td>
        <td>33.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Central African Republic</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Chad</td>
        <td>73.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Chile</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>China</td>
        <td>6.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Colombia</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Comoros</td>
        <td>61.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Congo</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cook Islands</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Costa Rica</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Croatia</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cuba</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Curacao</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Cyprus</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Czech Republic</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Denmark</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Djibouti</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Dominica</td>
        <td>37.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Dominican Republic</td>
        <td>12.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>DR Congo</td>
        <td>57.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ecuador</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Egypt</td>
        <td>24.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>El Salvador</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Equatorial Guinea</td>
        <td>43.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Eritrea</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Estonia</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Eswatini</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ethiopia</td>
        <td>86.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Falkland Islands</td>
        <td>34.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Faroe Islands</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Fiji</td>
        <td>41.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Finland</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>France</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>French Guiana</td>
        <td>46.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>French Polynesia</td>
        <td>45.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Gabon</td>
        <td>66.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Gambia</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Georgia</td>
        <td>26.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Germany</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ghana</td>
        <td>22.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Gibraltar</td>
        <td>27.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Greece</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Greenland</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Grenada</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guadeloupe</td>
        <td>34.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guam</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guatemala</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guernsey</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guinea</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guinea-Bissau</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Guyana</td>
        <td>45.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Haiti</td>
        <td>59.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Honduras</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Hong Kong</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Hungary</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Iceland</td>
        <td>17.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>India</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Indonesia</td>
        <td>66.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Iran</td>
        <td>62.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Iraq</td>
        <td>47.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ireland</td>
        <td>13.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Isle of Man</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Israel</td>
        <td>37.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Italy</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ivory Coast</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Jamaica</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Japan</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Jersey</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Jordan</td>
        <td>55.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kazakhstan</td>
        <td>55.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kenya</td>
        <td>26.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kiribati</td>
        <td>36.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Korea Republic of</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kosovo</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kuwait</td>
        <td>33.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Kyrgyzstan</td>
        <td>61.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Laos PDR</td>
        <td>15.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Latvia</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Lebanon</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Lesotho</td>
        <td>51.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Liberia</td>
        <td>34.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Libya</td>
        <td>81.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Liechtenstein</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Lithuania</td>
        <td>13.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Luxembourg</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Macao</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Macedonia</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Madagascar</td>
        <td>94.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Malawi</td>
        <td>57.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Malaysia</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Maldives</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mali</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Malta</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Marshall Islands</td>
        <td>40.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Martinique</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mauritania</td>
        <td>65.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mauritius</td>
        <td>40.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mayotte</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mexico</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Micronesia</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Moldova</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Monaco</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mongolia</td>
        <td>70.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Montenegro</td>
        <td>28.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Montserrat</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Morocco</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Mozambique</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Myanmar</td>
        <td>58.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Namibia</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Nauru</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Nepal</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Netherlands</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>New Caledonia</td>
        <td>44.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>New Zealand</td>
        <td>19.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Nicaragua</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Niger</td>
        <td>74.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Nigeria</td>
        <td>50.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Niue</td>
        <td>48.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Norfolk Island</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>North Macedonia</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Northern Cyprus</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Norway</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Oman</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Pakistan</td>
        <td>74.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Palau</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Palestinian Territory</td>
        <td>76.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Panama</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Papua New Guinea</td>
        <td>190.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Paraguay</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Peru</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Philippines</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Poland</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Portugal</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Puerto Rico</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Qatar</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Reunion/Mayotte</td>
        <td>48.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Romania</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Russia</td>
        <td>95.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Rwanda</td>
        <td>46.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Saint Kitts and Nevis</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Saint Lucia</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Saint Pierre and Miquelon</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Saint Vincent and The Grenadines</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Samoa</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>San Marino</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sao Tome and Principe</td>
        <td>32.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Saudi Arabia</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Senegal</td>
        <td>51.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Serbia</td>
        <td>60.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Seychelles</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sierra Leone</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Singapore</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sint Maarten</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Slovakia</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Slovenia</td>
        <td>37.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Solomon Islands</td>
        <td>20.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Somalia</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>South Africa</td>
        <td>3.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>South Ossetia</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>South Sudan</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Spain</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sri Lanka</td>
        <td>56.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sudan</td>
        <td>41.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Suriname</td>
        <td>32.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Swaziland</td>
        <td>23.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Sweden</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Switzerland</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Syria</td>
        <td>78.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Taiwan</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Tajikistan</td>
        <td>113.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Tanzania</td>
        <td>53.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Thailand</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Timor-Leste</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Togo</td>
        <td>38.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Tonga</td>
        <td>31.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Trinidad and Tobago</td>
        <td>30.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Tunisia</td>
        <td>70.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Turkey</td>
        <td>7.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Turkmenistan</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Turks and Caicos Islands</td>
        <td>33.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Tuvalu</td>
        <td>33.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Uganda</td>
        <td>40.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Ukraine</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>United Arab Emirates</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>United Kingdom</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Unknown</td>
        <td>39.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Uruguay</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Uzbekistan</td>
        <td>68.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Vanuatu</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Venezuela</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Vietnam</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Virgin Islands, British</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Virgin Islands, U.S.</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Wallis and Futuna</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Yemen</td>
        <td>60.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Zambia</td>
        <td>67.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>Zimbabwe</td>
        <td>35.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Authentication</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Marketing</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Marketing - BYO</td>
        <td>0.62</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Marketing - Optimized Delivery</td>
        <td>16.39</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Argentina Utility</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Authentication</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Marketing</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Marketing - BYO</td>
        <td>0.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Marketing - Optimized Delivery</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Brazil Utility</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Marketing</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Marketing - BYO</td>
        <td>0.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Marketing - Optimized Delivery</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Chile Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Authentication</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Marketing</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Marketing - BYO</td>
        <td>0.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Marketing - Optimized Delivery</td>
        <td>3.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Colombia Utility</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Authentication</td>
        <td>0.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Authentication International</td>
        <td>17.24</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Marketing</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Marketing - BYO</td>
        <td>0.64</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Marketing - Optimized Delivery</td>
        <td>28.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Egypt Utility</td>
        <td>1.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Authentication</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Marketing</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Marketing - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Marketing - Optimized Delivery</td>
        <td>37.99</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>France Utility</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Authentication</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Marketing</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Marketing - BYO</td>
        <td>1.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Marketing - Optimized Delivery</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Germany Utility</td>
        <td>14.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Authentication</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Authentication International</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Marketing</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Marketing - BYO</td>
        <td>0.12</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Marketing - Optimized Delivery</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>India Utility</td>
        <td>0.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Authentication</td>
        <td>6.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Authentication International</td>
        <td>36.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Marketing</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Marketing - BYO</td>
        <td>0.41</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Marketing - Optimized Delivery</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Indonesia Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Marketing</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Marketing - BYO</td>
        <td>0.35</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Marketing - Optimized Delivery</td>
        <td>9.36</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Israel Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Authentication</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Marketing</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Marketing - BYO</td>
        <td>0.69</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Marketing - Optimized Delivery</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Italy Utility</td>
        <td>7.96</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Authentication</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Authentication International</td>
        <td>11.09</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Marketing</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Marketing - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Marketing - Optimized Delivery</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Malaysia Utility</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Authentication</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Marketing</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Marketing - BYO</td>
        <td>0.31</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Marketing - Optimized Delivery</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Mexico Utility</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Authentication</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Marketing</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Marketing - BYO</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Marketing - Optimized Delivery</td>
        <td>42.37</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Netherlands Utility</td>
        <td>13.26</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Authentication</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Authentication International</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Marketing</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Marketing - BYO</td>
        <td>0.52</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Marketing - Optimized Delivery</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Nigeria Utility</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Authentication</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Marketing</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Marketing - BYO</td>
        <td>0.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Marketing - Optimized Delivery</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>North America Utility</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Authentication</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Marketing</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Marketing - BYO</td>
        <td>0.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Marketing - Optimized Delivery</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Other Utility</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Authentication International</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Marketing</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Marketing - BYO</td>
        <td>0.47</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Marketing - Optimized Delivery</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Pakistan Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Marketing</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Marketing - BYO</td>
        <td>0.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Marketing - Optimized Delivery</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Peru Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Authentication</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Marketing</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Marketing - BYO</td>
        <td>0.23</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Marketing - Optimized Delivery</td>
        <td>5.97</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Africa Utility</td>
        <td>1.06</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Authentication</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Marketing</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Marketing - BYO</td>
        <td>0.73</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Marketing - Optimized Delivery</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Asia Pacific Utility</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Authentication</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Marketing</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Marketing - BYO</td>
        <td>0.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Marketing - Optimized Delivery</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Central & Eastern Europe Utility</td>
        <td>5.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Authentication</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Marketing</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Marketing - BYO</td>
        <td>0.74</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Marketing - Optimized Delivery</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Latin America Utility</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Message Types - BYO</td>
        <td>0.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Authentication</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Marketing</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Marketing - BYO</td>
        <td>0.34</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Marketing - Optimized Delivery</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Middle East Utility</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Authentication</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Marketing</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Marketing - BYO</td>
        <td>0.59</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Marketing - Optimized Delivery</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Rest of Western Europe Utility</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Authentication</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Marketing</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Marketing - BYO</td>
        <td>0.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Marketing - Optimized Delivery</td>
        <td>21.28</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Russia Utility</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Authentication</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Authentication International</td>
        <td>15.86</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Marketing</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Marketing - BYO</td>
        <td>0.46</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Marketing - Optimized Delivery</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Saudi Arabia Utility</td>
        <td>3.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Authentication</td>
        <td>2.84</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Authentication International</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Marketing</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Marketing - BYO</td>
        <td>0.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Marketing - Optimized Delivery</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>South Africa Utility</td>
        <td>2.84</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Authentication</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Marketing</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Marketing - BYO</td>
        <td>0.62</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Marketing - Optimized Delivery</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Spain Utility</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Authentication</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Marketing</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Marketing - BYO</td>
        <td>0.11</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Marketing - Optimized Delivery</td>
        <td>2.89</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>Turkey Utility</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Authentication</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Authentication International</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Marketing</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Marketing - BYO</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Marketing - Optimized Delivery</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Arab Emirates Utility</td>
        <td>4.17</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Authentication</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Marketing</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Marketing - BYO</td>
        <td>0.53</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Marketing - Optimized Delivery</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>United Kingdom Utility</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>Line</td>
        <td>All Regions</td>
        <td>0.15</td>
    </tr>
    <tr>
        <td>KakaoTalk</td>
        <td>All Regions</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>웹훅</td>
        <td>표준</td>
        <td>0.08</td>
    </tr>
    <tr>
        <td>BYO SMS 커넥터</td>
        <td>Infobip - All Regions</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>BYO SMS 커넥터</td>
        <td>Twilio - All Regions</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Brazil - Basic</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Brazil - Single</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Colombia - Basic</td>
        <td>1.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Colombia - Single</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>France - Basic</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>France - Single</td>
        <td>12.60</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Germany - Basic</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Germany - Single</td>
        <td>12.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Italy - Basic</td>
        <td>4.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Italy - Single</td>
        <td>6.70</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Mexico - Basic</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Mexico - Single</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Singapore - Basic</td>
        <td>4.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Singapore - Single</td>
        <td>8.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Spain - Basic</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Spain - Single</td>
        <td>13.90</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Sweden - Basic</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>Sweden - Single</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United Kingdom - Basic</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United Kingdom - Single</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Basic - Deprecated</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Rich</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Rich Media</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>RCS</td>
        <td>United States - Single - Deprecated</td>
        <td>1.30</td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## 에이전트 콘솔 세부 정보 {#agent-console-details}
Braze는 Braze 플랫폼에서 발송된 에이전트 콘솔 호출(Invocation)에 대해 메시지 크레딧을 청구합니다. 호출은 에이전트가 LLM에 대한 호출을 시작할 때 기록됩니다. 기본적으로 계약에는 구독 기간의 각 기간당 만 건의 호출이 포함되어 있습니다.

## SMS/MMS 채널 세부 정보 {#smsmms-channel-details}

### SMS 메시지 세그먼트 {#sms-segments}

SMS 메시지 세그먼트는 SMS 업계에서 메시지를 집계하는 방식입니다. 메시지 세그먼트는 정해진 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)까지의 문자 그룹으로, 단일 SMS 발송으로 전송됩니다. GSM-7 인코딩을 사용하여 161자의 SMS를 발송하면 두(2)개의 메시지 세그먼트가 전송된 것을 확인할 수 있습니다. 여러 메시지 세그먼트를 발송하면 추가 요금이 발생합니다.

### MMS 메시지 세그먼트 {#mms-segments}

MMS의 경우 메시지 제한은 5MB입니다(멀티미디어 자산과 메시지 본문 크기 포함). 안전을 위해 Braze는 메시지 본문을 포함하면서 멀티미디어 자산을 600KB 이하로 유지할 것을 권장합니다.

### RCS 유형 {#rcs-types}

RCS는 차세대 SMS 및 MMS입니다. SMS와 같은 직접적이고 높은 참여도의 채널 이점을 제공하면서, 리치 콘텐츠(이미지, 동영상, 문서), 인증 및 브랜드 발신, 추천 답장 및 동작과 같은 인터랙티브 기능 등 현대 소비자가 기대하는 더 풍부한 기능을 갖추고 있습니다.

- RCS 과금은 두 가지 메시지 유형을 기준으로 합니다(미국의 경우 구분이 다름):
    - **Basic RCS:** 텍스트 전용, 최대 160자
    - **Single RCS:** 리치 콘텐츠를 포함하는 메시지 또는 160자를 초과하는 텍스트 전용 메시지
    - **Rich RCS (미국 전용):** 텍스트 전용, 제한된 제안/버튼(quickReply, dialPhone, 웹뷰 없는 openURL) 포함 가능, 160 UTF-8 바이트 단위로 분할
    - **Rich Media RCS (미국 전용):** 모든 미디어 또는 더 풍부한 제안/버튼(웹뷰, 위치, 캘린더 등)이 포함된 텍스트, 하나의 메시지로 집계

## WhatsApp 채널 세부 정보 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## 추가 채널 세부 정보 {#additional-channel-details}

### 웹훅 {#webhooks}

웹훅은 2024년 12월 9일부터 메시지 크레딧의 일부가 되었습니다. Braze는 Braze 플랫폼에서 발송되는 모든 웹훅에 대해 메시지 크레딧을 청구합니다. 기본적으로 계약에는 구독 기간의 각 기간당 십만 건의 웹훅이 포함되어 있습니다. 추가 웹훅은 주문서에 따라 청구됩니다.

### 자체 SMS 커넥터(BYO) {#bring-your-own-byo-sms-connectors}

Braze는 고객이 "BYO SMS 커넥터" 모델을 통해 서드파티 제공업체와 통합하여 SMS 메시지를 발송할 수 있도록 지원합니다. Braze는 BYO SMS 커넥터를 통해 Braze 플랫폼에서 발송되는 각 메시지에 대해 메시지 크레딧을 청구합니다.

### LINE

Braze는 Braze 플랫폼에서 발송되는 모든 LINE 메시지에 대해 메시지 크레딧을 청구합니다.

## 청구 지역 분류 {#billing-region-breakdown}

### 북미 {#north-america}

미국, 캐나다

### 기타 아프리카 {#rest-of-africa}

알제리, 앙골라, 베냉, 보츠와나, 부르키나파소, 부룬디, 카메룬, 차드, 콩고, 에리트레아, 에티오피아, 가봉, 감비아, 가나, 기니비사우, 코트디부아르, 케냐, 레소토, 라이베리아, 리비아,
마다가스카르, 말라위, 말리, 모리타니, 모로코, 모잠비크, 나미비아, 니제르, 르완다, 세네갈, 시에라리온, 소말리아, 남수단, 수단, 에스와티니, 탄자니아, 토고, 튀니지, 우간다, 잠비아

### 기타 아시아 태평양 {#rest-of-asia-pacific}

아프가니스탄, 호주, 방글라데시, 캄보디아, 중국, 홍콩, 일본, 라오스, 몽골, 네팔, 뉴질랜드, 파푸아뉴기니, 필리핀, 싱가포르, 스리랑카, 대만, 타지키스탄, 태국,
투르크메니스탄, 우즈베키스탄, 베트남

### 기타 중앙 및 동유럽 {#rest-of-central-eastern-europe}

알바니아, 아르메니아, 아제르바이잔, 벨라루스, 불가리아, 크로아티아, 체코, 조지아, 그리스, 헝가리, 라트비아, 리투아니아, 북마케도니아, 몰도바, 폴란드, 루마니아, 세르비아, 슬로바키아, 슬로베니아, 우크라이나

### 기타 라틴 아메리카 {#rest-of-latin-america}

볼리비아, 코스타리카, 도미니카 공화국, 에콰도르, 엘살바도르,
과테말라, 아이티, 온두라스, 자메이카, 니카라과, 파나마, 파라과이, 푸에르토리코, 우루과이, 베네수엘라

### 기타 중동 {#rest-of-middle-east}

바레인, 이라크, 요르단, 쿠웨이트, 레바논, 오만, 카타르, 예멘

### 기타 서유럽 {#rest-of-western-europe}

오스트리아, 벨기에, 덴마크, 핀란드, 아일랜드, 노르웨이, 포르투갈, 스웨덴, 스위스