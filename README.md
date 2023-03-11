# Messandei

A simple language detector for rest of us.

### Supported languages
- Arabic
- Bulgarian
- Catalan
- Czech
- Danish
- Dutch
- English
- Finnish
- French
- German
- Hungarian
- Indonesian
- Italian
- Norwegian
- Polish
- Portuguese
- Romanian
- Russian
- Spanish
- Swedish
- Turkish
- Ukrainian


## Installation
1. Clone [git repo](https://github.com/Ankush-Chander/messandei)
```
git clone git@github.com:Ankush-Chander/messandei.git
```
2. Install via pip
```
pip install -e .
```

## Basic usage
```
from messandei import detect_language
text = "Abstract: Academic procrastination has occurred throughout human life, but until now this behavior still continues to occur, even experienced by undergraduate and postgraduate students, so efforts to resolve must continue. This study aims to explore the causes, impacts, and strategies for handling academic procrastination in students. The subjects of this study were 20 students of the Faculty of Psychology at an accredited university in Surabaya, drawn randomly from 98 students who had previously stated their willingness to become research subjects. This research is descriptive qualitative research, making it possible to explore subjective experiences in greater depth. Data collection techniques in this study used open questions and in-depth interviews. The data obtained is then verbally digitized and analyzed to find themes related to the research objectives. The results found 10 categories and 25 sub-categories of internal factors causing academic procrastination, 3 categories, and 10 sub-categories of external factors causing academic procrastination. There are 8 categories and 32 impact sub-categories of academic procrastination. The handling strategies used by students vary greatly, most of which choose to motivate themselves and take notes on task reminders in writing. This study provides a very comprehensive picture so that it can be used as a reference in explaining and handling academic procrastination in students.Keywords: factors causing academic procrastination, the impact of academic procrastination, handling academic procrastination Abstrak: Prokrastinasi akademik telah terjadi sepanjang kehidupan manusia, tetapi hingga saat ini perilaku tersebut masih terus terjadi, bahkan banyak dialami oleh mahasiswa sarjana dan pasca sarjana, sehingga upaya untuk penyelesaian harus terus dilakukan. Penelitian ini bertujuan untuk mengeksplorasi faktor penyebab, dampak dan strategi penanganan prokrastinasi akademi pada mahasiswa. Subjek penelitian ini berjumlah 20 mahasiswa Fakultas Psikologi di sebuah universitas ter-akreditasi A di Surabaya, yang diambil secara random dari 98 mahasiswa yang sebelumnya telah menyatakan kesediaannya menjadi subjek penelitian. Penelitian ini adalah penelitian kualitatif deskriptif, sehingga memungkinkan untuk menggali pengalaman subjektif secara lebih mendalam. Teknik pengumpulan data dalam penelitian ini menggunakan pertanyaan terbuka dan wawancara mendalam. Data yang diperoleh kemudian dibuat verbatim secara digital dan dianalisis untuk menemukan tema-tema yang terkait dengan tujuan penelitian. Hasil penelitian menemukan 10 kategori dan 25 sub kategori faktor internal penyebab prokrastinasi akademik, 3 kategori dan 10 sub kategori faktor eksternal penyebab prokrastinasi akademik. Ada 8 kategori dan 32 sub kategori dampak dari prokrastinasi akademik. Strategi penangan yang digunakan mahasiswa sangat bervariasi, yang sebagian besar memilih memotivasi diri dan membuat catatan pengingat tugas secara tertulis. Penelitian ini memberikan gambaran yang sangat komprehensif sehingga dapat dijadikan sebagai acuan dalam menjelaskan dan menangani prokrastinasi akademik pada mahasiswa.Kata kunci: faktor penyebab prokrastinasi akademik, dampak prokrastinasi akademik, penangan prokrastinasi akademik"

language_detected = detect_language(text)
# Outputs: {'english': 56.8, 'indonesian': 41.0, 'romanian': 2.2}
```
