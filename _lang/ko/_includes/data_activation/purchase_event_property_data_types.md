`properties` 값은 최대 50&nbsp;KB 크기의 오브젝트여야 하며, 키는 등록정보 이름이고 값은 등록정보 값입니다. 등록정보 이름은 문자열이어야 하며, 255자 이하이고, 앞에 달러 기호(`$`)가 올 수 없습니다.

등록정보 값은 다음 데이터 유형 중 하나일 수 있습니다:

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | 정수 또는 플로트 |
| 부울 | `true` 또는 `false` 값 |
| 날짜/시간 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하 |
| 배열 | 지원됨. 배열 내에서 날짜/시간은 지원되지 않습니다. |
| 오브젝트 | 문자열로 수집됩니다(중첩 오브젝트가 아님). 중첩 데이터의 경우 문자열 값을 사용하세요(예: JSON 직렬화). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

다음 키는 예약되어 있으며 등록정보 이름으로 사용할 수 없습니다: `time`, `product_id`, `quantity`, `event_name`, `price`, `currency`. `properties` 오브젝트에서 예약된 키를 사용하면 "Invalid 'properties' field" 오류가 반환됩니다.