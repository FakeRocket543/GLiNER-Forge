# GLiNER Full Matrix Benchmark Report

**Date:** 2026-05-27 12:51
**Platform:** macOS Apple Silicon
**Test cases:** 18 (10 languages, Wikipedia: Taiwan)
**Threshold:** 0.3
**Timing:** 3 runs after 1 warmup

---
## Summary by Model × Backend

| Model | Variant | Backend | Avg F1 | Avg Latency | Languages OK | Errors |
|-------|---------|---------|--------|-------------|--------------|--------|
| gliner-x-base | pytorch | pytorch-cpu | 0.407 | 37ms | 10/10 | 0 |
| gliner-x-base | pytorch | pytorch-mps | 0.407 | 28ms | 10/10 | 0 |
| gliner-x-large | pytorch | pytorch-cpu | 0.437 | 80ms | 10/10 | 0 |
| gliner-x-large | pytorch | pytorch-mps | 0.437 | 29ms | 10/10 | 0 |
| gliner-x-small | pytorch | pytorch-cpu | 0.370 | 23ms | 10/10 | 0 |
| gliner-x-small | pytorch | pytorch-mps | 0.370 | 27ms | 10/10 | 0 |
| gliner2-multi-v1 | onnx-multi | gliner2 | 0.000 | 0ms | 0/10 | 1 |
| gliner_large-v2.5 | pytorch | pytorch-cpu | 0.329 | 118ms | 10/10 | 0 |
| gliner_large-v2.5 | pytorch | pytorch-mps | 0.329 | 31ms | 10/10 | 0 |
| gliner_medium-v2.5 | pytorch | pytorch-cpu | 0.352 | 44ms | 10/10 | 0 |
| gliner_medium-v2.5 | pytorch | pytorch-mps | 0.352 | 21ms | 10/10 | 0 |
| gliner_small-v2.5 | pytorch | pytorch-cpu | 0.370 | 25ms | 10/10 | 0 |
| gliner_small-v2.5 | pytorch | pytorch-mps | 0.370 | 21ms | 10/10 | 0 |
| large-v2.5 | fp32 | onnx-CPU | 0.490 | 51ms | 10/10 | 0 |
| large-v2.5 | fp32 | onnx-CoreML | 0.490 | 149ms | 10/10 | 0 |
| medium-v2.5 | fp16 | onnx-CPU | 0.441 | 33ms | 10/10 | 0 |
| medium-v2.5 | fp16 | onnx-CoreML | 0.441 | 35ms | 10/10 | 0 |
| medium-v2.5 | fp32 | onnx-CPU | 0.441 | 20ms | 10/10 | 0 |
| medium-v2.5 | fp32 | onnx-CoreML | 0.441 | 64ms | 10/10 | 0 |
| medium-v2.5 | int8 | onnx-CPU | 0.073 | 18ms | 10/10 | 0 |
| medium-v2.5 | int8 | onnx-CoreML | 0.036 | 62ms | 10/10 | 0 |
| openmed-relex-base-mlx | mlx | mlx | 0.368 | 11ms | 10/10 | 0 |
| small-v2.5 | fp16 | onnx-CPU | 0.465 | 19ms | 10/10 | 0 |
| small-v2.5 | fp16 | onnx-CoreML | 0.465 | 20ms | 10/10 | 0 |
| small-v2.5 | fp32 | cpp-native | 0.000 | 0ms | 0/10 | 18 |
| small-v2.5 | fp32 | onnx-CPU | 0.465 | 13ms | 10/10 | 0 |
| small-v2.5 | fp32 | onnx-CoreML | 0.465 | 38ms | 10/10 | 0 |
| small-v2.5 | int8 | onnx-CPU | 0.368 | 11ms | 10/10 | 0 |
| small-v2.5 | int8 | onnx-CoreML | 0.363 | 34ms | 10/10 | 0 |

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
| large-v2.5 | fp32 | onnx-CPU | 0.43 | 0.69 | 0.29 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| large-v2.5 | fp32 | onnx-CoreML | 0.43 | 0.69 | 0.29 | 0.00 | 0.86 | 0.73 | 0.60 | 0.36 | 0.00 | 0.62 |
| medium-v2.5 | fp16 | onnx-CPU | 0.20 | 0.61 | 0.60 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp16 | onnx-CoreML | 0.20 | 0.61 | 0.60 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp32 | onnx-CPU | 0.20 | 0.61 | 0.60 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | fp32 | onnx-CoreML | 0.20 | 0.61 | 0.60 | 0.00 | 0.75 | 0.73 | 0.73 | 0.29 | 0.33 | 0.83 |
| medium-v2.5 | int8 | onnx-CPU | 0.00 | 0.15 | 0.00 | 0.00 | 0.44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.29 |
| medium-v2.5 | int8 | onnx-CoreML | 0.00 | 0.05 | 0.00 | 0.00 | 0.22 | 0.22 | 0.00 | 0.00 | 0.00 | 0.00 |
| openmed-relex-base-mlx | mlx | mlx | 0.13 | 0.66 | 0.00 | 0.00 | 0.60 | 0.73 | 0.73 | 0.00 | 0.33 | 0.80 |
| small-v2.5 | fp16 | onnx-CPU | 0.27 | 0.63 | 0.50 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp16 | onnx-CoreML | 0.27 | 0.63 | 0.50 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp32 | onnx-CPU | 0.27 | 0.63 | 0.50 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | fp32 | onnx-CoreML | 0.27 | 0.63 | 0.50 | 0.00 | 0.88 | 0.73 | 0.83 | 0.46 | 0.33 | 0.50 |
| small-v2.5 | int8 | onnx-CPU | 0.08 | 0.59 | 0.44 | 0.00 | 0.80 | 0.73 | 0.91 | 0.20 | 0.33 | 0.36 |
| small-v2.5 | int8 | onnx-CoreML | 0.08 | 0.61 | 0.22 | 0.00 | 0.67 | 0.73 | 0.91 | 0.20 | 0.33 | 0.55 |

