## 지원되는 데이터 유형 {#supported-data-types}

다음 데이터 유형이 지원됩니다:

<table aria-label="지원되는 데이터 유형">
  <thead>
    <tr>
      <th>데이터 유형</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>숫자</td>
      <td>숫자 값으로, 예를 들어 <code>1</code> 또는 <code>5.5</code>입니다.</td>
    </tr>
    <tr>
      <td>문자열</td>
      <td>텍스트 값으로, 예를 들어 <code>"Hello"</code> 또는 <code>"The Hobbit"</code>입니다.</td>
    </tr>
    <tr>
      <td>부울</td>
      <td><code>true</code> 또는 <code>false</code>로 평가되는 값입니다.</td>
    </tr>
    <tr>
      <td>배열</td>
      <td>값의 목록으로, 예를 들어 <code>["red", "blue", "green"]</code>입니다.</td>
    </tr>
    <tr>
      <td>시간</td>
      <td>
        날짜 및 시간 비교에 사용되는 타임스탬프 값입니다. 중첩된 시간 커스텀 속성을 필터링할 때 다음 중 선택할 수 있습니다:<br><br>
        <ul>
          <li><strong>Day of Year</strong>: 비교를 위해 월과 일만 확인합니다. 예를 들어 <code>03-15</code>입니다.</li>
          <li><strong>Time</strong>: 연도를 포함한 전체 타임스탬프를 비교합니다. 예를 들어 <code>2023-03-15T12:00:00Z</code>입니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>오브젝트</td>
      <td>키-값 쌍으로 구성된 구조화된 값으로, 예를 들어 <code>{"author": "Tolkien"}</code>입니다.</td>
    </tr>
    <tr>
      <td>오브젝트 배열</td>
      <td>
        오브젝트의 목록으로, 예를 들어 <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>입니다.
        자세한 내용은
        <a href="{{site.baseurl}}/array_of_objects/">오브젝트 배열</a> 을 참조하세요.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 데이터 유형" }