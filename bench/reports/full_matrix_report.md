# GLiNER Full Matrix Benchmark Report

**Date:** 2026-05-27 11:37
**Platform:** macOS Apple Silicon
**Test cases:** 18 (10 languages, Wikipedia: Taiwan)
**Threshold:** 0.3
**Timing:** 3 runs after 1 warmup

---
## Summary by Model × Backend

| Model | Variant | Backend | Avg F1 | Avg Latency | Languages OK | Errors |
|-------|---------|---------|--------|-------------|--------------|--------|
| gliner-x-base | pytorch | pytorch-cpu | 0.407 | 35ms | 10/10 | 0 |
| gliner-x-base | pytorch | pytorch-mps | 0.407 | 22ms | 10/10 | 0 |
| gliner-x-large | pytorch | pytorch-cpu | 0.437 | 76ms | 10/10 | 0 |
| gliner-x-large | pytorch | pytorch-mps | 0.437 | 28ms | 10/10 | 0 |
| gliner-x-small | pytorch | pytorch-cpu | 0.370 | 21ms | 10/10 | 0 |
| gliner-x-small | pytorch | pytorch-mps | 0.370 | 21ms | 10/10 | 0 |
| gliner2-multi-v1 | onnx-multi | gliner2 | 0.000 | 0ms | 0/10 | 1 |
| gliner_large-v2.5 | pytorch | pytorch-cpu | 0.329 | 111ms | 10/10 | 0 |
| gliner_large-v2.5 | pytorch | pytorch-mps | 0.329 | 29ms | 10/10 | 0 |
| gliner_medium-v2.5 | pytorch | pytorch-cpu | 0.352 | 42ms | 10/10 | 0 |
| gliner_medium-v2.5 | pytorch | pytorch-mps | 0.352 | 20ms | 10/10 | 0 |
| gliner_small-v2.5 | pytorch | pytorch-cpu | 0.370 | 25ms | 10/10 | 0 |
| gliner_small-v2.5 | pytorch | pytorch-mps | 0.370 | 16ms | 10/10 | 0 |
| large-v2.5 | fp32 | onnx-CPU | 0.329 | 45ms | 10/10 | 0 |
| large-v2.5 | fp32 | onnx-CoreML | 0.329 | 129ms | 10/10 | 0 |
| medium-v2.5 | fp16 | onnx-CPU | 0.352 | 30ms | 10/10 | 0 |
| medium-v2.5 | fp16 | onnx-CoreML | 0.352 | 32ms | 10/10 | 0 |
| medium-v2.5 | fp32 | onnx-CPU | 0.352 | 18ms | 10/10 | 0 |
| medium-v2.5 | fp32 | onnx-CoreML | 0.352 | 56ms | 10/10 | 0 |
| medium-v2.5 | int8 | onnx-CPU | 0.073 | 14ms | 10/10 | 0 |
| medium-v2.5 | int8 | onnx-CoreML | 0.036 | 54ms | 10/10 | 0 |
| openmed-relex-base-mlx | mlx | mlx | 0.368 | 11ms | 10/10 | 0 |
| small-v2.5 | fp16 | onnx-CPU | 0.370 | 17ms | 10/10 | 0 |
| small-v2.5 | fp16 | onnx-CoreML | 0.370 | 18ms | 10/10 | 0 |
| small-v2.5 | fp32 | cpp-native | 0.000 | 0ms | 0/10 | 18 |
| small-v2.5 | fp32 | onnx-CPU | 0.370 | 11ms | 10/10 | 0 |
| small-v2.5 | fp32 | onnx-CoreML | 0.370 | 34ms | 10/10 | 0 |
| small-v2.5 | int8 | onnx-CPU | 0.337 | 9ms | 10/10 | 0 |
| small-v2.5 | int8 | onnx-CoreML | 0.324 | 29ms | 10/10 | 0 |

---
## Per-Language F1 Scores