---
## Detailed Results


### gliner-x-base / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 31ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 30ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 30ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 30ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 44ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 42ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 38ms | TSMC, 90%, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 40ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 32ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 26ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 39ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 34ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 43ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 47ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 43ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 46ms | تايوان, جمهورية الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.73 | 0.67 | 0.80 | 36ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 46ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-base / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 18ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 20ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 17ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 20ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 43ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 29ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 25ms | TSMC, 90%, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 30ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 21ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 19ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 29ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 23ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 34ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 36ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 38ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 37ms | تايوان, جمهورية الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.73 | 0.67 | 0.80 | 33ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 33ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-large / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 76ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 76ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 67ms | 台積電董事長魏哲家宣布在高雄 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 65ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.62 | 0.50 | 0.83 | 87ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 88ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 77ms | TSMC, market capitalization, 90%, Taiwan, GDP +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 76ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 66ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 64ms | 2017年台, 北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 87ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 80ms | 타이완은, 동아시아에, 중화민국이다, 타이베이이며, TSMC는 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 84ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 87ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 90ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.67 | 0.57 | 0.80 | 89ms | تايوان, جمهورية الصين, شرق آسيا, تايبيه, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.80 | 0.80 | 0.80 | 85ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 91ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-large / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 21ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 22ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 20ms | 台積電董事長魏哲家宣布在高雄 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 20ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.62 | 0.50 | 0.83 | 40ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 34ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 30ms | TSMC, market capitalization, 90%, Taiwan, GDP +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 30ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 20ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 19ms | 2017年台, 北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.73 | 0.67 | 0.80 | 33ms | 台湾, 東アジア, 中華民国, 台北市, 頼清徳 +1 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 28ms | 타이완은, 동아시아에, 중화민국이다, 타이베이이며, TSMC는 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 31ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 39ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 36ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.67 | 0.57 | 0.80 | 41ms | تايوان, جمهورية الصين, شرق آسيا, تايبيه, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.80 | 0.80 | 0.80 | 30ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 36ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-small / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 19ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 19ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 14ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 14ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 32ms | Taiwan, Republic of China, ROC, East Asia, East +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 27ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 22ms | TSMC, 90%, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 22ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 14ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 14ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.67 | 0.57 | 0.80 | 26ms | 台湾, 東アジア, 島, 中華民国, 台北市 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 22ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 27ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 32ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 29ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 34ms | تايوان, الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.36 | 0.33 | 0.40 | 25ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป TSMC, เซมิคอน +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 31ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner-x-small / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 20ms | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞洲大陸相望。目前為中華民國有效統治領土的主要部分。 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 20ms | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷蘭人。1895年，清廷因甲午戰爭失敗，簽訂馬關條約將臺灣割讓給日本。 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 18ms | 台積電董事長魏哲家宣布在高雄, 設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 17ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍之一。之後在1990年代躋身已開發國家之列。 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 34ms | Taiwan, Republic of China, ROC, East Asia, East +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 30ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 33ms | TSMC, 90%, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 27ms | Lai Ching-te, Democratic Progressive Party, Taiwan, 2024, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 18ms | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月潭為最大天然湖泊。 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 15ms | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.67 | 0.57 | 0.80 | 26ms | 台湾, 東アジア, 島, 中華民国, 台北市 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 23ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 타이베이이며 +2 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 30ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 42ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 34ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.33 | 0.29 | 0.40 | 37ms | تايوان, الصين, شرق آسيا, تايوان، المعروفة رسمياً بجمهورية الصين، هي دولة تقع في شرق آسيا. عاصمتها تايبي, TSMC +2 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.36 | 0.33 | 0.40 | 32ms | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป TSMC, เซมิคอน +1 | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 29ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á., Đài Bắc., TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner2-multi-v1 / onnx-multi / gliner2

