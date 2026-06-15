---
nav_title: Sageflo
article_title: Sageflo Radiate
description: "이 참조 문서에서는 Braze와 Sageflo 간의 파트너십을 설명합니다. Sageflo는 마케팅 승인 템플릿, 이미지, 오디언스 Segments를 Braze와의 API 통합을 통해 팀이 손쉽게 자체 이메일을 발송할 수 있도록 지원하는 분산 마케팅 도구입니다."
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiate](https://sageflo.com/radiate)는 마케팅 승인 템플릿, 이미지, 오디언스 Segments를 Braze와의 API 통합을 통해 로컬 팀이 손쉽게 자체 이메일을 발송할 수 있도록 지원하는 분산 마케팅 도구입니다.

_이 통합은 Sageflo에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

오디언스 세분화, 발송 빈도 관리, 동적 콘텐츠 등 Braze의 정교한 기능을 활용하여 로컬 팀이 더 스마트하게 마케팅할 수 있는 도구를 제공하면서도 브랜드 가이드라인을 유지할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sageflo Radiate 계정 | 이 파트너십을 활용하려면 Sageflo Radiate 계정이 필요합니다. |
| Braze REST API 키 | 전체 `templates` 및 `campaigns` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). API 엔드포인트는 Braze 인스턴스의 대시보드 URL과 일치합니다. <br><br> 예를 들어, 대시보드 URL이 `https://dashboard-03.braze.com`이면 엔드포인트는 `dashboard-03`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Radiate는 분산 팀이 Braze를 통해 로컬 오디언스에게 이메일을 발송할 수 있도록 지원하여 마케팅 활동을 확장하려는 프랜차이즈 및 리테일 비즈니스에 이상적입니다.

* 분산 팀이 마케팅 이메일과 SMS를 손쉽게 발송할 수 있도록 지원
* 고객과 커뮤니티 중심의 유대 관계 구축
* 내장된 가이드라인으로 브랜드 일관성 유지
* 본사 마케팅 팀의 부담 경감

## 통합 {#integration}

Sageflo 계정 팀이 통합 설정을 주도합니다. Braze API 자격 증명을 제공해야 하며, Sageflo는 마케팅 팀과 협력하여 특정 위치 및 지점에 대한 오디언스 Segments를 구성합니다.

연결이 완료되면 Sageflo에서 다음을 수행합니다.

* Radiate 환경 및 Braze 연결 설정
* Braze에서 위치 기반 오디언스 Segments 구성
* Campaign, 위치 및 사용자 그룹 설정 정의
* Braze의 템플릿을 Radiate Campaigns에서 사용할 수 있도록 매핑
* 사용자 교육 일정 수립 및 진행