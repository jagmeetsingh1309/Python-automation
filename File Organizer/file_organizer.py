import os
import shutil


def organize():
    home_path = 'C:\\Users\\Jagmeet singh\\Downloads\\'
    images_dir = home_path + 'Images'
    documents_dir = home_path + 'Documents'
    exe_dir = home_path + 'Executables'
    archive_dir = home_path + 'Archives'
    code_dir = home_path + 'Code';
    audio_dir = home_path + 'Audios'
    torrent_dir = home_path + 'Torrents'
    video_dir = home_path + 'Videos'
    output_dirs = [images_dir, documents_dir, archive_dir, exe_dir, code_dir, audio_dir, torrent_dir,video_dir]
    img_exts = ['png', 'jpg', 'jpeg']
    doc_exts = ['pdf', 'docx', 'ppt', 'pptx', 'doc', 'csv', 'txt', 'xls', 'xlsx', 'log']
    exe_exts = ['exe']
    archive_exts = ['zip', '.ar']
    code_exts = ['py', 'js', 'html', 'css']
    audio_exts = ['mp3']
    torrent_exts = ['torrent']
    video_exts = ['mp4']
    create_output_dir(home_path, output_dirs)
    files = os.listdir(home_path)
    for file in files:
        splitted_text = file.split('.')
        if len(splitted_text) > 1:
            ext = splitted_text[-1].lower()
            if ext in img_exts:
                movefile(home_path, file, images_dir)
            elif ext in doc_exts:
                movefile(home_path, file, documents_dir)
            elif ext in exe_exts:
                movefile(home_path, file, exe_dir)
            elif ext in archive_exts:
                movefile(home_path, file, archive_dir)
            elif ext in code_exts:
                movefile(home_path, file, code_dir)
            elif ext in audio_exts:
                movefile(home_path, file, audio_dir)
            elif ext in torrent_exts:
                movefile(home_path, file, torrent_dir)
            elif ext in video_exts:
                movefile(home_path, file, video_dir)

    __name__ = "__main__"


def movefile(home_path, file, dest):
    shutil.move(os.path.join(home_path, file), dest)


def create_output_dir(home_path, output_dirs):
    for output_dir in output_dirs:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)


organize()