**ERROR:** RepositoryNotFoundError: 404 Client Error. (Request ID: Root=1-6a16784d-615ed6d918afef930e24699c;f54e7215-7e0d-4480-8592-30a7805a1768)

Repository Not Found for url: https://huggingface.co/SemplificaAI/gliner2-multi-v1/resolve/main/config.json.
Please make sure you specified the correct `repo_id` and `repo_type`.
If you are trying to access a private or gated repo, make sure you are authenticated and your token has the required permissions.
For more details, see https://huggingface.co/docs/huggingface_hub/authentication


### gliner_large-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 108ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 109ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 102ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 119ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 124ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 116ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 107ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 96ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 112ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 99ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 114ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 116ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 130ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 130ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 117ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 123ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 172ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 125ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_large-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 27ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 30ms | 1624年, 1661年, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 23ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 26ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 35ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 32ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 28ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 28ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 26ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 23ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 27ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 32ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 35ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 36ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 32ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 36ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 47ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 37ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_medium-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 43ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 44ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 39ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 42ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 47ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 45ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 32ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 31ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 42ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 34ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 44ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 44ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 49ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 47ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 45ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 49ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 68ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 53ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_medium-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 19ms | 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 18ms | 1624年, 1661年, 鄭成功領軍攻臺, 1895年 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 15ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 15ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 27ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 22ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 21ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 20ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 18ms | 玉山為臺灣最高峰, 海拔3, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 15ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 18ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 22ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 21ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 24ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 23ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 23ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 31ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 24ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_small-v2.5 / pytorch / pytorch-cpu

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 24ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 25ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 22ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 24ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 28ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 26ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 20ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 19ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 24ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 20ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 23ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 25ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 28ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 28ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 27ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 29ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 38ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 30ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### gliner_small-v2.5 / pytorch / pytorch-mps

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 15ms | 臺灣位於東亞, 太平洋西北側的島嶼 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 18ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +1 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 16ms | 台積電董事長魏哲家宣布在高雄設立新廠 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 15ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟, 名列亞洲四小龍之一 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 28ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 23ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 24ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 18ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 17ms | 玉山為臺灣最高峰, 海拔3, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 12ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 16ms | 台湾は東アジアに位置する島で, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 21ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 21ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 27ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 22ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 27ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 29ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 20ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### large-v2.5 / fp32 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.57 | 0.57 | 0.57 | 67ms | 臺灣, 太平洋, 琉球群島, 菲律賓群島, 臺灣海 +2 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 67ms | 1624, 荷蘭東印度公司, 大員, 1661, 鄭 +3 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.36 | 0.29 | 0.50 | 56ms | 台積電, 魏哲, 高雄, 新廠, 新台幣 +2 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.50 | 1.00 | 0.33 | 58ms | 臺灣 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 46ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 42ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 31ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 30ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.60 | 0.60 | 0.60 | 53ms | 玉山, 臺灣, 臺灣, 河川, 高屏溪 +1 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.57 | 0.67 | 0.50 | 41ms | 臺北市, 王建民, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.29 | 0.50 | 0.20 | 57ms | 台北市, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 42ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 51ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 45ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 43ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 51ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 89ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 52ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### large-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.57 | 0.57 | 0.57 | 182ms | 臺灣, 太平洋, 琉球群島, 菲律賓群島, 臺灣海 +2 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 173ms | 1624, 荷蘭東印度公司, 大員, 1661, 鄭 +3 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.36 | 0.29 | 0.50 | 156ms | 台積電, 魏哲, 高雄, 新廠, 新台幣 +2 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.50 | 1.00 | 0.33 | 155ms | 臺灣 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.57 | 0.50 | 0.67 | 136ms | Taiwan, Republic of China, East Asia, South China Seas, northwestern Pacific Ocean +3 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.71 | 0.56 | 1.00 | 122ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 102ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 101ms | Lai Ching-te, Democratic Progressive Party, 2024 presidential election, Kuomintang, legislative election | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.60 | 0.60 | 0.60 | 152ms | 玉山, 臺灣, 臺灣, 河川, 高屏溪 +1 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.57 | 0.67 | 0.50 | 121ms | 臺北市, 王建民, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.29 | 0.50 | 0.20 | 167ms | 台北市, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 146ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.86 | 0.86 | 0.86 | 150ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +2 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 132ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.60 | 0.60 | 0.60 | 122ms | Taiwán, República de China, Asia Oriental, Tratado de Shimonoseki, TSMC | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.36 | 0.33 | 0.40 | 154ms | تايوان, الصين, شرق آسيا, TSMC, العالم +1 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 247ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.62 | 0.50 | 0.80 | 156ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +3 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp16 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.25 | 1.00 | 0.14 | 42ms | 東亞 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 40ms | 1624年, 1661年, 1895年, 清廷 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 35ms | 台積電董事長, 蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 36ms | 臺灣, 臺灣, 1990年代 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 32ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 30ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 26ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 24ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.29 | 0.50 | 0.20 | 34ms | 玉山, 臺灣 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 28ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.60 | 0.60 | 0.60 | 35ms | 台湾, 東アジア, 台北市, 頼清徳, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 28ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 32ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 31ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 29ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 33ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 45ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 37ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp16 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.25 | 1.00 | 0.14 | 43ms | 東亞 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 42ms | 1624年, 1661年, 1895年, 清廷 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 35ms | 台積電董事長, 蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 37ms | 臺灣, 臺灣, 1990年代 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 33ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 32ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 25ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 26ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.29 | 0.50 | 0.20 | 36ms | 玉山, 臺灣 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 30ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.60 | 0.60 | 0.60 | 39ms | 台湾, 東アジア, 台北市, 頼清徳, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 31ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 34ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 33ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 32ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 37ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 46ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 37ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp32 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.25 | 1.00 | 0.14 | 27ms | 東亞 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 26ms | 1624年, 1661年, 1895年, 清廷 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 21ms | 台積電董事長, 在高雄設立新廠, 蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 21ms | 臺灣, 臺灣, 1990年代 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 20ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 17ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 14ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 12ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.29 | 0.50 | 0.20 | 20ms | 玉山, 臺灣 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 16ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.60 | 0.60 | 0.60 | 23ms | 台湾, 東アジア, 台北市, 頼清徳, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 20ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 19ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 17ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 21ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 35ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 23ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.25 | 1.00 | 0.14 | 78ms | 東亞 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 77ms | 1624年, 1661年, 1895年, 清廷 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 61ms | 台積電董事長, 蔡英文總統出席動土典禮。 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 66ms | 臺灣, 臺灣, 1990年代 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 56ms | Taiwan, China, ROC, East Asia, East and South China Seas +9 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 53ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 46ms | TSMC, Taiwan, GDP, world, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 45ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.29 | 0.50 | 0.20 | 66ms | 玉山, 臺灣 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 54ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.60 | 0.60 | 0.60 | 72ms | 台湾, 東アジア, 台北市, 頼清徳, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 58ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.75 | 0.67 | 0.86 | 63ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 60ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 55ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.29 | 0.22 | 0.40 | 70ms | تايوان, شرق آسيا, تايبيه, شركة TSMC, العالم +4 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 101ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.83 | 0.71 | 1.00 | 71ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / int8 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 24ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 23ms |  | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 17ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 19ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.18 | 0.20 | 0.17 | 17ms | Taiwan, Republic of China, ROC, PRC, Japan | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.00 | 0.00 | 0.00 | 14ms | Fort Zeelandia, Tayouan, Shimonoseki | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.00 | 0.00 | 0.00 | 11ms | TSMC, Taiwan, Samsung | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.40 | 0.50 | 0.33 | 10ms | Democratic Progressive Party, Taiwan | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 18ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 13ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 20ms |  | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 15ms |  | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.44 | 1.00 | 0.29 | 16ms | Тайвань, Тайбэй | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.00 | 0.00 | 0.00 | 17ms | Taïwan, Shimonoseki, TSMC | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.00 | 0.00 | 0.00 | 15ms | Taiwán, Shimonoseki | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 19ms |  | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 30ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.29 | 0.50 | 0.20 | 19ms | Đài Loan, Trung Hoa Dân Quốc | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### medium-v2.5 / int8 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 74ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 73ms |  | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 57ms |  | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.00 | 0.00 | 0.00 | 63ms |  | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.00 | 0.00 | 0.00 | 55ms | Taiwan, PRC, Japan | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.20 | 0.20 | 0.20 | 51ms | Fort Zeelandia, Tayouan, Dutch, 1895, Shimonoseki | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.00 | 0.00 | 0.00 | 42ms | TSMC, Taiwan, Samsung | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.00 | 0.00 | 0.00 | 42ms | Democratic Progressive Party, Taiwan, 2024 presidential election, Kuomintang | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.00 | 0.00 | 0.00 | 65ms |  | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 48ms |  | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 73ms | TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 56ms |  | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.22 | 0.50 | 0.14 | 63ms | Филиппинами, Китайская Республика | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.22 | 0.25 | 0.20 | 60ms | Taïwan, Chine, Shimonoseki, TSMC | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.00 | 0.00 | 0.00 | 54ms | Taiwán, China, Asia Oriental | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 66ms |  | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.00 | 0.00 | 0.00 | 107ms |  | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.00 | 0.00 | 0.00 | 69ms | Trung Hoa | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### openmed-relex-base-mlx / mlx / mlx

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 10ms | 臺灣位於東亞, 西隔臺灣海峽與亞洲大陸相望 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 11ms | 1624年, 荷蘭東印度公司在大員建立熱蘭遮城, 1661年, 鄭成功領軍攻臺, 1895年 +2 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 9ms | 台積電董事長魏哲家宣布在高雄設立新廠, 蔡英文總統出席動土典禮 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.40 | 0.50 | 0.33 | 10ms | 臺灣自1960年代起在經濟與社會發展上突飛猛進, 臺灣奇蹟 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.50 | 0.40 | 0.67 | 13ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 12ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 11ms | TSMC, market capitalization, Taiwan, GDP, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 11ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.40 | 0.40 | 0.40 | 10ms | 玉山為臺灣最高峰, 臺灣主要河川有濁水溪, 高屏溪, 淡水河, 日月潭為最大天然湖泊 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 9ms | 2017年台北世大運在臺北市舉行, 棒球選手王建民曾效力於MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.00 | 0.00 | 0.00 | 10ms | 台湾は東アジアに位置する島で, 2024年に頼清徳が総統に就任した, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 11ms | 동아시아에, 섬나라로, 타이베이이며, TSMC는, 2024년 +1 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.60 | 1.00 | 0.43 | 12ms | Восточной Азии, Тайбэй, TSMC | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 13ms | Taïwan, République de Chine, Asie de l'Est, Japon, traité de Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.73 | 0.67 | 0.80 | 12ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.00 | 0.00 | 0.00 | 12ms | شرق آسيا, تايبيه, شركة TSMC, العالم, منصب الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 14ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.80 | 0.80 | 0.80 | 13ms | Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC, Lại Thanh Đức | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp16 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.60 | 1.00 | 0.43 | 25ms | 臺灣, 東亞, 琉球群島 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 25ms | 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 19ms | 董事長, 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 21ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 19ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 17ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 14ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 13ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.44 | 0.50 | 0.40 | 19ms | 玉山, 臺灣最高峰, 臺灣主要河川, 淡水河 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 16ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.50 | 0.43 | 0.60 | 22ms | 台湾, 東アジアに位置する島, 中華民国, 台北市, 頼清徳 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 16ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 18ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 19ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 17ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 19ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 25ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 21ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp16 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.60 | 1.00 | 0.43 | 26ms | 臺灣, 東亞, 琉球群島 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 24ms | 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 20ms | 董事長, 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 22ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 20ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 18ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 15ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 14ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.44 | 0.50 | 0.40 | 21ms | 玉山, 臺灣最高峰, 臺灣主要河川, 淡水河 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 17ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.50 | 0.43 | 0.60 | 21ms | 台湾, 東アジアに位置する島, 中華民国, 台北市, 頼清徳 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 17ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 19ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 20ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 18ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 20ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 27ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 23ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

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
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.60 | 1.00 | 0.43 | 17ms | 臺灣, 東亞, 琉球群島 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 17ms | 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 13ms | 董事長, 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 13ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 13ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 11ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 8ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 8ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.44 | 0.50 | 0.40 | 14ms | 玉山, 臺灣最高峰, 臺灣主要河川, 淡水河 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 9ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.50 | 0.43 | 0.60 | 14ms | 台湾, 東アジアに位置する島, 中華民国, 台北市, 頼清徳 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 10ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 12ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 12ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 11ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 13ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 20ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 14ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / fp32 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.60 | 1.00 | 0.43 | 47ms | 臺灣, 東亞, 琉球群島 | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 46ms | 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 38ms | 董事長, 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 41ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.53 | 0.38 | 0.83 | 37ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +8 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.67 | 0.50 | 1.00 | 33ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.67 | 0.50 | 1.00 | 29ms | TSMC, market capitalization, Taiwan, GDP, world +3 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 28ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.44 | 0.50 | 0.40 | 38ms | 玉山, 臺灣最高峰, 臺灣主要河川, 淡水河 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.29 | 0.33 | 0.25 | 31ms | 台北世大運, 臺北市, MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.50 | 0.43 | 0.60 | 41ms | 台湾, 東アジアに位置する島, 中華民国, 台北市, 頼清徳 +2 | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 33ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +4 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.88 | 0.78 | 1.00 | 37ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +4 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 37ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.83 | 0.71 | 1.00 | 34ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +2 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.46 | 0.38 | 0.60 | 39ms | تايوان, الصين, شرق آسيا, تايبيه, TSMC +3 | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 56ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.50 | 0.43 | 0.60 | 42ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +2 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / int8 / onnx-CPU

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 15ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 15ms | 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 11ms | 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 12ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 12ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.57 | 0.44 | 0.80 | 9ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +4 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.73 | 0.57 | 1.00 | 7ms | TSMC, market capitalization, Taiwan, GDP, semiconductor manufacturing company +2 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.67 | 0.50 | 1.00 | 6ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang +1 | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.22 | 0.25 | 0.20 | 11ms | 玉山, 臺灣最高峰, 臺灣主要河川, 高屏溪 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 8ms | MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.44 | 0.50 | 0.40 | 13ms | 台湾, 東アジアに位置する島, 台北市, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 8ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +3 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.80 | 0.75 | 0.86 | 10ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика +3 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 11ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.91 | 0.83 | 1.00 | 9ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.20 | 0.20 | 0.20 | 11ms | الصين, آسيا, TSMC, العالم, الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 17ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.36 | 0.33 | 0.40 | 12ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Thủ đô, Đài Bắc +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

