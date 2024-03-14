#1개의 명령어와 1개의 파일을 순차실행 
#mjpg 실행 후 플라스크 서버 실행 
import subprocess

def execute_command(directory, command):
    subprocess.Popen(command, cwd=directory, shell=True)

if __name__ == "__main__":
    commands = [
        ("/home/jang/test/mjpg/mjpg-streamer/mjpg-streamer-experimental/", "mjpg_streamer -o 'output_http.so -w ./www -p 8080' -i 'input_uvc.so'"),
        ("/home/jang/test/flask_opencv/", "python mjpgstream.py")
    ]

    for directory, command in commands:
        execute_command(directory, command)

