#상품 목록

products = [
    {"id": 1, "category": "상의", "name": "투톤 반팔 셔츠", "season": ["여름"], "price": 15000, "img":"https://img.29cm.co.kr/item/202405/11ef16738c54eaf1bb1443a7c3eb44de.jpg?width=700"},
    {"id": 2, "category": "상의", "name": "카라 화이트 블라우스", "season": ["봄", "가을"], "price": 25000, "img": "https://img.29cm.co.kr/next-product/2019/10/23/e946ab9e3dc44ee982120ef42857def4_20191023001147.jpg?width=700"},
    {"id": 3, "category": "상의", "name": "캐릭터 티셔츠", "season": ["봄", "가을", "여름"], "price": 35000, "img": "https://img.29cm.co.kr/next-product/2022/06/16/c9f1e2273e064d938a09a062f29f5611_20220616112810.jpg?width=700"},
    {"id": 4, "category": "상의", "name": "라운드넥 심플 블랙 티셔츠", "season": ["봄", "가을", "여름"], "price": 45000, "img": "https://img.29cm.co.kr/item/202403/11eeec1da2dccc62bb6a2f445e0bcb04.jpg?width=700"},
    {"id": 5, "category": "상의", "name": "브이넥 민소매", "season": ["여름"], "price": 30000, "img": "https://img.29cm.co.kr/next-product/2024/02/14/63e7f893125d4e6d8a85ead2cb7a7eb0_20240214183031.jpg?width=400"},
    {"id": 6, "category": "상의", "name": "긴소매 크롭 탑", "season": ["봄", "가을"], "price": 15000, "img": "https://img.29cm.co.kr/item/202405/11ef0c56ed26abfdb9bbe5cdaafbf2e7.jpg?width=700"},
    {"id": 7, "category": "상의", "name": "긴팔 스트라이프 블루 셔츠", "season": ["봄", "가을"], "price": 25000, "img":"https://img.29cm.co.kr/item/202308/11ee3a831bbd1fcf8a6969d67e2ce6f3.jpg?width=700"},
    {"id": 8, "category": "상의", "name": "심플 긴팔 니트", "season": ["가을", "겨울"], "price": 35000, "img": "https://img.29cm.co.kr/next-product/2023/06/07/8c910decf16b403c83ec6ab10c8d4d70_20230607183439.jpg?width=700"},
    {"id": 9, "category": "상의", "name": "기모 맨투맨", "season": ["가을", "겨울"], "price": 45000, "img": "https://img.29cm.co.kr/next-product/2022/08/22/d24018735c2c4df09214d5f42841a39d_20220822170736.jpg?width=700"},
    {"id": 10, "category": "상의",  "name": "피그먼트 후드티", "season": ["봄", "가을"], "price": 30000, "img": "https://img.29cm.co.kr/next-product/2021/10/01/601dec739c9141d68f59b29d3ad5d10a_20211001091804.jpg?width=700"},
    {"id": 11, "category" : "하의", "name": "미들 웨이스트 플리츠 치마바지", "season": ["봄", "가을"], "price": 40000, "img": "https://img.29cm.co.kr/item/202403/11eedd1fb54a64929a7665130c0acdce.jpg?width=700"},
    {"id": 12, "category" : "하의", "name": "데님 롱스커트", "season": ["봄", "가을"], "price": 35000, "img": "https://img.29cm.co.kr/next-product/2023/05/06/e2ec9d103b0b4b98889cb53e6ac97b51_20230506190404.jpg?width=700"},
    {"id": 13, "category" : "하의", "name": "흰 반바지", "season": ["여름"], "price": 25000, "img": "https://img.29cm.co.kr/item/202404/11eefde88157834388b12dc57a041cb9.jpg?width=700"},
    {"id": 14, "category" : "하의", "name": "긴 청바지", "season": ["겨울"], "price": 30000, "img": "https://img.29cm.co.kr/next-product/2021/02/25/3c1af1e3f79344f6b93fbeaf1e277710_20210225174242.jpg?width=700"},
    {"id": 15, "category" : "하의", "name": "짧은 청바지", "season": ["여름"], "price": 20000, "img": "https://img.29cm.co.kr/next-product/2024/01/10/070c3c4abb5f4c68ac78411cd1a54188_20240110123725.jpg?width=700"},
    {"id": 16, "category" : "하의", "name": "플로럴 레이어드 맥시 스커트", "season": ["봄", "가을"], "price": 40000, "img": "https://img.29cm.co.kr/item/202405/11ef18d96dd218c4892b7f5dd4232441.jpg?width=700"},
    {"id": 17, "category" : "하의", "name": "카고 조거 팬츠", "season": ["봄", "가을"], "price": 35000, "img": "https://img.29cm.co.kr/next-product/2021/11/11/3e2a65b4d4e841d89a639400673faca5_20211111113205.jpg?width=700"},
    {"id": 18, "category" : "하의", "name": "블랙 카고 반바지", "season": ["여름"], "price": 25000, "img":"https://img.29cm.co.kr/next-product/2024/04/23/9a9fb5c2513a4217a8f9ddb25bddffff_20240423140923.jpg?width=700"},
    {"id": 19, "category" : "하의", "name": "와이드 레그 팬츠", "season": ["겨울"], "price": 30000, "img": "https://img.29cm.co.kr/item/202401/11eec01ef52701e191eb715b9d2c4f9a.jpg?width=700"},
    {"id": 20, "category" : "하의", "name": "찢어진 스트레이트 레그 진", "season": ["여름"], "price": 20000, "img": "https://img.29cm.co.kr/next-product/2024/02/19/00486ace62c24af08de7f6651af4b6c5_20240219185431.jpg?width=700"},
    {"id": 21, "category" : "아우터", "name": "남색 바람막이", "season": ["봄", "가을"], "price": 55000, "img": "https://img.29cm.co.kr/item/202312/11eea524e67b260f91eb4742d23edb24.jpg?width=700"},
    {"id": 22, "category" : "아우터", "name": "레더 지퍼 자켓", "season": ["겨울"], "price": 70000, "img":"https://img.29cm.co.kr/item/202402/11eed08e7dde06bf91ebdb01a94e85b6.jpg?width=700"},
    {"id": 23, "category" : "아우터", "name": "아이보리 롱코트", "season": ["겨울"], "price": 80000, "img":"https://img.29cm.co.kr/next-product/2021/02/15/2c23d193bf344ea0956f31f75b164163_20210215145717.jpg?width=700"},
    {"id": 24, "category" : "아우터", "name": "후드집업", "season": ["봄", "가을"], "price": 45000, "img":"https://img.29cm.co.kr/item/202403/11eedbb038fe97e291a56f4e0ae4f355.jpg?width=700"},
    {"id": 25, "category" : "아우터", "name": "숏패딩", "season": ["겨울"], "price": 60000, "img":"https://img.29cm.co.kr/next-product/2021/01/12/62e75243675e48a78dc636992748c3be_20210112201551.jpg?width=700"},
    {"id": 26, "category" : "아우터", "name": "청자켓", "season": ["봄", "가을"], "price": 55000, "img":"https://img.29cm.co.kr/item/202405/11ef0c3d42731034892bf97715b8cb9a.png?width=700"},
    {"id": 27, "category" : "아우터", "name": "롱패딩", "season": ["겨울"], "price": 70000, "img": "https://img.29cm.co.kr/next-product/2022/09/13/b8a051e43f5b45d1868d417f5e1ea662_20220913172239.jpg?width=700"},
    {"id": 28, "category" : "아우터", "name": "바이커 크롭 자켓", "season": ["겨울"], "price": 80000, "img":"https://img.29cm.co.kr/item/202310/11ee716ebdb39cd58a7ffb36f50b7746.jpg?width=700"},
    {"id": 29, "category" : "아우터", "name": "조끼 패딩", "season": ["봄", "가을"], "price": 45000, "img":"https://img.29cm.co.kr/next-product/2022/11/10/8b7de9a1ea984abd8e639bbee939b748_20221110142021.jpg?width=700"},
    {"id": 30, "category" : "아우터", "name": "떡볶이 코트", "season": ["겨울"], "price": 60000, "img":"https://img.29cm.co.kr/item/202312/11ee9b15e44094a08377bb3254826260.jpg?width=700"},
]