| Model | Variant | Backend | zh-TW | en | ja | ko | ru | fr | es | ar | th | vi |
|-------|---------|---------|------|------|------|------|------|------|------|------|------|------|
| gliner-x-base | pytorch | pytorch-cpu | 0.00 | 0.67 | 0.73 | 0.00 | 0.86 | 0.73 | 0.73 | 0.33 | 0.73 | 0.55 |
| gliner-x-base | pytorch | pytorch-mps | 0.00 | 0.67 | 0.73 | 0.00 | 0.86 | 0.73 | 0.73 | 0.33 | 0.73 | 0.55 |
| gliner-x-large | pytorch | pytorch-cpu | 0.00 | 0.70 | 0.73 | 0.00 | 0.86 | 0.73 | 0.73 | 0.67 | 0.80 | 0.55 |
| gliner-x-large | pytorch | pytorch-mps | 0.00 | 0.70 | 0.73 | 0.00 | 0.86 | 0.73 | 0.73 | 0.67 | 0.80 | 0.55 |
| gliner-x-small | pytorch | pytorch-cpu | 0.00 | 0.61 | 0.67 | 0.00 | 0.86 | 0.73 | 0.73 | 0.33 | 0.36 | 0.55 |
| gliner-x-small | pytorch | pytorch-mps | 0.00 | 0.61 | 0.67 | 0.00 | 0.86 | 0.73 | 0.73 | 0.33 | 0.36 | 0.55 |
| gliner_large-v2.5 | pytorch | pytorch-cpu | 0.00 | 0.69 | 0.00 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| gliner_large-v2.5 | pytorch | pytorch-mps | 0.00 | 0.69 | 0.00 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| gliner_medium-v2.5 | pytorch | pytorch-cpu | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| gliner_medium-v2.5 | pytorch | pytorch-mps | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| gliner_small-v2.5 | pytorch | pytorch-cpu | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| gliner_small-v2.5 | pytorch | pytorch-mps | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| large-v2.5 | fp32 | onnx-CPU | 0.00 | 0.69 | 0.00 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| large-v2.5 | fp32 | onnx-CoreML | 0.00 | 0.69 | 0.00 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| medium-v2.5 | fp16 | onnx-CPU | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp16 | onnx-CoreML | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp32 | onnx-CPU | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp32 | onnx-CoreML | 0.04 | 0.61 | 0.00 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | int8 | onnx-CPU | 0.00 | 0.15 | 0.00 | 0.00 | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.29 |
| medium-v2.5 | int8 | onnx-CoreML | 0.00 | 0.05 | 0.00 | 0.00 | 0.22 | 0.22 | 0.00 | 0.00 | 0.00 | 0.00 |
| openmed-relex-base-mlx | mlx | mlx | 0.13 | 0.66 | 0.00 | 0.00 | 0.60 | 0.73 | 0.73 | 0.00 | 0.33 | 0.80 |
| small-v2.5 | fp16 | onnx-CPU | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp16 | onnx-CoreML | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp32 | onnx-CPU | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp32 | onnx-CoreML | 0.07 | 0.63 | 0.00 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | int8 | onnx-CPU | 0.07 | 0.59 | 0.00 | 0.00 | 0.80 | 0.73 | 0.91 | 0.20 | 0.33 | 0.36 |
| small-v2.5 | int8 | onnx-CoreML | 0.00 | 0.61 | 0.00 | 0.00 | 0.67 | 0.73 | 0.91 | 0.20 | 0.33 | 0.55 |

---
## Detailed Results


### gliner-x-base / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 29ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 29ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 28ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 29ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 42ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 38ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 34ms | TSMC, 90%, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 36ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 28ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 23ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 37ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 32ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 36ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 42ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 40ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 44ms | تايوان, جمهورية الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.73 | 0.67 | 0.80 | 34ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 41ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-base / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 20ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 21ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 15ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 14ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 31ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 24ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 22ms | TSMC, 90%, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 22ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 13ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 13ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 21ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 18ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 22ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 29ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 28ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 32ms | تايوان, جمهورية الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.73 | 0.67 | 0.80 | 21ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 25ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-large / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 73ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 72ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 64ms | 台積電董事長魏哲家宣布在高雄 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 63ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.62 | 0.50 | 0.83 | 85ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 85ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 73ms | TSMC, market capitalization, 90%, Taiwan, GDP +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 71ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 62ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 62ms | 2017年台, 北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 84ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 77ms | 타이완은, 동아시아에, 중화민국이다, 타이베이이며, TSMC는 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 82ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 83ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 87ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.67 | 0.57 | 0.80 | 85ms | تايوان, جمهورية الصين, شرق آسيا, تايبيه, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.80 | 0.80 | 0.80 | 80ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 87ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-large / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 23ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 20ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 19ms | 台積電董事長魏哲家宣布在高雄 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 18ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.62 | 0.50 | 0.83 | 38ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 32ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 28ms | TSMC, market capitalization, 90%, Taiwan, GDP +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 28ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 18ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 18ms | 2017年台, 北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 31ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 24ms | 타이완은, 동아시아에, 중화민국이다, 타이베이이며, TSMC는 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 29ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 37ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 34ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.67 | 0.57 | 0.80 | 39ms | تايوان, جمهورية الصين, شرق آسيا, تايبيه, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.80 | 0.80 | 0.80 | 28ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 34ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-small / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 17ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 16ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 13ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 12ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 30ms | Taiwan, Republic of China, ROC, East Asia, East +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 26ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 20ms | TSMC, 90%, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 20ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 12ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 12ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.67 | 0.57 | 0.80 | 24ms | 台湾, 東アジア, 島, 中華民国, 台北市 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 20ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 24ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 30ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 28ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 32ms | تايوان, الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.36 | 0.33 | 0.40 | 22ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป TSMC, เซมิคอน +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 28ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-small / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 20ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 13ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 14ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 14ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 31ms | Taiwan, Republic of China, ROC, East Asia, East +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 24ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 22ms | TSMC, 90%, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 22ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 12ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 12ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.67 | 0.57 | 0.80 | 20ms | 台湾, 東アジア, 島, 中華民国, 台北市 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 21ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 28ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 28ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 33ms | تايوان, الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.36 | 0.33 | 0.40 | 20ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป TSMC, เซมิคอน +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 27ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner2-multi-v1 / onnx-multi / gliner2

