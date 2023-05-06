import subprocess
import os, sys


# function for converting videos to specified format
def convert_video(path_in, path_out, to_file_ext, org_ext):
    '''
     Convert video files in a folder to different format
     Change ffpmeg command in subprocess to fit single ffmpeg from command line
     '''
    for file in os.scandir(path_in):
        if file.name.endswith(f'.{org_ext}'.upper()):
            file_path_in = os.path.join(path_in, file.name)
            path_out = f'{path_out}/'
            file_path_out = f'{path_out + os.path.splitext(file.name)[0]}.{to_file_ext}'
            subprocess.run(['ffmpeg', '-i', file_path_in, '-vn', '-acodec', 'pcm_s16le', '-ac', '1', file_path_out])


print("Conversion begins now:")

path_in = 'D:/Thesis_data/c3_muse_stress_2022/raw_data/video/1.MTS'  # files for conversion and uploading are stored here
path_out = 'D:/Thesis_data/1.wav'  # converted files are stored here temporarily

for p in [path_in, path_out]:
    if not (os.path.isdir(p)):
        try:
            os.mkdir(p)
        except OSError:
            print("Creation of the directory %s failed" % p)
        else:
            print("Successfully created the directory %s " % p)

# call videos to be processed

if __name__ == '__main__':
    org_ext = 'MTS'
    to_file_ext = 'wav'
    convert_video(path_in,path_out , to_file_ext, org_ext)

print("All files converted!")

