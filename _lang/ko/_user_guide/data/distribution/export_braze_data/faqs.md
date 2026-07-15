---
nav_title: FAQ
article_title: 내보내기 FAQ
page_order: 7
page_type: FAQ
description: "이 문서에서는 API 및 CSV 내보내기에 대해 자주 묻는 질문 몇 가지를 다룹니다."

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 API 및 CSV 내보내기에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 특정 내보내기만 S3 버킷에 표시하고 나머지는 표시하지 않도록 설정할 수 있나요? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

아니요. S3 인증정보를 제공한 경우 모든 내보내기가 사용자의 S3 버킷에 표시되며, 인증정보를 제공하지 않은 경우 모든 내보내기는 Braze에 속한 S3 버킷에 표시됩니다.

## 데이터를 내보내려면 Braze에 S3 인증정보를 추가해야 하나요? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

아니요. S3 인증정보를 추가하지 않으면 내보내기가 Braze에 속한 S3 버킷에 표시됩니다.

## 대시보드에서 S3 인증정보를 설정했지만 "Make this the default data export destination"을 선택하지 않은 경우 어떻게 되나요? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

**Make this the default data export destination** 확인란은 S3와 Azure 모두에 대한 인증정보를 추가했다고 가정할 때, 내보내기가 S3로 전송되는지 Azure로 전송되는지에 영향을 줍니다.

## 기본 데이터 내보내기 대상이 Braze 커런츠에 영향을 주나요? {#does-the-default-data-export-destination-affect-braze-currents}

아니요. Currents는 자체 커넥터 및 스토리지 설정을 사용합니다. CSV 및 API 기반 내보내기의 기본 내보내기 대상을 선택해도 Currents 데이터가 기록되는 위치는 변경되지 않습니다.

## 고객 프로필을 S3로 내보낼 때 여러 개의 파일을 받는 이유는 무엇인가요? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

이는 사용자가 많은 워크스페이스에서 예상되는 동작입니다. Braze는 워크스페이스의 사용자 수에 따라 내보내기를 여러 파일로 분할합니다. 일반적으로 사용자 5,000명당 1개의 파일이 출력됩니다. 큰 워크스페이스 내에서 작은 세그먼트를 내보내는 경우에도 여러 개의 파일을 받을 수 있다는 점에 유의하세요.

## REST API를 통해 세그먼트별로 사용자를 내보낼 때 중복된 사용자가 표시되는 이유는 무엇인가요? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

이는 데이터베이스 제공업체의 기본 아키텍처로 인해 발생하는 매우 드문 현상입니다. 중복 항목은 매주 정리되지만, 대부분의 경우 정리할 중복 항목이 없습니다.

## Excel에서 CSV 보고서를 열려면 어떻게 하나요? {#how-do-i-open-csv-reports-in-excel}

CSV 파일은 일반적으로 기본값으로 Excel에서 자동으로 열리지만, 항상 그런 것은 아닙니다. Excel을 기본 프로그램으로 설정하는 방법은 [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) 및 [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) 문제 해결 문서를 참조하세요.

CSV를 XLSX 또는 XLS로 변환하거나 데이터 값 사이의 쉼표를 제거하려면 Excel로 CSV를 가져오는 방법에 대한 [이 가이드](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard)를 참조하세요.

CSV 내보내기에서 사용자 ID의 앞자리 0이 제거되는 경우, 이는 Excel이 CSV의 숫자를 텍스트가 아닌 데이터로 처리하기 때문입니다. 이 문제를 해결하려면 [Excel 텍스트 가져오기 마법사](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros)를 실행하세요.