### small-v2.5 / int8 / onnx-CoreML

| Lang | Text | F1 | P | R | Latency | Found | Expected |
|------|------|----|----|---|---------|-------|----------|
| zh-TW | 臺灣位於東亞、太平洋西北側的島嶼，地處琉球群島與菲律賓群島之間，西隔臺灣海峽與亞… | 0.00 | 0.00 | 0.00 | 43ms |  | 臺灣, 東亞, 太平洋, 琉球群島, 菲律賓群島 |
| zh-TW | 1624年，荷蘭東印度公司在大員建立熱蘭遮城。1661年，鄭成功領軍攻臺，驅逐荷… | 0.00 | 0.00 | 0.00 | 42ms | 1661, 1895 | 荷蘭東印度公司, 鄭成功, 甲午戰爭, 馬關條約, 日本 |
| zh-TW | 台積電董事長魏哲家宣布在高雄設立新廠，預計投資超過新台幣三千億元。蔡英文總統出席… | 0.00 | 0.00 | 0.00 | 33ms | 新台幣三千億元 | 台積電, 魏哲家, 高雄, 蔡英文 |
| zh-TW | 臺灣自1960年代起在經濟與社會發展上突飛猛進，締造「臺灣奇蹟」，名列亞洲四小龍… | 0.29 | 0.25 | 0.33 | 36ms | 臺灣, 1960, 臺灣奇蹟, 1990 | 臺灣, 臺灣奇蹟, 亞洲四小龍 |
| en | Taiwan, officially the Republic of China… | 0.37 | 0.30 | 0.50 | 32ms | Taiwan, Republic of China, ROC, East Asia, East and South China Seas +5 | Taiwan, Republic of China, East Asia, Pacific Ocean, Japan |
| en | In 1624, the Dutch East India Company es… | 0.53 | 0.40 | 0.80 | 28ms | 1624, Dutch East India Company, Fort Zeelandia, Tayouan, Koxinga +5 | Dutch East India Company, Fort Zeelandia, Koxinga, Treaty of Shimonoseki, Empire of Japan |
| en | TSMC's market capitalization equated to … | 0.80 | 0.67 | 1.00 | 23ms | TSMC, Taiwan, GDP, semiconductor manufacturing company, Intel +1 | TSMC, Taiwan, Intel, Samsung |
| en | President Lai Ching-te of the Democratic… | 0.75 | 0.60 | 1.00 | 22ms | Lai Ching-te, Democratic Progressive Party, 2024, presidential election, Kuomintang | Lai Ching-te, Democratic Progressive Party, Kuomintang |
| zh-TW | 玉山為臺灣最高峰，海拔3,952公尺。臺灣主要河川有濁水溪、高屏溪、淡水河。日月… | 0.18 | 0.17 | 0.20 | 33ms | 玉山, 臺灣最高峰, 臺灣主要河川, 高屏溪, 淡水河 +1 | 玉山, 濁水溪, 高屏溪, 淡水河, 日月潭 |
| zh-TW | 2017年台北世大運在臺北市舉行。棒球選手王建民曾效力於MLB的紐約洋基隊。… | 0.00 | 0.00 | 0.00 | 26ms | MLB的紐約洋基隊 | 台北世大運, 臺北市, 王建民, 紐約洋基隊 |
| ja | 台湾は東アジアに位置する島で、正式名称は中華民国である。首都は台北市。2024年… | 0.22 | 0.25 | 0.20 | 41ms | 台湾, 東アジアに位置する島, 台北市。2024年に頼清徳, TSMCは世界最大の半導体製造企業である | 台湾, 中華民国, 台北市, 頼清徳, TSMC |
| ko | 타이완은 동아시아에 위치한 섬나라로, 공식 명칭은 중화민국이다. 수도는 … | 0.00 | 0.00 | 0.00 | 30ms | 타이완은, 동아시아에, 섬나라로, 중화민국이다, 수도는 +3 | 타이완, 중화민국, 타이베이, TSMC, 라이칭더 |
| ru | Тайвань расположен в Восточной Азии, меж… | 0.67 | 0.62 | 0.71 | 33ms | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика. Столица — Тайбэй +3 | Тайвань, Восточной Азии, Японией, Филиппинами, Китайская Республика |
| fr | Taïwan, officiellement la République de … | 0.73 | 0.67 | 0.80 | 34ms | Taïwan, République de Chine, Asie de l'Est, Japon, Shimonoseki +1 | Taïwan, République de Chine, Japon, traité de Shimonoseki, TSMC |
| es | Taiwán, oficialmente la República de Chi… | 0.91 | 0.83 | 1.00 | 30ms | Taiwán, República de China, Asia Oriental, Japón, Tratado de Shimonoseki +1 | Taiwán, República de China, Japón, Tratado de Shimonoseki, TSMC |
| ar | تايوان، المعروفة رسمياً بجمهورية الصين، … | 0.20 | 0.20 | 0.20 | 37ms | الصين, آسيا, TSMC, العالم, الرئيس | تايوان, جمهورية الصين, تايبيه, TSMC, لاي تشينغ ته |
| th | ไต้หวันตั้งอยู่ในเอเชียตะวันออก มีชื่ออย… | 0.33 | 1.00 | 0.20 | 57ms | TSMC | ไต้หวัน, เอเชียตะวันออก, สาธารณรัฐจีน, ไทเป, TSMC |
| vi | Đài Loan, tên chính thức là Trung Hoa Dâ… | 0.55 | 0.50 | 0.60 | 39ms | Đài Loan, Trung Hoa Dân Quốc, Đông Á, Đài Bắc, TSMC +1 | Đài Loan, Trung Hoa Dân Quốc, Đài Bắc, TSMC, Lại Thanh Đức |

---
## Quantization Impact

| Model | fp32 F1 | fp16 F1 | int8 F1 | fp16 Δ | int8 Δ |
|-------|---------|---------|---------|--------|--------|
| small-v2.5 | 0.465 | 0.465 | 0.365 | +0.000 | -0.100 |
| medium-v2.5 | 0.441 | 0.441 | 0.054 | +0.000 | -0.386 |
| large-v2.5 | 0.490 | — | — | — | — |

---
*Total benchmark time: 175s*
