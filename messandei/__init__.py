__all__ = ["SUPPORTED_LANGUAGES", "detect_language"]

from collections import defaultdict, Counter
import stop_words

SUPPORTED_LANGUAGES = stop_words.AVAILABLE_LANGUAGES
STOPWORD_LANGUAGE_MAP = defaultdict(list)


def _get_stop_words_by_language(lang: str) -> list:
    try:
        lang_stopwords = stop_words.get_stop_words(lang)
        return lang_stopwords
    except Exception as err:
        pass


for language in SUPPORTED_LANGUAGES:
    lang_stopwords = _get_stop_words_by_language(language)
    # print(lang_stopwords)
    for word in lang_stopwords:
        STOPWORD_LANGUAGE_MAP[word].append(language)


def detect_language(text: str) -> dict:
    # get potential languages for each stopword
    if not text.strip():
        return {}
    all_words = text.lower().split()
    stop_words = [word for word in all_words if word in STOPWORD_LANGUAGE_MAP]
    total_stopwords = len(stop_words)
    candidate_lang_list = []
    for word in stop_words:
        candidate_lang_list = candidate_lang_list + STOPWORD_LANGUAGE_MAP.get(word)

    doc_counter = Counter(candidate_lang_list)

    # pick most probable language for each stopword via majoritarianism
    language_list = []
    for word in stop_words:
        lang_candidates = STOPWORD_LANGUAGE_MAP.get(word)
        lang_candidates = sorted(lang_candidates, key=lambda x: doc_counter[x], reverse=True)
        language_list.append(lang_candidates[0])
    language_counter = dict(Counter(language_list))
    result = {key: round((value / total_stopwords) * 100, 1) for key, value in language_counter.items()}
    return result


if __name__ == '__main__':
    text = "Abstract: Academic procrastination has occurred throughout human life, but until now this behavior still continues to occur, even experienced by undergraduate and postgraduate students, so efforts to resolve must continue. This study aims to explore the causes, impacts, and strategies for handling academic procrastination in students. The subjects of this study were 20 students of the Faculty of Psychology at an accredited university in Surabaya, drawn randomly from 98 students who had previously stated their willingness to become research subjects. This research is descriptive qualitative research, making it possible to explore subjective experiences in greater depth. Data collection techniques in this study used open questions and in-depth interviews. The data obtained is then verbally digitized and analyzed to find themes related to the research objectives. The results found 10 categories and 25 sub-categories of internal factors causing academic procrastination, 3 categories, and 10 sub-categories of external factors causing academic procrastination. There are 8 categories and 32 impact sub-categories of academic procrastination. The handling strategies used by students vary greatly, most of which choose to motivate themselves and take notes on task reminders in writing. This study provides a very comprehensive picture so that it can be used as a reference in explaining and handling academic procrastination in students.Keywords: factors causing academic procrastination, the impact of academic procrastination, handling academic procrastination Abstrak: Prokrastinasi akademik telah terjadi sepanjang kehidupan manusia, tetapi hingga saat ini perilaku tersebut masih terus terjadi, bahkan banyak dialami oleh mahasiswa sarjana dan pasca sarjana, sehingga upaya untuk penyelesaian harus terus dilakukan. Penelitian ini bertujuan untuk mengeksplorasi faktor penyebab, dampak dan strategi penanganan prokrastinasi akademi pada mahasiswa. Subjek penelitian ini berjumlah 20 mahasiswa Fakultas Psikologi di sebuah universitas ter-akreditasi A di Surabaya, yang diambil secara random dari 98 mahasiswa yang sebelumnya telah menyatakan kesediaannya menjadi subjek penelitian. Penelitian ini adalah penelitian kualitatif deskriptif, sehingga memungkinkan untuk menggali pengalaman subjektif secara lebih mendalam. Teknik pengumpulan data dalam penelitian ini menggunakan pertanyaan terbuka dan wawancara mendalam. Data yang diperoleh kemudian dibuat verbatim secara digital dan dianalisis untuk menemukan tema-tema yang terkait dengan tujuan penelitian. Hasil penelitian menemukan 10 kategori dan 25 sub kategori faktor internal penyebab prokrastinasi akademik, 3 kategori dan 10 sub kategori faktor eksternal penyebab prokrastinasi akademik. Ada 8 kategori dan 32 sub kategori dampak dari prokrastinasi akademik. Strategi penangan yang digunakan mahasiswa sangat bervariasi, yang sebagian besar memilih memotivasi diri dan membuat catatan pengingat tugas secara tertulis. Penelitian ini memberikan gambaran yang sangat komprehensif sehingga dapat dijadikan sebagai acuan dalam menjelaskan dan menangani prokrastinasi akademik pada mahasiswa.Kata kunci: faktor penyebab prokrastinasi akademik, dampak prokrastinasi akademik, penangan prokrastinasi akademik"
    # text = ""
    x = detect_language(text)
    print(x)
