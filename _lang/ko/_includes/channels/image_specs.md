{% if include.variable_name == "image behavior" %}


| 레이아웃 | 동작 |
| --- | --- |
| 이미지 및 텍스트 | 세로로 길거나 좁은 이미지는 축소되어 가로 중앙에 배치됩니다. 넓은 이미지는 왼쪽과 오른쪽 가장자리가 잘립니다. |
| 이미지만 | 메시지는 대부분의 종횡비에 맞게 이미지 크기를 조정합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

{% endif %}

{% if include.variable_name == "payload size" %}

다음 페이로드 크기를 권장합니다:

| 메시징 시스템 | 권장 페이로드 |
| --- | --- |
| iOS(iOS 8 이전) | 0.256 KB |
| iOS(iOS 8 이후) | 2 KB |
| Android(FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

Modal 인앱 메시지는 선택한 이미지 또는 문구의 크기와 비율을 그대로 유지하면서 기기에 가장 알맞은 최적의 비율로 채워지도록 설계되었습니다.

인앱 메시지(버튼, 헤드라인, 본문 등)에 포함할 수 있는 텍스트 글자 수에는 제한이 없지만, 사용하는 텍스트 글자 수를 적절히 조절하는 것이 좋습니다. 텍스트가 너무 많으면 사용자가 메시지를 확장하고 스크롤해야 합니다.

모든 인앱 메시지의 권장 이미지 크기는 500KB, 최대 이미지 크기는 5MB이며 PNG, JPEG, GIF 파일 유형을 지원합니다. WebP 이미지는 모든 기기나 브라우저에서 지원되지 않으므로, 인앱 메시지에 추가하기 전에 WebP 이미지를 PNG 또는 JPEG로 변환하는 것이 좋습니다.

{% tabs %}
{% tab Portrait %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 텍스트가 포함된 세로 전체 화면 | 6:5 | 고해상도 1200 x 1000 px <br>최소 해상도 600 x 500 px | 모든 면에서 잘림이 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다. |
| 세로 전체 화면(이미지만, 버튼 유무에 관계없이) | 3:5 | 고해상도 1200 x 2000 px <br> 최소 해상도 600 x 1000 px | 세로로 긴 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="표" }

{% endtab %}
{% tab Landscape %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 텍스트가 포함된 가로 전체 화면 | 10:3 | 고해상도 2000 x 600 px <br>최소 해상도 1000 x 300 px | 모든 면에서 잘림이 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다. |
| 가로 전체 화면(이미지만, 버튼 유무에 관계없이) | 5:3 | 고해상도 2000 x 600 px <br> 최소 해상도 1000 x 600 px | 세로로 긴 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="표" }

{% endtab %}
{% tab 슬라이드업 %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| 슬라이드업 | 1:1 | 고해상도 150 x 150 px <br> 최소 해상도 50 x 50 px | 다양한 종횡비의 이미지가 잘리지 않고 정사각형 이미지 컨테이너에 맞춰집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="표" }

{% endtab %}
{% tab Modal %}

| 유형 | 종횡비 | 이미지 품질 | 참고 |
| --- | --- | --- | --- |
| Modal(이미지만) | 1:1 | 권장 최대 해상도: 1200 x 2000 px <br> 최소 해상도: 600 x 600 px | 메시지는 대부분의 종횡비에 맞게 이미지 크기를 조정합니다. 권장 최대 해상도는 3:5 종횡비이며, 최적의 결과를 제공하지 않을 수 있습니다. 더 큰 이미지도 사용할 수 있지만, 로드 시간이 길어질 수 있습니다. <br> 이미지의 이상적인 종횡비는 1:1이며, 이 비율을 충족하지 않으면 업로드 중에 경고가 표시될 수 있습니다. 이 경고는 최상의 결과를 위한 제안이며, 더 큰 이미지의 업로드를 방해하지 않습니다. |
| 텍스트가 있는 Modal | 29:10 | 고해상도 1450 x 500 px <br> 최소 해상도 600 x 205 px | 세로로 긴 이미지는 축소되어 가로 중앙에 배치됩니다. 넓은 이미지는 왼쪽과 오른쪽 가장자리가 잘립니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="표" }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| 메시지 유형 | 최대 메시지 길이 | 최대 제목 길이 |
| --- | --- | --- |
| iOS 잠금 화면 | 175자 | 43자 |
| iOS 알림 | 175자 | 43자 |
| iOS 배너 알림 | 85자 | 43자 |
| Android 잠금 화면 | 49자 | 43자 |
| Android 알림 서랍 | 597자 | 43자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="표" }

