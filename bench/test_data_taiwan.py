"""
Multilingual NER test data based on Wikipedia: Taiwan (臺灣)
Source: zh.wikipedia.org/wiki/台灣, en.wikipedia.org/wiki/Taiwan
"""

TEST_CASES = [
    # --- 中文（繁體）---
    {
        "lang": "zh-TW",
        "text": "臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。",
        "labels": ["location", "organization", "body_of_water"],
        "expected": [
            {"text": "臺灣", "label": "location"},
            {"text": "東亞", "label": "location"},
            {"text": "太平洋", "label": "location"},
            {"text": "琉球群島", "label": "location"},
            {"text": "菲律賓群島", "label": "location"},
            {"text": "臺灣海峽", "label": "body_of_water"},
            {"text": "中華民國", "label": "organization"},
        ],
    },
    {
        "lang": "zh-TW",
        "text": "1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。",
        "labels": ["person", "organization", "location", "event", "date"],
        "expected": [
            {"text": "荷蘭東印度公司", "label": "organization"},
            {"text": "鄭成功", "label": "person"},
            {"text": "甲午戰爭", "label": "event"},
            {"text": "馬關條約", "label": "event"},
            {"text": "日本", "label": "location"},
        ],
    },
    {
        "lang": "zh-TW",
        "text": "台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席動土典禮。",
        "labels": ["person", "organization", "location", "money"],
        "expected": [
            {"text": "台積電", "label": "organization"},
            {"text": "魏哲家", "label": "person"},
            {"text": "高雄", "label": "location"},
            {"text": "蔡英文", "label": "person"},
        ],
    },
    {
        "lang": "zh-TW",
        "text": "臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。",
        "labels": ["location", "event", "date"],
        "expected": [
            {"text": "臺灣", "label": "location"},
            {"text": "臺灣奇蹟", "label": "event"},
            {"text": "亞洲四小龍", "label": "location"},
        ],
    },
    # --- English ---
    {
        "lang": "en",
        "text": "Taiwan, officially the Republic of China (ROC), is a country in East Asia. It lies between the East and South China Seas in the northwestern Pacific Ocean, with the People's Republic of China (PRC) to the northwest, Japan to the northeast, and the Philippines to the south.",
        "labels": ["country", "organization", "body_of_water", "location"],
        "expected": [
            {"text": "Taiwan", "label": "country"},
            {"text": "Republic of China", "label": "organization"},
            {"text": "East Asia", "label": "location"},
            {"text": "Pacific Ocean", "label": "body_of_water"},
            {"text": "Japan", "label": "country"},
            {"text": "Philippines", "label": "country"},
        ],
    },
    {
        "lang": "en",
        "text": "In 1624, the Dutch East India Company established Fort Zeelandia on the coastal islet of Tayouan. Koxinga expelled the Dutch in 1662. The island was ceded to the Empire of Japan in 1895 by the Treaty of Shimonoseki.",
        "labels": ["person", "organization", "location", "event", "date"],
        "expected": [
            {"text": "Dutch East India Company", "label": "organization"},
            {"text": "Fort Zeelandia", "label": "location"},
            {"text": "Koxinga", "label": "person"},
            {"text": "Treaty of Shimonoseki", "label": "event"},
            {"text": "Empire of Japan", "label": "organization"},
        ],
    },
    {
        "lang": "en",
        "text": "TSMC's market capitalization equated to roughly 90% of Taiwan's GDP. The company is the world's biggest semiconductor manufacturing company, surpassing Intel and Samsung.",
        "labels": ["organization", "location", "metric"],
        "expected": [
            {"text": "TSMC", "label": "organization"},
            {"text": "Taiwan", "label": "location"},
            {"text": "Intel", "label": "organization"},
            {"text": "Samsung", "label": "organization"},
        ],
    },
    {
        "lang": "en",
        "text": "President Lai Ching-te of the Democratic Progressive Party won Taiwan's 2024 presidential election. The Kuomintang won 52 seats in the simultaneous legislative election.",
        "labels": ["person", "organization", "event", "date"],
        "expected": [
            {"text": "Lai Ching-te", "label": "person"},
            {"text": "Democratic Progressive Party", "label": "organization"},
            {"text": "Kuomintang", "label": "organization"},
        ],
    },
    # --- 地理 / Geography ---
    {
        "lang": "zh-TW",
        "text": "玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。",
        "labels": ["mountain", "river", "lake", "location"],
        "expected": [
            {"text": "玉山", "label": "mountain"},
            {"text": "濁水溪", "label": "river"},
            {"text": "高屏溪", "label": "river"},
            {"text": "淡水河", "label": "river"},
            {"text": "日月潭", "label": "lake"},
        ],
    },
    # --- 混合語言 Mixed ---
    {
        "lang": "zh-TW",
        "text": "2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。",
        "labels": ["person", "organization", "event", "location"],
        "expected": [
            {"text": "台北世大運", "label": "event"},
            {"text": "臺北市", "label": "location"},
            {"text": "王建民", "label": "person"},
            {"text": "紐約洋基隊", "label": "organization"},
        ],
    },
    # --- 日本語 ---
    {
        "lang": "ja",
        "text": "台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年に頼清徳が総統に就任した。TSMCは世界最大の半導体製造企業である。",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "台湾", "label": "location"},
            {"text": "中華民国", "label": "organization"},
            {"text": "台北市", "label": "location"},
            {"text": "頼清徳", "label": "person"},
            {"text": "TSMC", "label": "organization"},
        ],
    },
    # --- 한국어 ---
    {
        "lang": "ko",
        "text": "타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 타이베이이며, TSMC는 세계 최대의 반도체 제조 기업이다. 2024년 라이칭더가 총통으로 취임했다.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "타이완", "label": "location"},
            {"text": "중화민국", "label": "organization"},
            {"text": "타이베이", "label": "location"},
            {"text": "TSMC", "label": "organization"},
            {"text": "라이칭더", "label": "person"},
        ],
    },
    # --- Русский ---
    {
        "lang": "ru",
        "text": "Тайвань расположен в Восточной Азии, между Японией и Филиппинами. Официальное название — Китайская Республика. Столица — Тайбэй. Компания TSMC является крупнейшим производителем полупроводников в мире.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "Тайвань", "label": "location"},
            {"text": "Восточной Азии", "label": "location"},
            {"text": "Японией", "label": "location"},
            {"text": "Филиппинами", "label": "location"},
            {"text": "Китайская Республика", "label": "organization"},
            {"text": "Тайбэй", "label": "location"},
            {"text": "TSMC", "label": "organization"},
        ],
    },
    # --- Français ---
    {
        "lang": "fr",
        "text": "Taïwan, officiellement la République de Chine, est un pays d'Asie de l'Est. En 1895, l'île fut cédée au Japon par le traité de Shimonoseki. TSMC, fondée en 1987, est le plus grand fabricant de semi-conducteurs au monde.",
        "labels": ["person", "organization", "location", "event"],
        "expected": [
            {"text": "Taïwan", "label": "location"},
            {"text": "République de Chine", "label": "organization"},
            {"text": "Japon", "label": "location"},
            {"text": "traité de Shimonoseki", "label": "event"},
            {"text": "TSMC", "label": "organization"},
        ],
    },
    # --- Español ---
    {
        "lang": "es",
        "text": "Taiwán, oficialmente la República de China, es un país en Asia Oriental. La isla fue cedida a Japón en 1895 mediante el Tratado de Shimonoseki. TSMC es la empresa de semiconductores más grande del mundo.",
        "labels": ["person", "organization", "location", "event"],
        "expected": [
            {"text": "Taiwán", "label": "location"},
            {"text": "República de China", "label": "organization"},
            {"text": "Japón", "label": "location"},
            {"text": "Tratado de Shimonoseki", "label": "event"},
            {"text": "TSMC", "label": "organization"},
        ],
    },
    # --- العربية ---
    {
        "lang": "ar",
        "text": "تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبيه. شركة TSMC هي أكبر شركة لتصنيع أشباه الموصلات في العالم. في عام 2024، تولى لاي تشينغ ته منصب الرئيس.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "تايوان", "label": "location"},
            {"text": "جمهورية الصين", "label": "organization"},
            {"text": "تايبيه", "label": "location"},
            {"text": "TSMC", "label": "organization"},
            {"text": "لاي تشينغ ته", "label": "person"},
        ],
    },
    # --- ภาษาไทย ---
    {
        "lang": "th",
        "text": "ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย่างเป็นทางการว่าสาธารณรัฐจีน เมืองหลวงคือไทเป TSMC เป็นบริษัทผลิตเซมิคอนดักเตอร์ที่ใหญ่ที่สุดในโลก",
        "labels": ["organization", "location"],
        "expected": [
            {"text": "ไต้หวัน", "label": "location"},
            {"text": "เอเชียตะวันออก", "label": "location"},
            {"text": "สาธารณรัฐจีน", "label": "organization"},
            {"text": "ไทเป", "label": "location"},
            {"text": "TSMC", "label": "organization"},
        ],
    },
    # --- Tiếng Việt ---
    {
        "lang": "vi",
        "text": "Đài Loan, tên chính thức là Trung Hoa Dân Quốc, là một quốc gia tại Đông Á. Thủ đô là Đài Bắc. TSMC là công ty sản xuất chất bán dẫn lớn nhất thế giới. Năm 2024, ông Lại Thanh Đức nhậm chức tổng thống.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "Đài Loan", "label": "location"},
            {"text": "Trung Hoa Dân Quốc", "label": "organization"},
            {"text": "Đài Bắc", "label": "location"},
            {"text": "TSMC", "label": "organization"},
            {"text": "Lại Thanh Đức", "label": "person"},
        ],
    },
]

# Entity labels for NER
NER_LABELS = [
    "person", "organization", "location", "country",
    "body_of_water", "mountain", "river", "lake",
    "event", "date", "money", "metric",
]

# Relation labels for RE
RE_LABELS = [
    "located in", "capital of", "president of", "founded by",
    "ceded to", "part of", "headquartered in",
]
