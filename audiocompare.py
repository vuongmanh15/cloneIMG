import librosa
import numpy as np
import matplotlib.pyplot as plt
import os

def load_audio(file_path):
    audio, sr = librosa.load(file_path)
    return audio, sr
def list_audio_files(folder_path):
    # Lấy danh sách tất cả các file âm thanh trong thư mục
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    return audio_files

def equalize_amplitude(audio1, audio2):
    # Chia tỷ lệ âm lượng của audio2 để giảm chênh lệch
    rms1 = np.sqrt(np.mean(audio1**2))
    rms2 = np.sqrt(np.mean(audio2**2))

    audio2_equalized = audio2 * (rms1 / rms2)
    return audio2_equalized

def compute_similarity(audio1, audio2, sr):
    # Xử lý để làm cho âm lượng của hai file bằng nhau
    audio2_equalized = equalize_amplitude(audio1, audio2)

    # Extract multiple features using librosa
    chroma1 = librosa.feature.chroma_stft(y=audio1, sr=sr)
    mfcc1 = librosa.feature.mfcc(y=audio1, sr=sr)
    contrast1 = librosa.feature.spectral_contrast(y=audio1, sr=sr)

    chroma2 = librosa.feature.chroma_stft(y=audio2_equalized, sr=sr)
    mfcc2 = librosa.feature.mfcc(y=audio2_equalized, sr=sr)
    contrast2 = librosa.feature.spectral_contrast(y=audio2_equalized, sr=sr)

    # Normalize feature arrays
    chroma1_normalized = chroma1.flatten() / np.linalg.norm(chroma1)
    chroma2_normalized = chroma2.flatten() / np.linalg.norm(chroma2)

    mfcc1_normalized = mfcc1.flatten() / np.linalg.norm(mfcc1)
    mfcc2_normalized = mfcc2.flatten() / np.linalg.norm(mfcc2)

    contrast1_normalized = contrast1.flatten() / np.linalg.norm(contrast1)
    contrast2_normalized = contrast2.flatten() / np.linalg.norm(contrast2)

    # Resample the longer arrays to match the length of the shorter ones
    min_len_chroma = min(len(chroma1_normalized), len(chroma2_normalized))
    min_len_mfcc = min(len(mfcc1_normalized), len(mfcc2_normalized))
    min_len_contrast = min(len(contrast1_normalized), len(contrast2_normalized))

    chroma1_normalized = librosa.util.fix_length(chroma1_normalized, size=min_len_chroma)
    mfcc1_normalized = librosa.util.fix_length(mfcc1_normalized, size=min_len_mfcc)
    contrast1_normalized = librosa.util.fix_length(contrast1_normalized, size=min_len_contrast)

    chroma2_normalized = librosa.util.fix_length(chroma2_normalized, size=min_len_chroma)
    mfcc2_normalized = librosa.util.fix_length(mfcc2_normalized, size=min_len_mfcc)
    contrast2_normalized = librosa.util.fix_length(contrast2_normalized, size=min_len_contrast)

    # Compute similarity using cosine similarity for each feature
    similarity_chroma = np.dot(chroma1_normalized, chroma2_normalized)
    similarity_mfcc = np.dot(mfcc1_normalized, mfcc2_normalized)
    similarity_contrast = np.dot(contrast1_normalized, contrast2_normalized)

    # Take the average similarity
    similarity = (similarity_chroma + similarity_mfcc + similarity_contrast) / 3.0
    return similarity

def plot_waveform(audio1, audio2, sr, title1, title2, save_path=None):
    plt.close('all')
    plt.figure(figsize=(12, 5))
    
    # Plot Waveform of Audio 1 in black
    plt.plot(np.arange(len(audio1)) / sr, audio1, color='black', label='Audio original')

    # Plot Waveform of Audio 2 in red
    plt.plot(np.arange(len(audio2)) / sr, audio2, color='red', label='Audio test')

    plt.title('Waveform Comparison')
    plt.xlabel('Duration (s)')
    plt.ylabel('Amplitude')
    plt.legend()

    # Lưu biểu đồ thành hình ảnh nếu được chỉ định đường dẫn
    if save_path:
        plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

def main():

    # Đường dẫn của thư mục chứa các file âm thanh Audio1 và Audio2
    folder_path_audio1 = "C:\\Users\\vuong\\source\\source\\repos\\creatsub\\creatsub\\bin\\Release\\Done\\Audio"
    folder_path_audio2 = "C:\\Users\\vuong\\source\\source\\repos\\creatsub\\creatsub\\bin\\Release\\Done\\Audio2"

    # Lấy danh sách các file âm thanh trong mỗi thư mục
    audio_files_audio1 = list_audio_files(folder_path_audio1)
    audio_files_audio2 = list_audio_files(folder_path_audio2)

    # Lặp qua từng cặp file âm thanh có cùng tên trong hai thư mục
    for file_name in set(audio_files_audio1) & set(audio_files_audio2):
        # Đường dẫn đầy đủ của file trong mỗi thư mục
        file_path_audio1 = os.path.join(folder_path_audio1, file_name)
        file_path_audio2 = os.path.join(folder_path_audio2, file_name)

        # Load audio files
        audio1, sr = load_audio(file_path_audio1)
        audio2, _ = load_audio(file_path_audio2)

        # So sánh độ giống nhau
        similarity = compute_similarity(audio1, audio2, sr)
        print(f'\nSo sánh {file_name}: Mức độ giống nhau = {similarity}')
        if similarity < 0.9:
            print ("result: FAIL\n")
            plot_waveform(audio1, audio2, sr, 'Waveform of Audio 1', 'Waveform of Audio 2', save_path=f'C:\\Users\\vuong\\source\\source\\repos\\creatsub\\creatsub\\bin\\Release\\Done\\chart\\{file_name}_FAIL.png')
        else:
            print("result: PASS\n")
            plot_waveform(audio1, audio2, sr, 'Waveform of Audio 1', 'Waveform of Audio 2', save_path=f'C:\\Users\\vuong\\source\\source\\repos\\creatsub\\creatsub\\bin\\Release\\Done\\chart\\{file_name}_PASS.png')
        


if __name__ == "__main__":
    main()