모든 푸시 이미지의 권장 이미지 크기는 500KB입니다.

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="표">
  <thead>
    <tr>
      <th>이미지 유형</th>
      <th>종횡비</th>
      <th>최대 픽셀</th>
      <th>최대 이미지 크기</th>
      <th>파일 유형</th>
      <th>참고</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1(권장)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>2020년 1월부터 iOS 리치 푸시 알림은 10MB 미만인 경우 1038 x 1038 px 이미지를 처리할 수 있지만, 가능한 한 작은 파일 크기를 사용하는 것이 좋습니다. 실제로 대용량 파일을 전송하면 불필요한 네트워크 부하가 발생하고 다운로드 시간 초과가 더 자주 발생할 수 있습니다.<br><br>자세한 내용은 <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS 리치 알림</a> 을 참조하세요.</td>
    </tr>
    <tr>
      <td>Android 푸시 아이콘</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android 확장 알림 이미지</td>
      <td>2:1</td>
      <td><b>작음:</b><br>512 x 256<br><br><b>중간:</b><br>1024 x 512<br><br><b>큼:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td><a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android 리치 알림</a> 에 사용됩니다.</td>
    </tr>
    <tr>
      <td>Android 인라인 이미지</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>자세한 내용은 <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android 인라인 이미지 푸시</a> 를 참조하세요.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="표" }

{% endif %}

{% if include.variable_name == "email" %}

| 이메일 유형 | 권장 최대 크기 |
| --- | --- |
| 텍스트만 | 25 KB |
| 이미지가 포함된 텍스트 | 60 KB |
| 이메일 너비 | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

| 이미지 사양 | 권장 최대 크기 |
| --- | --- |
| 크기 | 5 MB |
| 너비 | 헤더: 600 px<br>본문: 480 px |
| 파일 유형 | PNG, JPEG, GIF<br><br> WebP 이미지 지원은 이메일 클라이언트마다 다릅니다. 안정적인 렌더링을 위해, 이메일 메시지에 추가하기 전에 WebP 이미지를 PNG 또는 JPEG로 변환하세요.<br><br>SVG 이미지는 Gmail 및 기타 주요 이메일 클라이언트와의 호환성 문제로 인해 이메일 메시지에 권장되지 않습니다. 대신 PNG, JPEG 또는 GIF를 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

| 텍스트 사양 | 권장 최대 크기 |
| --- | --- |
| 제목란 길이 | 35자<br>6~10단어 |
| `"From: Name"` 길이 | 25자 |
| 프리헤더 길이 | 85자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

{% endif %}

{% if include.variable_name == "content cards" %}

| 카드 유형 | 종횡비     | 이미지 품질       |
| --------- | ---------------- | ------------------- |
| 클래식   | 1:1 종횡비 | 60 x 60&nbsp;px        |
| 캡션 | 4:3 종횡비 | 최소 너비 600&nbsp;px |
| 배너    | 모든 종횡비 | 최소 너비 600&nbsp;px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="표" }

자세한 내용은 [Content Cards 크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details)를 참조하세요.

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

이 사양은 템플릿 헤더, 응답 미디어 메시지 및 이미지 메시지에 적용됩니다.

| 속성정보 | 사양 | 참고 |
|---|---|---|
| 지원 형식 | JPEG, PNG | Meta는 이미지 메시지에 대해 JPEG와 PNG만 공식적으로 지원합니다. WebP는 스티커에만 지원되며 일반 이미지 메시지에는 지원되지 않습니다. |
| 최대 파일 크기 | 5 MB | |
| 색상 모드 | 8비트, RGB 또는 RGBA | |
| 캡션(이미지 메시지만 해당) | 선택 사항; 최대 1,024자 | |
| 권장 크기 | 1,125 × 600 px | 기기 간 일관된 렌더링과 Meta 요구 사항 준수를 위해 1,125×600 px(1.91:1) 크기의 JPEG 또는 PNG 이미지를 사용하는 것이 좋습니다. |
| 권장 종횡비 | 1.91:1(와이드) | 정사각형(1:1) 및 와이드(16:9) 형식도 허용되지만, 사용자의 기기에 따라 이미지가 잘리거나 확대될 수 있습니다.<br><br> 캐러셀 카드의 경우, 헤더 이미지는 WhatsApp에 의해 자동으로 와이드 비율로 잘립니다. 단, 본문 텍스트가 없는 경우에는 정사각형으로 렌더링됩니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="표" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

다음 사양은 템플릿 헤더, 응답 미디어 메시지, 비디오 메시지 및 캐러셀 카드 헤더에 적용됩니다.

| 속성정보 | 사양 |
|---|---|
| 지원 형식 | MP4, 3GPP |
| 파일 크기 | 최대 16 MB |
| 비디오 코덱 | H.264만 지원 |
| 오디오 코덱 | AAC만 지원 |
| 오디오 스트림 | 단일 오디오 스트림 또는 오디오 스트림 없음 |
| 캡션(비디오 메시지만 해당) | 선택 사항; 최대 1,024자 |
| 권장 종횡비 | 1.91:1(와이드) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}