**ERROR:** RepositoryNotFoundError: 404 Client Error. (Request ID: Root=1-6a1666e2-25f19078185fdb2d772232b2;42fbc109-c264-4474-b4dc-5b826cd2d9cf)

Repository Not Found for url: https://huggingface.co/SemplificaAI/gliner2-multi-v1/resolve/main/config.json.
Please make sure you specified the correct `repo_id` and `repo_type`.
If you are trying to access a private or gated repo, make sure you are authenticated and your token has the required permissions.
For more details, see https://huggingface.co/docs/huggingface_hub/authentication


### gliner_large-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 104ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 105ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 99ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 109ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 114ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 111ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 93ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 92ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 109ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 97ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 109ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 113ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 115ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 117ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 112ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 118ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 158ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 119ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_large-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 26ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 28ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 22ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 24ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 34ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 31ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 27ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 26ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 25ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 21ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 26ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 29ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 32ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 34ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 30ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 34ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 45ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 36ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_medium-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 41ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 42ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 37ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 41ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 46ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 44ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 32ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 31ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 41ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 33ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 40ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 43ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 46ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 45ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 43ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 47ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 63ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 49ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_medium-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 17ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 17ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 14ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 14ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 25ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 27ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 19ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 18ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 16ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 12ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 17ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 22ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 19ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 21ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 20ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 21ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 29ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 22ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_small-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 23ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 24ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 21ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 23ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 28ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 26ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 20ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 19ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 23ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 19ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 22ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 24ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 27ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 27ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 25ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 27ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 37ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 29ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_small-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 14ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 16ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 13ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 14ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 21ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 18ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 16ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 14ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 15ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 11ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 13ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 16ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 15ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 19ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 16ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 17ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 22ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 20ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### large-v2.5 / fp32 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 42ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 42ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 32ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 42ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 46ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 43ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 33ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 32ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 40ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 30ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 41ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 43ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 53ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 45ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 44ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 53ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 93ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 56ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### large-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 125ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 125ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 102ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 117ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 124ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 119ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 99ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 98ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 119ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 98ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 123ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 129ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 144ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 131ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 121ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 154ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 238ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 155ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp16 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 29ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 30ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 24ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 28ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 33ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 30ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 25ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 24ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 27ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 22ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 28ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 30ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 34ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 32ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 30ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 35ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 46ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 37ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp16 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 30ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 31ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 26ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 30ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 35ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 32ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 27ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 26ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 30ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 24ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 30ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 32ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 35ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 34ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 32ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 35ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 48ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 38ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp32 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 15ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 16ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 12ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 15ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 20ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 18ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 14ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 13ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 15ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 11ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 15ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 20ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 20ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 18ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 22ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 34ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 22ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 53ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 54ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 45ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 51ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 59ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 53ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 46ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 44ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 50ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 42ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 51ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 55ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 62ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 59ms | Taïwan, République de Chine, Asie de l ' Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 54ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 67ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 99ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 67ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / int8 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 13ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 14ms |  | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 10ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 12ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.18 | 0.20 | 0.17 | 16ms | Taiwan, Republic of China, ROC, PRC, Japan | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.00 | 0.00 | 0.00 | 14ms | Fort Zeelandia, Tayouan, Shimonoseki | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.00 | 0.00 | 0.00 | 10ms | TSMC, Taiwan, Samsung | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.40 | 0.50 | 0.33 | 10ms | Democratic Progressive Party, Taiwan | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 12ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 9ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 12ms |  | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 14ms |  | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.44 | 1.00 | 0.29 | 16ms | Тайвань, Тайбэй | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.00 | 0.00 | 0.00 | 16ms | Taïwan, Shimonoseki, TSMC | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.00 | 0.00 | 0.00 | 14ms | Taiwán, Shimonoseki | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 17ms |  | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 29ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.29 | 0.50 | 0.20 | 19ms | Đài Loan, Trung Hoa Dân Quốc | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / int8 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 49ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 50ms |  | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 40ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 45ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.00 | 0.00 | 0.00 | 53ms | Taiwan, PRC, Japan | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.20 | 0.20 | 0.20 | 48ms | Fort Zeelandia, Tayouan, Dutch, 1895, Shimonoseki | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.00 | 0.00 | 0.00 | 39ms | TSMC, Taiwan, Samsung | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.00 | 0.00 | 0.00 | 38ms | Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 45ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 38ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 48ms |  | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 54ms |  | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.22 | 0.50 | 0.14 | 59ms | Филиппинами, Китайская Республика | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.22 | 0.25 | 0.20 | 59ms | Taïwan, Chine, Shimonoseki, TSMC | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.00 | 0.00 | 0.00 | 56ms | Taiwán, China, Asia Oriental | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 76ms |  | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 108ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.00 | 0.00 | 0.00 | 72ms | Trung Hoa | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### openmed-relex-base-mlx / mlx / mlx

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 12ms | 臺灣位於東亞, 西隔臺灣海峽與亞洲大陸相望 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 11ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +2 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 9ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 10ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 13ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 11ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 10ms | TSMC, market capitalization, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 10ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 10ms | 玉山為臺灣最高峰, 臺灣主要河川有濁水溪, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 9ms | 2017年台北世大運在臺北市舉行, 棒球選手王建民曾效力於MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 10ms | 台湾は東アジアに位置する島で, 2024年に頼清徳が総統に就任した, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 10ms | 동아시아에, 섬나라로, 타이베이이며, TSMC는, 2024년 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.60 | 1.00 | 0.43 | 11ms | Восточной Азии, Тайбэй, TSMC | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 12ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 11ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 12ms | شرق آسيا, تايبيه, شركة TSMC, العالم, منصب الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 14ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.80 | 0.80 | 0.80 | 12ms | Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC, Lại Thanh Đức | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp16 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 17ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 16ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 13ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 15ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 20ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 18ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 15ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 14ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 15ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 12ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 15ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 19ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 20ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 18ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 20ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 27ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 22ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp16 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 16ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 17ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 14ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 16ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 21ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 19ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 16ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 15ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 16ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 13ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 16ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 20ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 20ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 18ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 21ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 28ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 22ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp32 / cpp-native

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| en | Taiwan, officially the Republic of China | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| en | In 1624, the Dutch East India Company es | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| en | TSMC's market capitalization equated to  | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| en | President Lai Ching-te of the Democratic | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年 | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는  | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| ru | Тайвань расположен в Восточной Азии, меж | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| fr | Taïwan, officiellement la République de  | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| es | Taiwán, oficialmente la República de Chi | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين،  | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ | ERROR | — | — | — | — | CLI interface not yet implemented for batch testing |

