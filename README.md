Hàm `compute_similarity` trong mã nguồn trên được thiết kế để tính toán mức độ giống nhau giữa hai tín hiệu âm thanh dựa trên ba đặc trưng âm thanh khác nhau: chroma, mfcc, và spectral contrast. Dưới đây là giải thích chi tiết về cách hàm này hoạt động:

1. **Chroma, MFCC, và Spectral Contrast:**
    - `librosa.feature.chroma_stft(y=audio, sr=sr)`: Trả về ma trận chroma của tín hiệu âm thanh. Chroma là một biểu diễn của mức độ năng lượng của mỗi tần số cố định trong một phạm vi nhất định.
    - `librosa.feature.mfcc(y=audio, sr=sr)`: Trả về ma trận MFCC (Mel-Frequency Cepstral Coefficients) của tín hiệu âm thanh. MFCC là một biểu diễn của các đặc trưng tần số trong âm thanh, dựa trên thang tần số Mel.
    - `librosa.feature.spectral_contrast(y=audio, sr=sr)`: Trả về ma trận spectral contrast của tín hiệu âm thanh. Spectral contrast đo sự tương phản giữa các dải tần số khác nhau.

2. **Normalization:**
    - Mỗi ma trận đặc trưng được làm phẳng và chuẩn hóa bằng cách chia cho norm Euclidean của ma trận đó. Điều này giúp đảm bảo rằng mỗi đặc trưng có cùng một trọng số trong quá trình tính toán độ giống nhau.

3. **Resampling:**
    - Độ dài của mỗi đặc trưng có thể khác nhau giữa hai tín hiệu âm thanh. Do đó, ta resample (làm cho độ dài bằng nhau) bằng cách sử dụng hàm `librosa.util.fix_length`.

4. **Cosine Similarity:**
    - Sử dụng cosine similarity để đo độ tương đồng giữa hai vectơ đặc trưng đã chuẩn hóa. Đối với mỗi đặc trưng, tính cosine similarity bằng cách sử dụng hàm `np.dot` và sau đó chia cho tích của hai norm để chuẩn hóa.

5. **Average Similarity:**
    - Lấy trung bình của độ giống nhau từ ba đặc trưng (chroma, mfcc, và spectral contrast) để có mức độ giống nhau cuối cùng.

6. **Kết quả:**
    - Hàm trả về giá trị `similarity`, là mức độ giống nhau trung bình giữa các đặc trưng của hai tín hiệu âm thanh.