### small-v2.5 / fp32 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 9ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 10ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 7ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 9ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 14ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 12ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 9ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 8ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 9ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 6ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 9ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 10ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 12ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 13ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 11ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 13ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 21ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 15ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 32ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 32ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 27ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 30ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 37ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 34ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 30ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 28ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 30ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 25ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 30ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 32ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 36ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 36ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 34ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 39ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 56ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 41ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / int8 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 7ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 8ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 6ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 7ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 11ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.57 | 0.44 | 0.80 | 9ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 7ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 6ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 7ms | 玉山為臺灣最高峰, 臺灣主要河川有濁水溪, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 5ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 7ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 9ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +3 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.80 | 0.75 | 0.86 | 9ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +3 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 10ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.91 | 0.83 | 1.00 | 9ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.20 | 0.20 | 0.20 | 11ms | الصين, آسيا, TSMC, العالم, الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 17ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.36 | 0.33 | 0.40 | 12ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / int8 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 26ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 27ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 1895年, 清廷因甲午戰爭失敗 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 22ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 24ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 31ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 28ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 23ms | TSMC, Taiwan, GDP, semiconductor manufacturing company, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 22ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 24ms | 玉山為臺灣最高峰, 臺灣主要河川有濁水溪, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 19ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 24ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 27ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +3 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.67 | 0.62 | 0.71 | 30ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика . Столица — Тайбэй +3 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 31ms | Taïwan, République de Chine, Asie de l ' Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.91 | 0.83 | 1.00 | 28ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.20 | 0.20 | 0.20 | 35ms | الصين, آسيا, TSMC, العالم, الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 54ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 38ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

---
## Quantization Impact

| Model | fp32 F1 | fp16 F1 | int8 F1 | fp16 Δ | int8 Δ |
|-------|---------|---------|---------|--------|--------|
| small-v2.5 | 0.370 | 0.370 | 0.331 | +0.000 | -0.039 |
| medium-v2.5 | 0.352 | 0.352 | 0.054 | +0.000 | -0.297 |
| large-v2.5 | 0.329 | — | — | — | — |

---
*Total benchmark time: 159s*
